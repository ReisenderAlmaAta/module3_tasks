# пустой json файл users был создан заранее чтобы избежать перезаписи 
# списка пользователей
def register(login, passwd):
	import json
	with open('users.json', 'r') as f:
		users = json.load(f)
	users[login] = passwd
	with open('users.json', 'w') as f:
		json.dump(users, f)
register(input('Insert login: '), input('insert password: '))
