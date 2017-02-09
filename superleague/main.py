import sys, os

from superleague.rankings import (calculate_scores,
                                  rank_scores)

def main():
    if len(sys.argv) > 1:
        script_name = os.path.basename(sys.argv[0])
        print "Usage E.g: cat input.csv | {} > output.txt".format(
            sys.argv[0])
        sys.exit(1)

    point_scores = calculate_scores(sys.stdin)
    rankings = rank_scores(point_scores)
    for rank, name, points in rankings:
        # Note, python print statement takes care of platform differences in
        # line endings
        print "{}. {}, {} {}".format(
            rank, name, points, 'pts' if points != 1 else 'pt')
