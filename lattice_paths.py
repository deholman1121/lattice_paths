import math

'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes exist for a 20 x 20 grid?

To move from the top left corner of an n x n grid to the bottom right corner, you need to 
move right n times and down n times. In total, 2n moves. You can make those moves in any order,
which means you have (2n)! ways of doing the moves. However, you are restricted to the order in which
you can conduct the moves. E.g. you have to move from row 4 to row 5, before you can move from row 5 
to row 6. Of the n! moves to the right can be ordered, only one is valid. Same goes for moving down.
This gives us:
  (2n)!
--------
(n!)(n!) 

'''


def get_lattice_paths(n):
    return int(math.factorial(2 * n)/(math.factorial(n) * math.factorial(n)))


if __name__ == '__main__':
    print(f'2 x 2 grid: {get_lattice_paths(20)}')
