# Task 8: Cyber - Login Attempt Tracker


class Account:
    """A user account that locks after 3 failed logins."""

    MAX_ATTEMPTS = 3

    def __init__(self, username, password):
        """Store the login details and start with no failed attempts."""
        self.username = username
        self.password = password
        self.failed_attempts = 0

    def is_locked(self):
        """Return True if the account is locked."""
        return self.failed_attempts >= Account.MAX_ATTEMPTS

    def login(self, password):
        """Try to log in; return True if the password is right and not locked."""
        if self.is_locked():
            print(f"{self.username}: account locked - login refused.")
            return False
        if password == self.password:
            self.failed_attempts = 0
            print(f"{self.username}: login successful.")
            return True
        self.failed_attempts += 1
        print(f"{self.username}: wrong password ({self.failed_attempts}/{Account.MAX_ATTEMPTS}).")
        return False


account = Account("alice", "s3cret")
account.login("wrong")
account.login("s3cret")        # correct - resets the counter
account.login("bad1")
account.login("bad2")
account.login("bad3")          # third failure locks it
account.login("s3cret")        # refused even though correct
