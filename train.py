import numpy as np

def estimate_price(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)

def train_model(mileages, prices, learning_rate=0.1, epochs=1000):
    m = len(mileages)  # m is the number of training examples
    theta0, theta1 = 0, 0

    for _ in range(epochs):
        # Calculate predictions
        predictions = [estimate_price(mileage, theta0, theta1) for mileage in mileages]

        # Calculate temporary theta values
        tmp_theta0 = learning_rate * (1/m) * sum(predictions[i] - prices[i] for i in range(m))
        tmp_theta1 = learning_rate * (1/m) * sum((predictions[i] - prices[i]) * mileages[i] for i in range(m))

        # Simultaneously update theta values
        theta0 = theta0 - tmp_theta0
        theta1 = theta1 - tmp_theta1

    return theta0, theta1

def load_data(filename):
    try:
        data = np.loadtxt(filename, delimiter=',')
        return data[:, 0], data[:, 1]  # mileages, prices
    except:
        print(f"Error: Could not load data from {filename}")
        exit(1)

def save_thetas(theta0, theta1):
    np.savetxt('theta_values.txt', [theta0, theta1])

def main():
    # Load training data
    mileages, prices = load_data('data.csv')

    # Train the model
    theta0, theta1 = train_model(mileages, prices)

    # Save the trained parameters
    save_thetas(theta0, theta1)

    print(f"Training completed!")
    print(f"Theta0: {theta0}")
    print(f"Theta1: {theta1}")

if __name__ == "__main__":
    main()
