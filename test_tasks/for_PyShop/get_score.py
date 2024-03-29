'''
В примере кода ниже генерируется список фиксаций состояния счета игры в
течение матча.
Разработайте функцию get_score(game_stamps, offset), которая вернет счет на
момент offset в списке game_stamps.
Нужно суметь понять суть написанного кода, заметить нюансы, разработать
функцию вписывающуюся стилем в существующий код, желательно адекватной
алгоритмической сложности.
'''

from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()

if __name__ == "__main__":
    pprint(game_stamps)


def get_score(game_stamps, offset):
    '''
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.
    '''
    if offset >= game_stamps[-1]["offset"]:

        return game_stamps[-1]["score"]["home"], game_stamps[-1]["score"]["away"]

    guess_index = offset // 3
    while True:
        guess_offset = game_stamps[guess_index]["offset"]
        if offset - guess_offset > 2:
            guess_index = guess_index + ((offset - guess_offset) // 3)
            continue
        index = guess_index
        break
    for num, stmp in enumerate(game_stamps[index:index + 3]):
        if stmp["offset"] > offset:
            return home, away

        home = stmp["score"]["home"]
        away = stmp["score"]["away"]
        if stmp["offset"] == offset or num == 2:

            return home, away
