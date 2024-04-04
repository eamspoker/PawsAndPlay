# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.
label start:
    scene bg room
    jump hidden_objects
    return


label hidden_objects:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    show screen hidden_objects
    show screen inventory_display_toggle
    $ inventory_items.append("bone")
    pause
   


label hidden_objects_check:
    if items_found == total_hidden:
        jump found_all


label found_all:
    "you found everything!"
    return
