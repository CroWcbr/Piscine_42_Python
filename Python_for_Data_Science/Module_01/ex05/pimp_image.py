import numpy as np
import matplotlib.pyplot as plt


def display(image: np.ndarray):
    '''Displays image.'''
    # print("The shape of image is: ", image.shape)
    plt.imshow(image)
    plt.axis('off')
    plt.show()


def ft_invert(image: np.ndarray) -> np.ndarray:
    """This function inverts the color."""
    inverted_image = 255 - image
    display(inverted_image)
    return inverted_image


def ft_red(image: np.ndarray) -> np.ndarray:
    """This function keeps only the red color."""
    red_channel = image.copy()
    red_channel[:, :, 1] = 0
    red_channel[:, :, 2] = 0
    display(red_channel)
    return red_channel


def ft_green(image: np.ndarray) -> np.ndarray:
    """This function keeps only the green color."""
    green_channel = image.copy()
    green_channel[:, :, 0] = 0
    green_channel[:, :, 2] = 0
    display(green_channel)
    return green_channel


def ft_blue(image: np.ndarray) -> np.ndarray:
    """This function keeps only the blue color."""
    blue_channel = image.copy()
    blue_channel[:, :, 0] = 0
    blue_channel[:, :, 1] = 0
    display(blue_channel)
    return blue_channel


def ft_grey(image: np.ndarray) -> np.ndarray:
    """This function transforms in a grey scale."""
    grey_channel = (image[:, :, 0] / 3 + image[:, :, 1] / 3 + image[:, :, 2] / 3).astype(np.uint8)
    grey_image = np.stack([grey_channel, grey_channel, grey_channel], axis=2)
    display(grey_image)
    return grey_image
