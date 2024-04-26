# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Vet")
define player = Character("You")


# Define images
image background = "bg_planet.jpg"
image dog = "dog.png"
image bone = "bone.png"
# Initialize variables
default bone_found = False
default trust_level = 0  # Trust level as a percentage
default trust_level_max = 100  # Maximum trust level
# define bone_draggable = Draggable(
#     drag_name="bone",
#     child=Image("bone.png"),
#     draggable=True,
#     xanchor=0.5, yanchor=0.5,
#     xpos=0.5, ypos=0.5
# )
screen trust_meter_screen:
    frame:
        xalign 0.95 yalign 0.1
        vbox:
            text "Trust Meter" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 300
                    value VariableValue("trust_level", trust_level_max)
                    range trust_level_max
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                null width 5
                text "[trust_level] / [trust_level_max]" size 16
screen bone_draggable:
        drag:
            drag_name "bone"
            child "bone.png"
            xpos 0.25
            ypos 0.25
            draggable True



# function for adding an item
label addItem(item):
    $ inventory_items.append(item)

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define name = ""
define e = Character("New Anchor")
define man = Character("Official")
define player = Character("You")
define check = False
define levelCheck =  False
define mapClickCheck = False
# image portal movie = Movie(play="images/bg/portal_movie.webm")
image portal_movie = Movie(channel="movie_dp", play = "movies/portal_movie.webm", loop = False,keep_last_frame = True)
image portal_mars = Movie(channel="movie_dp", play="movies/portal_mars.webm", loop = False,keep_last_frame = True)
image portal_combined = Movie(channel="movie_dp", play="movies/portal_combined.webm", loop=False,keep_last_frame = True)

screen backpack:
    # zoom 0.7
    # window:
    #     background "black"
    #     xsize 200
    #     ysize 200
    imagebutton:
        idle "backpack glowing" at backpackPosition
        action [SetVariable("check", True), Jump("selectBackpackCheck")],
        xalign 0.7 yalign 0.045
        focus_mask True

screen map:
    imagebutton:
        idle "map click" at mapClick
        action [SetVariable("mapClickCheck", True), Jump("selectMapClickCheck")],
        xalign 0.7 yalign 0.045
        focus_mask True

screen level:
    imagebutton:
        idle "map level" at mapLevel
        action [SetVariable("levelCheck", True), Jump("selectLevelCheck")],
        xalign 0.7 yalign 0.045
        focus_mask True

# The game starts here.

label start:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg studio
    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    transform mapClick:
        xalign 0.535
        yalign 0.664
    transform mapLevel:
        xalign 0.07 yalign 0.6

    transform tophalf:
        xalign 0.5 yalign -0.07
        zoom 0.90
    
    transform interviewHalfAnchor:
        xalign 0.3 yalign -0.16
        zoom 0.90

    transform playerHalfFemaleInterview:
        xalign 0.7 yalign 0.035
        zoom  0.3

    transform playerHalfMaleInterview:
        xalign 0.7 yalign 0.045
        zoom 0.3
        xzoom -1.0

    transform backpackPosition:
        xalign 0.7 yalign 0.045
        zoom 0.7

    # transform backgroudSize:
    #     zoom 1.2

    show woman shocked at tophalf
    # show eileen happy

    # These display lines of dialogue.

    e "BREAKING NEWS! Did you hear the latest update on planet Earth?"

    e "All pets on Earth have gone to Mars! This is a catastrophe!"
    hide woman
    scene bg desert1
    

    e "We have here some pictures of this planet with no pets in it!"
    scene bg desert2
    e "Not one pet - not even a single one! "
    scene bg desert3
    e "This is very very astonishing!"

    scene bg studio
    show woman shocked at tophalf
    e "Who will save us now?!"

    hide woman
    show bg task

    man "Hello! I am the Director Of Pets. You must've seen the news."
    man "We need your help in bringing back the pets."
    man "We are choosing you to do this because we have heard of your ability to talk to pets and your great negotiation skills!"
    man "Hope you don't disappoint us!"

    # menu choices: #menus can have labels
    #     "What will you do?"
    #     "Yes":
    #         $ choice1 = True
    #         # jump somewhere_else_maybe
    #         man "Good. We will be giving you certain things to help you on your journey! Good luck!"
    #         # jump choices 
    #     "Hell yes!":
    #         $ choice2 = True
    #         # jump somewhere_else_maybe
    #         man "Good. We will be giving you certain things to help you on your journey! Good luck!"
    #         # jump choices

    # scene bg studio
    # show woman shocked at tophalf

    # e "BREAKING NEWS!"
    # e "We have a new update on the no pet situation!"
    # e "Someone has volunteered to go negotiate with all the pets!"
    # e "Let's go interview that person before they vanish off to mars."

    # menu gender: #menus can have labels
    #     "What gender would your character be?"
    #     "Female":
    #         $ female = True
    #         $ pronoun = "her"
    #         # jump somewhere_else_maybe
    #         # man "Good. We will be giving you certain things to help you on your journey! Good luck!"
    #         # jump choices 
    #     "Male":
    #         $ female = False
    #         $ pronoun = "him"
    #         # jump somewhere_else_maybe
    #         # man "Good. We will be giving you certain things to help you on your journey! Good luck!"
    #         # jump choices
    # if female:
    #     scene bg studio
    #     show woman interviewing at interviewHalfAnchor
    #     show player female interviewing at playerHalfFemaleInterview
    #     e "Our player is an amazing girl!"
    #     e "Let's find out who is our saviour?"
    #     $ name = renpy.input("Name your character!", "BadMustard").strip() or "BadMUstard"
    #     e "Welcome, [name] to the news set."
    #     e "I am pretty sure you must be nervous about this task. Can we know more about your background? We would love to -"

    #     # else:
    #     #     e "[persistent.mcName], you came back"
    #     #     e "if you love something set it free, if it come back KILL IT BEFORE IT GETS AWAY AGAIN..."

    # else:
    #     scene bg studio
    #     show woman interviewing at interviewHalfAnchor
    #     show player male interviewing at playerHalfMaleInterview
    #     e "Our player is an amazing guy!"
       
    #     $ name = renpy.input("Name your character!", "BadMustard").strip() or "BadMUstard"
        
    #     e "Welcome, [name] to the news set."
    #     e "I am pretty sure you must be nervous about this task. Can we know more about your background? We would love to -"
    
    # hide woman shocked
    # hide player female 
    # show bg task

    # man "Enough with the interviews and what not. We don't have time. The world is collapsing without the animals. The ecosystem is going to hell! We shall all perish if [name] does not succeed in the task. Stop holding [pronoun] back and let [pronoun] go."
    # man "We are giving you some resources to take with you when you leave for mars. They will come in handy for the starting few situations you might get into. We will always be available through satellite phone should you need any assistance. But remember you have to call for assistance only when it's extremely essential"
    man "If you go in through the room, you will see a backpack with some helpful resources and a map of the areas showing where the pets might be. "
    man "You might be wondering about how you would get to Mars? Don't worry, the map is magic!" 
    man "As soon as you tap on the glowing location, it will take you to where the pet is."
    man "You need to hurry up to get to Mars to bring the pets back. The glowing portal will only exist for a short while. Good luck!"

    # Show the bag 
        # Character saying - let me check the bag
    scene bg room
    show backpack color at backpackPosition
    player "Hmm... The director asked me to come here! Oh right, there's the backpack."
    hide backpack color
    show screen backpack
    jump repeat

label repeat:
    pause

label selectBackpackCheck:
    # Check if the backpack button was clicked before proceeding
    if check:
        jump selectBackpack
    else:
        man "Click on the backpack to access it!"  # Go back to the start label if the backpack button wasn't clicked
        jump repeat

label selectBackpack:
    # Scene of bag contents
        # Bone and map are the necessities

    hide screen backpack 
    scene bg nobone
    player "What do we have here?"
    show screen map
    jump mapClickRepeat
    

label mapClickRepeat:
    pause

label selectMapClickCheck:
    if mapClickCheck:
        jump mapScene
    else:
        man "You need to click on the map to access it!"
        jump mapClickRepeat

label mapScene:
    # Show map here
    show bg map
    hide screen map
    player "I think I have to find Scotty right now since the director mentioned that the map would take me to where I have to go."
    show screen level
   
    # Add screen for the clickable map
    jump repeatMap

label repeatMap:
    pause

label selectLevelCheck:
    # Check if the backpack button was clicked before proceeding
    if levelCheck:
        jump portalToMars
    else:
        man "Click on the level!"  # Go back to the start label if the backpack button wasn't clicked
        jump repeat

label portalToMars:
    show portal_combined
    hide bg map
    hide screen level
    player "Ahhhhh what's happening?"
    jump marsScene

label marsScene:
    scene background
    player "I think I am on Mars."
   

    # $ renpy.movie_cutscene("images/bg/portal_movie.webm")

    
    
    




    

    # Scene of open map
        # Clicking on the first place
    
    # Portal



    # 
    
    # This ends the game.
    jump aarthi_start

# Define images
image background = "bg_planet.jpg"
image dog = im.Scale("scotty.png", 800, 800)
image bone = "bone.png"
image collar = im.Scale("collar.png", 400, 400)
image checklist = im.Scale("checklist.png", 400, 400)
image hearts = "images/hearts.png"
transform upper_position:
    xalign 0.8
    yalign 0.5
define player = Character('You', color="#C8FFC8")
define s = Character('Scotty', color="#FF8080")
label aarthi_start:
    scene background
    show dog at left
    player "Hello there, Doggo! I've come all the way from Earth to bring you back."
    s "Woof! Woof! I'm Scotty."
    player "Hi Scotty. Can you help me understand why all the pets decided to leave Earth?"
    s "Look at dis collar."
    show collar at upper_position with easeinright
    player "There's a name and an address here."
    s "Yep yep, dat's where me hooman lived."
    player "Oh...Should I take you back there?"
    s "Hmm, before me think 'bout goin' back to Earth, me need make sure hoomans learned how to do the good care for us."
    s "You need know more 'bout how me was treated. Peep dis!"
    hide collar
    show checklist at upper_position with easeinright
    s "Go to me hooman's house and keep sniffin' 'round for these things... they might tell you something."
    menu:
            "Deal!":
                s "Woof! Good luck! All of us here are rootin' for ya."
                jump game_progress
            "I need to think about this...":
                s "Woof! Take your time. It's big important for all of us."
                jump reconsider_decision
label game_progress:
    e "Let's start by visiting your Earth home!"
    jump end_game
label reconsider_decision:
    e "I think I can do it."
    jump end_game
label end_game:
    hide dog
    hide checklist
    hide background
    $ renpy.movie_cutscene("images/portal_earth.webm")

   
# The game starts here.
label emily_start:
    call hidden_objects_intro
    scene vetclinic
    v "Hi, how may I help you today?"
    player "I was chosen to bring back the pets from Mars to Earth."
    player "But before they come, they wanted me to learn more about how pets SHOULD be taken care of."
    v "Oooh, we thought you looked famillar -- we remember seeing you on the news!"
    v "We would love to help!"
    call clinic
    player "I think I know how to use the evidence from in Scotty's home to explain why he left!"
    jump scotty_talk_start
    return

    
label clinic:
    hide screen inventory_item_description
    scene vetclinic
    v "What questions do you have?"
    menu questions:
        "What are basic necessities that owners should provide for pets?":
            v "Access to clean food and water bowls -- its pertinent that pet owners take the time to ensure their pets can eat and drink from a safe environment."
            v "You wouldn't want to eat off a dirty dinner plate, right?"
            jump questionsContinue
        "How much money does it cost to raise an animal and what are the main expenses that pets require?":
            v "For dogs specifically, anywhere between $1,200-$2,700 per year!"
            v "This depends on a variety of factors, including dog breed and size."
            v "A lot of this expense is the result of veterinary bills and pet medication."
            jump questionsContinue
        "How much time and attention does a young pet need?":
            v "Puppies require at least 3 hours of engaged interaction a day!" 
            v "Engaged interactions involve socializing your pet by taking them for regular walks (and making sure their leash/harness is in good shape!)"
            v "Or you can give your pets toys and other stimulation objects to keep them busy."
            jump questionsContinue
        "How can we make sure that we are providing the best environment for our pet?":
            v "By listening to your pet's body language and making sure they are in tiptop physical shape."
            v "If your dog has an odor emitting from their ears or matted fur, this can attract parasites like ticks and fleas."
            v "And is a sign that your pet needs more regular grooming sessions."
            jump questionsContinue

    menu questionsContinue:
        v "Would you like to ask another question?"
        "Yes":
            jump questions
        "No":
            player "Thank you so much for all your incredibly helpful information!"
    if lastPlace != "":
        jump expression lastPlace
    else:
        return




label hidden_objects_intro:
    scene bg desert3
    player "I guess this is Scotty's house!"
    player "I still have the checklist of things Scotty wanted me to look at."
    show screen checkbox with easeinright
    show screen checkbox_display with easeinright
    "[[Click on checklist icon to show/hide list.]"
    player "I guess once I go in, I can just put items in my backpack."
    show screen inventory_display_toggle with easeinleft
    player "Let's head in!"

    scene bg bedroom
    "[[Click on objects to add them to your bag.]"
    show screen hidden_objects
    jump hidden_objects

label hidden_objects:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    $ lastPlace = ""
    pause

    


label hidden_objects_check:
    if items_found == total_hidden:
        jump found_all
    else:
        jump hidden_objects



define s = Character("Scotty")
label found_all:
    player "Okay, I've finished investigating the house."
    "[[Click on bag icon to open bag.]"
    hide screen checkbox with easeoutright
    player "I should talk to a veterinary expert to make sense of all of this."
    $ temp_items = inventory_items
    return


label scotty_talk_start:
    scene background
    show screen inventory_item_description
    show dog
    $ lastPlace = ""
    show screen returnToClinic("scotty_talk_start")
    $ trust_level = 30
    show screen trust_meter_screen
    s "What did you find at my hooman's house?"
    $ isPresenting = True

label scotty_talk_loop:
    pause

label scotty_talk_check:
    if trust_level <= 0 or (presented >= total_hidden and trust_level < 70):
        jump scotty_fail

    if presented == 0:
        "[[Click on items in your backpack to present them to Scotty]"
        jump scotty_talk_loop

    if presented < total_hidden:
        s "What else do you have to show me?"
        jump scotty_talk_loop
    else:
        jump end
    


label scotty_talk(key, name, optionDict, isGood):
    if not isPresenting:
        return
    if hasPresented[key]:
        s "You've already told me about this."
        return
    s "What's this [name] evidence of?"
    $ presented += 1
    $ hasPresented[key] = True
    menu:
        "Humans doing something right!":
            if not isGood:
                jump scotty_strike
            if trust_level < 100:
                $ trust_level += 10 
            
        "Humans doing something wrong!":
            if isGood:
                jump scotty_strike
            if trust_level < 100:
                $ trust_level += 10 
    s "Why?"
    $ optionArray = list(optionDict.keys())
    menu:
        "[optionArray[0]]":
            if(not optionDict[optionArray[0]]):
                jump scotty_strike
        "[optionArray[1]]":
            if(not optionDict[optionArray[1]]):
                jump scotty_strike
        "[optionArray[2]]":
            if(not optionDict[optionArray[2]]):
                jump scotty_strike
    if trust_level < 100:
        $ trust_level += 10 
    s "Woof! That's right!" 
    
    
    jump scotty_talk_check



label scotty_strike:
    s ".... that don't smell right. Think again. Dig deeper."
    "[[Scotty was unconvinced by your explanation]"
    $ trust_level -= 10
    jump scotty_talk_check

label scotty_fail:
    s "Typical hooman... I don't think you get why I left."
    $ isPresenting = False
    $ presented = 0
    python:
        for k in list(hasPresented.keys()):
            hasPresented[k] = False
    menu:
        "I do understand! I'll explain it right, let me try again!":
            jump scotty_talk_start
        "You're right... I think I should talk to an expert about this":
            call clinic
            jump scotty_talk_start
    
        
label end:
    s "I'm so happy you figured it out -- if you promise that these issues will never happen again, all the dogs will come back to Earth!"
    player "I promise!"
    call end_end

label end_end:
    hide screen inventory_item_description
    hide screen returnToClinic
    scene bg studio
    show woman shocked at tophalf
    e "Breaking News: One dog has returned to Earth!"
    e "... can we convince the rest?"
    $ MainMenu(confirm=False)()
