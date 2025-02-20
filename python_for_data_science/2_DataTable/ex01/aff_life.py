import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Main function to execute the life expectancy visualization program.

    Loads the life expectancy dataset, extracts data for a specific country,
    and creates a line plot showing the evolution of life expectancy over time.
    The plot includes proper title, axis labels, grid, and formatted axes.

    Returns:
        None
    """
    # Load the dataset
    data = load("life_expectancy_years.csv")
    if data is None:
        return

    # Assuming you're in France (adjust country name as needed)
    country = "France"
    # country = "United States"
    # country = "Japan"
    # country = "Germany"

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
