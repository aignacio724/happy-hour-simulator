init:
    $ time = 0 # Time offset from the first meeting.
    $ endtime = 100;
    $ points = 0 # You get these for doing some things.
    $ fatigue = 0 # You get these for doing all things.

# TODO: Meeting groups.

# Images of meeting participants and their "animations" if applicable.

# DEBUG
image cats:
    "cat1.jpg"
    pause 1.0
    "cat2.jpg"
    pause 1.0
    "cat3.jpg"
    pause 1.0
    repeat

image cats2:
    "cat1.jpg"
    pause 1.0
    "cat2.jpg"
    pause 1.0
    "cat3.jpg"
    pause 1.0
    repeat

# The phone to check the time with.
screen phone:
    vbox xalign 0.1 yalign 0.1:
        imagebutton:
            idle "phoneoff.png"
            hover "phoneon.png"
            action ui.callsinnewcontext("time_screen_label")

screen time_screen:
    frame:
        has vbox
        text "Time: [time]"
        textbutton "Lock phone" action Return()

label time_screen_label:
    call screen time_screen
    return

label start:

    # TODO: Rename to the background we actually want and remove "images/monitor.png"
    scene monitor
    show screen phone

    # Show meeting participants
    # TODO: Extract out to helper function that populates call with multiple people

    # DEBUG
    show cats at top
    show cats2 # Appears at bottom center without "at"

    while time <= endtime:
        menu:
            "Talk about work.":
                "You talk about work."
                $time += 10
                $fatigue += 10

            "Talk about life.":
                "You talk about life."
                $time += 10
                $fatigue += 10
                $points += 10

            "Talk about the cat judging you from the sofa.":
                "The cat eyes you suspiciously."
                $time += 10
                $fatigue += 5

        "You have [fatigue] points of fatigue."

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
