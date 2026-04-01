# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")


# The game starts here.

#label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    #return

#SCENE 1 
e = Character("control", color="pink")
image chat_panel = "images/low-fidelity/chat_panel_placeholder.jpg"
label start:

    #Showing desktop background of CLEAR
    scene bg "images/low-fidelity/main_homescreen.jpg" with fade

     # Cutscene narration - player just reads/watches
    "The screen flickers to life."
    "This is your first day."
    
    # Pause for atmosphere before CONTROL appears
    pause 1.5

    # Chat panel appears (you'll add the image/overlay later)
    show chat_panel at right with dissolve

    control "Welcome Intern."
    control "Let's see how well you go."

    return