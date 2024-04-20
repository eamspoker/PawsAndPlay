# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Vet")
define name = ""

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
        xalign 0.5 yalign 0.1
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


define e = Character("New Anchor")
define man = Character("Official")
define player = Character([persistent.mcName])
define check = False
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
# The game starts here.
label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg studio
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
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
    e "BREAKING NEWS! Did you hear the latest update on planet earth?"
    e "All planets on Earth have gone to mars! This is a catastrophe"
    hide woman
    scene bg desert1
    
    e "We have here some pictures of this planet with no animals in it!"
    scene bg desert2
    e "Not one animal - not even a single one! "
    scene bg desert3
    e "This is very very astonishing!"
    scene bg studio
    show woman shocked at tophalf
    e "Who will save us now?!"
    hide woman
    show bg task
    man "Hello! I am the Director Of Pets. You must have seen the news"
    man "We need your help in bringing back the animals. We are choosing you to do this because we have heard of your great negotiation skills and your skills with animals!"
    man "Hope you don't disappoint us!"
    menu choices: #menus can have labels
        "What will you do?"
        "Yes":
            $ choice1 = True
            # jump somewhere_else_maybe
            man "Good. We will be giving you certain things to help you on your journey! Good luck!"
            # jump choices 
        "Hell yes!":
            $ choice2 = True
            # jump somewhere_else_maybe
            man "Good. We will be giving you certain things to help you on your journey! Good luck!"
            # jump choices
    scene bg studio
    show woman shocked at tophalf
    e "BREAKING NEWS!"
    e "We have a new update on the no pet situation!"
    e "Someone has volunteered to go negotiate with all the pets!"
    e "Let's go interview that person before they vanish off to mars."
    menu gender: #menus can have labels
        "What gender would your character be?"
        "Female":
            $ female = True
            # jump somewhere_else_maybe
            # man "Good. We will be giving you certain things to help you on your journey! Good luck!"
            # jump choices 
        "Male":
            $ female = False
            # jump somewhere_else_maybe
            # man "Good. We will be giving you certain things to help you on your journey! Good luck!"
            # jump choices
    if female:
        scene bg studio
        show woman interviewing at interviewHalfAnchor
        show player female interviewing at playerHalfFemaleInterview
        e "Our player is an amazing girl!"
        e "Let's find out who is our saviour?"
        $ name += renpy.input("Name your character!", "BadMustard").strip() or "BadMUstard"
        e "Welcome, [name] to the news set."
        e "I am pretty sure you must be nervous about this task. Can we know more about your background? We would love to -"
        # else:
        #     e "[persistent.mcName], you came back"
        #     e "if you love something set it free, if it come back KILL IT BEFORE IT GETS AWAY AGAIN..."
    else:
        scene bg studio
        show woman interviewing at interviewHalfAnchor
        show player male interviewing at playerHalfMaleInterview
        e "Our player is an amazing guy!"
       
        $ name = renpy.input("Name your character!", "BadMustard").strip() or "BadMUstard"
        e "Welcome, [name] to the news set."
        e "I am pretty sure you must be nervous about this task. Can we know more about your background? We would love to -"
    
    hide woman shocked
    hide player female 
    show bg task
    man "Enough with the interviews and what not. We don't have time. The world is collapsing without the animals. The ecosystem is going to hell! We shall all perish if [name] does not succeed in her task. Stop holding her back and let her go."
    man "[name], your first mission is to bring back this one dog named Scotty."
    man "Start off by investigating Scotty's old house on Earth, then we will send you to Mars to convince him."
    man "Off you go! Our top veterarian will answer any of your questions before you start your investigation."
    hide bg task
    jump aarthi_start

# Start of the game
label aarthi_start:
    scene background
    show dog at right
    show screen trust_meter_screen
    # Main game loop
    label game_loop:
        if not bone_found:
            menu:
                "Do you want to look for the bone?"
                "Yes":
                    $ bone_found = True
                    "You found a bone!"
                    show screen bone_draggable 
                    menu:
                            "Give the bone to the dog?"
                            "Yes":
                                hide bone
                                $ trust_level += 20  # Increase trust level by 20%
                                "You give the bone to the dog, and it looks less scared."
                            "No":
                                "You decide to keep the bone."
                "No":
                    "You decide not to look for the bone right now."
        else:
            "There's nothing else to do here for now."
            # Placeholder for additional game content or ending the game loop
            jump emily_start

define y = Character(name)
# The game starts here.
label emily_start:
    call clinic
    jump hidden_objects
    return

    

label clinic:
    scene vetclinic
    v "Hi, how may I help you today?"
    player "I was chosen to bring back the pets from Mars to Earth."
    player "But before they come, they wanted me to interview a vet expert to learn more about how pets SHOULD be taken care of."
    v "Oooh, we thought you looked famillar -- we remember seeing you on the news!"
    v "We would love to help, what questions do you have?"
    menu questions:
        "How much money does it cost to raise an animal and what are the main expenses that pets require?":
            v "For dogs specifically, anywhere between $1,200-$2,700 per year - this depends on the breed/size, age, and temperament of the dog."
            v "It can go up to $5,000 a year if there's medical conditions or other factors!"
            jump questionsContinue
        "How much time and attention does a young pet need?":
            v "A LOT! Its so important to properly train and socialize a young puppy."
            v "By this we mean not just exposing them to new experiences but putting in the time to make sure those experiences are positive!"
            jump questionsContinue
        "How can we make sure that we are providing the best environment for our pet?":
            v "Pet communication!  Our pets can't talk to us, but they are constantly using their body language to communicate their emotions to us. I think all pet owners can benefit from learning animal body language and really taking the time to understand what their pet is saying to them, and then listening to them!"
            v "When pets are communicating that they're uncomfortable, afraid, or otherwise having big emotions, knowing what they're saying and taking steps to help them feel better. will benefit everyone in the long run."
            v "These steps can include removing from the uncomfortable situation, advocating for their needs, and even working with a trainer to improve their associations with a negative trigger."
            jump questionsContinue
        "What are some responsibilities regarding pet care that may not be  obvious but are still important?":
            v "Food and clean water at regular times during the day
            \nConsistent grooming
            \nDaily walks to socialize and get out energy
            \nA structured schedule in terms of day to day life"
            v "Dental care as even dogs need their teeth clean
            \nSocialization with other dog and human friends
            \nPlay time with enrichment to prevent boredom and ensure our pets get mental stimulation
            \nAnnual vet checkups to maintain our pet's well being"
            jump questionsContinue


    menu questionsContinue:
        v "Would you like to ask another question?"
        "No":
            jump questions
        "Yes":
            player "Thank you so much for all your incredibly helpful information!"
            player "I learned a lot and now know what items to look for in Scotty's home environment to figure out why he left!"
    return




label hidden_objects:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg bedroom
    show screen hidden_objects
    show screen inventory_display_toggle
    show screen checkbox
    pause

    


label hidden_objects_check:
    if items_found == total_hidden:
        jump found_all
    else:
        jump hidden_objects



define s = Character("Scotty")
label found_all:
    player "Okay, I'm all done!"
    player "Let's head back to Mars!"
    $ temp_items = inventory_items
    jump scotty_talk_start


label scotty_talk_start:
    scene mars scenery
    show screen inventory_display_toggle
    hide screen checkbox
    show dog
    $ print(inventory_items)
    s "Tell me, what have you learned back on Earth?"
    $ isPresenting = True

label scotty_talk_loop:
    pause

label scotty_talk_check:
    if strikes > 1:
        jump scotty_fail

    if presented == 0:
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
    s "Tell me, what is this [name] evidence of?"
    $ presented += 1
    $ hasPresented[key] = True
    menu:
        "Humanity treating pets well!":
            if not isGood:
                jump scotty_strike
        "Something that humans need to do better!":
            if isGood:
                jump scotty_strike
    
    s "Hmmm... why do you think this is evidence of that?"
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

    s "I guess that makes sense?"    
    
    jump scotty_talk_check



label scotty_strike:
    s ".... I don't think that makes any sense."
    "[[Scotty was unconvinced by your explanation]"
    $ strikes += 1
    jump scotty_talk_check

label scotty_fail:
    s "I don't think you really understand why I left."
    $ isPresenting = False
    $ strikes = 0
    $ presented = 0
    python:
        for k in list(hasPresented.keys()):
            hasPresented[k] = False
    menu:
        "I do understand! I'll explain it right, let me try again!":
            jump scotty_talk_loop
        "You're right... I think I should talk to an expert about this":
            call clinic
            jump scotty_talk_start
    
        
label end:
    s "I'm so happy you figured it out -- if you promise that these issues will never happen again, all the dogs will come back to Earth!"
    player "I promise!"
    "Breaking News: All dogs have returned to Earth!"
    "... now what about the cats?"
    jump start