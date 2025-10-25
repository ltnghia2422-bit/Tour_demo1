
import json
from config import PROMOTIONS_FILE

def load_promotions():
    try:
        with open(PROMOTIONS_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def get_all_promotions():
    return load_promotions()
