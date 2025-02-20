import os
import sys
import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Load an image from a file and return it as a numpy array.

    Args:
        path (str): The path to the image file

    Returns:
        np.ndarray: The image as a numpy array

    Raises:
        FileNotFoundError: If the image file doesn't exist
        ValueError: If the file is not a valid image
        Exception: For other unexpected errors
    """
    try:
        # Check if file exists
        if not os.path.exists(path):
            raise FileNotFoundError(f"Error: No such file: '{path}'")

        # Check file extension
        ext = os.path.splitext(path)[1].lower()
        if ext not in ['.jpg', '.jpeg']:
            raise ValueError("Error: Unsupported image format.\
                             Only JPG/JPEG supported")

        # Load and convert image to numpy array
        img = np.array(Image.open(path))

        # Print image shape
        print(f"The shape of image is: {img.shape}")

        return img

    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(f"Error: Failed to load image: {str(e)}")
        sys.exit(1)
