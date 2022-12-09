#!/usr/bin/env python3

# Import the required modules
import pygame
import sys
import random

def move_ball():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    # Moving the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Checking for collision
    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(edge_sound)
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        if ball.left <= 0:
            player_score += 1
        else:
            opponent_score += 1
        ball_restart()
        pygame.mixer.Sound.play(score_sound)
    if ball.colliderect(player) or ball.colliderect(opponent):
        pygame.mixer.Sound.play(hit_sound)
        ball_speed_x *= -1

def opponent_ai():
    if opponent.top + 5 < ball.y:
        opponent.y += oppononent_speed
    if opponent.bottom - 5 > ball.y:
        opponent.y -= oppononent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Main Window
screen_width = 1280
screen_height = 920
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

# Game Font
font = pygame.font.Font('freesansbold.ttf', 32)

# Game Sounds
hit_sound = pygame.mixer.Sound('hit.mp3')
score_sound = pygame.mixer.Sound('reset.mp3')
edge_sound = pygame.mixer.Sound('edge.mp3')

# Game Variables
ball_speed_x = 7
ball_speed_y = 7
oppononent_speed = 7
player_score = 0
opponent_score = 0

# Colors
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

while True:
    # Handling Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] and player.top > 0:
        player.y -= 7
    if keys_pressed[pygame.K_DOWN] and player.bottom < screen_height:
        player.y += 7
   
    # Oppononent AI
    opponent_ai()
    # Moving the ball
    move_ball()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    player_text = font.render(f'{player_score}', False, light_grey)
    screen.blit(player_text, (660, 470))

    opponent_text = font.render(f'{opponent_score}', False, light_grey)
    screen.blit(opponent_text, (600, 470))

    
    pygame.display.flip()
    clock.tick(60)
