label immigration:
    $ immigration_questions_asked = 0
    $ immigration_q1_asked = False
    $ immigration_q2_asked = False
    $ immigration_q3_asked = False

label immigration_menu:
    menu:
        "Which question about immigration would you like to ask?"

        "\"Why did you wait to act on the border?\" (Ask Harris)" if not immigration_q1_asked:
            $ immigration_q1_asked = True
            jump immigration_q1
        "\"Why did you kill the border bill?\" (Ask Trump)" if not immigration_q2_asked:
            $ immigration_q2_asked = True
            jump immigration_q2
        "\"How would you deport millions?\" (Ask Trump)" if not immigration_q3_asked:
            $ immigration_q3_asked = True
            jump immigration_q3

label immigration_q1:
    $ current_question_num = immigration_questions_asked + 1
    $ harris_score += 4
    $ trump_score += 8

    p "Vice President Harris, you were tasked by President Biden with getting to the root causes of migration from Central America."
    p "We know that illegal border crossings reached a record high in the Biden administration."
    p "This past June, President Biden imposed tough new asylum restrictions."
    p "We know the numbers since then have dropped significantly."
    p "But my question to you tonight is why did the administration wait until six months before the election to act?"
    p "And would you have done anything differently from President Biden on this?"

    h "So I'm the only person on this stage who has prosecuted transnational criminal organizations for the trafficking of guns, drugs, and human beings."
    h "And let me say that the United States Congress, including some of the most conservative members of the United States Senate, came up with a border security bill which I supported."
    h "And that bill would have put 1,500 more border agents on the border."
    h "To help those folks who are working there right now over time trying to do their job."
    h "It would have allowed us to stem the flow of fentanyl coming into the United States."
    h "I know there are so many families watching tonight who have been personally affected by the surge of fentanyl in our country."
    h "That bill would have put more resources to allow us to prosecute transnational criminal organizations for trafficking in guns, drugs and human beings."
    h "But you know what happened to that bill?"
    h "Donald Trump got on the phone, called up some folks in Congress, and said kill the bill."
    h "And you know why? Because he preferred to run on a problem instead of fixing a problem."
    h "And I'll tell you something, he's going to talk about immigration a lot tonight even when it's not the subject that is being raised."
    h "And I'm going to actually do something really unusual."
    h "I'm going to invite you to attend one of Donald Trump's rallies."
    h "Because it's a really interesting thing to watch."
    h "You will see during the course of his rallies he talks about fictional characters like Hannibal Lecter."
    h "He will talk about windmills cause cancer."
    h "And what you will also notice is that people start leaving his rallies early out of exhaustion and boredom."
    h "And I will tell you the one thing you will not hear him talk about is you."
    h "You will not hear him talk about your needs, your dreams, your desires."
    h "And I'll tell you, I believe you deserve a president who actually puts you first. And I pledge to you that I will."

    menu:
        "Challenge Harris on the delay?"

        "Challenge her":
            jump immigration_q1_challenge
        "Let Trump respond":
            jump immigration_q1_trump

label immigration_q1_challenge:
    p "Vice President Harris, why did it take three and a half years to propose that bill? What were you doing during that time?"

    if renpy.random.random() > 0.5:
        jump immigration_q1_fumble
    else:
        jump immigration_q1_recover

label immigration_q1_fumble:
    $ harris_score -= 2
    $ harris_img = "harris default"
    h "We were working on the root causes of migration..."
    h "Immigration is a complex issue that requires comprehensive solutions..."
    t "She was the border czar. She failed."
    h "I was not the border czar--"
    t "That's what they called you! Border czar!"
    jump immigration_next

label immigration_q1_recover:
    $ harris_score += 2
    $ harris_img = "harris attack"
    h "Let me tell you what we did."
    h "We invested in Central America to address root causes. And you know what? Crossings from those countries are down."
    h "We inherited a system that Donald Trump had gutted."
    h "No immigration judges. No asylum officers. Remain in Mexico was a disaster."
    h "We rebuilt the system."
    h "And when we finally got bipartisan support for the toughest border bill in decades, Donald Trump killed it."
    h "He needs the chaos. He doesn't want solutions."
    t "That's not true--"
    h "You called Republican senators and told them to vote no."
    jump immigration_next

label immigration_q1_trump:
    t "First let me respond as to the rallies."
    t "She said people start leaving. People don't go to her rallies. There's no reason to go."
    t "And the people that do go, she's busing them in and paying them to be there."
    t "People don't leave my rallies."
    t "We have the biggest rallies, the most incredible rallies in the history of politics."
    t "That's because people want to take their country back."
    jump immigration_next

label immigration_q2:
    $ current_question_num = immigration_questions_asked + 1
    $ harris_score += 7
    $ trump_score += 5

    p "President Trump, why did you try to kill that border bill? It would have put thousands of additional agents and officers on the border."

    t "That bill was a disaster. It was a bad bill."
    t "It would have allowed millions of people to come in. Millions."
    t "They want you to think it was a border security bill. It wasn't."
    t "It was weak. It was pathetic. And I said, we can do better than that."

    $ harris_img = "harris smile"
    h "{i}[[shakes head]{/i}"
    $ harris_img = "harris default"

    $ trump_img = "trump attack"
    t "Our country is being lost. We're a failing nation."
    t "And it happened three and a half years ago when they came into office."
    t "What they have done to our country by allowing these millions and millions of people to come into our country."
    t "And look at what's happening to the towns all over the United States."
    t "And a lot of towns don't want to talk -- not going to be Aurora or Springfield."
    t "A lot of towns don't want to talk about it because they're so embarrassed by it."
    t "In Springfield, they're eating the dogs. The people that came in. They're eating the cats."

    $ harris_img = "harris default"
    h "{i}[[looks to camera]{/i}"

    $ trump_img = "trump attack"
    t "They're eating -- they're eating the pets of the people that live there."
    t "And this is what's happening in our country. And it's a shame."

    menu:
        "Fact-check the pets claim?"

        "Fact-check him":
            jump immigration_q2_challenge
        "Let Harris respond":
            jump immigration_q2_harris

label immigration_q2_challenge:
    p "I just want to clarify here. You bring up Springfield, Ohio."
    p "And ABC News did reach out to the city manager there."
    p "He told us there have been no credible reports of specific claims of pets being harmed, injured or abused by individuals within the immigrant community."

    if renpy.random.random() > 0.5:
        jump immigration_q2_fumble
    else:
        jump immigration_q2_recover

label immigration_q2_fumble:
    $ trump_score -= 2
    $ trump_img = "trump defensive"
    t "Well, I've seen people on television--"

    p "I'm not taking this from television. I'm taking it from the city manager."

    t "The people on television say my dog was taken and used for food."
    t "So maybe he said that and maybe that's a good thing to say for a city manager."

    p "But the people on television--"

    t "But the people on television say their dog was eaten by the people that went there."

    p "Again, the Springfield city manager says there's no evidence of that."

    t "We'll find out."
    jump immigration_q2_harris

label immigration_q2_recover:
    $ trump_score += 2
    $ trump_img = "trump default"
    t "Okay, maybe that particular story. But you know what's not made up? The strain on these communities is real."
    t "Schools are overwhelmed. Hospitals are overwhelmed. Resources are strained."
    t "20 million people came in illegally under their watch. That's bigger than most states."
    t "You can't do that to communities and not expect problems. The people of Springfield are struggling. That's a fact."
    jump immigration_q2_harris

label immigration_q2_harris:
    p "Vice President Harris, I'll let you respond to the rest of what you heard."

    h "Talk about extreme."
    h "You know, this is I think one of the reasons why in this election I actually have the endorsement of 200 Republicans."
    h "Republicans who have formally worked with President Bush, Mitt Romney, and John McCain."
    h "Including the endorsement of former Vice President Dick Cheney and Congressmember Liz Cheney."
    h "And if you want to really know the inside track on who the former president is, if he didn't make it clear already."
    h "Just ask people who have worked with him."
    h "His former chief of staff, a four-star general, has said he has contempt for the Constitution of the United States."
    h "His former national security adviser has said he is dangerous and unfit."
    h "His former secretary of defense has said the nation, the republic would never survive another Trump term."

    t "Yeah. When I hear that, see, I'm a different kind of a person."
    t "I fired most of those people. Not so graciously."
    t "They did bad things or a bad job. I fired them. They never fired one person."

    jump immigration_next

label immigration_q3:
    $ current_question_num = immigration_questions_asked + 1
    $ harris_score += 4
    $ trump_score += 8

    p "Let me continue on immigration. President Trump, you called this the largest domestic deportation operation in the history of our country."
    p "You say you would use the National Guard. You say if things get out of control you'd have no problem using the U.S. military."

    t "With local police."

    p "You also said you would use local police."
    p "How would you deport 11 million undocumented immigrants? I know you believe that number is much higher."
    p "Take us through this. What does this look like? Will authorities be going door to door?"

    t "Yeah. It is much higher because of them. They allowed criminals. Many, many, millions of criminals."
    t "They allowed terrorists. They allowed common street criminals. They allowed people to come in, drug dealers, to come into our country."
    t "And told by their countries like Venezuela don't ever come back or we're going to kill you."
    t "Do you know that crime in Venezuela and crime in countries all over the world is way down?"
    t "You know why? Because they've taken their criminals off the street and they've given them to her to put into our country."
    t "And this will be one of the greatest mistakes in history for them to allow."
    t "And I think they probably did it because they think they're going to get votes."
    t "But it's not worth it. Because they're destroying the fabric of our country."
    t "Millions of people let in. And all over the world crime is down. All over the world except here."
    t "Crime here is up and through the roof. Despite their fraudulent statements that they made."
    t "We have a new form of crime. It's called migrant crime. And it's happening at levels that nobody thought possible."

    menu:
        "Fact-check the crime statistics?"

        "Fact-check him":
            jump immigration_q3_challenge
        "Let Harris respond":
            jump immigration_q3_harris

label immigration_q3_challenge:
    p "President Trump, as you know, the FBI says overall violent crime is coming down in this country."

    if renpy.random.random() > 0.5:
        jump immigration_q3_fumble
    else:
        jump immigration_q3_recover

label immigration_q3_fumble:
    $ trump_score -= 2
    $ trump_img = "trump defensive"
    t "Excuse me, the FBI -- they were defrauding statements."
    t "They didn't include the worst cities. They didn't include the cities with the worst crime."
    t "It was a fraud."
    t "Just like their number of 818,000 jobs that they said they created turned out to be a fraud."
    p "So you're saying the FBI statistics are fraudulent?"
    t "They're defrauding the public! The FBI is corrupt!"
    jump immigration_q3_harris

label immigration_q3_recover:
    $ trump_score += 2
    $ trump_img = "trump attack"
    t "The FBI changed their methodology. They're not counting all the cities anymore."
    t "But I'll tell you what, talk to any police officer in this country. Talk to any sheriff."
    t "They'll tell you what they're dealing with. Venezuelan gangs. MS-13. Cartels."
    t "We're going to deport the criminals first. The gang members. The drug dealers. Nobody can argue with that."
    p "And after the criminals?"
    t "Then we go after the rest. We have to have a country. We have to have borders."
    jump immigration_q3_harris

label immigration_q3_harris:
    p "Vice President Harris, your response."

    h "Well, I think this is so rich coming from someone who has been prosecuted for national security crimes, economic crimes, election interference."
    h "Has been found liable for sexual assault."
    h "And his next big court appearance is in November at his own criminal sentencing."
    h "So let's be clear about where each person stands on the issue of respect for the rule of law."
    h "The former president called for defunding federal law enforcement, 45,000 agents, on the day after he was arraigned on 34 felony counts."

    t "Excuse me. Every one of those cases was started by them against their political opponent."
    t "And I'm winning most of them and I'll win the rest on appeal."
    t "And you saw that with the decision that came down just recently from the Supreme Court."

    h "Let's talk about what is important in this race."

    t "It's called weaponization. Never happened in this country."

    h "Frankly, the American people are exhausted with the same old tired playbook."

    jump immigration_next

label immigration_next:
    $ harris_img = "harris default"
    $ trump_img = "trump default"
    $ immigration_questions_asked += 1
    if immigration_questions_asked < 2:
        $ followup = renpy.random.choice([
            "Thank you both. Let's continue with another question on immigration.",
            "All right, thank you. I have one more question on this topic.",
            "Thank you. I'd like to stay on immigration for one more question."
        ])
        p "[followup]"
        jump immigration_menu
    return
