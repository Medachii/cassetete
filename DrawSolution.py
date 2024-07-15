# [[0, 0, 1, [[0, 1], [0, 0], [1, 1], [2, 1], [3, 1]]], [1, 0, 0, [[0, 0], [1, 1], [1, 0], [2, 0], [3, 0]]], [2, 4, 0, [[-2, 1], [-1, 1], [0, 2], [0, 1], [0, 0]]]] is an example of solution

#ask for 2 numbers, one for the number of rows and one for the number of columns
#ask for the solution with is a list of list
#each list contains 4 elements : the 2nd one is the position in rows, the 3rd one is the position in columns, the 4th one is the coordinates to color
import tkinter as tk
import random as rd

input1 = input("Enter the number of rows and columns separated by a space: ")
input2 = input("Enter the solution: ")

rows = int(input1.split()[0])
columns = int(input1.split()[1])

solution = eval(input2)

#draw grid using tkinter


class PixelGrid:
    def __init__(self, master, rows, columns, solution):
        self.rows = rows
        self.columns = columns
        self.solution = solution
        self.pixel = tk.PhotoImage(width=1, height=1)
        self.canvas = tk.Canvas(master, width=self.columns*50, height=self.rows*50, bg="white")
        self.canvas.pack()
        self.draw_grid()
        self.draw_solution()

    def draw_grid(self):
        for i in range(self.rows):
            for j in range(self.columns):
                x0, y0 = j*50, i*50
                x1, y1 = x0+50, y0+50
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="white", width=1)

    def draw_solution(self):
        for solution in self.solution:
            color = "#"+"".join([rd.choice("0123456789ABCDEF") for j in range(6)])
            z, x, y, coordinates = solution
            for coordinate in coordinates:
                x0, y0 = (y+coordinate[1])*50, (x+coordinate[0])*50
                x1, y1 = x0+50, y0+50
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=1)

root = tk.Tk()
grid = PixelGrid(root, rows, columns, solution)
root.mainloop()



# Example
