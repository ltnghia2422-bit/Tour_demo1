
import json
from config import TOURS_FILE

def load_tours():
    try:
        with open(TOURS_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def get_all_tours():
    return load_tours()

def get_tour_by_id(tour_id):
    tours = load_tours()
    for tour in tours:
        if tour['id'] == tour_id:
            return tour
    return None
