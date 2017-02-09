import unittest
import StringIO
import pkgutil

from superleague import rankings


# expected scores for test_input.csv data
EXPECTED_SCORES = {
    'Tarantulas': 6,
    'Lions': 5,
    'Another Average Team': 3,
    'Middlers': 3,
    'Zamblers': 3,
    'FC Awesome': 1,
    'Snakes': 1,
    'Grouches': 0,
}

EXPECTED_RANKINGS = (
    (1, 'Tarantulas', 6),
    (2, 'Lions', 5),
    (3, 'Another Average Team', 3),
    (3, 'Middlers', 3),
    (3, 'Zamblers', 3),
    (6, 'FC Awesome', 1),
    (6, 'Snakes', 1),
    (8, 'Grouches', 0)
)



class test_parse_team_score(unittest.TestCase):
    INPUTS = (
        'Team A 1', 'Otherteam 123',
        'The Bestest Team on Earth   912345')

    EXPECTED_OUTPUTS = (
        ('Team A', 1), ('Otherteam', 123),
        ('The Bestest Team on Earth', 912345))

    def test_parse_team_score(self):
         for input_val, desired_output in zip(
                 self.INPUTS, self.EXPECTED_OUTPUTS):
             actual_output = rankings.parse_team_score(input_val)
             self.assertEqual(actual_output, desired_output)

class test_pase_line(unittest.TestCase):
    INPUT_LINES = (
        'Lions 3, Snakes 3\n',
        'Tarantulas 1, FC Awesome 0\n',
        'Lions 1, FC Awesome 1')

    EXPECTED_OUTPUTS = (
        (('Lions', 3), ('Snakes', 3)),
        (('Tarantulas', 1), ('FC Awesome', 0)),
        (('Lions', 1), ('FC Awesome', 1))
    )

    def test_prase_line(self):
         for input_val, desired_output in zip(
                 self.INPUT_LINES, self.EXPECTED_OUTPUTS):
             actual_output = rankings.parse_line(input_val)
             self.assertEqual(actual_output, desired_output)

class test_calculate_scores(unittest.TestCase):
    def setUp(self):
        self.input_file = StringIO.StringIO(pkgutil.get_data(
            'superleague.tests', 'test_input.csv'))

    def test_calculate_scores(self):
        actual_scores = rankings.calculate_scores(self.input_file)
        self.assertEqual(actual_scores, EXPECTED_SCORES)

class test_rank_scores(unittest.TestCase):
    def test_rank_scores(self):
        self.assertEqual(
            rankings.rank_scores(EXPECTED_SCORES), list(EXPECTED_RANKINGS))
