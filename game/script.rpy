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
image actions_consequences = "images/Iteration_1/placeholder/actions_consequences_screen.png"
image tutorial_1 = "images/Iteration_1/placeholder/tutorial_1.png"
image tutorial_2 = "images/Iteration_1/placeholder/tutorial_2.png"
image wrong_answer1 = "images/Iteration_1/placeholder/wrong_answer_1.png"
image wrong_answer2 = "images/Iteration_1/placeholder/wrong_answer_2.png"
image the_doubt1 = "images/Iteration_1/placeholder/the_doubt_1.png"
image plain_homepage = "images/Iteration_1/placeholder/plain_desktop_screen.png"
image organisation_icon = "images/Iteration_1/organisation_icon.png"

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
    control "The name's Mike but while we're on the job, I'm Control. I'm here to look after you for the time being so don't disappoint us. No pressure." 

    player "Uh, sure, sir. Thanks for having me."
    
    jump scene_three

#SCENE 3
label scene_three:
    scene black 

    scene actions_consequences at fit_screen with fade
    pause 2.0

    

#SCENE 4
label scene_four:
    scene tutorial_1 at fit_screen with fade

    show control_icon at chat_panel_position with dissolve
    control "Alright, let's get this onboarding out of the way."
    control "You'll be scouring through posts, articles, and any form of media within our organisation's website."
    
    scene tutorial_2 at fit_screen
    control "Using that noggin of yours, you gotta piece together which media is true and which ones aren't."
    control "Most of them are real obvious. Stamping one with a circle means it's misinformation. You found the fake news and it gets removed from the public."
    control "Stamping them with an X means they're true, so they'll stay in the information systems. The public sees these news so it's imperative you choose the right one."

    scene tutorial_1 at fit_screen
    control "Go ahead and give it a try."

    menu:
        "Article 1":
            jump wrong_answer_1
        "Article 2":
            jump right_answer
        "Article 3":
            jump wrong_answer_2

#SCENE 4 but just with tutorial
label tutorial_scene:
    scene tutorial_1 at fit_screen with fade

    menu:
        "Article 1":
            jump wrong_answer_1
        "Article 2":
            jump right_answer
        "Article 3":
            jump wrong_answer_2

#Wrong Answer 1 SCENE
label wrong_answer_1:

    scene wrong_answer1 at fit_screen with fade
    pause 1.5

    show control_icon at chat_panel_position with dissolve
    control "This isn't supposed to be that difficult, intern. Try it again."

    jump tutorial_scene

#Wrong Answer 2 SCENE
label wrong_answer_2:

    scene wrong_answer2 at fit_screen with fade
    show control_icon at chat_panel_position with dissolve
    control "Are you doing this on purpose? Don't. Try it again."

    jump tutorial_scene

#Right Answer SCENE
label right_answer:

    scene tutorial_2 at fit_screen with fade

    show control_icon at chat_panel_position with dissolve
    control "Nicely done. Keep that up and we'll be keeping our society well informed."


#SCENE 5 Time Passes
label scene_five:
    scene black

    #narration
    "It's been a few days on the job."
    "You believe you've been doing well. You still believe you're making a difference."
    jump scene_six
#SCENE 6
label scene_six:
    scene the_doubt1 at fit_screen with fade

    show player_icon at player_icon_position 
    player "Huh, this post..."
    player "The stuff they're missing sounds like the things I've approved for removal in the information systems."
    player "I guess there's gotta be backlash everywhere, but was it really integral to that university?"

    pause 1.5

    player "If it's on here, I still got a job to do..."

    call screen article_choice #Made in screens.rpy 

#SCENE 7
label scene_seven:
    scene plain_homepage at fit_screen

    show control_icon at chat_panel_position with dissolve
    control "You've been doing pretty well, intern."
    
    show player_icon at player_icon_position 
    player "You know my name is [player_name], right? How long have I been here--"

    control "And my name's Mike but I'm Control here; it's more convenient to remember what position you are than names anyway."
    control "But I'm not here to dawdle, intern, I got good news."
    
    scene organisation_icon at fit_screen with fade

    control "The upstairs have granted you access to our Archives."

    pause 2.0

    scene scene plain_homepage at fit_screen with fade
    control "Enjoy the priviledge, we got high hopes for you." 

    player "Oh, wow, thanks. I really appreciate--"

    hide control_icon with dissolve

    player "And he's gone. Alright, let's get to it then."

    return

        
