from time import time
from os import get_terminal_size

def ft_progress(lst):
	str_info = len("ETA: XXs [XXX%][] XXX/XXX | elapsed time XXX.XXs")
	barlen = int(get_terminal_size().columns * 0.9) - str_info
	if (barlen < 0):
		print("terminal width too small")
		return
	lstlen = len(lst)
	time_start = time()
	eta = 0
	delta = None
	refresh_rate = lstlen / 10
	for i, elem in enumerate(lst, 1):
		ratio = i / lstlen
		percentage = ratio * 100
		bar = ("=" * int(ratio * (barlen - 1))) + ">"
		current_time = time()
		elapsed = current_time - time_start
		if delta is not None:
			eta = delta * (lstlen - i)
		print("\rETA: %.2fs [%3d%%][%-*s] %d/%d | elapsed time %.2fs"
			%(eta, percentage, barlen, bar, i, lstlen, elapsed), end="")
		yield(elem)
		if delta is None or (i % refresh_rate) == 0:
			delta = time() - current_time

