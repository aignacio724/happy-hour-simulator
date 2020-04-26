init python:
    # TODO: Display in 12H format.
    def format_time(minutes):
        return '{:02d}:{:02d}'.format(*divmod(int(minutes), 60))

init:
    $ time = 960 # Time offset from the first meeting in minutes. The first meeting starts at 04:00 PM.
    $ endtime = 1170 # Time offset from the first meeting in minutes. The last meeting ends at 07:30 PM.
    $ drunkMultiplier = 1.00 # This increases every time you drink. Affects time spent taking actions.

    # TODO: Gather points for different meetings.
    $ points = 0 # You get these for doing some things.

    $ baseTime = 10 # A base time value for all actions.

    $ fatigue = 0 # You get these for doing all things.
    $ baseFatigue = 5 # A base fatigue value for all actions.

    $ intro = True
    $ shib_mode = False

define player = Character("[name]", color="#FF0000")

# TODO: Meeting groups.

# Images of meeting participants and their "animations" if applicable.

image userA:
    "userA1.png"
    pause 5.0
    "userA2.png"
    pause 0.1
    "userA1.png"
    pause 3.0
    "userA2.png"
    pause 0.1
    repeat

image userB:
    "userB1.png"
    pause 4.0
    "userB2.png"
    pause 0.1
    "userB1.png"
    pause 6.5
    "userB2.png"
    pause 0.1
    repeat

image userC:
    "userC1.png"
    pause 0.1
    "userC2.png"
    pause 5.0
    "userC1.png"
    pause 2.0
    "userC2.png"
    pause 7.0
    repeat

image shiba:
    "shiba1.png"
    pause 5.0
    "shiba2.png"
    pause 0.3
    repeat

image skelly:
    "skelly1.png"
    pause 1.0
    "skelly2.png"
    pause 4.5
    "skelly1.png"
    pause 2.5
    "skelly2.png"
    pause 2.5
    repeat

image shiba1:
    "shiba1.png"
    pause 5.0
    "shiba2.png"
    pause 0.3
    repeat

image shiba2:
    "shiba1.png"
    pause 2.5
    "shiba2.png"
    pause 0.3
    "shiba1.png"
    pause 2.0
    "shiba2.png"
    pause 0.2
    repeat

image shiba3:
    "shiba1.png"
    pause 0.1
    "shiba2.png"
    pause 0.1
    repeat

image shiba4:
    "shiba1.png"
    pause 0.2
    "shiba2.png"
    pause 5.0
    repeat

image shiba5:
    "shiba1.png"
    pause 1.2
    "shiba2.png"
    pause 0.1
    "shiba1.png"
    pause 0.6
    "shiba2.png"
    pause 0.1
    "shiba1.png"
    pause 0.3
    "shiba2.png"
    pause 0.1
    repeat

image shiba6:
    "shiba1.png"
    pause 4.0
    "shiba2.png"
    pause 0.1
    repeat

# DEBUG: Used to see all variables at any point in the game.
screen debug:
    frame:
        xalign 1.0
        has vbox
        $ displayTime = format_time(time)
        text "Time: [time]"
        text "Display Time: [displayTime]"
        text "Points: [points]"
        text "Fatigue: [fatigue]"
        text "Drunk Multiplier: [drunkMultiplier]x"

# A convenient way to take actions.
label step_time(timeModifier = 0, fatigueModifier = 0):
    $ time += int((baseTime + timeModifier) * drunkMultiplier)
    $ fatigue += (baseFatigue + fatigueModifier)
    # Make sure fatigue can't go negative.
    if fatigue < 0:
        $fatigue = 0
    return

# label add_points(points, group):

# Give the player feedback based on how much fatigue they have.
# TODO: Only give each message once.
label fatigue_feedback:
    if fatigue < 20:
        pass
    elif fatigue < 30:
        "You're starting to feel a little tired."
    elif fatigue < 50:
        "You feel a little tired."
    elif fatigue < 70:
        "You're getting there."
    elif fatigue < 90:
        "You're about to pass out."
    elif fatigue < 100:
        "You really should call it a night."
    else:
        "You fool."

label populate_meeting:
    $ leftColumnX = 0.16
    $ centerColumnX = 0.50
    $ rightColumnX = 0.8425

    $ topRowY = 0.02
    $ centerRowY = 0.42

    # Row 1
    show userA:
        xalign leftColumnX
        yalign topRowY
    show userB:
        xalign centerColumnX
        yalign topRowY
    show shiba1:
        xalign rightColumnX
        yalign topRowY

    # Row 2
    show shiba3:
        xalign leftColumnX
        yalign centerRowY
    show userC:
        xalign centerColumnX
        yalign centerRowY
    show skelly:
        xalign rightColumnX
        yalign centerRowY
    return

label start:
    # TODO: Remove this and the function being called
    show screen debug

    # TODO: Rename to the background we actually want and remove "images/monitor.png"
    scene monitor
    if shib_mode:
        call populate_shiba
    else:
        call populate_meeting

    label intro:
        if intro:
            $ name = renpy.input("What's your name?")
            $ name = name.strip()
            "Hello! [name]!"
            "Calling into the first meeting. Make sure your webcam is in its fully upright position."
            $ intro = False # TODO: Figure out why this flag is necessary to keep this thing from appearing again and again.

    label begin:
        # TODO: Start the different meetings here.
        "People are talking..."

        menu:
            "Talk about work.":
                call work_topic

            "Talk about life.":
                call life_topic

            "Drink":
                "You do that"
                $ drunkMultiplier += 0.1
                call step_time(5)

        label after_menu:
            call fatigue_feedback

    if time <= endtime:
        jump begin
    else:
        return # Ends the game.
    return

label life_topic:
    $ rand_topic = "convo_" + str(renpy.random.choice(['drink', 'pets', 'family', 'weekend', 'home', 'exercise']))
    call expression rand_topic
    return

label work_topic:
    $ rand_topic = "convo_" + str(renpy.random.choice(['week', 'cheers', 'competitor', 'quarantine', 'zoom']))
    call expression rand_topic
    return

label convo_drink:

    "Hey [player], what are you drinking?"

    menu:
        "I have some beers left over":
            call step_time()

        "I found some old wine.":
            "Oh, what kind of wine?"
            menu:
                "A white":
                    call step_time()

                "A red":
                    call step_time()

        "I need to buy more drinks soon":
            call step_time()

        "<say nothing>":
            call end_conversation
    return

label convo_family:
    "Hey [player], how's your family?"

    menu:
        "They're doing well":
            call step_time()

        "I haven't talked to them":
            call step_time()

        "What family?":
            call end_conversation

        "<say nothing>":
            call end_conversation
    return

label convo_pets:
    "Hey [player], can I see your pet?"

    menu:
        "What pet?":
            call step_time()

        "Sure!":
            call step_time()
            call happy

        "I am the pet":
            call end_conversation
    return

label convo_week:
    "Hey [player], how was your week?"

    menu:
        "The week went by really quickly":
            call step_time()

        "Could have been shorter":
            call step_time()

        "It was okay":
            call step_time()

        "<say nothing>":
            call end_conversation
    return

label convo_cheers:
    "Cheers [player]!"
    menu:
        "Raise glass and cheer":
            if fatigue > 50:
                # TODO: Reset fatigue here?
                "You spill your drink. Your pants are wet"
                call step_time(5, 10)
            else:
                "You take a large sip"
                $drunkMultiplier += 0.5
                call step_time(2, 10)
        "Do nothing":
            call step_time()
    return

label convo_weekend:
    "Hey [player], any plans for the weekend?"

    menu:
        "Do some exercise":
            call step_time()

        "Wait in line at Costco":
            call step_time()
        "<Sarcastic Response>":
            call step_time()
    return

label convo_competitor:
    "Hah, hey [player] how do you think Company X is doing?"

    menu:
        "I actually like using their product!":
            call step_time()

        "Let's not bring up work in this...":
            call step_time()

        "Yeah, they're terrible":
            call step_time()
    return

label convo_home:
    "[player], how's home?"

    menu:
        "It's a mess":
            call step_time()

        "It has been claimed by my pet":
            call step_time()

        "Trying to fend off bandits":
            call step_time(fatigueModifier=10)
    return

label convo_exercise:
    "Did you do any exercise [player]?"

    menu:
        "Yeah, I just paced around my room":
            call step_time(fatigueModifier=5)

        "Went for a short walk":
            call step_time(fatigueModifier=15)

        "Nope!":
            call step_time(fatigueModifier=5)
    return

label convo_quarantine:
    "When do you think this quarantine is over [player]?"

    menu:
        "It will never end":
            call step_time(fatigueModifier=5)

        "<Optimistic response>":
            call step_time(fatigueModifier=10)

        "<Insert actual date>":
            call step_time(fatigueModifier=15)
    return

label convo_zoom:
    "[player]! Why aren't you using a Zoom Background!?"

    menu:
        "I think they're dumb":
            call step_time()

        "<Turn off camera>":
            call step_time(fatigueModifier=-1)

        "Fine, I'll put one on...":
            call step_time(fatigueModifier=20)
    return

label happy:
    "Awww what a cute <insert animal>"
    return

label end_conversation:
    "Okay..."
    call step_time()
    return

# This lets you easily add the Konami code to your Ren'Py game. When
# the Konami code (up up down down left right left right a b) has been
# entered, this calls the konami_code label (in a new context, so that
# the current game state isn't lost.

init python hide:

    class KonamiListener(renpy.Displayable):

        def __init__(self, target):

            renpy.Displayable.__init__(self)

            import pygame

            # The label we jump to when the code is entered.
            self.target = target

            # This is the index (in self.code) of the key we're
            # expecting.
            self.state = 0

            # The code itself.
            self.code = [
                pygame.K_UP,
                pygame.K_UP,
                pygame.K_DOWN,
                pygame.K_DOWN,
                pygame.K_LEFT,
                pygame.K_RIGHT,
                pygame.K_LEFT,
                pygame.K_RIGHT,
                pygame.K_b,
                pygame.K_a,
                ]

        # This function listens for events.
        def event(self, ev, x, y, st):
            import pygame

            # We only care about keydown events.
            if ev.type != pygame.KEYDOWN:
                return

            # If it's not the key we want, go back to the start of the statem
            # machine.
            if ev.key != self.code[self.state]:
                self.state = 0
                return

            # Otherwise, go to the next state.
            self.state += 1

            # If we are at the end of the code, then call the target label in
            # the new context. (After we reset the state machine.)
            if self.state == len(self.code):
                self.state = 0
                renpy.call_in_new_context(self.target)

            return

        # Return a small empty render, so we get events.
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)


    # Create a KonamiListener to actually listen for the code.
    store.konami_listener = KonamiListener('konami_code')

    # This adds konami_listener to each interaction.
    def konami_overlay():
        ui.add(store.konami_listener)

    config.overlay_functions.append(konami_overlay)


# This is called in a new context when the konami code is entered.
label konami_code:
    "BORK BORK BORK"
    scene monitor

    call populate_shiba
    "MUCH SURPRISE. MUCH SHIBA. WOW"
    while True:
        menu:
            "Pet":
                "You pet the Shibas"
                "Bork Bork!"
            "Smush face":
                "You smuch the doggo's face"
                "Borf Borf"
            "Give treat":
                "Much treat! Much Bork!"
            "Much tired":
                "You leave to nap"
                "*Whine* bork..?"
                return
        "BORK"
    return

label populate_shiba:
    $ leftColumnX = 0.16
    $ centerColumnX = 0.50
    $ rightColumnX = 0.8425

    $ topRowY = 0.02
    $ centerRowY = 0.42

    # Row 1
    show shiba2:
        xalign leftColumnX
        yalign topRowY
    show shiba5:
        xalign centerColumnX
        yalign topRowY
    show shiba1:
        xalign rightColumnX
        yalign topRowY

    # Row 2
    show shiba3:
        xalign leftColumnX
        yalign centerRowY
    show shiba6:
        xalign centerColumnX
        yalign centerRowY
    show shiba4:
        xalign rightColumnX
        yalign centerRowY
    return