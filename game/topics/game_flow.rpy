# Game Flow - Section Selection and Progression

label select_sections:

    p "We have many important issues to cover tonight, but time is limited."
    p "Which five topics should we focus on?"

    python:
        selected_sections = []

    menu section_1:
        "Select your first topic:"

        "Economy":
            $ selected_sections.append("economy")
        "Tariffs & Trade":
            $ selected_sections.append("tariffs")
        "Abortion":
            $ selected_sections.append("abortion")
        "Immigration":
            $ selected_sections.append("immigration")
        "January 6th & Democracy":
            $ selected_sections.append("january6")
        "Israel & Foreign Policy":
            $ selected_sections.append("israel")
        "Ukraine":
            $ selected_sections.append("ukraine")
        "Race & Identity":
            $ selected_sections.append("race")

    menu section_2:
        "Select your second topic:"

        "Economy" if "economy" not in selected_sections:
            $ selected_sections.append("economy")
        "Tariffs & Trade" if "tariffs" not in selected_sections:
            $ selected_sections.append("tariffs")
        "Abortion" if "abortion" not in selected_sections:
            $ selected_sections.append("abortion")
        "Immigration" if "immigration" not in selected_sections:
            $ selected_sections.append("immigration")
        "January 6th & Democracy" if "january6" not in selected_sections:
            $ selected_sections.append("january6")
        "Israel & Foreign Policy" if "israel" not in selected_sections:
            $ selected_sections.append("israel")
        "Ukraine" if "ukraine" not in selected_sections:
            $ selected_sections.append("ukraine")
        "Race & Identity" if "race" not in selected_sections:
            $ selected_sections.append("race")

    menu section_3:
        "Select your third topic:"

        "Economy" if "economy" not in selected_sections:
            $ selected_sections.append("economy")
        "Tariffs & Trade" if "tariffs" not in selected_sections:
            $ selected_sections.append("tariffs")
        "Abortion" if "abortion" not in selected_sections:
            $ selected_sections.append("abortion")
        "Immigration" if "immigration" not in selected_sections:
            $ selected_sections.append("immigration")
        "January 6th & Democracy" if "january6" not in selected_sections:
            $ selected_sections.append("january6")
        "Israel & Foreign Policy" if "israel" not in selected_sections:
            $ selected_sections.append("israel")
        "Ukraine" if "ukraine" not in selected_sections:
            $ selected_sections.append("ukraine")
        "Race & Identity" if "race" not in selected_sections:
            $ selected_sections.append("race")

    menu section_4:
        "Select your fourth topic:"

        "Economy" if "economy" not in selected_sections:
            $ selected_sections.append("economy")
        "Tariffs & Trade" if "tariffs" not in selected_sections:
            $ selected_sections.append("tariffs")
        "Abortion" if "abortion" not in selected_sections:
            $ selected_sections.append("abortion")
        "Immigration" if "immigration" not in selected_sections:
            $ selected_sections.append("immigration")
        "January 6th & Democracy" if "january6" not in selected_sections:
            $ selected_sections.append("january6")
        "Israel & Foreign Policy" if "israel" not in selected_sections:
            $ selected_sections.append("israel")
        "Ukraine" if "ukraine" not in selected_sections:
            $ selected_sections.append("ukraine")
        "Race & Identity" if "race" not in selected_sections:
            $ selected_sections.append("race")

    menu section_5:
        "Select your fifth and final topic:"

        "Economy" if "economy" not in selected_sections:
            $ selected_sections.append("economy")
        "Tariffs & Trade" if "tariffs" not in selected_sections:
            $ selected_sections.append("tariffs")
        "Abortion" if "abortion" not in selected_sections:
            $ selected_sections.append("abortion")
        "Immigration" if "immigration" not in selected_sections:
            $ selected_sections.append("immigration")
        "January 6th & Democracy" if "january6" not in selected_sections:
            $ selected_sections.append("january6")
        "Israel & Foreign Policy" if "israel" not in selected_sections:
            $ selected_sections.append("israel")
        "Ukraine" if "ukraine" not in selected_sections:
            $ selected_sections.append("ukraine")
        "Race & Identity" if "race" not in selected_sections:
            $ selected_sections.append("race")

    return

label run_debate:

    # Section 1
    if "economy" in selected_sections:
        call economy
    elif "tariffs" in selected_sections:
        call tariffs
    elif "abortion" in selected_sections:
        call abortion
    elif "immigration" in selected_sections:
        call immigration
    elif "january6" in selected_sections:
        call january6
    elif "israel" in selected_sections:
        call israel
    elif "ukraine" in selected_sections:
        call ukraine
    elif "race" in selected_sections:
        call race

    # Run each selected section in order
    python:
        for section in selected_sections:
            renpy.call(section)

    call closing

    jump show_results

label show_results:
    scene bg room

    p "And with that, we conclude tonight's presidential debate."
    p "The American people have witnessed a historic exchange."

    $ margin = abs(harris_score - trump_score)

    p "Based on tonight's performance, our analysts project..."

    # Harris wins
    if harris_score > trump_score:
        $ trump_img = None
        $ harris_img = "harris smile"
        $ current_speaker = "harris"

        if margin >= 15:
            p "A decisive victory for Vice President Kamala Harris."
        elif margin >= 8:
            p "A clear advantage for Vice President Kamala Harris."
        else:
            p "A narrow edge for Vice President Kamala Harris."

        p "Final tally: Harris [harris_score] - Trump [trump_score]."

        h "Thank you. I'm grateful for this opportunity to speak directly to the American people."
        h "Together, we will chart a new way forward."

        $ trump_img = "trump defensive"
        $ current_speaker = "trump"
        t "We'll see what happens. The fake news media doesn't decide elections. The people do."

        $ harris_img = "harris default"
        $ trump_img = "trump default"
        $ current_speaker = ""

        p "If this margin holds, Kamala Harris would become the 47th President of the United States."

    # Trump wins
    elif trump_score > harris_score:
        $ harris_img = None
        $ trump_img = "trump smile"
        $ current_speaker = "trump"

        if margin >= 15:
            p "A decisive victory for former President Donald Trump."
        elif margin >= 8:
            p "A clear advantage for former President Donald Trump."
        else:
            p "A narrow edge for former President Donald Trump."

        p "Final tally: Trump [trump_score] - Harris [harris_score]."

        t "Thank you. It was a beautiful debate. Everybody knows who won."
        t "We're going to make America great again. Greater than ever before."

        $ harris_img = "harris attack"
        $ current_speaker = "harris"
        h "The American people deserve better. This isn't over."

        $ harris_img = "harris default"
        $ trump_img = "trump default"
        $ current_speaker = ""

        p "If this margin holds, Donald Trump would return to the White House as the 47th President."

    # Tie (impossible?)
    else:
        $ harris_img = "harris default"
        $ trump_img = "trump default"
        $ current_speaker = ""

        p "Tonight's debate ends in a statistical tie."
        p "Final tally: Harris [harris_score] - Trump [trump_score]."

        h "The American people will make their voices heard in November."
        t "It's going to be close. But we're going to win. Believe me."

        p "This race remains too close to call."

    p "Thank you for watching tonight's debate from the National Constitution Center in Philadelphia."
    p "Good night, America."

    return
