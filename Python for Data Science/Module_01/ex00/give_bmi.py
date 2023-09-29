import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
            -> list[int | float]:
    """This function takes 2 lists of integers or floats in input.
It returns a list of BMI values."""
    assert isinstance(height, list) or isinstance(weight, list), \
        "The input must be lists."
    assert len(height) == len(weight), \
        "Unmatched size between height and weight"
    assert all(isinstance(h, (int, float)) for h in height), \
        "all height must be int or float"
    assert all(isinstance(w, (int, float)) for w in weight), \
        "all weight must be int or float"
    assert all(h > 0 for h in height), \
        "all height must be greate 0"
    assert all(w > 0 for w in weight), \
        "all weight must be greate 0"

    np_height = np.array(height)
    np_weight = np.array(weight)
    return (np_weight / (np_height ** 2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """This function accepts a list of integers or floats and an integer
representing a limit as parameters. It returns a list of booleans"""
    assert isinstance(bmi, list), \
        "The input must be lists."
    assert all(isinstance(b, (int, float)) for b in bmi), \
        "all height must be int or float"
    assert all(b > 0 for b in bmi), \
        "all bmi must be greate 0"

    b = np.array(bmi)
    return (b > limit).tolist()
