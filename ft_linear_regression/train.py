import numpy as np

def estimate_price(mileage, theta0, theta1, mileage_mean=0, mileage_std=1):
    # Use normalized mileage for prediction
    normalized_mileage = (mileage - mileage_mean) / mileage_std
    return theta0 + (theta1 * normalized_mileage)

def normalize_data(data):
    mean = np.mean(data)
    std = np.std(data)
    if std == 0:
        std = 1
    return (data - mean) / std, mean, std

def train_model(mileages, prices, learning_rate=0.01, epochs=1000):
    m = len(mileages)  # number of training examples

    # Normalize mileages
    normalized_mileages, mileage_mean, mileage_std = normalize_data(mileages)

    # Normalize prices
    normalized_prices, price_mean, price_std = normalize_data(prices)

    theta0, theta1 = 0, 0

    for epoch in range(epochs):
        # Calculate predictions
        predictions = [estimate_price(mileage, theta0, theta1, mileage_mean, mileage_std)
                        for mileage in mileages]

        # Calculate temporary theta values
        tmp_theta0 = learning_rate * (1/m) * sum(predictions[i] - normalized_prices[i]
                                                for i in range(m))
        tmp_theta1 = learning_rate * (1/m) * sum((predictions[i] - normalized_prices[i])
                                                * normalized_mileages[i] for i in range(m))

        # Simultaneously update theta values
        theta0 = theta0 - tmp_theta0
        theta1 = theta1 - tmp_theta1

        # Print progress every 100 epochs
        if epoch % 100 == 0:
            print(f"Epoch {epoch}: theta0 = {theta0:.4f}, theta1 = {theta1:.4f}")

    # Save normalization parameters along with thetas
    np.savetxt('theta_values.txt', [theta0, theta1, mileage_mean, mileage_std,
                                    price_mean, price_std])

    return theta0, theta1

def load_data(filename):
    try:
        data = np.loadtxt(filename, delimiter=',')
        return data[:, 0], data[:, 1]  # mileages, prices
    except Exception as e:
        print(f"Error: Could not load data from {filename}")
        print(f"Error details: {str(e)}")
        exit(1)

def main():
    # Load training data
    mileages, prices = load_data('data.csv')

    # Train the model
    theta0, theta1 = train_model(mileages, prices)

    print(f"\nTraining completed!")
    print(f"Theta0: {theta0:.4f}")
    print(f"Theta1: {theta1:.4f}")

if __name__ == "__main__":
    main()
