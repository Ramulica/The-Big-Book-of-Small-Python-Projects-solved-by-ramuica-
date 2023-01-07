import time
import tkinter as tk
import os
import random

class Game_interface:
    def __init__(self):


        self.root = tk.Tk()
        self.root.geometry('570x550')
        self.root.resizable(0, 0)
        self.root.configure(bg='#3B194C')

        self.frame = tk.Frame(self.root, width=570, height=550, bg='#3B194C')
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.grid()

        main_path = os.getcwd()
        os.chdir("image")
        self.empty_square = tk.PhotoImage(file='empty square.png')
        self.x_square = tk.PhotoImage(file='x square.png')
        self.o_square = tk.PhotoImage(file='o square.png')
        self.win_line = tk.PhotoImage(file='win_line.png')
        self.game_interface()
        self.main_menu_interface()

        self.root.mainloop()

    def main_menu_interface(self):
        row_1 = 1
        column_1 = 1
        while True:
            remove_squares = tk.Label(self.frame, text="\n\n\n\n\n\n\n\n\n", bg='#3B194C')
            remove_squares.grid(row=row_1, column=column_1, padx=10, pady=10, sticky=tk.W + tk.E)
            row_1 += 1
            if row_1 == 4:
                row_1 = 1
                column_1 += 1
            if column_1 == 4:
                break


        play_button = tk.Button(self.frame, text="TIC TAC TOE", bg='#8EB4E3', fg="white", font=('Arial', 20),
                                command=lambda: self.ttt_interface())
        play_button.grid(row=2, column=2, padx=10, pady=10, sticky=tk.W + tk.E)
        exit_button = tk.Button(self.frame, text="EXIT", bg='#8EB4E3', fg="white", font=('Arial', 20),
                                command=exit)
        exit_button.grid(row=3, column=2, padx=10, pady=10, sticky=tk.W + tk.E)


    def ttt_interface(self):
        row_1 = 1
        column_1 = 1
        while True:
            remove_squares = tk.Label(self.frame, text="\n\n\n\n\n\n\n\n\n", bg='#3B194C')
            remove_squares.grid(row=row_1, column=column_1, padx=10, pady=10, sticky=tk.W + tk.E)
            row_1 += 1
            if row_1 == 4:
                row_1 = 1
                column_1 += 1
            if column_1 == 4:
                break
        ttt_title = tk.Label(self.frame, text=f"TIC TAC TOE", bg='#3B194C', fg="white", font=('Arial', 20))
        ttt_title.grid(row=1, column=2, padx=10, pady=10, sticky=tk.W + tk.E)
        play_local = tk.Button(self.frame, text="1 VS 1", bg='#8EB4E3', fg="white", font=('Arial', 20),
                                command=lambda: self.game_interface())
        play_local.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W + tk.E)

        play_bot = tk.Button(self.frame, text="VS BOT", bg='#8EB4E3', fg="white", font=('Arial', 20),
                                command=lambda bot=random.choice(['x', 'o']): self.game_interface(bot))
        play_bot.grid(row=2, column=3, padx=10, pady=10, sticky=tk.W + tk.E)
        exit_button = tk.Button(self.frame, text="EXIT", bg='#8EB4E3', fg="white", font=('Arial', 20),
                                command=exit)
        exit_button.grid(row=3, column=2, padx=10, pady=10, sticky=tk.W + tk.E)

    def game_interface(self, bot="none"):
        self.bot = bot
        if self.bot == "x":
            self.bot = "o"
        elif self.bot == "o":
            self.bot = "x"
        self.round = 1
        self.board_list = [['e', 'e', 'e'], ['e', 'e', 'e'], ['e', 'e', 'e']]
        self.winner = "e"

        self.square_0_0 = tk.Button(self.frame, image=self.empty_square, bg='#3B194C', borderwidth=0,
                                    command=lambda row=1, column=1, bot_=self.bot: self.press_button(row, column, bot_))
        self.square_0_0.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W + tk.E)
        self.square_0_1 = tk.Button(self.frame, image=self.empty_square, bg='#3B194C', borderwidth=0,
                                    command=lambda row=1, column=2, bot_=self.bot: self.press_button(row, column, bot_))
        self.square_0_1.grid(row=1, column=2, padx=10, pady=10, sticky=tk.W + tk.E)
        self.square_0_2 = tk.Button(self.frame, image=self.empty_square, bg='#3B194C', borderwidth=0,
                                    command=lambda row=1, column=3, bot_=self.bot: self.press_button(row, column, bot_))
        self.square_0_2.grid(row=1, column=3, padx=10, pady=10, sticky=tk.W + tk.E)
        self.square_1_0 = tk.Button(self.frame, image= self.empty_square, bg='#3B194C', borderwidth=0,
                                    command=lambda row=2, column=1, bot_=self.bot: self.press_button(row, column, bot_))
        self.square_1_0.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W + tk.E)
        self.square_1_1 = tk.Button(self.frame, image=self.empty_square, bg='#3B194C', borderwidth=0,
                                    command=lambda row=2, column=2, bot_=self.bot: self.press_button(row, column, bot_))
        self.square_1_1.grid(row=2, column=2, padx=10, pady=10, sticky=tk.W + tk.E)
        self.square_1_2 = tk.Button(self.frame, image=self.empty_square, bg='#3B194C', borderwidth=0,
                                    command=lambda row=2, column=3, bot_=self.bot: self.press_button(row, column, bot_))
        self.square_1_2.grid(row=2, column=3, padx=10, pady=10, sticky=tk.W + tk.E)
        self.square_2_0 = tk.Button(self.frame, image=self.empty_square, bg='#3B194C', borderwidth=0,
                                    command=lambda row=3, column=1, bot_=self.bot: self.press_button(row, column, bot_))
        self.square_2_0.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W + tk.E)
        self.square_2_1 = tk.Button(self.frame, image=self.empty_square, bg='#3B194C', borderwidth=0,
                                    command=lambda row=3, column=2, bot_=self.bot: self.press_button(row, column, bot_))
        self.square_2_1.grid(row=3, column=2, padx=10, pady=10, sticky=tk.W + tk.E)
        self.square_2_2 = tk.Button(self.frame, image=self.empty_square, bg='#3B194C', borderwidth=0,
                                    command=lambda row=3, column=3, bot_=self.bot: self.press_button(row, column, bot_))
        self.square_2_2.grid(row=3, column=3, padx=10, pady=10, sticky=tk.W + tk.E)
        if self.bot == "x":
            button = tk.Label(self.frame, image=self.x_square, bg='#3B194C')
            button.grid(row=2, column=2, padx=10, pady=10, sticky=tk.W + tk.E)
            self.board_list[1][1] = "x"
            self.round += 1
            self.bot = "x"
        elif self.bot == "o":
            self.bot = "o"

    def winner_draw_interface(self):
        row_1 = 1
        column_1 = 1
        while True:
            remove_squares = tk.Label(self.frame, text="\n\n\n\n\n\n\n\n\n", bg='#3B194C')
            remove_squares.grid(row=row_1, column=column_1, padx=10, pady=10, sticky=tk.W + tk.E)
            row_1 += 1
            if row_1 == 4:
                row_1 = 1
                column_1 += 1
            if column_1 == 4:
                break
        if self.winner == 'draw':
            win_text = tk.Label(self.frame, text=f"draw", bg='#3B194C', fg="white", font=('Arial', 40))
        elif self.winner == "x" or self.winner == "o":
            win_text = tk.Label(self.frame, text=f"{self.winner} is the\nwinner", bg='#3B194C', fg="white", font=('Arial', 40))
        win_text.grid(row=1, column=2, padx=10, pady=10, sticky=tk.W + tk.E)

        play_button = tk.Button(self.frame, text="PLAY AGAIN", bg='#8EB4E3', fg="white", font=('Arial', 20),
                                command=lambda: self.game_interface(self.bot))
        play_button.grid(row=2, column=2, padx=10, pady=10, sticky=tk.W + tk.E)
        exit_button = tk.Button(self.frame, text="EXIT", bg='#8EB4E3', fg="white", font=('Arial', 20),
                                command=lambda: self.main_menu_interface())
        exit_button.grid(row=3, column=2, padx=10, pady=10, sticky=tk.W + tk.E)

    def decide_best_move(self, bot):
        time.sleep(2)
        # win situation
        not_bot = "x"
        if bot == "x":
            not_bot = "o"

        for i in range(3):
            if self.board_list[i].count(bot) == 2:
                for i_1, item in enumerate(self.board_list[i]):
                    if item == "e":
                        return i, i_1
        for i in range(3):
            if [self.board_list[0][i], self.board_list[1][i], self.board_list[2][i]].count(bot) == 2:
                for i_1, item in enumerate([self.board_list[0][i], self.board_list[1][i], self.board_list[2][i]]):
                    if item == "e":
                        return i_1, i
        if [self.board_list[0][0], self.board_list[1][1], self.board_list[2][2]].count(bot) == 2:
            for i, item in enumerate([self.board_list[0][0], self.board_list[1][1], self.board_list[2][2]]):
                if item == "e":
                    return i, i
        if [self.board_list[0][2], self.board_list[1][1], self.board_list[2][0]].count(bot) == 2:
            for i, item in enumerate([self.board_list[0][0], self.board_list[1][1], self.board_list[2][2]]):
                if item == "e":
                    if i == 0:
                        return 0, 2
                    if i == 1:
                        return 1, 1
                    if i == 0:
                        return 2, 0

        # defend situation

        for i in range(3):
            if self.board_list[i].count(not_bot) == 2:
                for i_1, item in enumerate(self.board_list[i]):
                    if item == "e":
                        return i, i_1
        for i in range(3):
            if [self.board_list[0][i], self.board_list[1][i], self.board_list[2][i]].count(not_bot) == 2:
                for i_1, item in enumerate([self.board_list[0][i], self.board_list[1][i], self.board_list[2][i]]):
                    if item == "e":
                        return i_1, i
        if [self.board_list[0][0], self.board_list[1][1], self.board_list[2][2]].count(not_bot) == 2:
            for i, item in enumerate([self.board_list[0][0], self.board_list[1][1], self.board_list[2][2]]):
                if item == "e":
                    return i, i
        if [self.board_list[0][2], self.board_list[1][1], self.board_list[2][0]].count(not_bot) == 2:
            for i, item in enumerate([self.board_list[0][0], self.board_list[1][1], self.board_list[2][2]]):

                if item == "e":
                    if i == 0:
                        return 0, 2
                    if i == 1:
                        return 1, 1
                    if i == 2:
                        return 2, 0
        # trying to win

        # not in danger, not in winning position
        if self.board_list[1][1] == "e":

            return 1, 1
        for i, item in enumerate([self.board_list[0][0], self.board_list[2][2], self.board_list[0][2], self.board_list[2][0]]):

            if item == "e":

                if i == 0:
                    return 0, 0
                if i == 1:
                    return 2, 2
                if i == 2:
                    return 0, 2
                if i == 3:
                    return 2, 0
        for i, item in enumerate([self.board_list[0][1], self.board_list[2][1], self.board_list[1][2], self.board_list[1][0]]):
            if item == "e":

                if i == 0:
                    return 0, 1
                if i == 1:
                    return 2, 1
                if i == 2:
                    return 1, 2
                if i == 3:
                    return 1, 0


    def press_button(self, row, column, bot):

        print(f"rounf is : self.round")
        if self.round % 2 == 0:

            new_square = self.o_square
            self.board_list[row-1][column-1] = "o"
        else:

            new_square = self.x_square
            self.board_list[row - 1][column - 1] = "x"
        button = tk.Label(self.frame, image=new_square, bg='#3B194C')
        button.grid(row=row, column=column, padx=10, pady=10, sticky=tk.W + tk.E)
        self.round += 1
        print(self.board_list)
        try:
            if bot != "none":

                if bot == "x":
                    bot_image = self.x_square
                else:
                    bot_image = self.o_square
                row_b, column_b = self.decide_best_move(bot)

                button = tk.Label(self.frame, image=bot_image, bg='#3B194C')
                button.grid(row=row_b+1, column=column_b+1, padx=10, pady=10, sticky=tk.W + tk.E)
                self.board_list[row_b][column_b] = self.bot
                self.round += 1
                print(f"rounf is : self.round")
                print(self.board_list)
        except TypeError:
            print("bot can't move")
        if self.winner == "e":
            for i in range(3):  # row win verification
                if self.board_list[i][0] == self.board_list[i][1] == self.board_list[i][2] and\
                        "e" not in self.board_list[i]:

                    self.winner = self.board_list[i][0]
                    print(f"{self.board_list[i][0]} wins")
                    self.winner_draw_interface()
                    break
        if self.winner == "e":
            for i in range(3):  # column win verification
                if self.board_list[0][i] == self.board_list[1][i] == self.board_list[2][i] == "x" or\
                        self.board_list[0][i] == self.board_list[1][i] == self.board_list[2][i] == "o":


                    self.winner = self.board_list[0][i]
                    print(f"{self.board_list[0][i]} wins")
                    self.winner_draw_interface()
                    break
        if self.winner == "e":

            if self.board_list[0][0] == self.board_list[1][1] == self.board_list[2][2] == "x" or \
                    self.board_list[0][0] == self.board_list[1][1] == self.board_list[2][2] == "o":

                print(f"{self.board_list[0][0]} wins")
                self.winner = self.board_list[0][0]
                self.winner_draw_interface()
        if self.winner == "e":

            if self.board_list[0][2] == self.board_list[1][1] == self.board_list[2][0] == "x" or \
                    self.board_list[0][2] == self.board_list[1][1] == self.board_list[2][0] == "o":

                print(f"{self.board_list[0][2]} wins")
                self.winner = self.board_list[0][2]
                self.winner_draw_interface()
        if self.round == 10 and self.winner == "e":
            print("Draw")
            self.winner = "draw"
            self.winner_draw_interface()

if __name__ == '__main__':
    menu = Game_interface()