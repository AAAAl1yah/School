import time
import sys
import pygame
import os
from colorama import Fore, Style, init

#BANAAG, CABONITA, GAVIOLA, TAMIROY, ROSINTO, VILLARETE

# Initialize colorama for colored text
init(autoreset=True)

# Initialize Pygame
pygame.init()
pygame.mixer.init()

os.environ["SDL_AUDIODRIVER"] = "dummy"

# Function to play music with an optional fade-in
def play_music(track, fade_in=2000):  # 2000ms (2 seconds) fade-in
    pygame.mixer.music.load(track)
    pygame.mixer.music.play(-1, fade_ms=fade_in)  # -1 loops indefinitely

# Function to transition between two songs
def transition_music(new_track, fade_out=2000, fade_in=2000):
    pygame.mixer.music.fadeout(fade_out)  # Fade out current music
    time.sleep(fade_out / 1000)  # Wait for fade-out to finish
    play_music(new_track, fade_in) 

while pygame.mixer.music.get_busy():
    time.sleep(1)

os.environ["SDL_AUDIODRIVER"] = "dummy"  # Prevents crashes in cloud environments
pygame.mixer.init()

#SFX
start = pygame.mixer.Sound("RetroGameOver.wav.wav") 
start.set_volume(0.7) 
thud = pygame.mixer.Sound("thud-291047.mp3")
thud.set_volume(1.0) 
paper_rip = pygame.mixer.Sound("paper-rip-fast-252617.mp3")
paper_rip.set_volume(1.0) 
phone_alarm = pygame.mixer.Sound("digital-alarm-107256.mp3")
phone_alarm.set_volume(0.8)

def get_choice(options):
    """Function to get a valid user choice from a list of options."""
    while True:
        choice = input("\nEnter the number of your choice: ")
        if choice in options:
            return choice
        else:
            type_text("Invalid choice. Please select a valid option.")

def type_text(text, color=Fore.WHITE, delay=0.02, new_line=True):
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
    type_text("  |    |   |  |  \_/ __ \  /    \  \/\__  \  /    \  \/ /\__  \  /  ___/ |    |   \__  \\ \/ \/ /", Fore.RED)
    type_text("  |    |   |   Y  \  ___/  \     \____/ __ \|   |  \   /  / __ \_\___ \  |    |___ / __ \\     / ", Fore.CYAN)
    print("  |____|   |___|  /\___  >  \______  (____  /___|  /\_/  (____  /____  > |_______ (____  /\/\_/  ")
    print("                \/     \/          \/     \/     \/           \/     \/          \/    \/        ")
intro() 

print("Press Enter to continue ₊˚⊹♡")
input()

def exp():
    play_music("2020-03-22_-_A_Bit_Of_Hope_-_David_Fesliyan.mp3")
    type_text("Welcome to Rivermere, a city where they follow a strict law,")
    time.sleep(0.5)
    type_text("The Canvas Law", Fore.CYAN)
    input()
    type_text("Basically, here's the main gist of the law:")
    type_text("Everyone is given a blank canvas on the day of their birth")
    input()
    type_text("Throughout their life, the decisions they make paints the canvas with different hues based on how bad or how good your choices have been")
    input()
    type_text("This canvas will be a very important aspect in your life")
    input()
    type_text("Based on how vibrant or how dull your canvas is, your life could be paradise on Earth")
    type_text("or")
    time.sleep(0.5)
    type_text("A living hell.", Fore.RED)
    input()
    type_text("You are Caroline Wellsford, a 19-year-old journalist with an average life and an average canvas, some vibrant yellows here, some black stains there")
    type_text("Good luck on your adventure, Caroline")
    input()
    start.play()
exp()

def wake_up_scene():
    play_music("2021-08-17_-_8_Bit_Nostalgia_-_www.FesliyanStudios.com.mp3")
    time.sleep(1)
    thud.play()
    type_text("\n[Sound of a dull *thud* against glass]") 
    time.sleep(0.5)
    type_text("You stir awake, the early morning light seeping through your curtains.")
    input()
    thud.play()
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
        phone_alarm.play()
        type_text("Your pocket vibrates – it's your alarm going off to wake you up for the day.")
    
    elif choice == "2":
        type_text("You lay back on the comfort of your bed, snuggling against the coldness of your pillow, ready to seep back into your dreams.")
        input()
        phone_alarm.play()
        type_text("...Until your phone alarm goes off to wake you up for the day.")
    elif choice == "3":
        type_text("You watch as the town around you slowly starts to wake up and feel more lively.")
        input()
        type_text("How do you feel about this?")
        type_text("1. It's calming and beautiful.")
        type_text("2. It irritates you – you wish it would be night forever.")
        type_text("3. You don’t care.")
        
        sub_choice = input("Enter your choice: ")
        
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
        phone_alarm.play()
        type_text("Suddenly, your phone alarm goes off")
        input()
        type_text("This is the signal to start your day")

# Run the scene
wake_up_scene()

def letter_quest():
    play_music("2021-08-17_-_8_Bit_Nostalgia_-_www.FesliyanStudios.com.mp3")
    time.sleep(1)
    type_text("\nAs you finish your morning routine, you find a letter on your kitchen table.")
    time.sleep(0.5)
    type_text("It's an envelope with no return address. The handwriting on it looks familiar... but you can't place it.")
    input()
    type_text("You slowly tear open the envelope, revealing a single sheet of paper.")
    paper_rip.play()
    input()
    
    type_text("The note reads:\n\n'Caroline,\n\nYour canvas is starting to change. You've been chosen. Meet me at the old library at 8pm.'")
    input()

    type_text("What do you do?")
    type_text("1. Ignore it, and go on with your day as usual.")
    type_text("2. Go to the old library tonight, and find out who sent the letter.")
    type_text("3. Investigate the handwriting and see if you can figure out who wrote it.")

    choice = input("\nEnter the number of your choice: ")

    letter_quest_decision(choice)

def bittersweet_ending():
    play_music("2019-03-17_-_Too_Crazy_-_David_Fesliyan.mp3")
    type_text("The cold night air is thick with tension as Caro, Samir, and Liora crouch behind the ruins of an old train car.", Fore.GREEN)
    type_text("Ahead, the hidden meeting has begun. Cloaked figures circle a massive canvas, chanting in unison.", Fore.RED)
    input()

    type_text("Samir clenches his jaw. 'We’re really doing this.'", Fore.MAGENTA)
    type_text("Liora tightens her grip on the files she stole. 'No turning back now.'", Fore.CYAN)
    input()

    type_text("The three of them storm in.", Fore.GREEN)
    type_text("Chaos erupts. The enforcers draw weapons. The leader shouts orders. The ritual halts.", Fore.RED)
    input()

    type_text("Samir lunges at the enforcers, throwing punches like his life depends on it.", Fore.MAGENTA)
    type_text("Liora climbs onto the stage, scattering stolen documents for all to see.", Fore.CYAN)
    input()

    type_text("Caro moves fast, finding the heart of the operation—the control panel that connects to every canvas in Rivermere.", Fore.GREEN)
    type_text("They only have seconds to act.", Fore.RED)
    input()

    type_text("'NOW, CARO!' Liora shouts.", Fore.CYAN)
    type_text("Caro takes a deep breath and pulls the lever.", Fore.GREEN)
    input()

    type_text("The entire system collapses.", Fore.RED)
    type_text("Canvases all over Rivermere flicker, distort, reset.", Fore.GREEN)
    input()

    type_text("The enforcers panic. The leader screams. The rebellion is won.", Fore.RED)
    input()

    type_text("Samir staggers toward Caro, blood on his hands, his usual smirk gone.", Fore.MAGENTA)
    type_text("'Guess we’re heroes now, huh?'", Fore.MAGENTA)
    type_text("Caro exhales, looking at the broken pieces of the machine. 'I just hope it was worth it.'", Fore.GREEN)
    input()

    type_text("The city will never be the same.", Fore.RED)
    type_text("You got the BITTERSWEET Ending")
    input()

def tough_choice():
    play_music("2019-03-17_-_Too_Crazy_-_David_Fesliyan.mp3")
    type_text("The leader of the group stands before Caro, eyes sharp, voice steady.", Fore.RED)
    type_text("'You think you’re different? That you’re better than us?'", Fore.RED)
    input()

    type_text("Caro’s fists clench. 'I think people should choose their own paths.'", Fore.GREEN)
    type_text("The leader smirks. 'Then make a choice. Right now.'", Fore.RED)
    input()

    type_text("'You can join us and maintain order...'", Fore.RED)
    type_text("'Or you can destroy everything and leave Rivermere in chaos.'", Fore.RED)
    input()

    type_text("Liora steps forward. 'Caro, you know what they’ve done. End this.'", Fore.CYAN)
    type_text("Samir shifts uncomfortably. 'Yeah, but... what happens if we do?'", Fore.MAGENTA)
    input()

    type_text("Caro swallows hard.", Fore.GREEN)
    type_text("Their entire life has led to this moment. One choice. One action. No turning back.", Fore.RED)
    input()

    type_text("With a heavy heart, Caro grips the lever and pulls.", Fore.GREEN)
    type_text("The system crashes. Every canvas in Rivermere flickers before going blank.", Fore.RED)
    input()

    type_text("People wake up to find their fates unwritten. No guidance. No restrictions. No control.", Fore.GREEN)
    type_text("Some rejoice. Others panic. Fear spreads like wildfire.", Fore.RED)
    input()

    type_text("Samir exhales, rubbing the back of his neck. 'You really just changed the world.'", Fore.MAGENTA)
    type_text("Caro stares at the city skyline, uncertainty settling deep in their chest. 'Yeah. I hope they don’t hate me for it.'", Fore.GREEN)
    input()

    type_text("The revolution is over. But at what cost?", Fore.RED)
    type_text("You got the TOUGH CHOICES Ending")
    input()

def ambiguous_ending():
    play_music("2019-03-17_-_Too_Crazy_-_David_Fesliyan.mp3")
    type_text("The leader of the group is dragged away in cuffs.", Fore.RED)
    type_text("Rivermere watches as the rebellion wins. The city is free.", Fore.GREEN)
    input()

    type_text("Days later, Caro finds something strange on their canvas.", Fore.GREEN)
    type_text("A new message, scrawled in deep red ink:", Fore.RED)
    input()

    type_text("'You think you’ve won?'", Fore.RED)
    type_text("'You don’t even know the half of it.'", Fore.RED)
    input()

    type_text("Their breath catches. The words seem to flicker, like they’re alive.", Fore.GREEN)
    type_text("Then, just as quickly as they appeared… they vanish.", Fore.RED)
    input()

    type_text("Samir frowns. 'Caro… what did you do?'", Fore.MAGENTA)
    type_text("Caro doesn’t answer.", Fore.GREEN)
    input()

    type_text("They just stare at the blank space on their canvas, heart pounding.", Fore.RED)
    type_text("As if something—or someone—is still watching.", Fore.RED)
    input()

    type_text("The fight might not be over.", Fore.RED)
    type_text("You got the AMBIGUOUS Ending")
    input()

def ending_choice():
    type_text("What will you do?", Fore.YELLOW)
    type_text("1. Confront the group head-on.", Fore.YELLOW)
    type_text("2. Destroy the system to free everyone.", Fore.YELLOW)
    type_text("3. Expose the group and let the town decide.", Fore.YELLOW)
    
    choice = input("Enter 1, 2, or 3: ")
    
    if choice == "1":
        bittersweet_ending()
    elif choice == "2":
        tough_choice()
    elif choice == "3":
        ambiguous_ending()
    else:
        type_text("Invalid choice. The revolution crumbles before it even begins.", Fore.RED)
        input()
  
def goodnight_caroline():
    time.sleep(0.3)
    play_music("2024-05-23_-_Ride_The_Mellow-vator_-_www.FesliyanStudios.com.mp3")
    type_text("You sit in your apartment, staring at the letter on your table.", Fore.GREEN)
    input()
    
    type_text("Going to that meeting feels like stepping into something too big, too dangerous.", Fore.GREEN)
    input()
    
    type_text("You tell yourself it’s not your fight. You’ll go to bed, wake up tomorrow, and everything will be normal.", Fore.GREEN)
    input()
    
    type_text("But normal doesn’t come.", Fore.RED)
    input()
    play_music("2019-03-17_-_Too_Crazy_-_David_Fesliyan.mp3")

    type_text("A soft *click* echoes from your front door.", Fore.RED)
    type_text("Your blood runs cold. You don’t remember unlocking it.", Fore.GREEN)
    input()
    
    type_text("Before you can react, a shadow moves in the darkness.", Fore.RED)
    type_text("A gloved hand clamps over your mouth.", Fore.RED)
    input()
    
    type_text("You struggle, but it’s useless. Cold metal presses against your skin.", Fore.RED)
    input()
    
    type_text("'Should've stayed quiet, Wellsford,' a voice murmurs.", Fore.CYAN)
    input()
    
    type_text("Pain blooms in your chest. Your body collapses to the floor, vision swimming.", Fore.RED)
    input()
    
    type_text("As the world fades, the last thing you see is red soaking into the floorboards—", Fore.RED)
    type_text("—your canvas, painted for the last time.", Fore.RED)
    input()

    type_text("You got the GOODNIGHT CAROLINE Ending", Fore.RED)
    input()


def midnight_meeting():
    play_music("2019-03-17_-_Too_Crazy_-_David_Fesliyan.mp3")
    type_text("The city is eerily quiet at this hour. Streetlights flicker, casting long shadows over the damp pavement.", Fore.RED)
    input()
    
    type_text("You pull your jacket tighter around you, scanning the area. Samir said to meet at the abandoned train station.", Fore.GREEN)
    type_text("Your heart pounds as you approach the rusted entrance, its metal gates slightly ajar.", Fore.RED)
    input()
    
    type_text("'Took you long enough.'", Fore.MAGENTA)
    type_text("Samir steps out of the darkness, arms crossed, his usual smirk replaced by something more serious.", Fore.RED)
    input()
    
    type_text("'Traffic was terrible,' you say dryly.", Fore.GREEN)
    type_text("He snorts. 'Classic Caro.'", Fore.MAGENTA)
    input()
    
    type_text("But before you can respond, a voice cuts through the silence.", Fore.RED)
    type_text("'You weren’t followed, were you?'", Fore.CYAN)
    input()
    
    type_text("A hooded figure emerges from the shadows. You tense up, instincts screaming at you to run.", Fore.GREEN)
    type_text("Samir raises a hand. 'Relax. This is Liora. She’s with us.'", Fore.MAGENTA)
    input()
    
    type_text("Liora pulls back her hood, revealing sharp eyes that assess you carefully.", Fore.RED)
    type_text("'We don’t have much time. The group is making a move soon. If we don’t act now, Rivermere is theirs.'", Fore.CYAN)
    input()
    
    type_text("You exchange a glance with Samir. This is bigger than you imagined. But there’s no turning back now.", Fore.GREEN)
    input()
    
    type_text("The revolution starts tonight.", Fore.RED)
    input()
    
    ending_choice()

def library_decision(choice):
    if choice == "1":
        type_text("'I’ll help you,' you say, determination in your voice. 'But we need to know more. We can't act blindly.'", Fore.GREEN)
        input()
        
        type_text("Samir smirks. 'That's my Caro. Always thinking ahead.'", Fore.MAGENTA)
        type_text("'Stopp,' you mutter, rolling your eyes.", Fore.GREEN)
        type_text("'Alright, alright.' He chuckles, but his expression quickly turns serious. 'There's a hidden group meeting in the city at midnight. I'll meet you there.'", Fore.MAGENTA)
        input()
        
        type_text("As you leave the library, you can’t shake the feeling that this is just the beginning of a much larger story.")
        type_text("You're in too deep now.", Fore.RED)
        #this is a Sum 41 reference ⤴
        midnight_meeting()

    elif choice == "2":
        type_text("'I can't get involved in this,' you say, shaking your head. 'I’ve got my own life to live.'", Fore.GREEN)
        input()
        
        type_text("Samir sighs dramatically. 'And here I thought we were in this together. Guess I’ll just get captured and tortured alone. No big deal.'", Fore.MAGENTA)
        
        type_text("'Samir, stopp,' you groan. 'This is serious.'", Fore.GREEN)
        input()
        
        type_text("His smirk fades slightly. 'I know. But so is your choice. Just… be careful, okay? Also, there's a hidden group meeting in the city at midnight if you want to know more''", Fore.MAGENTA)
        type_text("You nod, but as you leave the library and return home, a strange sense of guilt lingers.")
        type_text("What if you made the wrong choice?", Fore.RED)
        goodnight_caroline()

    elif choice == "3":
        type_text("'Before I make any decisions, I need to understand more,' you say. 'What exactly are you talking about?'", Fore.GREEN)
        input()
        
        type_text("Samir sighs, leaning against a bookshelf. 'Always the cautious one. Classic Caro.'", Fore.MAGENTA)
        type_text("'You’re really testing my patience right now,' you mutter.", Fore.GREEN)
        input()
        
        type_text("He holds up his hands in surrender, but his tone turns serious. 'Fine, fine. Look, the group knows people like you are starting to question them.'", Fore.MAGENTA)
        input()
        
        type_text("'What do they want?' you ask, the weight of the situation growing heavier by the second.", Fore.GREEN)
        
        type_text("'Power,' Samir replies simply. 'They manipulate people’s canvases to control them. We need to stop them before they gain more control over Rivermere. I heard there's a hidden group meeting in the city at midnight.'", Fore.MAGENTA)
        input()
        
        type_text("You nod slowly, weighing your options. This is bigger than you thought.", Fore.RED)
        midnight_meeting()


    else:
        type_text("Invalid choice. You stay silent and turn to leave the library")

        type_text("'Well, bye I guess..' You hear Samir say as you walk past the door", Fore.MAGENTA)
        input()

        type_text("Oh and by the way, there's a hidden group meeting in the city at midnight if you're interested' Samir adds", Fore.MAGENTA)

        type_text("You walk back home, the words from Samir's mouth never leaving your brain")
        midnight_meeting()

def library_encounter():
    play_music("2019-03-17_-_Too_Crazy_-_David_Fesliyan.mp3")
    time.sleep(1)

    type_text("8:00PM", Fore.RED)
    type_text("\nYou stand in front of the old library, its towering entrance looming over you.", Fore.CYAN)
    type_text("Before you can even touch the handle, the door creaks open on its own.")
    input()

    type_text("The air inside is thick with the scent of old parchment and dust, the shelves packed with forgotten knowledge.")
    type_text("Dim lights flicker above, casting restless shadows across the floor.")
    input()

    type_text("As you take a cautious step inside, a figure emerges from the darkened hallway.")
    type_text("Their cloak sways slightly, face hidden, but their presence is undeniably deliberate.")
    input()

    type_text("'I knew you'd come,' they murmur, voice calm but knowing. 'We have much to discuss, Caroline.'", Fore.RED)
    input()

    type_text("You tense, but before you can react, they pull back their hood, revealing—", Fore.RED)
    type_text("—a familiar face.", Fore.YELLOW)
    input()
    play_music("2023-08-18_-_Swingin_Yuletide_-_www.FesliyanStudios.com.mp3")
    type_text("It's Samir.", Fore.MAGENTA)
    
    input()

    type_text("'Samir?!' you blurt out, eyes wide. 'I thought you left Rivermere years ago!'", Fore.GREEN)
    
    type_text("Samir smirks, hands in his pockets. 'Aww, you missed me? I'm touched, Caro.'", Fore.MAGENTA)
    #this is a Caro-Kann Chess reference ⤴
    
    type_text("'Stopp,' you mumble, crossing your arms. 'What are you even doing here?'", Fore.GREEN)
    input()

    type_text("'Oh, you know. Being mysterious. Wearing dramatic cloaks. Stalking childhood friends in abandoned libraries... the usual.'", Fore.MAGENTA)
    
    type_text("'Samir, I swear—' you start, but he just grins.", Fore.GREEN)
    input()

    type_text("'Relax, relax. Alright, listen.' His playful tone fades slightly, but there's still a glint of amusement in his eyes.", Fore.MAGENTA)
    type_text("'I had to leave for a while, but I've been watching. Your canvas… it’s changing. And you need to understand why.'", Fore.MAGENTA)
    input()
    play_music("2019-03-17_-_Too_Crazy_-_David_Fesliyan.mp3")

    type_text("'What do you mean? What’s happening to my canvas?' You can’t hide the unease creeping into your voice.", Fore.GREEN)
    
    type_text("Samir steps forward and places a hand on your shoulder. His touch is warm, steady. Serious now.")
    type_text("'There’s a force in Rivermere. A group manipulating people’s canvases, controlling their lives without them even knowing. It’s time to fight back, Caro.'", Fore.MAGENTA)
    input()

    type_text("'You’re messing with me, right?' You force a chuckle, but it falls flat.", Fore.GREEN)

    type_text("'I wish I was.' His smirk is gone. 'This isn't just a story in one of these dusty books. It’s real. And you? You’re already caught in it.'", Fore.MAGENTA)
    input()

    type_text("A shiver runs down your spine. Could he be telling the truth?", Fore.RED)
    type_text("What do you do?")
    type_text("1. Agree to help Samir and join his cause to uncover the truth.")
    type_text("2. Reject the idea, not wanting to get involved in something so dangerous.")
    type_text("3. Ask Samir more questions to understand what he means before deciding.")

    choice = input("\nEnter your choice: ")

    library_decision(choice)


def handwriting_decision(choice):
    if choice == "1":
        type_text("\nYou decide to dig deeper, determined to uncover the truth.", Fore.GREEN)
    elif choice == "2":
        type_text("\nYou push the thoughts aside, trying to return to your normal life... but something feels off.", Fore.RED)
    else:
        type_text("\nYou hesitate, uncertain of what to do next.", Fore.YELLOW)

def letter_quest_decision(choice):
    if choice == "1":
        type_text("You shrug it off and continue your normal routine. However, the thought of the letter lingers in the back of your mind.")
        input()
        type_text("As the day passes, you feel an odd sense of dread. Something doesn't feel right.")
        input()
        type_text("Eventually, you try to push the thought away, but deep down, you wonder if you made the wrong choice.")
        input()
        type_text("Days pass. Your canvas begins to shift, subtly but undeniably. Was the letter a warning? Maybe you'll never know.")
        investigate_handwriting()
    
    elif choice == "2":
        library_encounter()
    
    elif choice == "3":
        type_text("You squint at the handwriting, trying to make sense of it. The letters are uneven, some almost frantic.")
        input()
        type_text("A thought crosses your mind—could it be someone you know? You rack your brain, but it’s a name you’ve never seen before.")
        input()
        type_text("You still feel the urge to follow up, but you don’t know where to start.")
        input()
        type_text("The handwriting remains a mystery, but it stirs something inside of you. You wonder if it’s time to take the leap and follow the strange instructions.")
        investigate_handwriting()
    else:
        type_text("Invalid choice. The mystery lingers in the air as you ponder your next move.")
        letter_quest()

def handwriting_decision(choice):
    if choice == "1":
        type_text("Determined to uncover the truth, you tighten your grip on the letter and take a deep breath. This mystery won’t solve itself.", Fore.GREEN)
        library_encounter()
    elif choice == "2":
        type_text("You shove the letter into a drawer, convincing yourself it’s nothing. But deep down, you know this isn’t over.", Fore.GREEN)
        library_encounter()
    else:
        type_text("Uncertain, you hesitate, realizing there may be no turning back once you decide.", Fore.GREEN)
        library_encounter()

def investigate_handwriting():
    play_music("2020-03-22_-_A_Bit_Of_Hope_-_David_Fesliyan.mp3")
    time.sleep(1)
    type_text("\nYou decide to investigate the handwriting on the letter, unsure if it's a friend or an enemy.", Fore.CYAN)
    input()

    # 🔹 **Post Office Scene**
    type_text("You start by visiting the local post office, hoping someone might remember who sent the mysterious letter.", Fore.CYAN)
    input()

    type_text("The clerk behind the counter, an old man with thick glasses, squints at the letter and lets out a thoughtful hum.", Fore.WHITE)
    type_text("'Hmm... the ink is expensive, and the handwriting is meticulous. That’s not something we see every day.'", Fore.YELLOW)
    
    type_text("\nDo you:", Fore.WHITE)
    type_text("1. Ask if they’ve seen anyone suspicious recently.", Fore.WHITE)
    type_text("2. Show them another letter to compare handwriting.", Fore.WHITE)

    choice = input("\nEnter your choice: ")
    
    if choice == "1":
        type_text("The old man scratches his chin and glances around before lowering his voice.", Fore.WHITE)
        type_text("'Now that you mention it... A woman dressed in black came in last week, asking about anonymous deliveries. She seemed nervous, kept looking over her shoulder.'", Fore.YELLOW)
    elif choice == "2":
        type_text("The old man adjusts his glasses and examines the second letter carefully.", Fore.WHITE)
        type_text("'This handwriting... it’s familiar. Years ago, there was a group that sent coded messages using a script just like this. I thought they had disappeared.'", Fore.YELLOW)
    else:
        type_text("The clerk shrugs and returns to his work, uninterested in speculation.", Fore.YELLOW)

    input()

    # 🔹 **Bookshop Scene**
    type_text("You decide to check the local bookshop, hoping to find something about the handwriting style.", Fore.CYAN)
    input()

    type_text("The bookshop is dimly lit, the scent of old paper hanging in the air. The shopkeeper, a woman in her fifties with ink-stained fingers, eyes you curiously as you approach.", Fore.WHITE)
    type_text("'Handwriting analysis? That’s a rare interest these days. Let me see...'", Fore.YELLOW)
    
    type_text("She flips through a dusty reference book and frowns.", Fore.WHITE)
    type_text("'This script is deliberate, meant to conceal the writer’s true style. Whoever wrote this was trained. It’s not just fancy penmanship—it’s a disguise.'", Fore.YELLOW)
    
    input()

    # 🔹 **Old Lady’s House Scene**
    type_text("Following a whispered tip from the bookshop owner, you make your way to the outskirts of town to visit an old woman who might recognize the script.", Fore.CYAN)
    input()

    type_text("The house is ancient, vines creeping up the stone walls. The door creaks as an elderly woman, wrapped in a thick shawl, peers at you suspiciously.", Fore.WHITE)
    type_text("'Strangers don't come here often. What do you want?'", Fore.YELLOW)

    type_text("You show her the letter. Her eyes widen, and her fingers tremble as she traces the ink.", Fore.WHITE)
    type_text("'I’ve seen this before... Long ago. These letters ruin lives. If you’ve received one, you must be careful.'", Fore.YELLOW)
    
    type_text("\nDo you:", Fore.WHITE)
    type_text("1. Ask who else has received such letters.", Fore.WHITE)
    type_text("2. Demand to know where these letters come from.", Fore.WHITE)

    choice = input("\nEnter your choice: ")
    
    if choice == "1":
        type_text("The old woman sighs, staring at the flickering candle on her table.", Fore.WHITE)
        type_text("'There were others... Journalists, officials, even a shopkeeper. Some vanished, others changed overnight—like they became different people.'", Fore.YELLOW)
    elif choice == "2":
        type_text("Her gaze darkens as she shakes her head.", Fore.WHITE)
        type_text("'You don’t find them. They find you. And once they do, there’s no going back.'", Fore.YELLOW)
    else:
        type_text("She presses her lips into a thin line and turns away. 'I’ve already said too much.'", Fore.YELLOW)
    
    input()

    # 🔹 **Police Station Scene**
    type_text("With unease settling in, you decide to visit the police station to see if they have records of similar cases.", Fore.CYAN)
    input()

    type_text("A young officer greets you with a raised brow as you present the letter.", Fore.WHITE)
    type_text("'We don’t usually deal with things like this... but let me check the archives.'", Fore.BLUE)

    type_text("After a few minutes, he returns, his expression unreadable.", Fore.WHITE)
    type_text("'There are old reports of letters like these, always tied to disappearances or sudden changes in behavior. Whatever this is, it’s not just a coincidence.'", Fore.BLUE)
    
    input()
    
    # 🔹 **Decision Point**
    type_text("You leave the police station with a growing sense of unease. The puzzle pieces are falling into place, but what they form is still unclear.", Fore.RED)
    input()
    
    type_text("\nYou now have a choice: What will you do next?", Fore.WHITE)
    type_text("1. Follow the clues and try to track down the group.", Fore.WHITE)
    type_text("2. Ignore it and go back to your normal life.", Fore.WHITE)

    choice = input("\nEnter your choice: ")
    
    handwriting_decision(choice)

letter_quest()

play_music("2019-06-17_-_Super_Spiffy_-_David_Fesliyan.mp3")
type_text("Thank you for playing the demo to my game! (˶˃ ᵕ ˂˶) .ᐟ.ᐟ")
type_text("Credits: \nDev \n-Aaliyah Gaviola \nEmotional Supporters \n-Kiza Jean Banaag \n-Toni Reese Leigh Villarete \n-Mariam Angel Cabonita \n-Cassie Rosinto \n-Thea Nicole Tamiroy")
type_text("Untill next time")
type_text("...Caroline", Fore.RED)

print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣄⡀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠟⠉⠉⠉⠻⣮⡄")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡏⠀⠀⠀⠀⠀⢻⣿")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⠀⠀⠀⠀⠀⢸⣿")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡟⠀⠀⠀⠀⠀⠀⣾⡿")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⡀⣀⡀⠀⠀⣠⣿⠟⠀⠀⠀⠀⠀⠀⣸⣿⠁")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⠿⠟⠛⠛⠙⠛⠛⠛⠳⢷⣾⡟⠉⠀⠀⠀⠀⠀⢀⣴⣿⠃⠀")
print("⠀⠀⠀⠀⠀⠀⣀⣀⣴⡾⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠀⠀⠀⠀⢀⣤⣾⠟⠁⠀⠀")
print("⠀⠀⠀⠀⣤⡿⠟⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣦⣶⡿⠟⠁⠀⠀⠀⠀")
print("⠀⠀⠀⣼⡟⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠘⢿⣆⠀⠀⠀⠀⠀⠀")
print("⠀⠀⢰⣿⠃⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠁⠹⠆⠀⠀⠈⣿⡆⠀⠀⠀⠀⠀")
print("⠀⠀⣾⡏⠀⣿⠀⠀⠀⣴⠛⢳⡄⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀")
print("⠀⣸⡿⠁⠀⣟⠀⠀⠀⠃⠀⠀⠀⠀⢰⣇⣤⠖⠲⠶⠛⠀⠀⠀⠀⠀⠀⣠⣾⠟⠀⠀⠀⠀⠀⠀")
print("⣰⣿⠃⠀⠀⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⡾⠟⠉⠀⠀⠀⠀⠀⠀⠀")
print("⣿⡇⠀⠀⠀⠀⠛⢶⣤⣀⣀⣀⣀⣀⣀⣠⣤⣤⣴⣶⡶⠿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⢿⣧⠀⠀⠀⠀⠀⠀⠀⣽⡿⠛⠛⠛⠋⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠈⢿⣧⣀⣀⣀⣀⣤⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠉⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
 