import tkinter as tk
import board
playboard = board.grid

class App(object):
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def keyPressed(self,event):

        if event.keysym == 'Escape':
            root.destroy()
        elif event.keysym == 'Right':
            self.right = True
        elif event.keysym == 'Left':
            self.left = True
        elif event.keysym == 'Up':
            self.up = True
        elif event.keysym == 'Down':
            self.down = True

    def keyReleased(self,event):
        if event.keysym == 'Right':
            self.right = False
        elif event.keysym == 'Left':
            self.left = False
        elif event.keysym == 'Up':
            self.up = False
        elif event.keysym == 'Down':
            self.down = False

    def task(self):
        if self.right:

            board.moveright(playboard)
            print(playboard,"\n")

        elif self.left:

            board.moveleft(playboard)
            print(playboard,"\n")
        elif self.up:

            board.moveup(playboard)
            print(playboard,"\n")
        elif self.down:

            board.movedown(playboard)
            print(playboard,"\n")
        root.after(100,self.task)

application = App()
root = tk.Tk()
print("***2048***")
print( "Press arrow keys to move board (Escape key to exit):","\n")
print(playboard,"\n")

root.bind_all('<Key>', application.keyPressed)
root.bind_all('<KeyRelease>', application.keyReleased)
root.after(100,application.task)
root.withdraw()
root.mainloop()
