import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def main():
    """
    Visualizes population growth comparison between two countries
    from 1800 to 2050 using data from population_total.csv.
    """
    # Load the data
    data = load("population_total.csv")
    if data is None:
        print("Error: Failed to load data")
        return

    # Select countries to compare
    country1 = "Belgium"
    country2 = "France"

    try:
        # Get the data for selected countries
        country1_data = data.loc[data['country'] == country1]
        country2_data = data.loc[data['country'] == country2]

        if country1_data.empty:
            print(f"No data found for {country1}")
            return
        if country2_data.empty:
            print(f"No data found for {country2}")
            return

        # Convert years to numeric and filter for 1800-2050
        years = [year for year in country1_data.columns
                 if str(year).isdigit() and 1800 <= int(str(year)) <= 2050]

        # Convert population values to numeric, removing 'M' and 'k' suffixes
        def convert_population(value):
            if isinstance(value, (str, pd.Series)):
                # Convert Series to string if necessary
                value = str(value.iloc[0]
                            if isinstance(value, pd.Series) else value)
                if value.endswith('M'):
                    return float(value[:-1]) * 1000000
                elif value.endswith('k'):
                    return float(value[:-1]) * 1000
            return float(value)

        # Extract population data for both countries
        pop1 = [convert_population(country1_data[year]) for year in years]
        pop2 = [convert_population(country2_data[year]) for year in years]

        # Create the plot
        plt.figure(figsize=(10, 6))
        plt.plot(years, pop1, label=country1, marker='.')
        plt.plot(years, pop2, label=country2, marker='.')

        # Customize the plot
        plt.title(f'Population Projections Comparison\n\
                  {country1} vs {country2}')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.legend()
        plt.grid(True)

        # Rotate x-axis labels
        plt.xticks(rotation=45)

        # Format y-axis labels
        # plt.FuncFormatter(lambda x, p: f'{int(x/1000000)}M') :
        # Creates a custom formatter function that:
        # Takes a number x (the original value)
        # and position p (unused in this case)
        # Divides the value by 1,000,000 to convert it to millions
        # Converts it to an integer with int()
        # Adds an 'M' suffix
        # Returns the formatted string
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
