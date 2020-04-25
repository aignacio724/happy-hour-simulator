init python:
    # TODO: Display in 12H format?
    def format_time(minutes):
        return '{:02d}:{:02d}'.format(*divmod(minutes, 60))

init:
    $ time = 960 # Time offset from the first meeting in minutes. The first meeting starts at 04:00 PM.
    $ endtime = 1170 # Time offset from the first meeting in minutes. The last meeting ends at 07:30 PM.
    # TODO: Gather points for different meetings.
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
    vbox xalign 0.05 yalign 0.05:
        imagebutton:
            idle "phoneoff.png"
            hover "phoneon.png"
            action ui.callsinnewcontext("time_screen_label")

screen time_screen(displayTime):
    frame:
        has vbox
        text "[displayTime]"
        textbutton "Lock phone" action Return()

label time_screen_label:
    $ displayTime = format_time(time)
    call screen time_screen(displayTime)
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

    # This ends the game.

    return
