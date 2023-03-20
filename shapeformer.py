import tkinter as tk

class PixelGrid:
    def __init__(self, master):
        self.master = master
        self.pixel_size = 50
        self.grid_size = 10
        self.pixels = [[0 for x in range(self.grid_size)] for y in range(self.grid_size)]
        self.top_left_pixel = [0, 0]
        
        self.canvas = tk.Canvas(master, width=self.pixel_size*self.grid_size, height=self.pixel_size*self.grid_size)
        self.canvas.pack()
        
        self.canvas.bind("<Button-1>", self.handle_click)
        
        self.button = tk.Button(master, text="Créer liste", command=self.create_list)
        self.button.pack()
        
        self.draw_grid()
    
    def draw_grid(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                x1 = col*self.pixel_size
                y1 = row*self.pixel_size
                x2 = x1+self.pixel_size
                y2 = y1+self.pixel_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
                
    def handle_click(self, event):
        row = event.y // self.pixel_size
        col = event.x // self.pixel_size
        self.toggle_pixel(row, col)
    
    def toggle_pixel(self, row, col):
        if self.pixels[row][col] == 0:
            self.pixels[row][col] = 1
            color = "black"
        else:
            self.pixels[row][col] = 0
            color = "white"
        x1 = col*self.pixel_size
        y1 = row*self.pixel_size
        x2 = x1+self.pixel_size
        y2 = y1+self.pixel_size
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
    
    def create_list(self):
        pixel_list = []
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if self.pixels[row][col] == 1:
                    x = col - self.top_left_pixel[0]
                    y = row - self.top_left_pixel[1]
                    pixel_list.append([x, y])
        
        finalList = []
        for pixel in pixel_list:
            newPixel = [pixel[0] - pixel_list[0][0], pixel[1] - pixel_list[0][1]]
            finalList.append(newPixel)
        print(finalList)
        #mettre la finalList dans le presse-papier
        self.master.clipboard_clear()
        self.master.clipboard_append(str(finalList))
        self.master.update()
    
        #reset grid
        self.pixels = [[0 for x in range(self.grid_size)] for y in range(self.grid_size)]
        self.draw_grid()

        



root = tk.Tk()
grid = PixelGrid(root)
root.mainloop()
