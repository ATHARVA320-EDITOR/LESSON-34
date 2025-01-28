import math
import random
import pygame
screen_width = 800
screen_height = 500
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 4
enemy_speed_y = 40
bullet_speed = 10
collision_distance = 27
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("background.png")
pygame.display.set_caption("SPACE INVADER")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
playerImg = pygame.image.load("player.png")
playerx = player_start_x
playery = player_start_y
playerx_change = 0
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemines = 6
for i in range(num_of_enemines):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, screen_width - 64))
    enemyY.append(random.randint(enemy_start_y_min, enemy_start_y_max))
    enemyX_change.append(enemy_speed_x)
    enemyY_change.append(enemy_speed_y)
    bulletImg = pygame.image.load("bullet.png")
    bulletX = 0
    bulletY = player_start_y
    bulletX_change = 0
    bulletY_change = bullet_speed
    bullet_state = "ready"
    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    textX = 10
    textY = 10
    over_font = pygame.font.Font('freesansbold.ttf', 64)
    def show_score(x, y):
        score = font.render("Score : " + str(score_value), True, (255, 255, 255))
        screen.blit(score,(x, y))