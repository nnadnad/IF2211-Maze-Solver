"""
Maze Solver with BFS Algorithm.

Created by:

M.Algah Fattah I / 13517122
Yudy Valentino / 13517128

"""

# !/usr/bin/python
from matplotlib import pyplot as plt
from matplotlib import colors
import sys
# from termcolor import colored

filename = sys.argv[1]
sauce = open("mazes/" + filename).read()
sauce = sauce.split()

maze = []

for i in sauce:
    row = []
    for c in i:
        if c == '0':
            row.append(1)  # grid
        else:
            row.append(0)  # wall
    maze.append(row)


# cc adalah currentCell
# currentCell berupa list dengan dua elemen
# elemen pertama = row, elemen kedua = col

def upOK(cc):
    return (cc[0] > 0 and maze[cc[0] - 1][cc[1]] == 1)


def downOK(cc):
    return (cc[0] < len(maze) - 1 and maze[cc[0] + 1][cc[1]] == 1)


def leftOK(cc):
    return (cc[1] > 0 and maze[cc[0]][cc[1] - 1] == 1)


def rightOK(cc):
    return (cc[1] < len(maze[0]) - 1 and maze[cc[0]][cc[1] + 1] == 1)


def upOf(cc):
    temp = [cc[0] - 1]
    temp.append(cc[1])
    return temp


def downOf(cc):
    temp = [cc[0] + 1]
    temp.append(cc[1])
    return temp


def leftOf(cc):
    temp = [cc[0]]
    temp.append(cc[1] - 1)
    return temp


def rightOf(cc):
    temp = [cc[0]]
    temp.append(cc[1] + 1)
    return temp


def BFS(src, dest):
    # queue = [] #antrian cabang
    # visited = [] #daftar cell yang sudah dikunjungi
    # queue.append(src) #tambahkan ke antrian
    # visited.append(src) #masukkan ke daftar cell yang sudah dikunjungi
    # curpath = []
    # curpath.append(src)
    # path = [] # jalan yang sudah kita tempuh
    # path.append(curpath) #masukkan ke daftar jalan yang sudah kita tempuh

    path = [src]
    queue = []
    queue.append(path)
    visited = []  # daftar cell yang sudah dikunjungi
    visited.append(src)  # masukkan ke daftar cell yang sudah dikunjungi
    while(queue):
        # print "before", queue
        path = queue.pop(0)
        currentCell = path[-1]
        # print "after",queue

        if(currentCell == dest):  # berhenti jika sudah mencapai destinasi
            return path
            # exit()

        if(upOK(currentCell) and upOf(currentCell) not in visited):
            visited.append(upOf(currentCell))  # catat ketika sudah dikunjungi
            temp = [i for i in path] 
            temp.append(upOf(currentCell))
            queue.append(temp)
            # queue.append(upOf(currentCell)) #masukkan ke antrian
            # temp = curpath #
            # temp.append(upOf(currentCell))
            # path.append(temp)
        if(downOK(currentCell) and downOf(currentCell) not in visited):
            visited.append(downOf(currentCell))
            temp = [i for i in path]
            temp.append(downOf(currentCell))
            queue.append(temp)
            # queue.append(downOf(currentCell))
            # temp = curpath
            # temp.append(downOf(currentCell))
            # path.append(temp)
        if(leftOK(currentCell) and leftOf(currentCell) not in visited):
            visited.append(leftOf(currentCell))
            temp = [i for i in path]
            temp.append(leftOf(currentCell))
            queue.append(temp)
            # queue.append(leftOf(currentCell))
            # temp = curpath
            # temp.append(leftOf(currentCell))
            # path.append(temp)
        if(rightOK(currentCell) and rightOf(currentCell) not in visited):
            visited.append(rightOf(currentCell))
            temp = [i for i in path]
            temp.append(rightOf(currentCell))
            queue.append(temp)
            # queue.append(rightOf(currentCell))
            # temp = curpath
            # temp.append(rightOf(currentCell))
            # path.append(temp)

s = [int(i) for i in sys.argv[2].split(',')]
d = [int(i) for i in sys.argv[3].split(',')]

jalur = BFS(s, d)
# print jalur
# result = []

for i in jalur:
    maze[i[0]][i[1]] = 3
# for i in maze:
#   print i
#   row = []
#   for c in i:
#       if([maze.index(i), i.index(c)] in jalur ):
#           print "%d, %d is in jalur" %(maze.index(i), i.index(c))
#           row.append(3) # jalan kebenaran
#           pass
#       else:
#           row.append(c) # wall

#   result.append(row)

# for i in maze:
#   print (i)

plt.title("Maze Solver with BFS Algorithm")
plt.pcolormesh(maze)
plt.axes().set_aspect('equal')  # set the x and y axes to the same scale
plt.xticks([])  # remove the tick marks by setting to an empty list
plt.yticks([])  # remove the tick marks by setting to an empty list
plt.axes().invert_yaxis()  # invert the y-axis so the first row of data is at the top
plt.show()
