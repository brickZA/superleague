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



def calculate_scores(lines):
    scores = defaultdict(lambda : 0)
    draw_points = 1
    win_points = 3

    for line in lines:
        if not line:
            continue        # Skip empty lines

        # Get the team names and scores for the current line
        ((team_a, score_a),
         (team_b, score_b)) = parse_line(line)

        # Access both teams to ensure that they are initialised to zero in case
        # the team never scores any points
        scores[team_a]
        scores[team_b]

        if score_a > score_b:
            scores[team_a] += win_points
        elif score_b < score_a:
            scores[team_b] += win_points
        elif score_a == score_b:
            scores[team_a] += draw_points
            scores[team_b] += draw_points

    return scores
