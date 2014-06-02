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
        print(20*"\n")
        print("***2048***")
        print( "Press arrow keys or WASD to move tiles! (Escape key to exit):","\n")
        print(current_game,"\n","\n","Score: %d"%game_logic.score,"\n")


    def keyPressed(self,event):

        if event.keysym == 'Escape':
            root.destroy()
        elif event.keysym == 'Right'or event.keysym == 'd':
            self.right = True
        elif event.keysym == 'Left' or event.keysym == 'a':
            self.left = True
        elif event.keysym == 'Up' or event.keysym == 'w':
            self.up = True
        elif event.keysym == 'Down' or event.keysym == 's':
            self.down = True

    def keyReleased(self,event):
        if event.keysym == 'Right'or event.keysym == 'd':
            self.right = False
        elif event.keysym == 'Left' or event.keysym == 'a':
            self.left = False
        elif event.keysym == 'Up' or event.keysym == 'w':
            self.up = False
        elif event.keysym == 'Down' or event.keysym == 's':
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
print(20*"\n")
print("***2048***")
print( "Press arrow keys or WASD to move tiles! (Escape key to exit):","\n")
print(current_game,"\n","\n","Score: %d"%game_logic.score,"\n")

root.bind_all('<Key>', application.keyPressed)
root.bind_all('<KeyRelease>', application.keyReleased)
root.after(100,application.task)
root.withdraw()
root.mainloop()
