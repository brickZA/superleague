import argparse

from sys import stdin, stdout, stderr
from collections import defaultdict

# TODO check what pep-8 says about close brakets

def parse_team_score(team_score):
    try:
        team_name, score = team_score.rsplit(team_score, 1)
    except ValueError:
        print >> stderr, ('Team scores should be in the format:\n\n'
                          '"Team Name 5",\n\nwhere 5 is the number of goals '
                          'scored. You provided:\n\n{!r}'.format(team_score))
    team_name = team_name.strip()
    return team_name, score

def parse_line(line):
    try:
        team_score1, team_score2 = line.strip().split(',')
    except ValueError:
        print >> stderr, (
            'Game results should be in the format:\n\n'
            '"Team A 3, Team B 1",\n\n where 3 and 1 are the number of goals '
            'scored by the respective teams. You provided:\n\n'
            '{!r}'.format(line))
    return [
        process_team_score(tscore)
        for tscore in (team_score1, team_score2)]



# def process(fd_in, fd_out):
#     scores = defaultdict(lambda : 0)
#     for line in fd_in:
