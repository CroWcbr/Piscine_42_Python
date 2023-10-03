from typing import Any


def ft_mean(lst) -> float:
    """Calculate mean"""
    return sum(lst) / len(lst)


def ft_variance(lst) -> float:
    """Calculate variance"""
    mean = ft_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)


def ft_standard_deviation(lst) -> float:
    """Calutate standard deviation"""
    return ft_variance(lst) ** .5


def ft_quartile(lst) -> list:
    """Calculate quartile"""
    length = len(lst)
    lst = sorted(lst)
    return [lst[length // 4], lst[3 * length // 4]]


def ft_median(lst) -> float:
    """Calculate median"""
    length = len(lst)
    lst = sorted(lst)
    mid = length // 2
    median = lst[mid]
    if length % 2 == 0:
        median = (lst[mid - 1] + median) / 2
    return median


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """calulat the Mean, Median, Quartile (25% and 75%),
Standard Deviation and Variance"""
    if len(args) == 0:
        print('ERROR\n' * len(kwargs), end='')
        return

    for all in kwargs.values():
        match all:
            case 'mean':
                result = ft_mean(args)
            case 'median':
                result = ft_median(args)
            case 'quartile':
                result = ft_quartile(args)
            case 'std':
                result = ft_standard_deviation(args)
            case 'var':
                result = ft_variance(args)
            case _:
                continue
        print(f"{all} : {result}")
