from sys import argv
from ast import literal_eval
import floydWarshallAlgorithm as fw

# Example of an valid input: py main.py [[0,3,inf,7],[8,0,2,inf],[5,inf,0,1],[2,inf,inf,0]] 1

# Expected result: [[0, 3, inf, 7], [8, 0, 2, 15], [5, 8, 0, 1], [2, 5, inf, 0]]
 
try:
    if len(argv) > 1:
        print(str(fw.output(literal_eval(argv[1].replace('inf', 'None')), literal_eval(argv[2]))).replace('None', 'inf'))
    else:
        print("Invalid input; this only works with more than 3 inputs on the command line.")
except:
    print('An error has ocurred while reading the previous input.')

# Tests cases:

#1 py main.py [[0,inf,-2,inf],[4,0,3,inf],[inf,inf,0,2],[inf,-1,inf,0]] 4
#2 python3 floyd.py [[0,3,inf,7],[8,0,2,inf],[5,inf,0,1],[2,inf,inf,0]] 1-4 OR
# py main.py [[0,3,inf,7],[8,0,2,inf],[5,inf,0,1],[2,inf,inf,0]] 4

# results of #2:
    #[[0, 3, inf, 7], [8, 0, 2, 15], [5, 8, 0, 1], [2, 5, inf, 0]]
    #[[0, 3, 5, 7], [8, 0, 2, 15], [5, 8, 0, 1], [2, 5, 7, 0]]
    #[[0, 3, 5, 6], [7, 0, 2, 3], [5, 8, 0, 1], [2, 5, 7, 0]]
    #[[0, 3, 5, 6], [5, 0, 2, 3], [3, 6, 0, 1], [2, 5, 7, 0]]