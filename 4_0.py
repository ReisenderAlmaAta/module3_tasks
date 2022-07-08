import json
users = {}
with open('users.json', 'w') as f:
	json.dump(users, f)