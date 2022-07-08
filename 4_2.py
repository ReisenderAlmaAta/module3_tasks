def register(login, passwd):
	import json
	with open('users.json', 'r') as f:
		users = json.load(f)
	if login not in users.keys():
		users[login] = passwd
		with open('users.json', 'w') as f:
			json.dump(users, f)
	else:
			print('Login is taken, try another login')
register(input('Insert login: '), input('Insert password: '))
