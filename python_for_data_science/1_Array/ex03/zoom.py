import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def zoom_image(image_path="animal.jpeg"):
    """Load an image, display it, and show a zoomed grayscale version.

    This function loads an image from the specified path,
    displays the original image alongside a zoomed and grayscaled
    version of its center portion (400x400 pixels).
    The function also prints the shape information of both the original
    and zoomed arrays.

    Args:
        image_path (str, optional): Path to the image file.
        Defaults to "animal.jpeg".

    Raises:
        FileNotFoundError: If the specified image file cannot be found.
        Exception: For other potential errors during image processing.
    """
    try:
        # Load the image
        img = Image.open(image_path)
        img_array = np.array(img)

        # Print original shape information
        print(f"The shape of image is: {img_array.shape}")
        print(img_array)

        # Create zoomed version (center crop)
        height, width = img_array.shape[:2]
        center_y, center_x = height // 2, width // 2
        size = 200  # Half of the desired 400x400 output
        zoomed = img_array[center_y-size:center_y+size,
                           center_x-size:center_x+size]

        # Convert to grayscale by taking mean across channels
        zoomed = np.mean(zoomed, axis=2, keepdims=True).astype(np.int32)

        # Print zoomed shape information
        print(f"New shape after slicing: \
              {zoomed.shape} or ({zoomed.shape[0]}, {zoomed.shape[1]})")
        print(zoomed)

        # Create figure with two subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        # Display original image
        ax1.imshow(img_array)
        ax1.set_title("Original Image")
        ax1.axis('on')

        # Display zoomed image
        ax2.imshow(zoomed[:, :, 0], cmap='gray')
        ax2.set_title("Zoomed Image")
        ax2.axis('on')

        plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    zoom_image()
