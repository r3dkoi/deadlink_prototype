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
image welcome_back_screen = "images/Iteration_1/placeholder/Welcome_back.png"
image control_icon = "images/Iteration_1/control_icon.png"
image player_icon = "images/Iteration_1/player_icon.png"


#Image scaling definitions 
transform fit_screen:
    xalign 0.5
    yalign 0.5
    xsize config.screen_width
    ysize config.screen_height
    fit "cover"

#Icon positions
transform chat_panel_position:
    xalign 0.99        # pushes to the right
    yalign 0.05        # sits near the top
    zoom 0.55           # scales it down to 40% of original size

transform player_icon_position:
    xalign 0.01 #far left 
    yalign 0.72 #near bottom 
    zoom 0.35


#CHARACTER DEFINITIONS
define control = Character("CONTROL", color="#00FF00")
define player = DynamicCharacter("player_name", color="#0f1190")


#Default Character Name
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
            #Pressing ENTER triggers same action as clicking CONFIRM
            action [
                SetVariable("player_name", player_name.strip()),
                Jump("scene_two")
            ]

        #Only shows button once player has typed something
        showif player_name.strip() !="":
            textbutton "CONFIRM?":
                action [
                    SetVariable("player_name", player_name.strip()), #Saves type name into player_name
                    Jump("scene_two")
                ]
                #Hover styling - changes colour when mouse is over it
                text_hover_color "#343568"   # goes green on hover (matches CONTROL colour)
                text_idle_color "#FFFFFF"    # white when not hovered
                text_size 30
                at transform:
                    alpha 0.0
                    linear 0.8 alpha 1.0
#SCENE 1
label start:
    scene black #Sets background just to black for scene 1
    call screen name_input_screen() 


#SCENE 2
label scene_two:

    #Showing desktop background of CLEAR
    scene welcome_back_screen at fit_screen with fade
    #player icon above chatbox
    show player_icon at player_icon_position 

    #Cutscene narration 
    "You are at your desk, preparing for your first day at CLEAR."
    "CLEAR - The Content Legitimacy & Evidence Assessment Registry."
    "Here you believe you can make a difference. That's why you've worked this hard. There's too much fake news around lately."
    "It really takes a toll on people. Including you; what news outlets can you trust nowadays?"
    
    # Pause for atmosphere before CONTROL appears
    pause 1.5

    show control_icon at chat_panel_position with dissolve

    control "Welcome Intern."
    control "The name's Mike, I'm here to look after you for the time being So don't disappoint us. No pressure." 

    player "Uh, sure, sir. Thanks for having me."
    
    Jump("scene_three")

#SCENE 3
label scene_three:
    scene black with fade

    "{color=#00FF00}Make the right choices, because you'll shape what's real in our society.{/color}"