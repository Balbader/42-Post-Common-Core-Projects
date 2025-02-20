import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def ft_transpose(array):
    """Manually transpose a 2D array without using numpy.transpose.

    Args:
        array (np.ndarray): 2D array to transpose

    Returns:
        np.ndarray: Transposed array
    """
    height, width = array.shape
    transposed = np.zeros((width, height), dtype=array.dtype)

    for i in range(height):
        for j in range(width):
            transposed[j][i] = array[i][j]

    return transposed


def rotate(image_path="animal.jpeg"):
    """Load an image, cut a square part, and transpose it.

    Args:
        image_path (str, optional): Path to the image file.
        Defaults to "animal.jpeg".

    Raises:
        FileNotFoundError: If the image file is not found
        ValueError: If the file format is not supported
        Exception: For other unexpected errors
    """
    try:
        # Check file extension
        valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
        file_extension = image_path.lower()[image_path.rfind('.'):]
        if file_extension not in valid_extensions:
            raise ValueError(f"Unsupported file format. Supported formats: \
                            {', '.join(valid_extensions)}")

        # Load the image
        img = Image.open(image_path)
        img_array = np.array(img)

        # Create square version (center crop)
        height, width = img_array.shape[:2]
        center_y, center_x = height // 2, width // 2
        size = 200  # Half of the desired 400x400 output
        square = img_array[center_y-size:center_y+size,
                           center_x-size:center_x+size]

        # Convert to grayscale
        grayscale = np.mean(square, axis=2, keepdims=True).astype(np.int32)

        # Print original shape and data
        print(f"The shape of image is: {grayscale.shape} or \
({grayscale.shape[0]}, {grayscale.shape[1]})")
        print(grayscale)

        # Transpose the image manually
        transposed = ft_transpose(grayscale[:, :, 0])

        # Print new shape and data
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        # Display the transposed image
        plt.imshow(transposed, cmap='gray')
        plt.title("Transposed Image")
        plt.axis('on')
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    rotate()
