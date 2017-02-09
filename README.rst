===========
Superleague
===========

Calculates soccer league tables.

Rules
=====

A draw (tie) is worth 1 point and a win is worth 3 points. A loss is worth 0
points.  If two or more teams have the same number of points, they will have
the same rank and will be printed in alphabetical order.

Usage
=====

Example input ::

  Lions 3, Snakes 3
  Tarantulas 1, FC Awesome 0
  Lions 1, FC Awesome 1
  Tarantulas 3, Snakes 1
  Lions 4, Grouches 0

Example output ::

  1. Tarantulas, 6 pts
  2. Lions, 5 pts
  3. FC Awesome, 1 pt
  3. Snakes, 1 pt
  5. Grouches, 0 pts

Assuming the input is in a file named input.csv ::

  cat input.csv | superleague

Installation
============

If the source is checked out in the current directory ::

  pip install .

Running tests
-------------

After installation run ::

  python setup.py test
