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
    $ multiplier = 1 # This is used to multiply the '$time' value. This multiplier is increased when you drink

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
                $time += (10 * multiplier)
                call work_topic

            "Talk about life.":
                "You talk about life."
                $time += (10 * multiplier)
                $points += 10
                call life_topic

            "Talk about the cat judging you from the sofa.":
                "The cat eyes you suspiciously."
                $time += (10 * multiplier)
                $fatigue += 5

            "Drink":
                "You take a swig of your drink."
                $multiplier += 1
                $time += (10 * multiplier)
                $fatigue += 5

        "You have [fatigue] points of fatigue."

    # This ends the game.

    return

label life_topic:
    $rand_topic = "convo_" + str(renpy.random.choice(['drink', 'pets', 'family', 'weekend', 'home', 'exercise']))
    call expression rand_topic
    return

label work_topic:
    $rand_topic = "convo_" + str(renpy.random.choice(['week', 'cheers', 'competitor', 'quarantine', 'zoom']))
    call expression rand_topic
    return

label convo_drink:

    $added_fatigue = 0
    "What are you drinking?"

    menu:

        "I have some beers left over":
            $time += (10 * multiplier)
            $added_fatigue = 10

        " I found some old wine.":
            "Oh, what kind of wine?"
            menu:
                "A white":
                    $time += (10 * multiplier)
                    $added_fatigue = 10

                "A red":
                    $time += (10 * multiplier)
                    $added_fatigue = 10

        "I need to buy more drinks soon":
            $time += (10 * multiplier)
            $added_fatigue = 10

        "<say nothing>":
            call end_conversation
    "Gained +[added_fatigue] points of fatigue."
    $fatigue += added_fatigue
    return

label convo_family:
    $added_fatigue = 0
    "How's your family?"

    menu:
        "They're doing well":
            $time += (10 * multiplier)
            $added_fatigue = 10

        "I haven't talked to them":
            $time += (10 * multiplier)
            $added_fatigue = 10

        "What family?":
            $added_fatigue = 10
            call end_conversation

        "<say nothing>":
            $added_fatigue = 10
            call end_conversation

    "Gained +[added_fatigue] points of fatigue."
    $fatigue += added_fatigue
    return

label convo_pets:
    $added_fatigue = 0
    "Can I see your pet?"

    menu:
        "What pet?":
            $time += (10 * multiplier)
            $added_fatigue += 10

        "Sure!":
            $time += (10 * multiplier)
            $added_fatigue += 10
            call happy

        "I am the pet":
            $added_fatigue = 10
            call end_conversation

    "Gained +[added_fatigue] points of fatigue."
    $fatigue += added_fatigue
    return

label convo_week:
    $added_fatigue = 0
    "How was your week?"

    menu:
        "The week went by really quickly":
            $time += (10 * multiplier)
            $added_fatigue += 10

        "Could have been shorter":
            $time += (10 * multiplier)
            $added_fatigue += 10

        "It was okay":
            $time += (10 * multiplier)
            $added_fatigue += 10

        "<say nothing>":
            $added_fatigue = 10
            call end_conversation

    "Gained +[added_fatigue] points of fatigue."
    $fatigue += added_fatigue
    return

label convo_cheers:
    $added_fatigue = 0
    "Cheers!"
    menu:
        "Raise glass and cheer":
            if fatigue > 50:
                "You spill your drink. Your pants are wet"
                $added_fatigue = 30
                $time += 30
            else:
                "You take a large sip"
                $added_fatigue = 20
                $multiplier += 2
        "Do nothing":
            $added_fatigue = 50

    "Gained +[added_fatigue] points of fatigue."
    $fatigue += added_fatigue
    return

label convo_weekend:
    $added_fatigue = 0
    "Any plans for the weekend?"

    menu:
        "Do some exercise":
            $time += (10 * multiplier)
            $added_fatigue = 20
        "Wait in line at Costco":
            $time += (10 * multiplier)
            $added_fatigue = 10
        "<Sarcastic Response>":
            $time += (10 * multiplier)
            $added_fatigue = 5

    "Gained +[added_fatigue] points of fatigue."
    $fatigue += added_fatigue
    return

label convo_competitor:
    $added_fatigue = 0
    "Hah, how do you think Company X is doing?"

    menu:
        "I actually like using their product!":
            $time += 50
            $added_fatigue = 30
        "Let's not bring up work in this...":
            $time += (10 * multiplier)
            $added_fatigue = 10
        "Yeah, they're terrible":
            $time += (10 * multiplier)
            $added_fatigue = 10

    "Gained +[added_fatigue] points of fatigue."
    $fatigue += added_fatigue
    return

label convo_home:
    $added_fatigue = 0
    "How's home?"

    menu:
        "It's a mess":
            $time += (10 * multiplier)
            $added_fatigue = 10
        "It has been claimed by my pet":
            $time += (10 * multiplier)
            $added_fatigue = 10
        "Trying to fend off bandits":
            $time += (10 * multiplier)
            $added_fatigue = 20

    "Gained +[added_fatigue] points of fatigue."
    $fatigue += added_fatigue
    return

label convo_exercise:
    $added_fatigue = 0
    "Did you do any exercise?"

    menu:
        "Yeah, I just paced around my room":
            $time += (10 * multiplier)
            $added_fatigue = 15
        "Went for a short walk":
            $time += (10 * multiplier)
            $added_fatigue = 25
        "Nope!":
            $time += (10 * multiplier)
            $added_fatigue = 5

    "Gained +[added_fatigue] points of fatigue."
    $fatigue += added_fatigue
    return

label convo_quarantine:
    $added_fatigue = 0
    "When do you think this quarantine is over?"

    menu:
        "It will never end":
            $time += (10 * multiplier)
            $added_fatigue = 15
        "<Optimistic response>":
            $time += (10 * multiplier)
            $added_fatigue = 20
        "<Insert actual date>":
            $time += (10 * multiplier)
            $added_fatigue = 25

    "Gained +[added_fatigue] points of fatigue."
    $fatigue += added_fatigue
    return

label convo_zoom:
    $added_fatigue = 0
    "Why aren't you using a Zoom Background"

    menu:
        "I think they're dumb":
            $time += (10 * multiplier)
            $added_fatigue = 10
        "Turn off camera":
            $time += (10 * multiplier)
            $added_fatigue = 1
        "Fine, I'll put one on...":
            $time += (10 * multiplier)
            $added_fatigue = 30

    "Gained +[added_fatigue] points of fatigue."
    $fatigue += added_fatigue
    return

label happy:
    "Awww what a cute <insert animal>"
    return

label end_conversation:
    "Okay..."
    return