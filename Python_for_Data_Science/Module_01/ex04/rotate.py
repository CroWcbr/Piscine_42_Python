from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def zoom(array: np.ndarray, x: int, y: int, size: int) -> np.ndarray:
    """This function slices the np.ndarray as zoom square np.ndarray"""
    return array[y:(y + size), x:(x + size)]


def grayscaling(image: np.ndarray) -> np.ndarray:
    """This function grayscaled image"""
    return np.array(np.mean(image, -1))


def transposing(image: np.ndarray) -> np.ndarray:
    """This function transposed image"""
    transposed_image = np.empty((400, 400), dtype=np.int32)
    for i in range(400):
        for j in range(400):
            transposed_image[i][j] = image[j][i]
    return transposed_image
    # return np.transpose(image, (1, 0)).astype(int)


def main():
    """This function cut a square part from"""
    try:
        animal = ft_load("../animal.jpeg")
        assert animal is not None, "load error"
        animal = zoom(animal, 450, 100, 400)
        animal = grayscaling(animal)
        animal = transposing(animal)

        print(animal)
        print("New shape after slicing:", animal.shape,
              "or", animal.shape[:2])
        print(animal)
        plt.figure()
        plt.imshow(animal, cmap="gray")  # without graphic interface don't show
        plt.savefig("zoom.jpeg")
        plt.show()
        plt.close()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
