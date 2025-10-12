import pygame
import random
import math
from pygame import mixer
from pathlib import Path


pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader")
icon_variable = pygame.image.load("Assets/Images/spaceship1.png")
pygame.display.set_icon(icon_variable)
bg = pygame.image.load("Assets/Images/bg.jpg")

# Background Sound
mixer.music.load("Assets/Sounds/background.wav")
mixer.music.play(-1)  # -1 inside bracket means to loop

# In game sounds
c_sound = mixer.Sound("Assets/Sounds/explosion.wav")
bullet_sound = mixer.Sound("Assets/Sounds/laser.wav")

# Main Menu
# main_menu, main_game, game_over
state = "main_menu"


# Initial Player Properties
spaceship1 = pygame.image.load("Assets/Images/spaceship1.png")
spaceship2 = pygame.image.load("Assets/Images/spaceship2.png")
spaceship3 = pygame.image.load("Assets/Images/spaceship3.png")
spaceship4 = pygame.image.load("Assets/Images/spaceship4.png")
spaceship = "Assets/Images/spaceship1.png"
player_img = pygame.image.load(spaceship)
playerx = 370
playery = 480
playerx_change = 0

# Initial Enemy Properties
enemy_img = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 4
spawn_enemy_event = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_enemy_event, 7000)

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load("Assets/Images/enemy.png"))
    enemyx.append(random.randint(0, 735))
    enemyy.append(random.randint(50, 150))
    enemyx_change.append(random.choice([0.3, -0.3]))
    enemyy_change.append(60)

# Initial Bullet Properties
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bullet_img = pygame.image.load("Assets/Images/bullet.png")
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = -2
bullet_state = "ready"
bullets = []
max_bullets = 10


# Player Performance Parameters
aliens_killed = 0
bullets_used = 0
accuracy = 0
time_taken = 0


# Fonts
statistics_font_1 = pygame.font.Font("Assets/Fonts/font.ttf", 32)
statistics_font2 = pygame.font.Font("Assets/Fonts/font.ttf", 40)
title_font = pygame.font.Font("Assets/Fonts/title.otf", 72)
credits_font = pygame.font.Font("Assets/Fonts/credits.ttf", 16)
main_menu_font = pygame.font.Font("Assets/Fonts/menu_text.ttf", 32)
main_menu_font2 = pygame.font.Font("Assets/Fonts/menu_text.ttf", 16)
main_menu_font3 = pygame.font.Font("Assets/Fonts/menu_text.ttf", 16)
over_title_font = pygame.font.Font('Assets/Fonts/game_over.TTF', 64)
total_points_font = pygame.font.Font('Assets/Fonts/total_points.otf', 48)
restart_font = pygame.font.Font("Assets/Fonts/menu_text.ttf", 26)
high_score_font = pygame.font.Font("Assets/Fonts/total_points.otf", 48)

# Aliens killed statistics
def show_aliens_killed(font, x, y):
    aliens_killed_text = font.render("Alines Destroyed: " + str(aliens_killed), True, (255, 255, 255))
    screen.blit(aliens_killed_text, (x, y))

#Bullets Used Statistics
def show_bullets_used(font, x, y):
    bullets_used_text = font.render("Bullets Used: " + str(bullets_used), True, (255, 255, 255))
    screen.blit(bullets_used_text, (x,y))

# Accuracy Statistics
def show_accuracy(font, x, y):
    try:
        exact_accuracy = aliens_killed/bullets_used * 100
        rounded_accuracy = round(exact_accuracy, 2)
        accuracy = ("Accuracy: " + str(rounded_accuracy) + "%")
        accuracy_text = font.render(accuracy, True, (255, 255, 255))
        screen.blit(accuracy_text, (x, y))
    except ZeroDivisionError:
        accuracy = "0"
        accuracy_text = font.render("Accuracy: " + accuracy, True, (255, 255, 255))
        screen.blit(accuracy_text, (x, y))

# Total Points
def show_total_points(points3, x, y, a, b):
    total_points_text_1 = statistics_font2.render("Total Points:", True, (255, 255, 255))
    screen.blit(total_points_text_1, (x, y))
    points4 = str(points3)
    total_points_text_2 = total_points_font.render(points4, True, (255, 255, 255))
    screen.blit(total_points_text_2, (a,b))


def enemy(x, y, i):
    global enemy_img
    screen.blit(enemy_img[i], (x, y))


def add_new_enemy():
    global num_of_enemies
    global enemyx_change
    num_of_enemies += 1
    enemy_img.append(pygame.image.load("Assets/Images/enemy.png"))
    enemyx.append(random.randint(0, 735))
    enemyy.append(random.randint(50, 150))
    enemyx_change.append(random.choice([0.3, -0.3]))
    enemyy_change.append(60)

def player(x, y):
    screen.blit(player_img, (x, y))  # blit means to display


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


def iscollision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt(
        math.pow((enemyx - bulletx), 2) + math.pow((enemyy - bullety), 2)
    )
    if distance <= 36:
        return True
    else:
        return False
    
def events_in_over(x1, y1, x2, y2):
    events_text1 = restart_font.render("Press RETURN to restart the game.", True, (255, 255, 255))
    screen.blit(events_text1, (x1, y1))
    events_text2 = restart_font.render("Press ESCAPE to return to main menu.", True, (255, 255, 255))
    screen.blit(events_text2, (x2, y2))

path1 = Path('Assets/Data/high_score.txt')
content = path1.read_text() 
high_score_int = int(content)
high_score_str = str(content)

def update_high_score(high_score, points1):
    if points1 > high_score:
        path1.write_text(str(points1))

def show_high_score(high_score_current, x, y, a, b):
    high_score_text1 = high_score_font.render("High Score: ", True, (255, 255, 255))
    screen.blit(high_score_text1, (x, y))
    high_score_text2 = high_score_font.render(high_score_current, True, (255, 255, 255))
    screen.blit(high_score_text2, (a, b))


def game_over():
    over_title_text = over_title_font.render("GAME OVER", True, (255, 255, 255)) #blood red - 120, 6, 6
    screen.blit(over_title_text, (125, 40))

    bullets_missed = bullets_used - aliens_killed
    points = aliens_killed * 10 - bullets_missed*5

    show_aliens_killed(statistics_font2, 75, 200)
    show_bullets_used(statistics_font2, 75, 275)
    show_accuracy(statistics_font2, 75, 350)
    show_total_points(points, 500, 200, 550, 250)
    events_in_over(75,475, 75, 500 )
    update_high_score(high_score_int, points)
    content2 = path1.read_text()
    show_high_score(content2, 500, 300, 550, 350)



def main_menu():

    # Title
    title_text = title_font.render("Space Invader", True, (255, 200, 200))
    screen.blit(title_text, (90, 100))

    # Credits
    credits_text = credits_font.render("by: closedultra", True, (255, 255, 255))
    screen.blit(credits_text, (575, 500))

    # Main Text
    main_text_1 = main_menu_font.render("Start Game", True, (255, 255, 255))
    screen.blit(main_text_1, (150, 250))
    main_text_1_2 = main_menu_font2.render("(Press Spacebar)", True, (255, 255, 255))
    screen.blit(main_text_1_2, (335, 260))

    # Spaceship selection
    main_text_2 = main_menu_font.render(
        "Choose your spaceship: ", True, (255, 255, 255)
    )
    screen.blit(main_text_2, (150, 300))
    screen.blit(spaceship1, (150, 350))
    screen.blit(spaceship2, (250, 350))
    screen.blit(spaceship3, (350, 350))
    screen.blit(spaceship4, (450, 350))
    spaceship_selection1 = main_menu_font.render("1", True, (255, 255, 255))
    spaceship_selection2 = main_menu_font.render("2", True, (255, 255, 255))
    spaceship_selection3 = main_menu_font.render("3", True, (255, 255, 255))
    spaceship_selection4 = main_menu_font.render("4", True, (255, 255, 255))
    screen.blit(spaceship_selection1, (175, 425))
    screen.blit(spaceship_selection2, (275, 425))
    screen.blit(spaceship_selection3, (375, 425))
    screen.blit(spaceship_selection4, (475, 425))
    spaceship_selection_main = main_menu_font3.render('Press the number of the Space shooter you want to choose.', True, (255, 255, 255))
    screen.blit(spaceship_selection_main, (150, 475))
    quit = main_menu_font.render('Press esc to Quit.', True, (255, 255, 255))
    screen.blit(quit, (150, 500))

def reset_game():
    global playerx, playery, aliens_killed, bullets_used, bullets, num_of_enemies
    playerx = 370
    playery = 480
    aliens_killed = 0
    bullets_used = 0
    bullets.clear()

    enemyx.clear()
    enemyy.clear()
    enemyx_change.clear()
    enemyy_change.clear()
    num_of_enemies = 4
    for i in range(num_of_enemies):
        enemyx.append(random.randint(0, 735))
        enemyy.append(random.randint(50, 150))
        enemyx_change.append(random.choice([0.3, -0.3]))
        enemyy_change.append(60)



running = True

while running:

    screen.fill((0, 153, 176))
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        # using this pygame will loop over all events that occur
        if event.type == pygame.QUIT:  # <--- Changed from pygame.Quit to pygame.QUIT
            running = False
        if state == "main_menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    state = "main_game"
                if event.key == pygame.K_1:
                    spaceship = "Assets/Images/spaceship1.png"
                    player_img = pygame.image.load(spaceship)
                if event.key == pygame.K_2:
                    spaceship = "Assets/Images/spaceship2.png"
                    player_img = pygame.image.load(spaceship)
                if event.key == pygame.K_3:
                    spaceship = "Assets/Images/spaceship3.png"
                    player_img = pygame.image.load(spaceship)
                if event.key == pygame.K_4:
                    spaceship = "Assets/Images/spaceship4.png"
                    player_img = pygame.image.load(spaceship)
        elif state == "main_game":
            if event.type == pygame.KEYDOWN:             
                if event.key == pygame.K_LEFT:
                    playerx_change = -0.7
                if event.key == pygame.K_RIGHT:
                    playerx_change = 0.7
                if event.key == pygame.K_SPACE:
                    if len(bullets) <= max_bullets:
                        bulletx = playerx
                        bullets.append([bulletx, playery])
                        bullets_used += 1
                        bullet_sound.play()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    playerx_change = 0

            if event.type == spawn_enemy_event:
                add_new_enemy()
        
        elif state == 'game_over':
            if event.type == pygame.KEYDOWN:                                 
                if event.key == pygame.K_RETURN:
                    reset_game()
                    state = "main_game"
                elif event.key == pygame.K_ESCAPE:
                    reset_game()
                    state = "main_menu"


    if state == "main_menu":
        main_menu()

    elif state == "main_game":

        # creating boundary for player
        playerx += playerx_change
        if playerx <= 0:
            playerx = 0
        elif (
            playerx >= 736
        ):  # considering size of image like our is 64 therefore 800-64=736
            playerx = 736

        # creating boundary for enemy
        for i in range(num_of_enemies):
            # Game Over
            if enemyy[i] > 440:
                state = "game_over"

            enemyx[i] += enemyx_change[i]
            if enemyx[i] <= 0:
                enemyx_change[i] = 0.5
                enemyy[i] += enemyy_change[i]
            elif enemyx[i] >= 736:
                enemyx_change[i] = -0.5
                enemyy[i] += enemyy_change[i]

            # Collision
            for bullet in bullets[:]:
                collision = iscollision(enemyx[i], enemyy[i], bullet[0], bullet[1])
                if collision:
                    c_sound.play()
                    bullet[1] = 480
                    aliens_killed += 1
                    bullets.remove(bullet)
                    enemyx[i] = random.randint(0, 735)
                    enemyy[i] = random.randint(50, 150)
                    break

            enemy(enemyx[i], enemyy[i], i)
        # Bullet Movement
        for bullet in bullets[:]:   # use a copy to modify safely
            bullet[1] += bullety_change
            screen.blit(bullet_img, (bullet[0] + 16, bullet[1] + 10))
            
            if bullet[1] < 0:
                bullets.remove(bullet)

        player(playerx, playery)
        show_aliens_killed(statistics_font_1, 10, 10)
        show_bullets_used(statistics_font_1, 10, 40)
        show_accuracy(statistics_font_1, 10, 70)

    if state == "game_over":
        game_over()

    pygame.display.update()
