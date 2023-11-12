import json


def task() -> float:
    filename = 'input.json'
    with open(filename) as file:
        json_data = json.load(file)

    weighted_scores = [item['score'] * item['weight'] for item in json_data]
    overall_weighted_score = round(sum(weighted_scores), 3)
    return overall_weighted_score


print(task())
