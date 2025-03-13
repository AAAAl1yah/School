import time
import sys
import pygame
from colorama import Fore, Style, init

#BANAAG, CABONITA, GAVIOLA, TAMIROY, ROSINTO, VILLARETE

# Initialize colorama for colored text
init(autoreset=True)

def type_text(text, color=Fore.WHITE, delay=0.05, new_line=True):
    """Types out text character by character with optional color and delay."""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    if new_line:
        print(Style.RESET_ALL)  # Reset color and move to the next line

def intro():
    print("___________.__             _________                                     .____                   ")
    print("\__    ___/|  |__   ____   \_   ___ \_____    _______  _______    ______ |    |   _____ __  _  __")
    print("  |    |   |  |  \_/ __ \  /    \  \/\__  \  /    \  \/ /\__  \  /  ___/ |    |   \__  \\ \/ \/ /")
    print("  |    |   |   Y  \  ___/  \     \____/ __ \|   |  \   /  / __ \_\___ \  |    |___ / __ \\     / ")
    print("  |____|   |___|  /\___  >  \______  (____  /___|  /\_/  (____  /____  > |_______ (____  /\/\_/  ")
    print("                \/     \/          \/     \/     \/           \/     \/          \/    \/        ")
intro() 

print("Press Enter to continue")
input()

def exp():
    type_text("Welcome to Rivermere, a city where they follow a strict law,")
    time.sleep(0.5)
    type_text("The Canvas Law", Fore.CYAN)
    input()
    type_text("Basically, here's the main jist of the law:")
    type_text("Everyone is given a blank canvas on the day of their birth")
    input()
    type_text("Throughout their life, the decisions they make paints the canvas with different hughs based on how bad or how good your choices have been")
    input()
    type_text("This canvas will be a very very important aspect in your life")
    input()
    type_text("Based on how vibrant or how dull your canvas is, your life could be paradise on Earth")
    type_text("or")
    time.sleep(0.5)
    type_text("A living hell.", Fore.RED)
    input()
    type_text("You are Caroline Wellsford, a 19 year old journalist with an average life and an average canvas, some vibrant yellows here, some black stains there")
    type_text("Good luck on your adventure, Caroline")
    input()
exp()

def wake_up_scene():
    time.sleep(1)
    type_text("\n[Sound of a dull *thud* against glass]")
    time.sleep(0.5)
    type_text("You stir awake, the early morning light seeping through your curtains.")
    input()
    type_text("Another *thud*. You blink the sleep from your eyes and glance at the window.")
    input()
    type_text("A crumpled newspaper lies against the glass, slowly sliding down.")
    input()
    type_text("It must be the newspaper man making his early morning rounds.")
    
    # Player choice
    type_text("\nWhat do you do?")
    type_text("1. Get up and retrieve the newspaper.")
    type_text("2. Ignore it and go back to sleep.")
    type_text("3. Open the window and check outside.")
    
    choice = input("\nEnter the number of your choice: ")

    scene_one(choice)

def scene_one(choice):
    if choice == "1":
        type_text("You get up to get the newspaper, your blanket still on you, dragging across the floor.")
        input()
        type_text("You go back inside, close the door, and put the newspaper on the kitchen table.")
        input()
        type_text("Your pocket vibrates – it's your alarm going off to wake you up for the day.")
    
    elif choice == "2":
        type_text("You lay back on the comfort of your bed, snuggling against the coldness of your pillow, ready to seep back into your dreams.")
        input()
        type_text("...Until your phone alarm goes off to wake you up for the day.")
    elif choice == "3":
        type_text("You watch as the town around you slowly starts to wake up and feel more lively.")
        input()
        type_text("How do you feel about this?")
        type_text("1. It's calming and beautiful.")
        type_text("2. It irritates you – you wish it would be night forever.")
        type_text("3. You don’t care.")
        
        sub_choice = input("Enter your choice (1, 2, or 3): ")
        
        if sub_choice == "1":
            type_text("You smile at the scene and continue to feel the wind blow through your hair.")
        elif sub_choice == "2":
            type_text("You close the windows, people are insufferable.")
        elif sub_choice == "3":
            type_text("You walk back to your bed.")
        else:
            type_text("Invalid choice. You stare at the ceiling for a while, then your phone alarm goes off.")
    
    else:
        type_text("Invalid choice. You stare at the ceiling for a while")
        input()
        type_text("Suddenly, your phone alarm goes off")
        input()
        type_text("This is the signal to start your day")

# Run the scene
wake_up_scene()
