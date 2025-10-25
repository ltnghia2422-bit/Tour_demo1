
import json
from config import REVIEWS_FILE

def load_reviews():
    try:
        with open(REVIEWS_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def get_reviews_for_tour(tour_id):
    reviews = load_reviews()
    return [r for r in reviews if r['tour_id'] == tour_id]

def add_review(tour_id, review_text, rating, username='Anonymous'):
    reviews = load_reviews()
    reviews.append({
        'tour_id': tour_id,
        'review_text': review_text,
        'rating': rating,
        'username': username
    })
    with open(REVIEWS_FILE, 'w') as f:
        json.dump(reviews, f)
