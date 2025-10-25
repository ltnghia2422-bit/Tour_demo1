
import json
from config import ACCOUNTS_FILE
from utils.security import hash_password, check_password

def load_accounts():
    try:
        with open(ACCOUNTS_FILE, 'r') as f:
            content = f.read().strip()
            if not content:  # If file is empty
                return {}
            return json.loads(content)
    except FileNotFoundError:
        save_accounts({})
        return {}
    except json.JSONDecodeError:
        return {}

def save_accounts(accounts):
    with open(ACCOUNTS_FILE, 'w') as f:
        json.dump(accounts, f)

def signup(username, password):
    accounts = load_accounts()
    if username in accounts:
        return False
    accounts[username] = hash_password(password)
    save_accounts(accounts)
    return True

def login(username, password):
    accounts = load_accounts()
    return username in accounts and check_password(accounts[username], password)

def get_all_accounts():
    return load_accounts()
