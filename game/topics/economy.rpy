label economy:
    $ economy_questions_asked = 0
    $ economy_q1_asked = False
    $ economy_q2_asked = False
    $ economy_q3_asked = False

label economy_menu:
    menu:
        "Which question would you like to ask about the economy?"

        "\"Are Americans better off?\" (Ask Harris)" if not economy_q1_asked:
            $ economy_q1_asked = True
            jump economy_q1
        "\"Who's to blame for inflation?\" (Ask Trump)" if not economy_q2_asked:
            $ economy_q2_asked = True
            jump economy_q2
        "\"What are your economic plans?\" (Ask Both)" if not economy_q3_asked:
            $ economy_q3_asked = True
            jump economy_q3

label economy_q1:
    $ current_question_num = economy_questions_asked + 1
    $ harris_score += 5
    $ trump_score += 7

    p "Vice President Harris, your opponent often asks supporters: are you better off than you were four years ago?"
    p "Do you believe Americans are better off than they were four years ago?"

    $ harris_img = "harris default"
    h "So, I was raised as a middle-class kid."
    h "And I am actually the only person on this stage who has a plan that is about lifting up the middle class and working people of America."
    h "I believe in the ambition, the aspirations, the dreams of the American people."
    h "And that is why I imagine and have actually a plan to build what I call an opportunity economy."
    h "Because here's the thing. We know that we have a shortage of homes and housing."
    h "The cost of housing is too expensive for far too many people."
    h "We know that young families need support to raise their children."
    h "And I intend on extending a tax cut for those families of $6,000, which is the largest child tax credit that we have given in a long time."
    h "So that those young families can afford to buy a crib, buy a car seat, buy clothes for their children."
    h "My passion, one of them, is small businesses."
    h "My mother raised my sister and me but there was a woman who helped raise us. We call her our second mother. She was a small business owner."
    h "I love our small businesses."
    h "My plan is to give a $50,000 tax deduction to start-up small businesses, knowing they are part of the backbone of America's economy."
    $ harris_img = "harris attack"
    h "My opponent, on the other hand, his plan is to do what he has done before."
    h "Provide a tax cut for billionaires and big corporations, which will result in $5 trillion to America's deficit."
    h "My opponent has a plan that I call the Trump sales tax, which would be a 20%% tax on everyday goods that you rely on to get through the month."

    p "President Trump, I'll give you two minutes."

    $ trump_img = "trump attack"
    t "First of all, I have no sales tax. That's an incorrect statement. She knows that."
    t "We're doing tariffs on other countries. Other countries are going to finally, after 75 years, pay us back for all that we've done for the world."
    t "And the tariff will be substantial in some cases."
    t "I took in billions and billions of dollars, as you know, from China. In fact, they never took the tariff off because it was so much money, they can't."
    t "When I had it, I had tariffs and yet I had no inflation."
    t "Look, we've had a terrible economy because inflation has -- which is really known as a country buster. It breaks up countries."
    t "We have inflation like very few people have ever seen before. Probably the worst in our nation's history."
    t "We were at 21%%. But that's being generous because many things are 50, 60, 70, and 80%% higher than they were just a few years ago."
    t "This has been a disaster for people, for the middle class, but for every class."
    t "On top of that, we have millions of people pouring into our country from prisons and jails, from mental institutions and insane asylums."
    t "And they're coming in and they're taking jobs that are occupied right now by African Americans and Hispanics and also unions."
    t "Unions are going to be affected very soon."
    t "You see what's happening. You look at Springfield, Ohio. You look at Aurora in Colorado."
    t "They are taking over the towns. They're taking over buildings. They're going in violently."
    t "These are the people that she and Biden let into our country."
    t "And they're destroying our country. They're dangerous. They're at the highest level of criminality."
    $ trump_img = "trump smile"
    t "I created one of the greatest economies in the history of our country. I'll do it again and even better."

    p "We are going to get to immigration and border security during this debate. But I would like to let Vice President Harris respond on the economy here."

    $ harris_img = "harris attack"
    h "Well, I would love to. Let's talk about what Donald Trump left us."
    h "Donald Trump left us the worst unemployment since the Great Depression."
    h "Donald Trump left us the worst public health epidemic in a century."
    h "Donald Trump left us the worst attack on our democracy since the Civil War."
    h "And what we have done is clean up Donald Trump's mess."
    h "What we have done and what I intend to do is build on what we know are the aspirations and the hopes of the American people."
    h "But I'm going to tell you all, in this debate tonight, you're going to hear from the same old, tired playbook, a bunch of lies, grievances and name-calling."
    h "What you're going to hear tonight is a detailed and dangerous plan called Project 2025 that the former president intends on implementing if he were elected again."

    p "President Trump, I'll give you a minute here to respond."

    $ trump_img = "trump defensive"
    t "Number one, I have nothing to do, as you know and as she knows better than anyone, I have nothing to do with Project 2025."
    t "That's out there. I haven't read it. I don't want to read it, purposely. I'm not going to read it."
    t "This was a group of people that got together, they came up with some ideas. I guess some good, some bad."
    t "But it makes no difference. Everybody knows I'm an open book. Everybody knows what I'm going to do."
    $ trump_img = "trump smile"
    t "Cut taxes very substantially. And create a great economy like I did before. We had the greatest economy."
    t "We got hit with a pandemic. And not since 1917 where 100 million people died has there been anything like it."
    t "We did a phenomenal job with the pandemic."
    t "We handed them over a country where the economy and the stock market was higher than it was before the pandemic came in."
    t "Nobody's ever seen anything like it."

    jump economy_next

label economy_q2:
    $ current_question_num = economy_questions_asked + 1
    $ harris_score += 4
    $ trump_score += 8

    p "President Trump, you claim the current administration caused the worst inflation in history."
    p "But economists point to global factors, supply chain issues, and pandemic recovery."
    p "Why should voters believe you can control inflation better?"

    t "Because I did it before! I had virtually no inflation. Virtually none."
    t "We were at 21%% under them. But that's being generous. Many things are 50, 60, 70, 80%% higher than just a few years ago."
    t "People can't go out and buy cereal, bacon, or eggs. The people of our country are absolutely dying with what they've done."
    t "They've destroyed the economy and all you have to do is look at a poll."
    t "The polls say 80 and 85 and even 90%% that the Trump economy was great, that their economy was terrible."

    p "Vice President Harris, your response."

    h "Let's talk about what Donald Trump left us."
    h "Donald Trump left us the worst unemployment since the Great Depression."
    h "Donald Trump left us the worst public health epidemic in a century."
    h "And what we have done is clean up Donald Trump's mess."

    menu:
        "Challenge Vice President Harris on inflation?"

        "Challenge her":
            jump economy_q2_challenge
        "Move on":
            jump economy_next

label economy_q2_challenge:
    p "Vice President Harris, but inflation did reach 40-year highs under this administration. Families are struggling to afford groceries. How do you respond to that?"

    if renpy.random.random() > 0.5:
        jump economy_q2_fumble
    else:
        jump economy_q2_recover

label economy_q2_fumble:
    $ harris_score -= 2
    $ harris_img = "harris default"
    h "Well, we... we inherited a very difficult situation."
    h "The economy is complex and there are many factors at play..."
    h "We've been working to address it."
    jump economy_next

label economy_q2_recover:
    $ harris_score += 2
    $ harris_img = "harris attack"
    h "I'm glad you asked because let me be specific about what we've actually done."
    h "We brought inflation down from 9%% to under 3%%."
    h "We capped insulin at $35 a month for seniors. We're capping prescription costs at $2,000 a year."
    h "That's real relief."
    h "Donald Trump talks about inflation? He had four years and he didn't cap insulin. He didn't lower drug prices. We did."
    t "That's not true--"
    h "It is true."
    t "We had a plan for insulin--"
    h "You had four years."
    jump economy_next

label economy_q3:
    $ current_question_num = economy_questions_asked + 1
    $ harris_score += 7
    $ trump_score += 5

    p "I'd like both candidates to outline their specific economic plans."
    p "Vice President Harris, what exactly will you do in your first 100 days?"

    h "I am offering what I describe as an opportunity economy."
    h "And the best economists in our country, if not the world, have reviewed our relative plans."
    h "Goldman Sachs has said that Donald Trump's plan would make the economy worse. Mine would strengthen it."
    h "The Wharton School says Donald Trump's plan would explode the deficit."
    h "Sixteen Nobel laureates described his plan as something that would increase inflation."
    h "And invite a recession by the middle of next year."
    h "I have a plan for $50,000 tax deductions for startup businesses."
    h "$6,000 tax credits for young families for the first year of your child's life."
    h "$25,000 down payment assistance for first-time home buyers."
    h "And I'd invite you to know that Donald Trump actually has no plan for you."
    h "Because he is more interested in defending himself than he is in looking out for you."

    t "That's just a sound bite. They gave her that to say."
    t "Look, I went to the Wharton School of Finance."
    t "And many of those professors, the top professors, think my plan is a brilliant plan, it's a great plan."
    t "It's going to bring up our worth, our value as a country."
    t "And she doesn't have a plan. She copied Biden's plan. It's like four sentences, like run-Spot-run."

    $ harris_img = "harris laugh"
    h "{i}[[slight laugh]{/i}"
    $ harris_img = "harris default"

    $ trump_img = "trump attack"
    t "She doesn't have a plan. Take a look at her plan. She doesn't have a plan."

    menu:
        "Challenge President Trump on his lack of specifics?"

        "Challenge him":
            jump economy_q3_challenge
        "Move on":
            jump economy_next

label economy_q3_challenge:
    p "President Trump, with respect, you've said she has no plan three times now but you haven't told us yours. What specifically would you do?"

    if renpy.random.random() > 0.5:
        jump economy_q3_fumble
    else:
        jump economy_q3_recover

label economy_q3_fumble:
    $ trump_score -= 2
    $ trump_img = "trump defensive"
    t "I have concepts of a plan. I'm not president right now."
    t "But if we come up with something I would only change it if we come up with something better and less expensive."
    t "And there are concepts and options we have to do that."
    t "You'll be hearing about it in the not-too-distant future."
    p "So just a yes or no, you still do not have a plan?"
    t "I have concepts of a plan."
    jump economy_next

label economy_q3_recover:
    $ trump_score += 2
    $ trump_img = "trump attack"
    t "I'll tell you exactly what I'll do. Day one, we drill, baby, drill. Energy costs go down. When energy goes down, everything goes down."
    t "We cut regulations. We cut taxes. We bring back manufacturing from China."
    t "We did it before, greatest economy in history, and we'll do it again. Even better. Even stronger."
    h "He still hasn't said--"
    t "I just told you! Drill, cut taxes, cut regulations. It's not complicated."
    jump economy_next

label economy_next:
    $ harris_img = "harris default"
    $ trump_img = "trump default"
    $ economy_questions_asked += 1
    if economy_questions_asked < 2:
        $ followup = renpy.random.choice([
            "Thank you both. Let's continue with another question on the economy.",
            "All right, thank you. I have one more question on this topic.",
            "Thank you. I'd like to stay on the economy for one more question."
        ])
        p "[followup]"
        jump economy_menu
    return
