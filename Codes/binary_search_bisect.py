import bisect

list = [2, 5, 8, 9, 15, 20, 60, 86, 96, 102, 106, 205, 536]

result = bisect.bisect_left(list, 86)

print(result)
