class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, site, password):
        self.passwords[site] = password

    def get_password(self, site):
        return self.passwords.get(site)

    def remove_password(self, site):
        if site in self.passwords:
            del self.passwords[site]
