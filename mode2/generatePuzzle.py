
import random


def generate()->list[list[int]]:
    puzzle = []

    
    rows=[[] for _ in range(9) ]
    cols=[[] for _ in range(9) ]

    blocks = [[[] for b in range(3)] for a in range(3)]

    # print(blocks)
    # print(rows)
    # print(cols)

    

    return puzzle


if __name__=='__main__':
    test = generate()

    for j in range(9):
        for i in range(9):
            print(test[i][j])