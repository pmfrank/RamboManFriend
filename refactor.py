import pygame
import time
import numbers

WIN_WIDTH = 800
WIN_HIEGHT = 600

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HIEGHT))

# Removed this code because it's all in the wrong place
# pygame.display.flip()
# This is why your window was locking up. The loop never exits
# while True:
#     pass
# running = True
# This loop only has one exit and that is to close the windows and terminate the program
# while running:
#     for even in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# Set up the rest of the screen
pygame.display.set_caption('Flappy Rambo')
background_color = (255, 255, 255)
screen.fill(background_color)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# In your old code the loop stayed here, and would only exit by closing the window

# Removed this code because it was move before the main while Look
# pygame.display.set_caption('Flappy Rambo')
# background_color = (255, 255, 255)
# screen.fill(background_color)

# This code was orginally not idented. From what I can tell you wanted it to be part of your while loop so I indented it
    print("Welcome to roobet.com")
    question = 'How much do you wanna lose today?' # Since this string is assigned to a variable named question I think you wanted this to be an input, we'll cover that when we get to talk

    yes = 5000
    no = 100 # You will notice that for these variables I used lowercase names, upper case names are typically reserved for constants and assigned at the top. Something we'll cover when we get to talk
    # print("question") # The way this is written it would literally print the word 'question' the next line below is how you print a variable
    print(question)

    # That's it. You have some import things work it just about learning the process of execution and the syntax. If you stick with it you can be a coder sooner than you may think.