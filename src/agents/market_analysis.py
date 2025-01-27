from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
from google.genai.types import Tool, ToolConfig, GenerateContentConfig, GoogleSearch, FunctionCallingConfig
import os
import json
from dotenv import load_dotenv
from config import (
    market_analysis_response_schema,
    market_analysis_system_instruction,
    idea_feasibility_response_schema,
)

load_dotenv()

app = FastAPI()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
model_id = "gemini-2.0-flash-exp"

# Market Analysis Configuration
market_analysis_response_schema = market_analysis_response_schema
market_analysis_system_instruction = market_analysis_system_instruction

market_tool_config = ToolConfig(
    function_calling_config=FunctionCallingConfig(
        mode="ANY",
        allowed_function_names=["GoogleSearch"]
    )
)

market_config = GenerateContentConfig(
    system_instruction=market_analysis_system_instruction,
    tools=[Tool(google_search=GoogleSearch())],
    tool_config=market_tool_config,
    temperature=0.1,
    max_output_tokens=4000
)

# Idea Feasibility Configuration
idea_feasibility_response_schema = idea_feasibility_response_schema

idea_feasibility_config = GenerateContentConfig(
    system_instruction=(
        "First validate via web search:\n"
        "- Market size (2024)\n"
        "- Competitor features\n"
        "- Regulatory requirements\n"
        f"Then format as: {idea_feasibility_response_schema}"
    ),
    tools=[Tool(google_search=GoogleSearch())],
    temperature=0.1,
    max_output_tokens=4000,
)

# Request Models
class StartupIdea(BaseModel):
    idea: str

# Market Analysis Endpoint
@app.post("/analyze-market/")
async def analyze_market(startup_idea: StartupIdea):
    contents = [f"""Analyze market for: {startup_idea.idea}
    Include 2024 data with EXACT NUMBERS from:
    - Market research reports (2023-2024)
    - Competitor annual reports
    - Government economic data
    Output MUST CONTAIN NUMERIC VALUES for all fields"""]

    response = client.models.generate_content(
        model=model_id,
        contents=contents,
        config=market_config
    )

    if response:
        try:
            market_analysis = response.text
            if "```json" in market_analysis:
                json_text = market_analysis.split("```json")[-1].split("```")[0].strip()
            else:
                json_text = market_analysis.strip()

            market_analysis = json.loads(json_text)

            return {"market_analysis": market_analysis}

        except json.JSONDecodeError as e:
            raise HTTPException(status_code=500, detail=f"JSON parsing error: {str(e)}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing response: {str(e)}")
    else:
        raise HTTPException(status_code=500, detail="No response received")

# Idea Feasibility Endpoint
@app.post("/analyze-idea-feasibility/")
async def analyze_idea_feasibility(startup_idea: StartupIdea):
    contents = [
        "Analyze this startup idea with REQUIRED WEB SEARCH:",
        startup_idea.idea,
        "Cite sources from industry reports and competitor websites.",
        "Format response as JSON with sources."
    ]

    response = client.models.generate_content(
        model=model_id,
        contents=contents,
        config=idea_feasibility_config
    )

    if response:
        try:
            idea_feasibility = response.text
            if "```json" in idea_feasibility:
                json_text = idea_feasibility.split("```json")[-1].split("```")[0].strip()
            else:
                json_text = idea_feasibility.strip()

            idea_feasibility = json.loads(json_text)

            return {"idea_feasibility": idea_feasibility}

        except json.JSONDecodeError as e:
            raise HTTPException(status_code=500, detail=f"JSON parsing error: {str(e)}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing response: {str(e)}")
    else:
        raise HTTPException(status_code=500, detail="No response received")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)