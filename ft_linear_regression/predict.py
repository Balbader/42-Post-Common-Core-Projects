import numpy as np

def estimate_price(mileage, theta0, theta1, mileage_mean, mileage_std):
    # Normalize the input mileage
    normalized_mileage = (mileage - mileage_mean) / mileage_std
    return theta0 + (theta1 * normalized_mileage)

def load_parameters():
    try:
        # Load theta values and normalization parameters from file
        params = np.loadtxt('theta_values.txt')
        return params[0], params[1], params[2], params[3], params[4], params[5]
    except:
        print("Error: Could not load model parameters")
        return 0, 0, 0, 1, 0, 1

def main():
    # Load trained parameters
    theta0, theta1, mileage_mean, mileage_std, price_mean, price_std = load_parameters()

    try:
        # Get mileage input from user
        mileage = float(input("Enter mileage of the car: "))
        if mileage < 0:
            print("Error: Mileage cannot be negative")
            return

        # Calculate and display estimated price
        estimated_price = estimate_price(mileage, theta0, theta1, mileage_mean, mileage_std)
        # Denormalize the price
        final_price = estimated_price * price_std + price_mean
        print(f"Estimated price for {mileage} miles: ${final_price:,.2f}")

    except ValueError:
        print("Error: Please enter a valid number for mileage")

if __name__ == "__main__":
    main()
