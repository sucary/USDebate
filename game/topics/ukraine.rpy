label ukraine:
    $ ukraine_questions_asked = 0
    $ ukraine_q1_asked = False
    $ ukraine_q2_asked = False
    $ ukraine_q3_asked = False

label ukraine_menu:
    menu:
        "Which question about Ukraine would you like to ask?"

        "\"How would you end it in 24 hours?\" (Ask Trump)" if not ukraine_q1_asked:
            $ ukraine_q1_asked = True
            jump ukraine_q1
        "\"Do you want Ukraine to win?\" (Ask Trump)" if not ukraine_q2_asked:
            $ ukraine_q2_asked = True
            jump ukraine_q2
        "\"Why should we support NATO?\" (Ask Harris)" if not ukraine_q3_asked:
            $ ukraine_q3_asked = True
            jump ukraine_q3

label ukraine_q1:
    $ current_question_num = ukraine_questions_asked + 1
    $ harris_score += 7
    $ trump_score += 5

    p "Mr. President, we're two and a half years into the war in Ukraine."
    p "The Biden administration believes we must defend Ukraine from Russia, from Vladimir Putin."
    p "To defend their sovereignty and democracy."
    p "They argue that if Putin wins he may be emboldened to move further into other countries."
    p "You have said you would solve this war in 24 hours."
    p "You said so just before the break tonight. How exactly would you do that?"

    t "I want the war to stop. I want to save lives that are being uselessly, people being killed by the millions."
    t "It's the millions. It's so much worse than the numbers that you're getting, which are fake numbers."
    t "Look, we're in for 250 billion or more."
    t "Because they don't ask Europe, which is a much bigger beneficiary to getting this thing done than we are."
    t "They're in for $150 billion less because Biden and her don't have the courage to ask Europe like I did with NATO."
    t "They paid billions and billions, hundreds of billions of dollars."
    t "When I said either you pay up or we're not going to protect you anymore."
    t "So that may be one of the reasons they don't like me as much as they like weak people."
    t "But you take a look at what's happening."
    t "We're in for 250 to 275 billion. They're into 100 to 150. They should be forced to equalize."
    t "I want to get the war settled."
    t "I know Zelenskyy very well and I know Putin very well."
    t "I have a good relationship. And they respect your president."
    t "They don't respect Biden. How would you respect him? Why? For what reason?"
    t "He hasn't even made a phone call in two years to Putin. Hasn't spoken to anybody."

    menu:
        "Press for specifics on the deal?"

        "Press him":
            jump ukraine_q1_challenge
        "Let Harris respond":
            jump ukraine_q1_harris

label ukraine_q1_challenge:
    p "But what specifically would you propose? What would the terms of the deal look like?"

    if renpy.random.random() > 0.5:
        jump ukraine_q1_fumble
    else:
        jump ukraine_q1_recover

label ukraine_q1_fumble:
    $ trump_score -= 2
    $ trump_img = "trump defensive"
    t "I can't tell you that because if I tell you, I lose all my negotiating power."
    t "But I'll get it done. I'll speak to one, I'll speak to the other. I'll get them together."
    t "That war would have never happened. And I'll end it fast."
    p "So you won't share any specifics?"
    t "You'll see. When I'm president, you'll see. It'll be beautiful."
    jump ukraine_q1_harris

label ukraine_q1_recover:
    $ trump_score += 2
    $ trump_img = "trump attack"
    t "Here's what I would do. I would tell Zelenskyy, you're going to have to make a deal. The war has to end."
    t "And I would tell Putin, you don't make a deal, we're going to give Ukraine everything. Everything they need."
    t "Both sides need to come to the table. Right now, nobody's talking. Nobody's even trying."
    t "I'm the only one who can make that happen because both sides respect me."
    jump ukraine_q1_harris

label ukraine_q1_harris:
    p "Vice President Harris, your response."

    h "Well, first of all, it's important to remind the former president you're not running against Joe Biden."
    h "You're running against me."
    h "I believe the reason that Donald Trump says that this war would be over within 24 hours is because he would just give it up."
    h "And that's not who we are as Americans."
    h "Let's understand what happened here."
    h "I actually met with Zelenskyy a few days before Russia invaded."
    h "Before Russia tried through force to change territorial boundaries."
    h "I shared with him American intelligence about how he could defend himself."
    h "Days later I went to NATO's eastern flank, to Poland and Romania."
    h "And through the work that I and others did we brought 50 countries together."
    h "To support Ukraine in its righteous defense."
    h "And because of our support, because of the air defense, the ammunition, the artillery."
    h "The javelins, the Abrams tanks that we have provided."
    h "Ukraine stands as an independent and free country."
    h "If Donald Trump were president, Putin would be sitting in Kyiv right now."

    jump ukraine_next

label ukraine_q2:
    $ current_question_num = ukraine_questions_asked + 1
    $ harris_score += 7
    $ trump_score += 5

    p "And I want to ask you a very simple question tonight."
    p "Do you want Ukraine to win this war?"

    t "I want the war to stop. I want to save lives."

    p "Just to clarify: Do you believe it's in the U.S. best interests for Ukraine to win this war? Yes or no?"

    t "I think it's in the U.S. best interest to get this war finished and just get it done. All right. Negotiate a deal."
    t "Because we have to stop all of these human lives from being destroyed."

    menu:
        "Press for a yes or no answer?"

        "Press him":
            jump ukraine_q2_challenge
        "Let Harris respond":
            jump ukraine_q2_harris

label ukraine_q2_challenge:
    p "That's not a yes or no. Do you want Ukraine to win?"

    if renpy.random.random() > 0.5:
        jump ukraine_q2_fumble
    else:
        jump ukraine_q2_recover

label ukraine_q2_fumble:
    $ trump_score -= 2
    $ trump_img = "trump defensive"
    t "I want the war to end. That's the answer. That's what the American people want."
    t "I want to save lives. Millions of people are dying."
    p "But should Ukraine win or Russia?"
    t "Everybody wins when the war ends. That's winning."
    h "He won't say it. He won't say Ukraine should win."
    jump ukraine_q2_harris

label ukraine_q2_recover:
    $ trump_score += 2
    $ trump_img = "trump default"
    t "I want America to win. I want peace."
    t "Look, Ukraine wins when the war stops."
    t "They've been incredibly brave. They've fought hard."
    t "But this war has to end. More fighting means more dying."
    t "We can get a deal done that preserves Ukraine's independence."
    t "That's winning. That's how I see it."
    jump ukraine_q2_harris

label ukraine_q2_harris:
    p "Vice President Harris, your response."

    h "First of all, it's important to remind the former president you're not running against Joe Biden."
    h "You're running against me."
    h "I believe the reason that Donald Trump says that this war would be over within 24 hours is because he would just give it up."
    h "And that's not who we are as Americans."
    h "I actually met with Zelenskyy a few days before Russia invaded."
    h "I shared with him American intelligence about how he could defend himself."
    h "Days later I went to NATO's eastern flank, to Poland and Romania."
    h "And through the work that I and others did we brought 50 countries together to support Ukraine."
    h "Because of our support, Ukraine stands as an independent and free country."
    h "If Donald Trump were president, Putin would be sitting in Kyiv right now."

    t "I have to respond."

    p "Please, I'll give you a minute."

    t "Putin would be sitting in Moscow and he wouldn't have lost 300,000 men and women."

    $ harris_img = "harris attack"
    h "{i}[[inaudible]{/i}"

    $ trump_img = "trump attack"
    t "Quiet, please. He would have been sitting in Moscow much happier than he is right now."
    t "But eventually, you know, he's got a thing that other people don't have. He's got nuclear weapons."
    t "They don't ever talk about that. He's got nuclear weapons. Nobody ever thinks about that."
    t "And eventually maybe he'll use them. Maybe he hasn't been that threatening. But he does have that."

    jump ukraine_next

label ukraine_q3:
    $ current_question_num = ukraine_questions_asked + 1
    $ harris_score += 5
    $ trump_score += 7

    p "Vice President Harris, some Americans question why we should spend hundreds of billions defending Ukraine."
    p "How would you make the case to them?"

    h "Putin's agenda is not just about Ukraine."
    h "Understand why the European allies and our NATO allies are so thankful that you are no longer president."
    h "They understand the importance of the greatest military alliance the world has ever known."
    h "Which is NATO."
    h "And what we have done to preserve the ability of Zelenskyy and the Ukrainians."
    h "To fight for their independence."
    h "Otherwise, Putin would be sitting in Kyiv with his eyes on the rest of Europe. Starting with Poland."
    h "And why don't you tell the 800,000 Polish Americans right here in Pennsylvania."
    h "How quickly you would give up for the sake of favor."
    h "And what you think is a friendship with what is known to be a dictator who would eat you for lunch."

    t "They sent her to negotiate peace before this war started."
    t "Three days later he went in and he started the war."
    t "Because everything they said was weak and stupid. They said the wrong things."
    t "That war should have never started."
    t "She was the emissary. They sent her in to negotiate with Zelenskyy and Putin."
    t "And she did and the war started three days later."

    p "Vice President Harris, have you ever met Vladimir Putin?"

    h "Yet again, I said it at the beginning of this debate, you're going to hear a bunch of lies coming from this fella."
    h "And that is another one."
    h "When I went to meet with President Zelenskyy, I've now met with him over five times."
    h "It has been about standing as America always should, as a leader upholding international rules and norms."

    t "David, one thing. Secretary General Stoltenberg said Trump did the most amazing thing I've ever seen."
    t "He got these countries, the 28 countries at the time, to pay up."
    t "He said I've never seen -- he's the head of NATO."
    t "For years we were paying almost all of NATO."
    t "We were being ripped off by European nations both on trade and on NATO."
    t "I got them to pay by saying one of the statements, if you don't pay we're not going to protect you."

    p "President Trump--"

    t "Otherwise we would've never gotten it."
    t "He said it was one of the most incredible jobs that he's ever seen done."

    jump ukraine_next

label ukraine_next:
    $ harris_img = "harris default"
    $ trump_img = "trump default"
    $ ukraine_questions_asked += 1
    if ukraine_questions_asked < 2:
        $ followup = renpy.random.choice([
            "Thank you both. Let's continue with another question on Ukraine.",
            "All right, thank you. I have one more question on this topic.",
            "Thank you. I'd like to stay on Ukraine for one more question."
        ])
        p "[followup]"
        jump ukraine_menu
    return
