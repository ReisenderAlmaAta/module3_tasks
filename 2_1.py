l = [1,2,3,'ba' 4,4,'ab', 5,5,'hello', 51, 'hello', 2]
tmp = []
for i in l:
	count = l.count(i)
	if count > 1:
		tmp.append(i)
print(list(set(tmp)))