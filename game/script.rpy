# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg = "images/raw/bg.jpg"

define p = Character("Moderator", color="#ffffff", callback=set_speaker_moderator)
define h = Character("Kamala Harris", color="#7ebfeb", callback=set_speaker_harris)
define t = Character("Donald Trump", color="#ea8d8d", callback=set_speaker_trump)

default current_topic = ""

# The game starts here.

label debate_menu:
    # Count how many sections are done
    $ sections_done = done_economy + done_tariffs + done_abortion + done_immigration + done_jan6 + done_foreign_policy + done_ukraine + done_identity

    if sections_done >= 5:
        jump ending

    menu:
        "The economy" if not done_economy:
            $ current_topic = "The Economy"
            call topic_intro
            call economy
            $ done_economy = True

        "Tariffs & Trade" if not done_tariffs:
            $ current_topic = "Tariffs & Trade"
            call topic_intro
            call tariffs
            $ done_tariffs = True

        "Abortion" if not done_abortion:
            $ current_topic = "Abortion"
            call topic_intro
            call abortion
            $ done_abortion = True

        "Immigration" if not done_immigration:
            $ current_topic = "Immigration"
            call topic_intro
            call immigration
            $ done_immigration = True

        "January 6th & Democracy" if not done_jan6:
            $ current_topic = "January 6th & Democracy"
            call topic_intro
            call january6
            $ done_jan6 = True

        "Israel & Gaza" if not done_foreign_policy:
            $ current_topic = "Israel & Gaza"
            call topic_intro
            call israel
            $ done_foreign_policy = True

        "Ukraine" if not done_ukraine:
            $ current_topic = "Ukraine"
            call topic_intro
            call ukraine
            $ done_ukraine = True

        "Race & Identity" if not done_identity:
            $ current_topic = "Race & Identity"
            call topic_intro
            call race
            $ done_identity = True


    jump debate_menu

label topic_intro:
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

label start:

    scene bg

    "10 PM, Sept. 10, 2024. National Constitution Center, Philadelphia."

    p "Good evening! Ladies, gentlemen, and non-binaries."
    p "Tonight, the high-stakes showdown here in Philadelphia between Vice President Kamala Harris and former President Donald Trump."
    p "Their first face-to-face meeting in this presidential election. Their first face-to-face meeting ever."
    p "The candidates separated by the smallest of margins. Essentially tied in the polls nationally."
    p "The rules tonight: 90 minutes, no commercial breaks. No topics or questions have been shared with the campaigns."
    p "Candidates will have two minutes to answer, two minutes for rebuttals, one minute for follow-ups."
    p "Immediately after the debate, the public will be voting on who won."
    p "The winner of the debate will win the election!"
    p "So let's welcome the candidates to the stage."

    $ harris_img = "harris default"
    $ trump_img = "trump default"
    show screen debate_stage

    h "Kamala Harris. Let's have a good debate."
    t "Nice to see you. Have fun."
    h "Thank you."
    t "Thank you."

    p "Welcome to you both. It's an honor to have you here tonight."
    p "Let's begin."

    p "We have many issues to cover tonight."

    show screen section_banner
    jump debate_menu

label ending:
    $ current_section_name = "Closing Statements"
    $ current_section_num = 0
    $ current_question_num = 0

    # Closing statements
    p "The time has come for closing statements."
    p "Vice President Harris, we begin with you."

    $ harris_img = "harris default"
    h "So I think you've heard tonight two very different visions for our country."
    h "One that is focused on the future and the other that is focused on the past."
    h "And an attempt to take us backward. But we're not going back."
    h "I do believe that the American people know we all have so much more in common than what separates us."
    h "And we can chart a new way forward."
    h "A vision that includes having a plan, understanding the aspirations, the dreams, the hopes of the American people."
    h "Which is why I intend to create an opportunity economy."
    h "Investing in small businesses, in new families, in what we can do around protecting seniors."
    h "I believe in what we can do together. Sustaining America's standing in the world."
    h "I will be a president that will protect our fundamental rights and freedoms."
    h "Including the right of a woman to make decisions about her own body."
    h "I started my career as a prosecutor. I was a D.A. I was an attorney general."
    h "A United States senator. And now vice president."
    h "I've only had one client. The people."
    h "And that's the kind of president we need right now."
    h "Someone who cares about you and is not putting themselves first."
    h "I intend to be a president for all Americans."

    p "Thank you, Vice President Harris. President Trump, your closing statement."

    $ trump_img = "trump attack"
    t "So, she just started by saying she's going to do this, she's going to do that."
    t "She's going to do all these wonderful things. Why hasn't she done it?"
    t "She's been there for three and a half years."
    t "They've had three and a half years to fix the border."
    t "Three and a half years to create jobs and all the things we talked about."
    t "Why hasn't she done it?"
    t "She should leave right now, go down to that beautiful White House."
    t "Go to the Capitol, get everyone together and do the things you want to do."
    t "But you haven't done it. And you won't do it."
    t "Because you believe in things that the American people don't believe in."
    t "We're a failing nation. We're a nation that's in serious decline."
    t "We're being laughed at all over the world. All over the world, they laugh."
    t "I know the leaders very well. They're coming to see me. They call me."
    t "We have wars going on in the Middle East. We have wars going on with Russia and Ukraine."
    t "We're going to end up in a third World War."
    t "And it will be a war like no other because of nuclear weapons, the power of weaponry."
    t "What these people have done to our country."
    t "And maybe toughest of all is allowing millions of people to come into our country."
    t "Many of them are criminals. And they're destroying our country."
    t "The worst president, the worst vice president in the history of our country."

    p "President Trump, thank you."
    p "And that concludes tonight's debate from the National Constitution Center in Philadelphia."

    # Transition to results
    "The candidates shake hands as the debate ends."
    "Across the nation, Americans are casting their votes..."

    p "Ladies and gentlemen, the votes are now being counted."

    "Minutes pass as the nation waits with bated breath..."

    p "We are now ready to announce the results of tonight's debate."

    # Calculate percentages based on score ratio
    $ total_score = harris_score + trump_score
    $ harris_percent = int(round((harris_score / float(total_score)) * 100)) if total_score > 0 else 50
    $ trump_percent = 100 - harris_percent

    p "The American people have spoken."

    "The results appear on screens across the country..."

    p "Vice President Kamala Harris... [harris_percent]%%."

    "A pause as the tension builds..."

    p "Former President Donald Trump... [trump_percent]%%."

    # Announce winner
    if harris_score > trump_score:
        "The crowd erupts as the winner is announced."
        p "The winner of tonight's presidential debate..."
        p "Vice President Kamala Harris!"
        $ harris_img = "harris smile"
        h "Thank you, America. Together, we will chart a new way forward."
        h "We're not going back!"
    elif trump_score > harris_score:
        "The crowd erupts as the winner is announced."
        p "The winner of tonight's presidential debate..."
        p "Former President Donald Trump!"
        $ trump_img = "trump smile"
        t "Thank you. We're going to make America great again."
        t "Greater than ever before!"
    else:
        p "In a historic outcome... tonight's debate is a tie."
        p "The American people remain divided."
        h "The fight continues."
        t "We'll see you at the next one."

    "And so concludes the presidential debate of September 10th, 2024."
    "The fate of the nation now rests in the hands of the voters."

    # Hide banner and show final tally
    $ current_section_name = ""
    hide screen section_banner
    p "Final debate scores:"
    p "Harris: [harris_score] points ([harris_percent]%%)"
    p "Trump: [trump_score] points ([trump_percent]%%)"

    p "Thank you for watching."
    p "We'll see you four years from now for the next debate."
    p "Good night, America!"

    return

