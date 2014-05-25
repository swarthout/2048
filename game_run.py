import tkinter as tk
import game_logic
game_logic.newboard()
current_game = game_logic.grid

class App(object):
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
    def output():
        print(10*"\n")
        print("***2048***")
        print( "Press arrow keys to move tiles! (Escape key to exit):","\n")
        print(current_game,"\n","\n","Score: %d"%game_logic.score,"\n")


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

            game_logic.moveright(current_game)
            App.output()

        elif self.left:

            game_logic.moveleft(current_game)
            App.output()

        elif self.up:

            game_logic.moveup(current_game)
            App.output()
        elif self.down:

            game_logic.movedown(current_game)
            App.output()

        root.after(100,self.task)

application = App()
root = tk.Tk()
print(10*"\n")
print("***2048***")
print( "Press arrow keys to move tiles! (Escape key to exit):","\n")
print(current_game,"\n","\n","Score: %d"%game_logic.score,"\n")

root.bind_all('<Key>', application.keyPressed)
root.bind_all('<KeyRelease>', application.keyReleased)
root.after(100,application.task)
root.withdraw()
root.mainloop()
