import unittest

from superleague import rankings

class test_parse_team_score(unittest.TestCase):
    VALID_INPUTS = (
        'Team A 1', 'Otherteam 123',
        'The Bestest Team on Earth   912345')

    EXPECTED_VALID_OUTPUTS = (
        ('Team A', 1), ('Otherteam', 123),
        ('The Bestest Team on Earth', 912345))

    def test_parse_team_score(self):
         for input_val, desired_output in zip(
                 self.VALID_INPUTS, self.EXPECTED_VALID_OUTPUTS):
             actual_output = rankings.parse_team_score(input_val)
             self.assertEqual(actual_output, desired_output)
