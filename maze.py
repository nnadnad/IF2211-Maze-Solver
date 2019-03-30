"""
Maze Solver with BFS Algorithm.

Created by:

M.Algah Fattah I / 13517122
Yudy Valentino / 13517128

"""

#!/usr/bin/python
from matplotlib import pyplot as plt
import sys
from math import sqrt


def insert(e, l):
    i = 0
    while(i < len(l) and e[0] > l[i][0]):
        i += 1

    l.insert(i, e)
    return l


class Maze:
    def __init__(self, filename, source, dest):
        self.source = source
        self.dest = dest
        self.maze = self.createMaze(filename)

    #this method return a 2d list which is the maze
    def createMaze(self, filename):
        sauce = open("mazes/"+filename).read().split('\n')
        result = []
        for i in sauce:
            row = []
            for c in i:
                if c == '0':
                    row.append(1) #grid
                else:
                    row.append(0) #wall
            result.append(row)
        return result

    def BFS(self):

        path = [self.source]
        queue = []
        queue.append(path)
        visited = [self.source] #daftar cell yang sudah dikunjungi
        # visited.append(self.source) #masukkan ke daftar cell yang sudah dikunjungi


        while(queue):
    
            path = queue.pop(0)
            currentCell = path[-1]      
            
            if(currentCell == self.dest): #berhenti jika sudah mencapai destinasi
                return path
                # exit()

                
            if(self.upOK(currentCell) and self.upOf(currentCell) not in visited):
                visited.append(self.upOf(currentCell)) #catat ketika sudah dikunjungi
                temp = [i for i in path] 
                temp.append(self.upOf(currentCell))
                queue.append(temp)

            if(self.downOK(currentCell) and self.downOf(currentCell) not in visited):
                visited.append(self.downOf(currentCell))
                temp = [i for i in path]
                temp.append(self.downOf(currentCell))
                queue.append(temp)

            if(self.leftOK(currentCell) and self.leftOf(currentCell) not in visited):
                visited.append(self.leftOf(currentCell))
                temp = [i for i in path]
                temp.append(self.leftOf(currentCell))
                queue.append(temp)

            if(self.rightOK(currentCell) and self.rightOf(currentCell) not in visited):
                visited.append(self.rightOf(currentCell))
                temp = [i for i in path]
                temp.append(self.rightOf(currentCell))
                queue.append(temp)


    def drawBFS(self):
        jalur = self.BFS()
        for i in jalur:
            self.maze[i[0]][i[1]] = 3

        plt.pcolormesh(self.maze)
        plt.axes().set_aspect('equal') #set the x and y axes to the same scale
        plt.xticks([]) # remove the tick marks by setting to an empty list
        plt.yticks([]) # remove the tick marks by setting to an empty list
        plt.axes().invert_yaxis() #invert the y-axis so the first row of data is at the top
        plt.show()
        

    def aStar(self):
        path = [0, [self.source]]
        queue = []
        queue.append(path)
        visited = [self.source] #daftar cell yang sudah dikunjungi
        # visited.append(self.source) #masukkan ke daftar cell yang sudah dikunjungi


        while(queue):
    
            path = queue.pop(0) # [kedalaman, [daftar cell yang sudah dikunjungi]]
            currentCell = path[-1][-1]  # cell  
            
            if(currentCell == self.dest): #berhenti jika sudah mencapai destinasi
                return path[-1]
                # exit()

                
            if(self.upOK(currentCell) and self.upOf(currentCell) not in visited):
                visited.append(self.upOf(currentCell)) #catat ketika sudah dikunjungi
                p = [i for i in path[-1]] #salinan dari path
                p.append(self.upOf(currentCell))
                c = path[0] + 10 + self.manhattan(self.upOf(currentCell)) #hitung cost dari cell tsb
                temp = [c, p] # salinan dari path, cost
                insert(temp, queue) #selipkan ke queue 

            if(self.downOK(currentCell) and self.downOf(currentCell) not in visited):
                visited.append(self.downOf(currentCell))
                p = [i for i in path[-1]] #salinan dari path
                p.append(self.downOf(currentCell))
                c = path[0] + 10 + self.manhattan(self.downOf(currentCell)) #hitung cost dari cell tsb
                temp = [c, p] # salinan dari path, cost
                insert(temp, queue) #selipkan ke queue 

            if(self.leftOK(currentCell) and self.leftOf(currentCell) not in visited):
                visited.append(self.leftOf(currentCell))
                p = [i for i in path[-1]] #salinan dari path
                p.append(self.leftOf(currentCell))
                c = path[0] + 10 + self.manhattan(self.leftOf(currentCell)) #hitung cost dari cell tsb
                temp = [c, p] # salinan dari path, cost
                insert(temp, queue) #selipkan ke queue 

            if(self.rightOK(currentCell) and self.rightOf(currentCell) not in visited):
                visited.append(self.rightOf(currentCell))
                p = [i for i in path[-1]] #salinan dari path
                p.append(self.rightOf(currentCell))
                c = path[0] + 10 + self.manhattan(self.rightOf(currentCell)) #hitung cost dari cell tsb
                temp = [c, p] # salinan dari path, cost
                insert(temp, queue) #selipkan ke queue 


    def drawAStar(self):
        jalur = self.aStar()
        for i in jalur:
            self.maze[i[0]][i[1]] = 3

        plt.pcolormesh(self.maze)
        plt.axes().set_aspect('equal') #set the x and y axes to the same scale
        plt.xticks([]) # remove the tick marks by setting to an empty list
        plt.yticks([]) # remove the tick marks by setting to an empty list
        plt.axes().invert_yaxis() #invert the y-axis so the first row of data is at the top
        plt.show()

    #mengembalikan jarak dari currentCell ke destinasi
    def euclid(self,cc):
        return sqrt((self.dest[0] - cc[0])**2 + (self.dest[1] - cc[1])**2)

    def manhattan(self, cc):
        return ((self.dest[0] - cc[0]) + (self.dest[1] - cc[1]))


    #cc adalah currentCell
    #currentCell berupa list dengan dua elemen
    #elemen pertama = row, elemen kedua = col

    def upOK(self, cc):
        return (cc[0] > 0 and self.maze[cc[0]-1][cc[1]] == 1)

    def downOK(self, cc):
        return (cc[0] < len(self.maze)-1 and self.maze[cc[0]+1][cc[1]] == 1)

    def leftOK(self, cc):
        return (cc[1] > 0 and self.maze[cc[0]][cc[1]-1] == 1)

    def rightOK(self, cc):
        return (cc[1] < len(self.maze[0])-1 and self.maze[cc[0]][cc[1]+1] == 1)

    #
    def upOf(self, cc):
        temp = [cc[0]-1]
        temp.append(cc[1])
        return temp

    def downOf(self, cc):
        temp = [cc[0]+1]
        temp.append(cc[1])
        return temp

    def leftOf(self, cc):
        temp = [cc[0]]
        temp.append(cc[1]-1)
        return temp

    def rightOf(self, cc):
        temp = [cc[0]]
        temp.append(cc[1]+1)
        return temp





#main
f = sys.argv[1]
s = [int(i) for i in sys.argv[2].split(',')]
d = [int(i) for i in sys.argv[3].split(',')]
algo = sys.argv[4]
labirin = Maze(f,s,d)
if(algo == 'a'):
    # print "coming soon"
    labirin.drawAStar()
elif(algo == 'b'):  
    labirin.drawBFS()
else:
    print ("it is either a or b bro")



