import os
import exceptions

import pkg_resources
import subprocess
import unittest

class test_superleague(unittest.TestCase):
    def test_superleague(self):
        input_file = pkg_resources.resource_stream(
            'superleague.tests', 'test_input.csv')
        try:
            actual_output = subprocess.check_output(
                'superleague', stdin=input_file)
        except exceptions.OSError:
            raise RuntimeError(
                'Cannot do integration test since command "superleague" does '
                'not seem to be installed.')

        expected_output = pkg_resources.resource_string(
            'superleague.tests', 'expected_output.txt')

        self.assertEqual(actual_output, expected_output)
