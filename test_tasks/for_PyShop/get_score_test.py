'''Для разработанной в предыдущем задании функции get_score(game_stamps,
offset) разработайте unit-тесты на фреймворке unittest.
Тесты должны учитывать все возможные случаи использования функции,
концентрироваться на проверке одного случая, не повторяться, название тестов
должно отражать суть выполняемой проверки.'''

from unittest import main, TestCase
from get_score import get_score


class GetScoreTest(TestCase):

    def test_game_start(self):
        offsets_case = (0, 3, 4, 5)
        home_scores_case = (0, 1, 2, 2)
        away_scores_case = (0, 0, 0, 1)
        game_stamps_case = [
            {
                "offset": off,
                "score":
                    {
                        "home": home,
                        "away": away
                        }
                    }
            for off, home, away
            in zip(offsets_case, home_scores_case, away_scores_case)
            ]
        self.assertEqual(get_score(game_stamps_case, 0), (0, 0))

    def test_game_end(self):
        offsets_case = (0, 2, 5, 7)
        home_scores_case = (0, 0, 1, 1)
        away_scores_case = (0, 1, 1, 2)
        game_stamps_case = [
            {
                "offset": off,
                "score":
                    {
                        "home": home,
                        "away": away
                        }
                    }
            for off, home, away
            in zip(offsets_case, home_scores_case, away_scores_case)
            ]
        self.assertEqual(get_score(game_stamps_case, 7), (1, 2))

    def test_game_middle(self):
        offsets_case = (0, 1, 2, 4)
        home_scores_case = (0, 0, 1, 2)
        away_scores_case = (0, 0, 0, 0)
        game_stamps_case = [
            {
                "offset": off,
                "score":
                    {
                        "home": home,
                        "away": away
                        }
                    }
            for off, home, away
            in zip(offsets_case, home_scores_case, away_scores_case)
            ]
        self.assertEqual(get_score(game_stamps_case, 2), (1, 0))

    def test_missing_offset(self):
        offsets_case = (0, 3, 6, 8)
        home_scores_case = (0, 0, 1, 1)
        away_scores_case = (0, 1, 1, 2)
        game_stamps_case = [
            {
                "offset": off,
                "score":
                    {
                        "home": home,
                        "away": away
                        }
                    }
            for off, home, away
            in zip(offsets_case, home_scores_case, away_scores_case)
            ]
        self.assertEqual(get_score(game_stamps_case, 5), (0, 1))

    def test_after_game_end(self):
        offsets_case = (0, 3, 5, 6)
        home_scores_case = (0, 1, 2, 3)
        away_scores_case = (0, 0, 0, 0)
        game_stamps_case = [
            {
                "offset": off,
                "score":
                    {
                        "home": home,
                        "away": away
                        }
                    }
            for off, home, away
            in zip(offsets_case, home_scores_case, away_scores_case)
            ]
        self.assertEqual(get_score(game_stamps_case, 100), (3, 0))

    def test_guessing_index(self):
        offsets_case = tuple(range(0, 90_001, 3))
        home_scores_case = (0,) * 30_001
        away_scores_case = (0,) * 29_000
        away_scores_case += (1,)
        away_scores_case += (1,) * 1_000
        game_stamps_case = [
            {
                "offset": off,
                "score":
                    {
                        "home": home,
                        "away": away
                        }
                    }
            for off, home, away
            in zip(offsets_case, home_scores_case, away_scores_case)
            ]
        self.assertEqual(get_score(game_stamps_case, 87_001), (0, 1))


if __name__ == "__main__":
    main()
