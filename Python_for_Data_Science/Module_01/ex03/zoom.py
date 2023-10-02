from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def slice_me(array: np.ndarray, x: int, y: int, size: int) -> np.ndarray:
    """This function slices the np.ndarray as zoom square np.ndarray"""
    return array[y:(y + size), x:(x + size)]


def main():
    try:
        animal = ft_load("../animal.jpeg")
        assert animal is not None, "load error"

        slice_animal = slice_me(animal, 450, 100, 400)
        print(animal)
        print("New shape after slicing:", slice_animal.shape,
              "or", slice_animal.shape[:2])
        print(slice_animal)

        plt.figure()
        plt.imshow(slice_animal)  # without graphical interface don't show
        plt.savefig("zoom.jpeg")
        plt.show()
        plt.close()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
