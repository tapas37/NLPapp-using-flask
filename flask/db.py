
import json
import os

class database:
    def __init__(self):
        self.file_path = 'users.json'
        if not os.path.exists(self.file_path) or os.path.getsize(self.file_path) == 0:
            with open(self.file_path, 'w') as f:
                json.dump({}, f)

    def insert(self, name, email, password):
        with open(self.file_path, 'r') as rf:
            try:
                users = json.load(rf)
            except json.JSONDecodeError:
                users = {}

        if email in users:
            return 0
        else:
            users[email] = [name, password]
            with open(self.file_path, 'w') as wf:
                json.dump(users, wf, indent=4)
            return 1




    def search(self,email,password):
        with open(self.file_path, 'r') as rf:
            users = json.load(rf)
            if email in users:
                if users[email][1]==password:
                    return 1
                else:
                    return 0
            else:
                return 0



