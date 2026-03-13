label tariffs:
    $ tariffs_questions_asked = 0
    $ tariffs_q1_asked = False
    $ tariffs_q2_asked = False
    $ tariffs_q3_asked = False

label tariffs_menu:
    menu:
        "Which question about trade would you like to ask?"

        "\"Will tariffs raise consumer prices?\" (Ask Trump)" if not tariffs_q1_asked:
            $ tariffs_q1_asked = True
            jump tariffs_q1
        "\"How will you handle China?\" (Ask Both)" if not tariffs_q2_asked:
            $ tariffs_q2_asked = True
            jump tariffs_q2
        "\"What about the trade deficit?\" (Ask Harris)" if not tariffs_q3_asked:
            $ tariffs_q3_asked = True
            jump tariffs_q3

label tariffs_q1:
    $ current_question_num = tariffs_questions_asked + 1
    $ harris_score += 6
    $ trump_score += 5

    p "Mr. President, I do want to drill down on something you both brought up."
    p "The vice president mentioned your tariffs and you responded."
    p "Your proposal calls for tariffs on foreign imports across the board."
    p "You recently said you might impose tariffs up to 20%% on goods coming into this country."
    p "As you know, many economists say that with tariffs at that level costs are then passed onto the consumer."
    p "Vice President Harris has argued it will mean higher prices on gas, food, clothing, medication."
    p "Costing families nearly four thousand dollars a year."
    p "Do you believe Americans can afford higher prices because of tariffs?"

    t "They aren't gonna have higher prices. What's gonna have higher prices is China!"
    t "And all of the countries that have been ripping us off for years."
    t "I charge, I was the only president ever, China was paying us hundreds of billions of dollars and so were other countries."
    t "And you know, if she doesn't like them, they should have gone out and they should have immediately cut the tariffs."
    t "But those tariffs are there three and a half years now under their administration."
    t "We are gonna take in billions of dollars, hundreds of billions of dollars. I had no inflation, virtually no inflation."
    t "They had the highest inflation, perhaps in the history of our country because I've never seen a worse period of time."
    t "People can't go out and buy cereal, bacon, or eggs or anything else."
    t "The people of our country are absolutely dying with what they've done."

    menu:
        "Challenge President Trump on how tariffs work?"

        "Challenge him":
            jump tariffs_q1_challenge
        "Let Vice President Harris respond":
            jump tariffs_q1_harris

label tariffs_q1_challenge:
    p "But economists say tariffs are paid by American importers, not foreign countries. Those costs get passed to consumers. How do you respond?"

    if renpy.random.random() > 0.5:
        jump tariffs_q1_fumble
    else:
        jump tariffs_q1_recover

label tariffs_q1_fumble:
    $ trump_score -= 2
    $ trump_img = "trump defensive"
    t "The economists, they don't know what they're talking about. They're wrong. They're all wrong."
    t "Look, I know more about tariffs than anybody. I went to Wharton. Believe me."
    t "We'll have the best tariffs. The best. China will pay."
    $ harris_img = "harris laugh"
    h "{i}[[laughs]{/i}"
    $ trump_img = "trump attack"
    t "She thinks that's funny. It's not funny."
    jump tariffs_q1_harris

label tariffs_q1_recover:
    $ trump_score += 2
    $ trump_img = "trump default"
    t "Let me explain something. Let me explain how this works."
    t "When we put tariffs on China, they devalue their currency to offset it. So they're paying for it."
    t "And what happens? American companies bring manufacturing back home. That creates jobs. Creates competition. Prices come down."
    t "We had tariffs. We had no inflation. That's a fact. That's not a theory. We did it."
    jump tariffs_q1_harris

label tariffs_q1_harris:
    p "Vice President Harris, I do want to ask for your response."
    p "You heard what the president said there because the Biden administration did keep a number of the Trump tariffs in place. How do you respond?"

    h "Well, let's be clear that the Trump administration resulted in a trade deficit."
    h "One of the highest we've ever seen in the history of America."
    h "He invited trade wars."
    h "You wanna talk about his deal with China?"
    h "What he ended up doing is under Donald Trump's presidency he ended up selling American chips to China to help them improve and modernize their military."
    h "Basically sold us out."
    h "A policy about China should be about making sure the United States of America wins the competition for the 21st century."
    h "Which means focusing on relationships with our allies."
    h "Focusing on investing in American-based technology so that we win the race on AI and quantum computing."

    jump tariffs_next

label tariffs_q2:
    $ current_question_num = tariffs_questions_asked + 1
    $ harris_score += 4
    $ trump_score += 8

    p "Both candidates have taken tough stances on China."
    p "President Trump, you imposed tariffs. Vice President Harris, the Biden administration kept many of them."
    p "What would each of you do differently going forward?"

    t "First of all, they bought their chips from Taiwan."
    t "We hardly make chips anymore because of philosophies like they have and policies like they have."
    t "I don't say her because she has no policy."
    t "Everything that she believed three years ago and four years ago is out the window."
    t "She's going to my philosophy now. In fact, I was going to send her a MAGA hat."

    $ harris_img = "harris laugh"
    h "{i}[[laughs]{/i}"
    $ harris_img = "harris default"

    $ trump_img = "trump default"
    t "She's gone to my philosophy. But if she ever got elected, she'd change it."
    t "And it will be the end of our country."
    t "She's a Marxist. Everybody knows she's a Marxist."
    t "Her father's a Marxist professor in economics. And he taught her well."

    p "Vice President Harris?"

    $ harris_img = "harris smile"
    h "Okay. {i}[[still amused]{/i}"
    $ harris_img = "harris default"
    h "What we need to focus on is investing in American-based technology so that we win the race on AI and quantum computing."
    h "Focusing on relationships with our allies."
    h "Focusing on supporting America's workforce so that we don't end up on the short end in terms of workers' rights."
    h "But what Donald Trump did, let's talk about this with COVID."
    h "He actually thanked President Xi for what he did during COVID. Look at his tweet."
    h "\"Thank you, President Xi,\" exclamation point."
    h "When we know that Xi was responsible for lacking and not giving us transparency about the origins of COVID."

    t "First of all, they bought their chips from Taiwan. We hardly make chips anymore--"

    p "You said that, Mr. President."

    t "Because of policies like they have. I don't say her because she has no policy."
    t "And look at what she's done to our country."
    t "Millions and millions of people, I believe 21 million people, not the 15 that people say."
    t "That's bigger than New York state. Pouring in."
    t "And just look at what they're doing to our country. They're criminals. Many of these people coming in are criminals."
    t "And that's bad for our economy too."

    p "President Trump, we're going to get to immigration later--"

    t "Bad immigration is the worst thing that can happen to our economy."
    t "They have and she has destroyed our country with policy that's insane."
    t "Almost policy that you'd say they have to hate our country."

    menu:
        "Challenge Vice President Harris on her China policy?"

        "Challenge her":
            jump tariffs_q2_challenge
        "Move on":
            jump tariffs_next

label tariffs_q2_challenge:
    p "Vice President Harris, but the Biden administration also continued engagement with China on climate and trade."
    p "How is your approach substantively different from President Trump's?"

    if renpy.random.random() > 0.5:
        jump tariffs_q2_fumble
    else:
        jump tariffs_q2_recover

label tariffs_q2_fumble:
    $ harris_score -= 2
    $ harris_img = "harris default"
    h "Well, our approach is... we believe in diplomacy."
    h "We believe in working with our allies while also being tough."
    h "It's a different approach."
    t "She can't answer the question."
    jump tariffs_next

label tariffs_q2_recover:
    $ harris_score += 2
    $ harris_img = "harris attack"
    h "Here's the difference."
    h "Donald Trump started trade wars that hurt American farmers and manufacturers."
    h "We kept strategic tariffs but we also invested $280 billion in American semiconductors through the CHIPS Act."
    h "We're bringing chip manufacturing back home. Creating jobs here. That's how you compete with China."
    t "We had the chips--"
    h "Not with tweets and tantrums. With actual investment."
    t "The chips were going to Taiwan--"
    p "Mr. President, her time."
    jump tariffs_next

label tariffs_q3:
    $ current_question_num = tariffs_questions_asked + 1
    $ harris_score += 5
    $ trump_score += 7

    p "Vice President Harris, the trade deficit has remained high under this administration."
    p "What have you done to bring manufacturing jobs back to America?"

    h "Let's be clear about what we've accomplished."
    h "We passed the CHIPS Act, investing in American semiconductor manufacturing."
    h "We passed the Inflation Reduction Act, creating over 800,000 new manufacturing jobs."
    h "We're opening factories across the country."
    h "Donald Trump promised manufacturing jobs. He lost manufacturing jobs."
    h "We've had the largest increase in domestic manufacturing investment in decades."
    h "I'm also proud to have the endorsement of the United Auto Workers and Shawn Fain."
    h "They know that part of building a clean energy economy includes investing in American-made products, American automobiles."
    h "It includes growing what we can do around American manufacturing."
    h "Opening up auto plants, not closing them like what happened under Donald Trump."

    t "That didn't happen under Donald Trump."
    t "Let me just tell you, they lost 10,000 manufacturing jobs this last month. It's going -- they're all leaving."
    t "They're building big auto plants in Mexico. In many cases owned by China."
    t "They're building these massive plants, and they think they're going to sell their cars into the United States because of these people."
    t "What they have given to China is unbelievable. But we're not going to let that happen."
    t "We'll put tariffs on those cars so they can't come into our country."
    t "Because they will kill the United Auto Workers and any auto worker, whether it's in Detroit or South Carolina or any other place."
    t "What they've done to manufacturing is horrible."

    p "President Trump--"

    t "And we're going to fix it. We're going to fix it fast."

    jump tariffs_next

label tariffs_next:
    $ harris_img = "harris default"
    $ trump_img = "trump default"
    $ tariffs_questions_asked += 1
    if tariffs_questions_asked < 2:
        $ followup = renpy.random.choice([
            "Thank you both. Let's continue with another question on trade.",
            "All right, thank you. I have one more question on this topic.",
            "Thank you. I'd like to stay on trade for one more question."
        ])
        p "[followup]"
        jump tariffs_menu
    return
