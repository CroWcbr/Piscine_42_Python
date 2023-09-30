from os import get_terminal_size


def print_prog(current: int, total: int, barlen: int):
    '''Helper function that updates and prints the bar'''
    str_info = len("100%") + len("/") + 2 * len(str(total))
    barlen -= str_info
    percentage = int(current / total * 100)
    per_str = str(percentage).rjust(3)
    bar_pc = int(barlen * (percentage / 100))
    bar_prog = "{}{}".format("█" * bar_pc, " " * (barlen - bar_pc))
    print(f"\r{per_str}%|{bar_prog}|{current}/{total}", end="")


def ft_tqdm(lst: range) -> None:
    '''This function is the same the tqdm function'''
    barlen = int(get_terminal_size().columns * 0.9)
    total = len(lst)
    for current in lst:
        yield
        print_prog(current, total, barlen)
    print_prog(total, total, barlen)
