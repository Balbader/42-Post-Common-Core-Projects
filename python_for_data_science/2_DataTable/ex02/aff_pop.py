import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Visualizes population growth comparison between two countries
    (France and Spain)
    from 1800 to 2050 using data from population_total.csv.
    The function loads the data, processes it, and creates a line plot showing
    the population trends for both countries over time.
    """
    # Load the data
    data = load("../resources/population_total.csv")
    if data is None:
        return

    # Select countries to compare (France and Spain as examples)
    country1 = "France"
    country2 = "Spain"

    # Get the data for selected countries
    try:
        country1_data = data.loc[country1]
        country2_data = data.loc[country2]

        # Convert years to numeric and filter for 1800-2050
        years = [year for year in country1_data.index
                 if year.isdigit() and 1800 <= int(year) <= 2050]

        # Convert population values to numeric, removing 'M' and 'k' suffixes
        def convert_population(value):
            if isinstance(value, str):
                if value.endswith('M'):
                    return float(value[:-1]) * 1000000
                elif value.endswith('k'):
                    return float(value[:-1]) * 1000
            return float(value)

        pop1 = [convert_population(country1_data[year]) for year in years]
        pop2 = [convert_population(country2_data[year]) for year in years]

        # Create the plot
        plt.figure(figsize=(12, 6))
        plt.plot(years, pop1, label=country1, marker='o')
        plt.plot(years, pop2, label=country2, marker='o')

        # Customize the plot
        plt.title(f'Population Growth: {country1} vs {country2} (1800-2050)')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.legend()
        plt.grid(True)

        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)

        # Format y-axis labels to show millions
        plt.gca().yaxis.set_major_formatter(
            plt.FuncFormatter(lambda x, p: f'{int(x/1000000)}M'))

        plt.tight_layout()
        plt.show()

    except KeyError as e:
        print(f"Error: Country not found in dataset - {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
