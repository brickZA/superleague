from collections import defaultdict

# TODO check what pep-8 says about close brakets

def parse_team_score(team_score):
    """Parse a single team score to a team name and integer score

    Parameters
    ----------

    team_score : str
        e.g. "Team A 3"

    Returns
    -------

    (team_name, score)
    team_name : str
        e.g. "Team A"
    score : int
        e.g. 3

    """
    team_name, score = team_score.rsplit(' ', 1)
    score = int(score)
    team_name = team_name.strip()

    return team_name, score

def parse_line(line):
    """Parse input line containing a match result

    Parameters
    ----------
    line: str
        e.g. "Tarantulas 1, FC Awesome 0\n"

    Returns
    -------
    ((team_a, score_a), (team_b, score_b))
    team_a/b : str
        Name of team a/b, e.g. "Tarantuals" or "FC Awesome"
    score_a/b : int
        Number of goals scored by team a/b, e.g. 1 or 0.

    """
    team_score1, team_score2 = line.strip().split(',')
    return tuple(
        parse_team_score(tscore.strip())
        for tscore in (team_score1, team_score2))



def calculate_scores(lines):
    points = defaultdict(lambda : 0)
    draw_points = 1
    win_points = 3

    for line in lines:
        # Note, python file iterator takes care of platform differences in line
        # endings
        if not line.strip():
            continue        # Skip empty lines

        # Get the team names and points for the current line
        ((team_a, score_a),
         (team_b, score_b)) = parse_line(line)

        # Access both teams to ensure that they are initialised to zero in case
        # the team never scores any points
        points[team_a]
        points[team_b]

        if score_a > score_b:
            points[team_a] += win_points
        elif score_b < score_a:
            points[team_b] += win_points
        elif score_a == score_b:
            points[team_a] += draw_points
            points[team_b] += draw_points

    return points

def rank_scores(points):
    sorted_rankings = sorted(
        points.items(), key=lambda item: (-item[1], item[0]))
    ranking = 1
    prev_score = None
    prev_ranking = 1
    ranking_output = []
    for i, (team, points_score) in enumerate(sorted_rankings, 1):
        if points_score == prev_score:
            ranking = prev_ranking
        else:
            ranking = i
        prev_score = points_score
        prev_ranking = ranking
        ranking_output.append((ranking, team, points_score))
    return ranking_output
