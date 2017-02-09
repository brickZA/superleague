import unittest

from superleague import rankings

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
