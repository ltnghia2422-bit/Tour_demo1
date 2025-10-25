
class Review:
    def __init__(self, tour_id, review_text, rating, username='Anonymous'):
        self.tour_id = tour_id
        self.review_text = review_text
        self.rating = rating
        self.username = username
