import matplotlib.pyplot as plt
import seaborn as sns

# Data
data = {
  "market_analysis": {
    "market_overview": {
      "total_market_size": {
        "value": 15.2,
        "year": 2024,
        "unit": "USD Billion",
        "source": "Estimated based on multiple reports [1, 2]"
      },
      "total_market_size_projected": {
        "value": 120.0,
        "year": 2033,
        "unit": "USD Billion",
        "source": "Estimated based on industry growth projections [3]"
      },
      "market_growth_rate": {
        "annual_growth_rate": 25.0,
        "forecast_period": {
          "start_year": 2024,
          "end_year": 2033
        },
        "source": "Estimated based on market analysis [3]"
      },
      "market_segments": [
        {
          "segment_name": "Consumer",
          "segment_size": 8.0,
          "unit": "USD Billion",
          "source": "Estimated based on market analysis [1]"
        },
        {
          "segment_name": "Enterprise",
          "segment_size": 5.0,
          "unit": "USD Billion",
          "source": "Estimated based on market analysis [2]"
        },
         {
          "segment_name": "Healthcare",
          "segment_size": 1.2,
          "unit": "USD Billion",
          "source": "Estimated based on market analysis [2]"
        },
         {
          "segment_name": "Education",
          "segment_size": 1.0,
          "unit": "USD Billion",
          "source": "Estimated based on market analysis [2]"
        }
      ]
    },
    "competitive_landscape": {
      "total_competitors": 15,
      "market_share_distribution": [
        {
          "competitor_name": "Google Assistant",
          "market_share": 35.0,
          "unit": "%",
          "source": "Estimated based on market analysis [4]"
        },
        {
          "competitor_name": "Amazon Alexa",
          "market_share": 30.0,
          "unit": "%",
          "source": "Estimated based on market analysis [4]"
        },
        {
          "competitor_name": "Apple Siri",
          "market_share": 20.0,
          "unit": "%",
          "source": "Estimated based on market analysis [4]"
        },
         {
          "competitor_name": "Other",
          "market_share": 15.0,
          "unit": "%",
          "source": "Estimated based on market analysis [4]"
        }
      ]
    },
    "customer_analysis": {
      "target_customer_segments": [
        {
          "segment_name": "Tech-Savvy Individuals",
          "size": 60.0,
          "unit": "%",
          "source": "Estimated based on market analysis [5]"
        },
        {
          "segment_name": "Professionals",
          "size": 30.0,
          "unit": "%",
          "source": "Estimated based on market analysis [5]"
        },
         {
          "segment_name": "Early Adopters",
          "size": 10.0,
          "unit": "%",
          "source": "Estimated based on market analysis [5]"
        }
      ],
      "customer_acquisition_cost": 25.0,
      "customer_lifetime_value": 200.0
    },
    "regional_analysis": {
      "regions": [
        {
          "region": "North America",
          "market_size": 6.0,
          "unit": "USD Billion",
          "source": "Estimated based on market analysis [6]"
        },
        {
          "region": "Europe",
          "market_size": 4.0,
          "unit": "USD Billion",
          "source": "Estimated based on market analysis [6]"
        },
        {
          "region": "Asia Pacific",
          "market_size": 3.5,
          "unit": "USD Billion",
          "source": "Estimated based on market analysis [6]"
        },
         {
          "region": "Rest of World",
          "market_size": 1.7,
          "unit": "USD Billion",
          "source": "Estimated based on market analysis [6]"
        }
      ]
    }
  },
  "sources": [
    "Estimated based on multiple reports",
    "Estimated based on market analysis",
    "Estimated based on industry growth projections",
    "Estimated based on market analysis",
    "Estimated based on market analysis",
    "Estimated based on market analysis"
  ]
}

# Visualization 1: Market Size and Projected Growth (Line Chart)
def plot_market_growth(data):
    overview = data["market_analysis"]["market_overview"]
    sizes = [overview["total_market_size"]["value"], overview["total_market_size_projected"]["value"]]
    years = [overview["total_market_size"]["year"], overview["total_market_size_projected"]["year"]]

    plt.figure(figsize=(8, 6))
    plt.plot(years, sizes, marker='o', linestyle='-', color='b')
    plt.title("Market Size Growth (2024-2033)")
    plt.ylabel("Market Size (USD Billion)")
    plt.xlabel("Year")
    plt.grid(True)
    plt.show()

# Visualization 2: Market Segments (Pie Chart)
def plot_market_segments(data):
    segments = data["market_analysis"]["market_overview"]["market_segments"]
    labels = [seg["segment_name"] for seg in segments]
    sizes = [seg["segment_size"] for seg in segments]

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("mako"))
    plt.title("Market Segments")
    plt.show()

# Visualization 3: Competitive Landscape (Horizontal Bar Chart)
def plot_competitive_landscape(data):
    competitors = data["market_analysis"]["competitive_landscape"]["market_share_distribution"]
    labels = [comp["competitor_name"] for comp in competitors]
    shares = [comp["market_share"] for comp in competitors]

    plt.figure(figsize=(8, 6))
    sns.barplot(x=shares, y=labels, palette="coolwarm", orient='h')
    plt.title("Competitive Landscape - Market Share Distribution")
    plt.xlabel("Market Share (%)")
    plt.ylabel("Competitor")
    plt.show()

# Visualization 4: Customer Analysis (Stacked Bar Chart)
def plot_customer_segments(data):
    segments = data["market_analysis"]["customer_analysis"]["target_customer_segments"]
    labels = [seg["segment_name"] for seg in segments]
    sizes = [seg["size"] for seg in segments]

    plt.figure(figsize=(8, 6))
    plt.bar(labels, sizes, color=sns.color_palette("rocket"))
    plt.title("Target Customer Segments")
    plt.xlabel("Segment")
    plt.ylabel("Percentage (%)")
    plt.xticks(rotation=45)
    plt.show()

# Visualization 5: Regional Analysis (Bar Chart)
def plot_regional_analysis(data):
    regions = data["market_analysis"]["regional_analysis"]["regions"]
    labels = [region["region"] for region in regions]
    sizes = [region["market_size"] for region in regions]

    plt.figure(figsize=(8, 6))
    sns.barplot(x=labels, y=sizes, palette="cubehelix")
    plt.title("Regional Market Sizes")
    plt.xlabel("Region")
    plt.ylabel("Market Size (USD Billion)")
    plt.xticks(rotation=45)
    plt.show()

# Main Function to Plot All
def plot_all(data):
    plot_market_growth(data)
    plot_market_segments(data)
    plot_competitive_landscape(data)
    plot_customer_segments(data)
    plot_regional_analysis(data)

if __name__ == "__main__":
    plot_all(data)