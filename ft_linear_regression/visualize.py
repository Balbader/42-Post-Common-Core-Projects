import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from predict import estimate_price, load_parameters
from train import load_data


def plot_regression():
    # Load the data
    try:
        mileages, prices = load_data('data.csv')
    except Exception as e:
        print(f"Error: Could not load data for visualization: {e}")
        return

    # Load model parameters
    theta0, theta1, mileage_mean, mileage_std, price_mean, price_std\
        = load_parameters()

    # Create prediction line
    x = np.linspace(min(mileages), max(mileages), 100)
    y = [estimate_price(xi, theta0, theta1, mileage_mean, mileage_std)
         * price_std + price_mean
         for xi in x]

    # Calculate R-squared score
    y_pred = [estimate_price(m, theta0, theta1, mileage_mean, mileage_std)
              * price_std + price_mean
              for m in mileages]
    r2 = r2_score(prices, y_pred)

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.scatter(mileages, prices, color='blue', alpha=0.5, label='Data points')
    plt.plot(x, y, color='red', label='Regression line')

    plt.title('Car Price vs Mileage Linear Regression')
    plt.xlabel('Mileage')
    plt.ylabel('Price ($)')

    # Add R-squared value to plot
    plt.text(0.05, 0.95, f'R² Score: {r2:.4f}',
             transform=plt.gca().transAxes,
             bbox=dict(facecolor='white', alpha=0.8))

    plt.legend()
    plt.grid(True, alpha=0.3)

    # Save the plot
    plt.savefig('regression_plot.png')
    plt.close()

    # Print metrics
    print("\nModel Performance Metrics:")
    print(f"R² Score: {r2:.4f}")

    # Calculate Mean Absolute Error (MAE)
    mae = np.mean(np.abs(np.array(y_pred) - prices))
    print(f"Mean Absolute Error: ${mae:,.2f}")

    # Calculate Mean Squared Error (MSE)
    mse = np.mean((np.array(y_pred) - prices) ** 2)
    print(f"Mean Squared Error: ${mse:,.2f}")

    # Calculate Root Mean Squared Error (RMSE)
    rmse = np.sqrt(mse)
    print(f"Root Mean Squared Error: ${rmse:,.2f}")


if __name__ == "__main__":
    plot_regression()
