# ft_linear_regression

This project is a simple linear regression model implemented in Python. It allows users to train a linear regression model on a dataset and then use it to predict the price of a car based on its mileage.

## Features

- Train a linear regression model on a dataset
- Use the model to predict the price of a car based on its mileage
- Visualize the training process and the model's performance

## Installation

```bash
pip install numpy matplotlib scikit-learn
```

## Usage

```bash
python train.py
```

```bash
python predict.py
```

## Visualization

```bash
python visualize.py
```

## How it works
- Train the model

- Create a plot showing:
  - Original data points in blue
  - Regression line in red
  - R² score in the top-left corner

- Save the plot as 'regression_plot.png'

- Display performance metrics including:
  - R² Score (coefficient of determination)
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
  - Root Mean Squared Error (RMSE)

You can also run the visualization separately:

The R² score will tell you how well your model fits the data:
- R² = 1.0 indicates a perfect fit
- R² = 0.0 indicates the model is no better than a horizontal line
- Negative R² indicates the model performs worse than a horizontal line

The other metrics (MAE, MSE, RMSE) give you the average prediction error in dollars, with RMSE penalizing large errors more heavily than MAE.
