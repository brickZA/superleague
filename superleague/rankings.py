import argparse

from sys import stdin, stdout
from collections import defaultdict

# TODO check what pep-8 says about close brakets

def parse_team_score(team_score):
    team_name, score = team_score.rsplit(' ', 1)
    score = int(score)
    team_name = team_name.strip()

    return team_name, score

def parse_line(line):
    team_score1, team_score2 = line.strip().split(',')
    return tuple(
        parse_team_score(tscore.strip())
        for tscore in (team_score1, team_score2))



# def process(fd_in, fd_out):
#     scores = defaultdict(lambda : 0)
#     for line in fd_in:
#         if not line:
#             continue
