import matplotlib.pyplot as plt
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


def display_image(image, title):
    """Display an image with its title"""
    plt.figure(figsize=(5, 5))
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()


def main():
    # Load the image
    array = ft_load("landscape.jpg")
    print("The shape of image is:", array.shape)
    print(array)

    # Display original and transformed images
    display_image(array, "Original")
    display_image(ft_invert(array), "Inverted")
    display_image(ft_red(array), "Red Channel")
    display_image(ft_green(array), "Green Channel")
    display_image(ft_blue(array), "Blue Channel")
    display_image(ft_grey(array), "Greyscale")

    # Print docstring
    print(ft_invert.__doc__)
    print(ft_red.__doc__)
    print(ft_green.__doc__)
    print(ft_blue.__doc__)
    print(ft_grey.__doc__)


if __name__ == "__main__":
    main()
