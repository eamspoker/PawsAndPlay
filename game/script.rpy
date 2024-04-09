# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Vet")
define y = Character("You")

# function for adding an item
label addItem(item):
    $ inventory_items.append(item)

# The game starts here.
label start:
    scene vetclinic
    v "Hi, how may I help you today?"
    y "I was chosen to bring back the pets from Mars to Earth."
    y "But before they come, they wanted me to interview a vet expert to learn more about how pets SHOULD be taken care of."
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
        v "I know I just gave you a lot of information -- did you get all that?"
        "No":
            jump questions
        "Yes":
            y "Thank you so much for all your incredibly helpful information!"
            y "I learned a lot and now know what items to look for in Scotty's home environment to figure out why he left!"
    jump hidden_objects



label decide(item):
    $ findItem(item)
    y "Hmmmm... does this seem like it fulfills Scotty's needs?"
    menu:
        "Yes!":
            if isItemGood(item):
                $ colorItem(True, item)
                jump hidden_objects_check
                return
        "No...":
            if not isItemGood(item):
                $ colorItem(False, item)
                jump hidden_objects_check
                return
    y "That doesn't seem right... let me try again"
    call decide(item)

   


label hidden_objects:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg room
    show screen hidden_objects
    show screen inventory_display_toggle
    show screen checkbox
    pause
    return
    


label hidden_objects_check:
    if items_found == total_hidden:
        jump found_all
    else:
        jump hidden_objects
    

define s = Character("Scotty")
label found_all:
    y "Okay, I'm all done!"
    y "I believe that Scotty left because of his food bowl and dirty water bowl did not fulfill his needs."
    jump scotty_end

label scotty_end:
    s "I've been watching you through our Mars telescope and I'm so happy you figured it out!"
    s "If you promise that these issues will never happen again, all the dogs will come back to Earth!"
    y "I promise!"
    jump end
    

label end:
    "Breaking News: All dogs have returned to Earth!"
    "... now what about the cats?"
    return