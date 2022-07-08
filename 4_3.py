def login_function(login, passwd): 
	secret_info = 42
	import json
	with open('users.json', 'r') as f:
		users = json.load(f)
	if login in users.keys() and passwd == users[login]:
		print('Correct, secret info is: ', secret_info)
	else:
		print("Login / password don't match or login doesn't exist")
login_function(input('Insert login: '), input('Insert password: '))