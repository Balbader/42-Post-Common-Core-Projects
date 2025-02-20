import pandas as pd
import matplotlib.pyplot as plt


def load(path: str) -> pd.DataFrame:
    """Load a dataset from a CSV file and return a pandas DataFrame."""
    try:
        data = pd.read_csv(path)
        print("Loading dataset of dimensions", data.shape)
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None


def main():
    # Load the dataset
    data = load("life_expectancy_years.csv")
    if data is None:
        return

    # Assuming you're in France (adjust country name as needed)
    country = "France"

    # Get the data for the country
    country_data = data.loc[data['country'] == country]

    if country_data.empty:
        print(f"No data found for {country}")
        return

    # Convert columns to numeric, excluding the 'country' column
    years = country_data.columns[1:].astype(int)
    life_expectancy = country_data.iloc[0, 1:].astype(float)

    # Create the plot
    plt.figure(figsize=(12, 6))
    plt.plot(years, life_expectancy, marker='o')

    # Customize the plot
    plt.title(f'Life Expectancy Over Time in {country}')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy (years)')
    plt.grid(True, linestyle='--', alpha=0.7)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

    # Display the plot
    plt.show()


if __name__ == "__main__":
    main()
