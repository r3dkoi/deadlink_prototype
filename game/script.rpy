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
image bg main_homescreen = "images/low_fidelity/main_homescreen.jpg"
image bg main_menu_screen = "images/low_fidelity/main_menu_screen.png"
image bg background_alley = "images/low_fidelity/background_alley.jpg"
image bg end_shift_screen = "images/low_fidelity/end_shift_screen.jpg"
image bg destroy_keep_evidence = "images/low_fidelity/destroy_keep_evidence.jpg"
image bg coworkers_icons = "images/low_fidelity/coworkers_icons.jpg"
image control_icon = "images/low_fidelity/control_icon.jpg"

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

#SCENE 1 
define control = Character("CONTROL", color="#00FF00")
label start:

    #Showing desktop background of CLEAR
    scene bg main_homescreen at fit_screen with fade
    
     # Cutscene narration - player just reads/watches
    "The screen flickers to life."
    "This is your first day."
    
    # Pause for atmosphere before CONTROL appears
    pause 1.5

    # Chat panel appears (you'll add the image/overlay later)
    show control_icon at chat_panel_position with dissolve

    control "Welcome Intern."
    control "Let's see how well you go."

    return

