import Model as m
import View as v
import tkinter as tk


class Application(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.gameboard = v.GameBoard(self)
        self.gameboard.grid()
        model = m.TXTModel('default1.txt')
        self.currfile = model.filename

        #self.game = v.gameboard(self)

    def save(self):
        score = self.gameboard.score
        map = self.gameboard.map
        model = m.TXTModel(self.currfile)
        model.save_game(score, map)

    def load(self):
        model = m.TXTModel(self.currfile)
        stuff = model.load_game()
        return stuff

    def opener(self):
        model = m.TXTModel(self.currfile)
        while self == 'demo.txt':  # If self still default file break askopenfilename
            break
        else:
            self.file_in = filedialog.askopenfilename(initialdir='C:\Documents\Github\211-pacman',
                                                      filetypes=[('File', '*.txt')],
                                                      title='Search a file')  # Search for a file
            self.currfile = self.file_in  # Set currfile as new file name found above
        messagebox.showinfo('Load File', 'loading selected file...')
        run = self.load()  # load selected file
        print('File loaded successfully')

    def gameover(self):
        messagebox.showinfo('Game Over', 'The ghosts got you, wasted...')


        
            
                 
if __name__ == "__main__":
    app = Application()
    app.mainloop()