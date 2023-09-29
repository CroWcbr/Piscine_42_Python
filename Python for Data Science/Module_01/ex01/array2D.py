import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """This function takes as parameters a 2D array, prints its shape,
and returns a truncated version of the array based on the provided
start and end arguments."""

    assert isinstance(family, list), "family must be a list"

    np_family = np.array(family)
    slice_np_family = np_family[slice(start, end)]
    print("My shape is :", np_family.shape)
    print("My new shape is :", slice_np_family.shape)
    return slice_np_family.tolist()
