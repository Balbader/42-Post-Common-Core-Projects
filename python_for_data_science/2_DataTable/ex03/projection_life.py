from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Visualizes the relationship between GDP per capita and life expectancy
    in 1900.

    Creates a scatter plot comparing the GDP per capita(adjusted for inflation)
    against life expectancy for different countries in the year 1900.
    The GDP values are displayed on a logarithmic scale for bettervisualization
    of the wide range of values.

    The function:
    - Loads two CSV datasets: income data and life expectancy data
    - Extracts data for the year 1900
    - Creates a scatter plot with GDP per capita on x-axis and life expectancy
      on y-axis
    - Adds appropriate labels, title, and grid

    Returns:
        None
    """
    # Load the datasets
    income_data =\
        load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy_data =\
        load("life_expectancy_years.csv")

    if income_data is None or life_expectancy_data is None:
        print("Error: Failed to load data")
        return

    # Get data for the year 1900
    income_1900 = income_data['1900']
    life_expectancy_1900 = life_expectancy_data['1900']

    # Create the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(income_1900, life_expectancy_1900, alpha=0.5)
    plt.xscale('log')  # Use log scale for income as GDP values can vary widely

    # Add labels and title
    plt.xlabel('GDP per capita ($ adjusted for inflation)')
    plt.ylabel('Life Expectancy (years)')
    plt.title('Life Expectancy vs GDP per Capita in 1900')

    # Add grid for better readability
    plt.grid(True, alpha=0.3)
    plt.show()


if __name__ == "__main__":
    main()
