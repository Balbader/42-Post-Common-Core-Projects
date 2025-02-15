import numpy as np

def estimate_price(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)

def load_thetas():
    try:
        # Load theta values from file
        thetas = np.loadtxt('theta_values.txt')
        return thetas[0], thetas[1]
    except:
        # Return default values if file doesn't exist
        return 0, 0

def main():
    # Load trained parameters
    theta0, theta1 = load_thetas()

    try:
        # Get mileage input from user
        mileage = float(input("Enter mileage of the car: "))
        if mileage < 0:
            print("Error: Mileage cannot be negative")
            return

        # Calculate and display estimated price
        estimated_price = estimate_price(mileage, theta0, theta1)
        print(f"Estimated price for {mileage} miles: ${estimated_price:,.2f}")

    except ValueError:
        print("Error: Please enter a valid number for mileage")

if __name__ == "__main__":
    main()
