"""
You have rating (0-10) of the hotels per user in this format:

scores = [
    {'hotel_id': 1001, 'user_id': 501, 'score': 7},
    {'hotel_id': 1001, 'user_id': 502, 'score': 7},
    {'hotel_id': 1001, 'user_id': 503, 'score': 7},
    {'hotel_id': 2001, 'user_id': 504, 'score': 10},
    {'hotel_id': 3001, 'user_id': 505, 'score': 5},
    {'hotel_id': 2001, 'user_id': 506, 'score': 5}
]

Any given hotel might have more than one score.

Implement a function, get_hotels(scores, min_avg_score) that returns a list of hotel ids that have average score equal to or higher than min_avg_score.

get_hotels(scores, 5) -> [1001, 2001, 3001]
get_hotels(scores, 7) -> [1001, 2001]
""" 

