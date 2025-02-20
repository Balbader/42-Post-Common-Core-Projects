import numpy as np


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    Args:
        array: numpy.ndarray representing the image
    Returns:
        numpy.ndarray: inverted image array
    """
    return 255 - array


def ft_red(array) -> np.ndarray:
    """
    Keeps only the red channel of the image.
    Args:
        array: numpy.ndarray representing the image
    Returns:
        numpy.ndarray: red channel image array
    """
    red = array.copy()
    red[:, :, 1:] = 0  # Set green and blue channels to 0
    return red


def ft_green(array) -> np.ndarray:
    """
    Keeps only the green channel of the image.
    Args:
        array: numpy.ndarray representing the image
    Returns:
        numpy.ndarray: green channel image array
    """
    green = array.copy()
    green[:, :, 0] = 0  # Set red channel to 0
    green[:, :, 2] = 0  # Set blue channel to 0
    return green


def ft_blue(array) -> np.ndarray:
    """
    Keeps only the blue channel of the image.
    Args:
        array: numpy.ndarray representing the image
    Returns:
        numpy.ndarray: blue channel image array
    """
    blue = array.copy()
    blue[:, :, 0:2] = 0  # Set red and green channels to 0
    return blue


def ft_grey(array) -> np.ndarray:
    """
    Converts the image to grayscale.
    Args:
        array: numpy.ndarray representing the image
    Returns:
        numpy.ndarray: grayscale image array
    """
    grey = array.copy()
    grey = (grey[:, :, 0] / 3 + grey[:, :, 1] / 3 + grey[:, :, 2] / 3)
    grey = grey[:, :, None]  # Add channel dimension back
    return grey.repeat(3, axis=2)  # Repeat the values across all channels
