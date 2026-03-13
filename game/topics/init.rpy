# Character images
image harris default = "images/raw/harris_default.png"
image harris smile = "images/raw/harris_smile.png"
image harris laugh = "images/raw/harris_laugh.png"
image harris attack = "images/raw/harris_attack.png"

image trump default = "images/raw/trump_default.png"
image trump smile = "images/raw/trump_smile.png"
image trump attack = "images/raw/trump_attack.png"
image trump defensive = "images/raw/trump_defensive.png"

default current_speaker = ""
default harris_img = "harris default"
default trump_img = "trump default"
default debate_started = False

screen debate_stage():
    zorder 0

    if harris_img:
        add harris_img:
            xalign 0.2
            ypos 80
            yanchor 0.0
            alpha (1.0 if (current_speaker == "harris" or current_speaker == "") else 0.4)

    if trump_img:
        add trump_img:
            xalign 0.8
            ypos 80
            yanchor 0.0
            alpha (1.0 if (current_speaker == "trump" or current_speaker == "") else 0.4)

# Initialize game variables and section management

init -10 python:
    def set_speaker_harris(event, interact=True, **kwargs):
        if event == "begin":
            store.current_speaker = "harris"

    def set_speaker_trump(event, interact=True, **kwargs):
        if event == "begin":
            store.current_speaker = "trump"

    def set_speaker_moderator(event, interact=True, **kwargs):
        if event == "begin":
            store.current_speaker = ""

    def harris(expression):
        store.harris_img = "harris " + expression
        renpy.restart_interaction()

    def trump(expression):
        store.trump_img = "trump " + expression
        renpy.restart_interaction()

init python:
    all_sections = [
        ("economy", "Economy"),
        ("tariffs", "Tariffs & Trade"),
        ("abortion", "Abortion"),
        ("immigration", "Immigration"),
        ("january6", "January 6th & Democracy"),
        ("israel", "Israel & Foreign Policy"),
        ("ukraine", "Ukraine"),
        ("race", "Race & Identity")
    ]

    # Colorize names in dialog and menus
    def colorize_names(s):
        replacements = []
        name_colors = [
            # Main candidates
            ("Donald Trump", "#ea8d8d"),
            ("Kamala Harris", "#7ebfeb"),
            ("Trump", "#ea8d8d"),
            ("Harris", "#7ebfeb"),
            # Other political figures
            ("Joe Biden", "#7ebfeb"),
            ("Biden", "#7ebfeb"),
            ("JD Vance", "#ea8d8d"),
            ("Vance", "#ea8d8d"),
            ("Nancy Pelosi", "#7ebfeb"),
            ("Pelosi", "#7ebfeb"),
            ("Obama", "#7ebfeb"),
            # Foreign leaders
            ("Vladimir Putin", "#cc4444"),
            ("Putin", "#cc4444"),
            ("Zelenskyy", "#ffd700"),
            ("Kim Jong Un", "#cc4444"),
            ("Viktor Orban", "#cc4444"),
            ("Orban", "#cc4444"),
            ("Netanyahu", "#6699cc"),
            # Other names
            ("Liz Cheney", "#9999dd"),
            ("Dick Cheney", "#9999dd"),
            ("Mitt Romney", "#9999dd"),
            ("John McCain", "#9999dd"),
            ("George Bush", "#9999dd"),
            ("Ronald Reagan", "#9999dd"),
            ("Abraham Lincoln", "#9999dd"),
        ]

        for i, (name, color) in enumerate(name_colors):
            placeholder = "\x00{}\x00".format(i)
            if name in s:
                s = s.replace(name, placeholder)
                replacements.append((placeholder, name, color))

        for placeholder, name, color in replacements:
            colored = "{{color={}}}{}{{/color}}".format(color, name)
            s = s.replace(placeholder, colored)

        return s

    config.say_menu_text_filter = colorize_names

default harris_score = 0
default trump_score = 0
default sections_completed = 0
default selected_sections = []

default current_section_name = ""
default current_question_num = 0
default total_sections = 5

# Section banner screen
screen section_banner():
    if current_section_name:
        frame:
            xalign 0.5
            ypos 10
            padding (30, 10)
            background "#000000aa"
            hbox:
                spacing 20
                if current_section_num > 0:
                    text "[current_section_num]. [current_section_name]" size 24 color "#ffffff"
                else:
                    text current_section_name size 24 color "#ffffff"
                if current_question_num > 0:
                    text "|" size 24 color "#666666"
                    text "Question [current_question_num]/2" size 24 color "#cccccc"

default current_section_num = 0

default done_economy = False
default done_tariffs = False
default done_abortion = False
default done_immigration = False
default done_jan6 = False
default done_foreign_policy = False
default done_ukraine = False
default done_identity = False
