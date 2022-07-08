ls = [59,9,11,2]

from itertools import permutations

def largest(l):
	lst = []
	for i in permutations(l, len(l)):

		lst.append("".join(map(str,i)))
	return max(lst)
print(largest(ls))
