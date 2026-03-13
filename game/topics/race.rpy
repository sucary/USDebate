label race:
    $ race_questions_asked = 0
    $ race_q1_asked = False
    $ race_q2_asked = False
    $ race_q3_asked = False

label race_menu:
    menu:
        "Which question about race would you like to ask?"

        "\"Why question her racial identity?\" (Ask Trump)" if not race_q1_asked:
            $ race_q1_asked = True
            jump race_q1
        "\"How would you unite the country?\" (Ask Harris)" if not race_q2_asked:
            $ race_q2_asked = True
            jump race_q2
        "\"What's your record on race?\" (Ask Both)" if not race_q3_asked:
            $ race_q3_asked = True
            jump race_q3

label race_q1:
    $ current_question_num = race_questions_asked + 1
    $ harris_score += 9
    $ trump_score += 2

    p "Mr. President, you recently said of Vice President Harris:"
    p "\"I didn't know she was Black until a number of years ago when she happened to turn Black, and now she wants to be known as Black.\""
    p "I want to ask a bigger-picture question here tonight."
    p "Why do you believe it's appropriate to weigh in on the racial identity of your opponent?"

    t "I don't. And I don't care."
    t "I don't care what she is. I don't care."
    t "You make a big deal out of something. I couldn't care less."
    t "Whatever she wants to be is okay with me."

    p "But those were your words. So, I'm asking--"

    t "I don't know. I don't know. All I can say is I read where she was not Black, that she put out."
    t "And, I'll say that. And then I read that she was Black."
    t "And that's okay. Either one was okay with me. That's up to her."

    menu:
        "Challenge him on this?"

        "Challenge him":
            jump race_q1_challenge
        "Let Harris respond":
            jump race_q1_harris

label race_q1_challenge:
    p "But sir, Vice President Harris has always identified as both Black and South Asian."
    p "Her parents are Jamaican and Indian. Why question it at all?"

    if renpy.random.random() > 0.5:
        jump race_q1_fumble
    else:
        jump race_q1_recover

label race_q1_fumble:
    $ trump_score -= 2
    $ trump_img = "trump defensive"
    t "Look, I just said what I read. I don't know. I don't care."
    t "Can we talk about something important? We have a country that's being destroyed."
    t "This is not an important issue. The border is important. Inflation is important."
    p "You raised the issue, sir."
    t "I didn't raise it! You raised it!"
    jump race_q1_harris

label race_q1_recover:
    $ trump_score += 2
    $ trump_img = "trump default"
    t "You know what? I shouldn't have said it. It doesn't matter. It's not important."
    t "What's important is her policies. And her policies are destroying this country."
    t "She can call herself whatever she wants. I'm focused on the economy, the border, making America safe again."
    t "Let's talk about that instead of gotcha questions."
    jump race_q1_harris

label race_q1_harris:
    p "Vice President Harris, your thoughts on this?"

    h "I think it's a tragedy that we have someone who wants to be president."
    h "Who has consistently over the course of his career attempted to use race to divide the American people."
    h "You know, I do believe that the vast majority of us know that we have so much more in common."
    h "Than what separates us."
    h "And we don't want this kind of approach that is just constantly trying to divide us, and especially by race."
    h "And let's remember how Donald Trump started."
    h "He was investigated because he refused to rent property to Black families."
    h "Let's remember, this is the same individual who took out a full-page ad in The New York Times."
    h "Calling for the execution of five young Black and Latino boys who were innocent."
    h "The Central Park Five."
    h "This is the same individual who spread birther lies about the first Black President of the United States."
    h "And I think the American people want better than that. Want better than this."
    h "We don't want a leader who is constantly trying to have Americans point their fingers at each other."

    jump race_next

label race_q2:
    $ current_question_num = race_questions_asked + 1
    $ harris_score += 8
    $ trump_score += 3

    p "Vice President Harris, you've accused President Trump of being divisive."
    p "But some say the left has also contributed to division. How would you bring the country together?"

    h "I believe in what we can do together. I travel our country."
    h "We see in each other a friend. We see in each other a neighbor."
    h "People tell me, can we please just have discourse about how we're going to invest in the aspirations."
    h "And the ambitions and the dreams of the American people?"
    h "Knowing that regardless of people's color or the language their grandmother speaks."
    h "We all have the same dreams and aspirations."
    h "And want a president who invests in those, not in hate and division."
    h "I intend to be that president. A president for all Americans."

    t "This is the most divisive presidency in the history of our country."
    t "There's never been anything like it. They're destroying our country."
    t "And they come up with things like what she just said going back many, many years."
    t "When a lot of people including Mayor Bloomberg agreed with me on the Central Park Five."
    t "They admitted, they said, they pled guilty."
    t "And I said, well, if they pled guilty they badly hurt a person, killed a person ultimately."

    h "They were exonerated."

    t "And if they pled guilty, then they pled we're not guilty."
    t "But this is a person that has to stretch back years, 40, 50 years ago because there's nothing now."
    t "I built one of the greatest economies in the history of the world and I'm going to build it again."
    t "It's going to be bigger, better and stronger."

    p "Mr. President, your time is up."

    h "I want to respond to that, though. I want to just respond briefly."
    h "Clearly, I am not Joe Biden, and I am certainly not Donald Trump."
    h "And what I do offer is a new generation of leadership for our country."
    h "One who believes in what is possible."
    h "One who brings a sense of optimism about what we can do instead of always disparaging the American people."
    h "I believe in what we can do to strengthen our small businesses, which is why I have a plan."
    h "Let's talk about our plans. And let's compare the plans."
    h "I have a plan to give startup businesses $50,000 tax deduction."
    h "To pursue their ambitions, their innovation, their ideas."
    h "I have a plan, $6,000 for young families for the first year of your child's life."
    h "I have a plan that is about allowing people to pursue what has been fleeting in terms of the American dream."
    h "By offering $25,000 down payment assistance for first-time home buyers."
    h "That's the kind of conversation I believe people really want tonight."
    h "As opposed to a conversation that is constantly about belittling and name-calling."
    h "Let's turn the page and move forward."

    t "She is destroying our country."
    t "She has a plan to defund the police. She has a plan to confiscate everybody's gun."
    t "She has a plan to not allow fracking in Pennsylvania or anywhere else. That's what her plan is."

    p "President Trump. We have to move on."

    jump race_next

label race_q3:
    $ current_question_num = race_questions_asked + 1
    $ harris_score += 6
    $ trump_score += 6

    p "Let's discuss your records on race."
    p "Vice President Harris, as a prosecutor, some say you were too tough on Black communities."
    p "President Trump, you've faced criticism for your comments and housing discrimination."
    p "How do you each respond?"

    h "As a prosecutor, I never asked a victim or a witness, are you a Republican or a Democrat?"
    h "The only thing I ever asked them, are you okay?"
    h "I fought for people. All people. That's what I'll do as president."

    t "I got criminal justice reform done. The First Step Act."
    t "Obama couldn't do it. Biden couldn't do it. I did it."
    t "I got opportunity zones for Black communities. Historic funding for HBCUs."
    t "I did more for the Black community than any president since Abraham Lincoln."

    menu:
        "Challenge Trump on that claim?"

        "Challenge him":
            jump race_q3_challenge
        "Move on":
            jump race_next

label race_q3_challenge:
    p "President Trump, you said you did more for Black Americans than any president since Lincoln."
    p "Historians dispute that. Do you stand by it?"

    if renpy.random.random() > 0.5:
        jump race_q3_fumble
    else:
        jump race_q3_recover

label race_q3_fumble:
    $ trump_score -= 2
    $ trump_img = "trump defensive"
    t "Absolutely. Look at the numbers. Look at the economy."
    t "Black unemployment was the lowest in history. Lowest ever recorded."
    t "And she wants to take credit for what I did."
    t "Lincoln freed the slaves, I got criminal justice reform. Pretty comparable."
    h "That's absurd."
    jump race_next

label race_q3_recover:
    $ trump_score += 2
    $ trump_img = "trump default"
    t "Maybe it was a strong statement. But here's what I did."
    t "Criminal justice reform, something Obama and Biden tried and failed."
    t "Opportunity zones, billions in investment in Black communities."
    t "Record funding for HBCUs, historically Black colleges."
    t "Lowest Black unemployment ever recorded. I judge by results."
    jump race_next

label race_next:
    $ harris_img = "harris default"
    $ trump_img = "trump default"
    $ race_questions_asked += 1
    if race_questions_asked < 2:
        $ followup = renpy.random.choice([
            "Thank you both. Let's continue with another question on this topic.",
            "All right, thank you. I have one more question on this subject.",
            "Thank you. I'd like to stay on this topic for one more question."
        ])
        p "[followup]"
        jump race_menu
    return
