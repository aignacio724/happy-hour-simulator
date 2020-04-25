# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# This is where the different conversation groups would go.

# define e = Character("Eileen")

# The game starts here.

image cats:
    "cat1.jpg"
    pause 1.0
    "cat2.jpg"
    pause 1.0
    "cat3.jpg"
    pause 1.0
    repeat

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene monitor

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # This is where the different monitor backgrounds would go.

    # show eileen happy

    # These display lines of dialogue.

    show cats at top

    "Test."

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
