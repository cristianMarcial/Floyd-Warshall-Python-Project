from sys import argv
import ast, floydWarshallAlgorithm as fw

# Example of an valid input: py main.py [[0,3,inf,7],[8,0,2,inf],[5,inf,0,1],[2,inf,inf,0]] 1
# Expected result: [[0, 3, inf, 7], [8, 0, 2, 15], [5, 8, 0, 1], [2, 5, inf, 0]]

#try:
if(len(argv) > 1):
    print(fw.output(ast.literal_eval(argv[1].replace('inf', 'None')), ast.literal_eval(argv[2])))
else:
    print("Invalid input; this only works with more than 3 inputs on the command line.")
# except:
#     print('An error has ocurred while reading the previous input.')