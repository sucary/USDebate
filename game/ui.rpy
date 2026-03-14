# UI Screens and Styling

# Character images
image harris default = "images/raw/harris_default.png"
image harris smile = "images/raw/harris_smile.png"
image harris laugh = "images/raw/harris_laugh.png"
image harris attack = "images/raw/harris_attack.png"

image trump default = "images/raw/trump_default.png"
image trump smile = "images/raw/trump_smile.png"
image trump attack = "images/raw/trump_attack.png"
image trump defensive = "images/raw/trump_defensive.png"

# Speaker state
default current_speaker = ""
default harris_img = "harris default"
default trump_img = "trump default"

# Debate stage - shows candidates
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

# Section banner - top center
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

# Score strip - horizontal layout, vertical bars, top right, shown between topics
default show_score_strip = False
default harris_support_prev = 50
default trump_support_prev = 50
default topics_shown = 0

screen score_strip():
    zorder 10
    if show_score_strip:
        # Calculate current support
        $ h_support = max(1, min(99, 50 + harris_score - trump_score))
        $ t_support = 100 - h_support
        $ h_change = h_support - harris_support_prev
        $ t_change = t_support - trump_support_prev

        frame:
            xalign 1.0
            ypos 10
            xoffset -10
            padding (10, 8)
            background "#000000cc"

            hbox:
                spacing 12

                # Harris support (blue) - vertical bar growing upward
                vbox:
                    spacing 2
                    fixed:
                        xsize 30
                        ysize 60
                        frame:
                            xsize 8
                            ysize int(60 * h_support / 100)
                            xalign 0.5
                            yalign 1.0
                            background "#7ebfeb"
                            padding (0, 0)
                    text "[h_support]%" size 12 color "#7ebfeb" bold True text_align 0.5 xalign 0.5
                    if topics_shown > 0:
                        if h_change > 0:
                            text "(+[h_change]%)" size 10 color "#88cc88" text_align 0.5 xalign 0.5
                        elif h_change < 0:
                            text "([h_change]%)" size 10 color "#cc8888" text_align 0.5 xalign 0.5
                        else:
                            text "0%" size 10 color "#888888" text_align 0.5 xalign 0.5

                # Divider
                frame:
                    xsize 1
                    ysize (70 if topics_shown > 0 else 55)
                    yalign 0.5
                    background "#666666"
                    padding (0, 0)

                # Trump support (red) - vertical bar growing upward
                vbox:
                    spacing 2
                    fixed:
                        xsize 30
                        ysize 60
                        frame:
                            xsize 8
                            ysize int(60 * t_support / 100)
                            xalign 0.5
                            yalign 1.0
                            background "#ea8d8d"
                            padding (0, 0)
                    text "[t_support]%" size 12 color "#ea8d8d" bold True text_align 0.5 xalign 0.5
                    if topics_shown > 0:
                        if t_change > 0:
                            text "(+[t_change]%)" size 10 color "#88cc88" text_align 0.5 xalign 0.5
                        elif t_change < 0:
                            text "([t_change]%)" size 10 color "#cc8888" text_align 0.5 xalign 0.5
                        else:
                            text "0%" size 10 color "#888888" text_align 0.5 xalign 0.5
