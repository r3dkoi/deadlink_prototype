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

#Image definitions
image welcome_back_screen = "images/Iteration_1/placeholder/Welcome_back_screen.png"
image control_icon = "images/Iteration_1/control_icon.png"
image player_icon = "images/Iteration_1/player_icon.png"


#Image scaling definitions 
transform fit_screen:
    xalign 0.5
    yalign 0.5
    xsize config.screen_width
    ysize config.screen_height
    fit "cover"

transform chat_panel_position:
    xalign 0.99        # pushes to the right
    yalign 0.05        # sits near the top
    zoom 0.5           # scales it down to 40% of original size

#PLAYER NAME
default player_name = "" ## 'default' ensures the variable exists even if the game is loaded from a save


#INPUT NAME PLAYER CODE

screen name_input_screen():
    vbox: 
    align (0.5, 0.5)
    spacing 20

    text "WHAT IS YOUR NAME, INTERN?" size 30 #Text prompt for player

    input:
    value VariableInputValue("player_name")
    length 20 
    pixel_width 300

    textbutton "Is this true?"
    action [
        SetVariable("player_name", player_name.strip()), #Saves type name into player_name
        Jump("scene_two")
    ]
    sensitive player_name.strip() != "" # Keeps the button greyed out and unclickable until the player has typed something

#SCENE 1
label start:
    scene black #Sets background just to black for scene 1
    call screen name_input_screen() 

#SCENE 2
label scene_two





#SCENE 2
define control = Character("CONTROL", color="#00FF00")
define player = 
label start:

    #Showing desktop background of CLEAR
    scene bg main_homescreen at fit_screen with fade
    
     # Cutscene narration - player just reads/watches
    "The screen flickers to life."
    ""
    
    # Pause for atmosphere before CONTROL appears
    pause 1.5

    # Chat panel appears (you'll add the image/overlay later)
    show control_icon at chat_panel_position with dissolve

    control "Welcome Intern."
    control "Let's see how well you go."

    return

