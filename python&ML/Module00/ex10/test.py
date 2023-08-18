from time import sleep
from loading import ft_progress

print("Test1:")
listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	sleep(0.01)
print()
print(ret)

print("Test2:")
listy = range(3333)
ret = 0
for elem in ft_progress(listy):
	ret += elem
	sleep(0.005)
print()
print(ret)
