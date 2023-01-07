import tkinter as tk
import os
import random
import pygame



pygame.mixer.init()
jump_time = 0
count_pixel = 0
icon_pixel_count = 350
list_obstacles = []
list_of_obstacle_height = []
location = 1000
game_condition = 'c'
score = 0
difficulty = [0, 266]

def move_background():
    """

    :return:
    """
    global count_pixel

    if count_pixel != -1910 and game_condition == "c":
        count_pixel -= 10

        background_1.place_configure(x=count_pixel)
        background_2.place_configure(x=1900 + count_pixel)
        root.after(20, move_background)
    elif game_condition == "c":
        background_1.place_configure(x=0)
        background_2.place_configure(x=1900)
        count_pixel = 0
        root.after(20, move_background)


def move_icon():
    """

    :return:
    """
    global icon_pixel_count

    if icon_pixel_count != 800 and game_condition == "c":
        icon_pixel_count += 10

        player_icon.place_configure(y=icon_pixel_count)

        root.after(5, move_icon)
    elif game_condition == "c":
        end_game()



def leftclick(event):
    global jump_time
    if game_condition == "c":
        jump_time = 0
        print("left")
        jump_sound()
        icon_jump()


def icon_jump():
    global icon_pixel_count, jump_time
    if jump_time != 10:
        jump_time += 1
        icon_pixel_count -= 25
        player_icon.place_configure(y=icon_pixel_count)
        root.after(5, icon_jump)


def create_obstacle():
    global list_obstacles, list_of_obstacle_height
    height = random.choice(range(1, 5))
    obstacle_down = []
    obstacle_up = []

    for _ in range(height):
        obstacle_down.append(tk.Label(root, image=obstacle_body, borderwidth=0))
    obstacle_down.append(tk.Label(root, image=obstacle_bot, borderwidth=0))

    for _ in range(5 - height):
        obstacle_up.append(tk.Label(root, image=obstacle_body, borderwidth=0))
    obstacle_up.append(tk.Label(root, image=obstacle_top, borderwidth=0))

    list_obstacles.append([obstacle_down, obstacle_up])
    list_of_obstacle_height.append(height * 72 + 84)


def show_obstacles(location):
    global list_obstacles, difficulty
    x_obs = location

    for obstacle in list_obstacles:
        y_obs_d = 723
        y_obs_u = difficulty[0]
        for item in obstacle[0][0:-1]:
            item.place(x=x_obs, y=y_obs_d)
            y_obs_d -= 72
        obstacle[0][-1].place(x=x_obs - 10, y=y_obs_d)
        for item in obstacle[1][0:-1]:
            item.place(x=x_obs, y=y_obs_u)
            y_obs_u += 72
        obstacle[1][-1].place(x=x_obs - 10, y=y_obs_u)
        x_obs += 400


def move_obstacles():
    global location, list_obstacles, list_of_obstacle_height
    if location != -1200 and game_condition == "c":
        location -= 10
        show_obstacles(location)
        check_position()
        root.after(20, move_obstacles)
    elif game_condition == "c":
        list_obstacles = list_obstacles[3::]
        list_of_obstacle_height = list_of_obstacle_height[3::]
        for i in range(3):
            create_obstacle()
        location = 0
        root.after(20, move_obstacles)


def end_game():
    global game_condition
    stop_music()
    game_condition = 'e'
    game_over_scene = tk.Label(root, image=game_over_image, borderwidth=0)
    game_over_scene.place(x=250, y=150)
    game_over_score_scene = tk.Label(root, text=f'SCORE: {int(score / 25)}', bg='#9E9381', font='Helvetica 20 bold', fg='#FF9A4A', borderwidth=0)
    game_over_score_scene.place(x=440, y=420)
    button_restart = tk.Button(root, image=restart_button_image, borderwidth=0, bg='#9E9381',
                    command=lambda: [start_game(), move_background(), move_icon(), move_obstacles(),
                                        button_restart.destroy(), game_over_scene.destroy(),
                                     game_over_score_scene.destroy(), ])
    button_restart.place(x=360, y=500)


def start_game():
    global game_condition, jump_time, count_pixel, icon_pixel_count, location, list_obstacles, score, list_of_obstacle_height
    play_music()
    for obstacle in list_obstacles:

        for item_1 in obstacle[0]:
            item_1.destroy()
        for item in obstacle[1]:
            item.destroy()
    root.bind("<Key>", leftclick)
    jump_time = 0
    count_pixel = 0
    icon_pixel_count = 350
    list_obstacles = []
    list_of_obstacle_height = []
    score = 0

    location = 1000
    game_condition = 'c'

    background_1.place(x=0)
    background_2.place(x=1900)
    for _ in range(6):
        create_obstacle()
    player_icon.place(x=100, y=350)


def check_position():
    global icon_pixel_count, location, list_of_obstacle_height, score, difficulty
    actual_icon_location = 795 - icon_pixel_count
    if location in range(-50, 200):

        if actual_icon_location < list_of_obstacle_height[0] + 85 or (list_of_obstacle_height[0] + difficulty[1]) < actual_icon_location:
            end_game()
        else:
            score += 1
    if location in range(-450, -200):
        if actual_icon_location < list_of_obstacle_height[1] + 85 or (list_of_obstacle_height[1] + difficulty[1]) < actual_icon_location:
            end_game()
        else:
            score += 1
    if location in range(-850, -600):
        if actual_icon_location < list_of_obstacle_height[2] + 85 or (list_of_obstacle_height[2] + difficulty[1]) < actual_icon_location:
            end_game()
        else:
            score += 1
    if location in range(-1200, -1000):
        if actual_icon_location < list_of_obstacle_height[3] + 85 or (list_of_obstacle_height[3] + difficulty[1]) < actual_icon_location:
            end_game()
        else:
            score += 1
    present_score.config(text=f"score: {int(score / 25)}")


def easy_game():
    global difficulty
    difficulty = [-100, 366]


def play_music():
    global main_path
    os.chdir('sounds')
    pygame.mixer.music.load('long_crow.mp3')
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('long_crow.mp3'))
    pygame.mixer.Channel(0).set_volume(0.05)
    os.chdir(main_path)


def stop_music():
    pygame.mixer.Channel(0).stop()


def jump_sound():
    global main_path
    os.chdir('sounds')
    pygame.mixer.music.load('jump_sound.mp3')

    pygame.mixer.music.play(loops=1)
    pygame.mixer.music.set_volume(0.01)
    os.chdir(main_path)



root = tk.Tk()
root.geometry('1000x825')
root.configure(bg='#807869')

main_path = os.getcwd()
os.chdir('images')
background_image = tk.PhotoImage(file='background.png')
player_icon_image = tk.PhotoImage(file='icon.png')
obstacle_body = tk.PhotoImage(file='obstacle_body.png')
obstacle_bot = tk.PhotoImage(file='obstacle_bot.png')
obstacle_top = tk.PhotoImage(file='obstacle_top.png')
game_over_image = tk.PhotoImage(file='Game_over.png')
game_start_image = tk.PhotoImage(file='omega_rage.png')
game_over_score_image = tk.PhotoImage(file='Game_over_score.png')
restart_button_image = tk.PhotoImage(file='restart_button.png')
easy_button = tk.PhotoImage(file='easy_button.png')
hard_button = tk.PhotoImage(file='hard_button.png')
os.chdir(main_path)


background_1 = tk.Label(root, image=background_image, borderwidth=0)
background_1.place(x=0)

background_2 = tk.Label(root, image=background_image, borderwidth=0)
background_2.place(x=1900)


# obstacle_test_4 = tk.Label(root, image=obstacle_bot, borderwidth=0)
# obstacle_test_4.place(x=690, y=435)
for _ in range(6):
    create_obstacle()


player_icon = tk.Label(root, image=player_icon_image, bg='black')
player_icon.place(x=100, y=350)



game_start_scene = tk.Label(root, image=game_start_image, borderwidth=0)
game_start_scene.place(x=250, y=150)

button_play_easy = tk.Button(root, image=easy_button, borderwidth=0, bg='#9E9381',
                command=lambda: [start_game(), move_background(), move_icon(), move_obstacles(),
                                    button_play_easy.destroy(), game_start_scene.destroy(), button_play_hard.destroy(),
                                 easy_game()])
button_play_easy.place(x=365, y=430)

button_play_hard = tk.Button(root, image=hard_button, borderwidth=0, bg='#9E9381',
                command=lambda: [start_game(), move_background(), move_icon(), move_obstacles(),
                                    button_play_easy.destroy(), game_start_scene.destroy(), button_play_hard.destroy()])
button_play_hard.place(x=365, y=550)
present_score = tk.Label(root, text=f"score: {score}", bg='#807869', font='Helvetica 20 bold', fg='#FF9A4A', borderwidth=0)
present_score.place(x=870, y=795)





root.mainloop()

