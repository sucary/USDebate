# Core game flow

# Character definitions
image bg = "images/raw/bg.jpg"

define p = Character("Moderator", color="#ffffff", callback=set_speaker_moderator)
define h = Character("Kamala Harris", color="#7ebfeb", callback=set_speaker_harris)
define t = Character("Donald Trump", color="#ea8d8d", callback=set_speaker_trump)

default current_topic = ""

# Game entry point
label start:
    scene bg
    call opening
    show screen section_banner
    show screen score_strip
    jump debate_menu

# Main debate menu
label debate_menu:
    $ sections_done = done_economy + done_tariffs + done_abortion + done_immigration + done_jan6 + done_foreign_policy + done_ukraine + done_identity

    if sections_done >= 5:
        jump ending

    menu:
        "The economy" if not done_economy:
            $ current_topic = "The Economy"
            call topic_intro
            call economy
            $ done_economy = True
            $ show_score_strip = True
            $ topics_shown += 1

        "Tariffs & Trade" if not done_tariffs:
            $ current_topic = "Tariffs & Trade"
            call topic_intro
            call tariffs
            $ done_tariffs = True
            $ show_score_strip = True
            $ topics_shown += 1

        "Abortion" if not done_abortion:
            $ current_topic = "Abortion"
            call topic_intro
            call abortion
            $ done_abortion = True
            $ show_score_strip = True
            $ topics_shown += 1

        "Immigration" if not done_immigration:
            $ current_topic = "Immigration"
            call topic_intro
            call immigration
            $ done_immigration = True
            $ show_score_strip = True
            $ topics_shown += 1

        "January 6th & Democracy" if not done_jan6:
            $ current_topic = "January 6th & Democracy"
            call topic_intro
            call january6
            $ done_jan6 = True
            $ show_score_strip = True
            $ topics_shown += 1

        "Israel & Gaza" if not done_foreign_policy:
            $ current_topic = "Israel & Gaza"
            call topic_intro
            call israel
            $ done_foreign_policy = True
            $ show_score_strip = True
            $ topics_shown += 1

        "Ukraine" if not done_ukraine:
            $ current_topic = "Ukraine"
            call topic_intro
            call ukraine
            $ done_ukraine = True
            $ show_score_strip = True
            $ topics_shown += 1

        "Race & Identity" if not done_identity:
            $ current_topic = "Race & Identity"
            call topic_intro
            call race
            $ done_identity = True
            $ show_score_strip = True
            $ topics_shown += 1

    jump debate_menu

label topic_intro:
    $ show_score_strip = False
    $ harris_support_prev = max(1, min(99, 50 + harris_score - trump_score))
    $ trump_support_prev = 100 - harris_support_prev
    $ current_section_name = current_topic
    $ current_section_num = sections_done + 1
    $ current_question_num = 0
    if sections_done == 0:
        p "Let's start with [current_topic]."
    else:
        $ transitions = [
            "Thank you. Let's move on to {}.",
            "We need to move on. Let's turn to {}.",
            "I want to shift gears now to {}.",
            "Let's turn to another issue that voters care about: {}.",
            "Time is limited. Let's discuss {}.",
            "Our next topic is {}."
        ]
        $ transition = renpy.random.choice(transitions).format(current_topic)
        p "[transition]"
    return

# Ending sequence
label ending:
    $ show_score_strip = False
    $ current_section_name = "Closing Statements"
    $ current_section_num = 0
    $ current_question_num = 0

    call ending_sequence

    menu:
        "Announce the winner":
            pass

    # Calculate final support percentages
    $ harris_percent = max(1, min(99, 50 + harris_score - trump_score))
    $ trump_percent = 100 - harris_percent

    call winner_announcement

    # Hide UI
    $ current_section_name = ""
    $ show_score_strip = False
    hide screen section_banner
    hide screen score_strip

    return
