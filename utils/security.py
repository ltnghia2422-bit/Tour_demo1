
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(hashed, password):
    return hashed == hash_password(password)
