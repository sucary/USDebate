label israel:
    $ israel_questions_asked = 0
    $ israel_q1_asked = False
    $ israel_q2_asked = False
    $ israel_q3_asked = False

label israel_menu:
    menu:
        "Which question about foreign policy would you like to ask?"

        "\"How would you achieve a ceasefire?\" (Ask Harris)" if not israel_q1_asked:
            $ israel_q1_asked = True
            jump israel_q1
        "\"Do you support Israel?\" (Ask Both)" if not israel_q2_asked:
            $ israel_q2_asked = True
            jump israel_q2
        "\"Why do dictators support you?\" (Ask Trump)" if not israel_q3_asked:
            $ israel_q3_asked = True
            jump israel_q3

label israel_q1:
    $ current_question_num = israel_questions_asked + 1
    $ harris_score += 6
    $ trump_score += 6

    p "Vice President Harris, in December you said Israel has a right to defend itself."
    p "But you added international humanitarian law must be respected, Israel must do more to protect innocent civilians."
    p "You said that nine months ago."
    p "Now an estimated 40,000 Palestinians are dead. Nearly 100 hostages remain."
    p "Just last week Prime Minister Benjamin Netanyahu said there's not a deal in the making."
    p "President Biden has not been able to break through the stalemate. How would you do it?"

    h "Well, let's understand how we got here."
    h "On October 7th, Hamas, a terrorist organization, slaughtered 1,200 Israelis."
    h "Many of them young people who were simply attending a concert. Women were horribly raped."
    h "And so absolutely, I said then, I say now, Israel has a right to defend itself."
    h "We would. And how it does so matters."
    h "Because it is also true far too many innocent Palestinians have been killed. Children. Mothers."
    h "What we know is that this war must end. It must end immediately."
    h "And the way it will end is we need a ceasefire deal and we need the hostages out."
    h "And so we will continue to work around the clock on that."
    h "We must chart a course for a two-state solution."
    h "And in that solution, there must be security for the Israeli people and Israel and in equal measure for the Palestinians."
    h "But the one thing I will assure you always, I will always give Israel the ability to defend itself."
    h "In particular as it relates to Iran and any threat that Iran and its proxies pose to Israel."

    p "President Trump, how would you negotiate with Netanyahu and also Hamas in order to get the hostages out and prevent the killing of more innocent civilians in Gaza?"

    t "If I were president it would have never started."
    t "If I were president, Russia would have never, ever, I know Putin very well, he would have never."
    t "And there was no threat of it either, by the way, for four years."
    t "Have gone into Ukraine and killed millions of people when you add it up."
    t "Far worse than people understand what's going on over there."
    t "But when she mentions about Israel, all of a sudden, she hates Israel."

    $ harris_img = "harris smile"
    h "{i}[[shakes head]{/i}"
    $ harris_img = "harris default"

    $ trump_img = "trump attack"
    t "She wouldn't even meet with Netanyahu when he went to Congress to make a very important speech."
    t "She refused to be there because she was at a sorority party of hers."
    t "She wanted to go to the sorority party."
    t "She hates Israel."
    t "If she's president, I believe that Israel will not exist within two years from now."
    t "And I've been pretty good at predictions. And I hope I'm wrong about that one."
    t "She hates Israel. At the same time in her own way she hates the Arab population because the whole place is going to get blown up."
    t "It would have never happened."
    t "Iran was broke under Donald Trump."
    t "Now Iran has $300 billion because they took off all the sanctions that I had."
    t "Iran had no money for Hamas or Hezbollah or any of the 28 different spheres of terror."

    jump israel_next

label israel_q2:
    $ current_question_num = israel_questions_asked + 1
    $ harris_score += 4
    $ trump_score += 8

    p "Vice President Harris, President Trump says you hate Israel. How do you respond?"

    h "That's absolutely not true."
    h "I have my entire career and life supported Israel and the Israeli people. He knows that."
    h "He's trying to again divide and distract from the reality."
    h "Which is it is very well known that Donald Trump is weak and wrong on national security and foreign policy."
    h "It is well known that he admires dictators, wants to be a dictator on day one according to himself."
    h "It is well known he said of Putin that he can do whatever the hell he wants and go into Ukraine."
    h "It is well known when Russia went into Ukraine it was brilliant."
    h "It is well known he exchanged love letters with Kim Jong Un."
    h "And it is absolutely well known that these dictators and autocrats are rooting for you to be president again."
    h "Because they're so clear, they can manipulate you with flattery and favors."
    h "And that is why so many military leaders who you have worked with have told me you are a disgrace."

    menu:
        "Challenge Harris on skipping Netanyahu's speech?"

        "Challenge her":
            jump israel_q2_challenge
        "Let Trump respond":
            jump israel_q2_trump

label israel_q2_challenge:
    p "Vice President Harris, but you did skip Netanyahu's address to Congress. Can you explain why?"

    if renpy.random.random() > 0.5:
        jump israel_q2_fumble
    else:
        jump israel_q2_recover

label israel_q2_fumble:
    $ harris_score -= 2
    $ harris_img = "harris default"
    h "I had a prior commitment. A scheduling conflict."
    h "My support for Israel speaks for itself through my actions."
    t "A sorority party! She went to a sorority party!"
    jump israel_q2_trump

label israel_q2_recover:
    $ harris_score += 2
    $ harris_img = "harris attack"
    h "I met with Prime Minister Netanyahu privately. We had a substantive, candid conversation."
    h "I don't need a photo op to prove my support for Israel. What matters is policy."
    h "And I've been clear: Israel has the right to defend itself. I've condemned Hamas unequivocally."
    h "Unlike Donald Trump, who invited the Taliban to Camp David."
    t "That's not the same thing--"
    h "You invited terrorists to Camp David."
    jump israel_q2_trump

label israel_q2_trump:
    t "They're the ones, and she's the one that caused it, that's weak on national security."
    t "Allowing every nation, last month for the year, 168 different countries sending people into our country."
    t "Their crime rates are way down."
    t "Putin endorsed her last week. Said I hope she wins."
    t "And I think he meant it."
    t "Because what he's gotten away with is absolutely incredible. It wouldn't have happened with me."

    jump israel_next

label israel_q3:
    $ current_question_num = israel_questions_asked + 1
    $ harris_score += 5
    $ trump_score += 7

    p "President Trump, you've spoken highly of leaders like Viktor Orban, Vladimir Putin, and Kim Jong Un."
    p "Your critics say you admire authoritarian leaders. How do you respond?"

    t "Let me tell you about world leaders."
    t "Viktor Orban, one of the most respected men, they call him a strong man."
    t "He's a tough person. Smart. Prime Minister of Hungary."
    t "They said why is the whole world blowing up? Three years ago it wasn't. Why is it blowing up?"
    t "He said because you need Trump back as president. They were afraid of him."
    t "China was afraid."
    t "And I don't like to use the word afraid but I'm just quoting him. China was afraid of him. North Korea was afraid of him."
    t "I ended the Nord Stream 2 pipeline and Biden put it back on day one."
    t "But he ended the XL pipeline in our country."
    t "He let the Russians build a pipeline going all over Europe and heading into Germany."
    t "The biggest pipeline in the world."
    t "Look, Viktor Orban said it. He said the most respected, most feared person is Donald Trump."
    t "We had no problems when Trump was president."

    menu:
        "Challenge him on dictator support?"

        "Challenge him":
            jump israel_q3_challenge
        "Move on":
            jump israel_next

label israel_q3_challenge:
    p "But why is it a good thing that authoritarian leaders want you to win? Doesn't that concern you?"

    if renpy.random.random() > 0.5:
        jump israel_q3_fumble
    else:
        jump israel_q3_recover

label israel_q3_fumble:
    $ trump_score -= 2
    $ trump_img = "trump defensive"
    t "They want me to win because they respect me. They're afraid of me."
    t "Putin endorsed her because he knows she's weak. He knows he can walk all over her."
    t "Look at Biden. He can't even put a sentence together. They laugh at him. They laugh at her too."
    p "But again, why is it good that dictators support you?"
    t "Because they know there will be strength! Strength!"
    jump israel_next

label israel_q3_recover:
    $ trump_score += 2
    $ trump_img = "trump default"
    t "I'll tell you why. Because they know there will be peace."
    t "When I was president, no new wars. We had peace through strength."
    t "China didn't move on Taiwan. Russia didn't move on Ukraine. Iran was broke."
    t "Now look at the world. It's on fire. That's what weakness gets you."
    t "They want me back because they know I'll bring stability."
    t "That's good for everyone."
    jump israel_next

label israel_next:
    $ harris_img = "harris default"
    $ trump_img = "trump default"
    $ israel_questions_asked += 1
    if israel_questions_asked < 2:
        $ followup = renpy.random.choice([
            "Thank you both. Let's continue with another question on foreign policy.",
            "All right, thank you. I have one more question on this topic.",
            "Thank you. I'd like to stay on foreign policy for one more question."
        ])
        p "[followup]"
        jump israel_menu
    return
