label january6:
    $ january6_questions_asked = 0
    $ january6_q1_asked = False
    $ january6_q2_asked = False
    $ january6_q3_asked = False

label january6_menu:
    menu:
        "Which question about democracy would you like to ask?"

        "\"Do you have any regrets about January 6th?\" (Ask Trump)" if not january6_q1_asked:
            $ january6_q1_asked = True
            jump january6_q1
        "\"Do you accept you lost in 2020?\" (Ask Trump)" if not january6_q2_asked:
            $ january6_q2_asked = True
            jump january6_q2
        "\"What's the greatest threat to democracy?\" (Ask Both)" if not january6_q3_asked:
            $ january6_q3_asked = True
            jump january6_q3

label january6_q1:
    $ current_question_num = january6_questions_asked + 1
    $ harris_score += 8
    $ trump_score += 4

    p "We have an election in just 56 days."
    p "I want to talk about the peaceful transfer of power, which of course we all know is a cornerstone of our democracy."
    p "And the role of a president in a moment of crisis."
    p "Mr. President, on January 6th you told your supporters to march to the Capitol."
    p "You said you would be right there with them."
    p "The country and the world saw what played out at the Capitol that day."
    p "The officers coming under attack."
    p "Aides in the West Wing say you watched it unfold on television off the Oval Office."
    p "You did send out tweets, but it was more than two hours before you sent out that video message telling your supporters to go home."
    p "Is there anything you regret about what you did on that day?"

    t "You just said a thing that isn't covered."
    t "Peacefully and patriotically, I said during my speech. Not later on. Peacefully and patriotically."
    t "And nobody on the other side was killed."
    t "Ashli Babbitt was shot by an out-of-control police officer that should have never, ever shot her. It's a disgrace."
    t "But we didn't do this. This group of people that have been treated so badly."
    t "I ask, what about all the people that are pouring into our country and killing people?"
    t "That she allowed to pour in."
    t "She was the border czar. Remember that."
    t "She was the border czar. She doesn't want to be called the border czar because she's embarrassed by the border."
    t "What about those people? When are they going to be prosecuted?"
    t "When are the people that burned down Minneapolis going to be prosecuted? Or in Seattle?"
    t "They went into Seattle, they took over a big percentage of the city of Seattle."
    t "When are those people going to be prosecuted?"

    menu:
        "Press for a direct answer?"

        "Press him":
            jump january6_q1_challenge
        "Let Harris respond":
            jump january6_q1_harris

label january6_q1_challenge:
    p "But let me just ask you--"

    t "But when are those people going to be prosecuted?"

    p "But let me just ask you-- You were the president. You were watching it unfold on television."
    p "It's a very simple question as we move forward toward another election."
    p "Is there anything you regret about what you did on that day? Yes or no."

    if renpy.random.random() > 0.5:
        jump january6_q1_fumble
    else:
        jump january6_q1_recover

label january6_q1_fumble:
    $ trump_score -= 2
    $ trump_img = "trump defensive"
    t "I had nothing to do with that other than they asked me to make a speech."
    t "I showed up for a speech."
    t "I went to Nancy Pelosi and the mayor of Washington, D.C."
    t "And the mayor put it back in writing, as you know."
    t "I said I'd like to give you 10,000 National Guard or soldiers. They rejected me."
    t "Nancy Pelosi rejected me."
    t "It was just two weeks ago, her daughter has a tape of her saying she is fully responsible for what happened."
    t "It would have never happened if Nancy Pelosi and the mayor of Washington did their jobs."
    t "I wasn't responsible for security. Nancy Pelosi was responsible."

    p "The question was about you as president, not about Former Speaker Pelosi."
    jump january6_q1_harris

label january6_q1_recover:
    $ trump_score += 2
    $ trump_img = "trump default"
    t "Look. Do I wish it hadn't gotten out of control? Of course I do."
    t "I told them to go home. I wanted a peaceful protest. I said peacefully and patriotically in my speech."
    t "But I'll tell you what I regret. I regret that nobody talks about the violence from the other side."
    t "The double standard is what the American people are really upset about."
    jump january6_q1_harris

label january6_q1_harris:
    p "Vice President Harris, I want to get your response here."

    h "I was at the Capitol on January 6th."
    h "I was the Vice President-Elect. I was also an acting senator. I was there."
    h "And on that day, the president of the United States incited a violent mob to attack our nation's Capitol."
    h "To desecrate our nation's Capitol."
    h "On that day, 140 law enforcement officers were injured. And some died."
    h "And understand, the former president has been indicted and impeached for exactly that reason."
    h "But this is not an isolated situation."
    h "Let's remember Charlottesville, where there was a mob of people carrying tiki torches, spewing antisemitic hate."
    h "And what did the president then at the time say? There were fine people on each side."
    h "Let's remember that when it came to the Proud Boys, a militia, the president said, the former president said, \"Stand back and stand by.\""
    h "So for everyone watching who remembers what January 6th was, I say we don't have to go back."
    h "Let's not go back. We're not going back."
    h "It's time to turn the page."
    h "And if that was a bridge too far for you, well, there is a place in our campaign for you."
    h "To stand for country. To stand for our democracy. To end the chaos."

    t "I have to respond to that. I have to respond."
    t "I have said bloodbath. It was a different term, and it was a term that related to energy."
    t "Because they have destroyed our energy business. That was where bloodbath was."
    t "Also, on Charlottesville, that story has been, as you would say, debunked."
    t "Laura Ingraham, Sean Hannity, Jesse, all of these people, they covered it."
    t "If they go an extra sentence, they will see it was perfect. It was debunked in almost every newspaper."

    p "Mr. President--"

    t "But they still bring it up just like they bring 2025 up."

    jump january6_next

label january6_q2:
    $ current_question_num = january6_questions_asked + 1
    $ harris_score += 8
    $ trump_score += 3

    p "Mr. President, for three and a half years after you lost the 2020 election you repeatedly falsely claimed that you won."
    p "Many times saying you won in a landslide."
    p "In the past couple of weeks leading up to this debate, you have said, quote, you lost by a whisker."
    p "That you, quote, didn't quite make it, that you came up a little bit short."

    t "I said that?"

    p "Are you now acknowledging that you lost in 2020?"

    t "No, I don't acknowledge that at all."

    p "But you did say that."

    t "I said that sarcastically. You know that."
    t "It was said, oh we lost by a whisker. That was said sarcastically."
    t "Look, there's so much proof. All you have to do is look at it."
    t "And they should have sent it back to the legislatures for approval."
    t "I got almost 75 million votes. The most votes any sitting president has ever gotten."
    t "Our elections are bad."
    t "And a lot of these illegal immigrants coming in, they're trying to get them to vote."
    t "They can't even speak English. They don't even know what country they're in practically."

    menu:
        "Challenge him on the court cases?"

        "Challenge him":
            jump january6_q2_challenge
        "Let Harris respond":
            jump january6_q2_harris

label january6_q2_challenge:
    p "I did watch all of these pieces of video. I didn't detect the sarcasm."
    p "You and your allies, 60 cases in front of many judges. Many of them appointed by you."

    t "No judge looked at it."

    p "And said there was no widespread fraud."

    if renpy.random.random() > 0.5:
        jump january6_q2_fumble
    else:
        jump january6_q2_recover

label january6_q2_fumble:
    $ trump_score -= 2
    $ trump_img = "trump defensive"
    t "They said we didn't have standing. That's the other thing."
    t "They said we didn't have standing. A technicality."
    t "Can you imagine a system where a person in an election doesn't have standing?"
    t "The President of the United States doesn't have standing? That's how we lost."
    t "If you look at the facts, and I'd love to have you, you'll do a special on it."
    t "I'll show you Georgia and I'll show you Wisconsin and I'll show you Pennsylvania."
    t "We have so many facts and statistics."
    p "60 judges, including judges you appointed, found no evidence of fraud."
    t "They didn't look at the evidence!"
    jump january6_q2_harris

label january6_q2_recover:
    $ trump_score += 2
    $ trump_img = "trump default"
    t "You know what? That doesn't matter. That's old news."
    t "The problem that we have right now is we have a nation in decline."
    t "And they have put it into decline."
    t "We have a nation that is dying. Let's focus on fixing it. Let's focus on the future."
    t "The American people want to talk about inflation, about the border, about crime."
    t "Not about 2020."
    jump january6_q2_harris

label january6_q2_harris:
    p "Vice President Harris, your response."

    h "Donald Trump was fired by 81 million people."
    h "So let's be clear about that."
    h "And clearly, he is having a very difficult time processing that."
    h "But we cannot afford to have a president of the United States who attempts, as he did in the past, to upend the will of the voters in a free and fair election."
    h "And I'm going to tell you that I have traveled the world as vice president."
    h "And world leaders are laughing at Donald Trump."
    h "I have talked with military leaders, some of whom worked with you."
    h "And they say you're a disgrace."
    h "And when you then talk in this way in a presidential debate and deny what over and over again are court cases you have lost..."
    h "because you did in fact lose that election."
    h "It leads one to believe that perhaps we do not have the temperament or the ability to not be confused about fact."
    h "That's deeply troubling. And the American people deserve better."

    jump january6_next

label january6_q3:
    $ current_question_num = january6_questions_asked + 1
    $ harris_score += 6
    $ trump_score += 6

    p "Vice President Harris, President Trump has said:"
    p "\"When I win, those people who cheated will be prosecuted to the fullest extent of the law, including long-term prison sentences.\""
    p "Your campaign says this is voter intimidation. Is that what you believe?"

    h "Let's talk about extreme."
    h "And understand the context in which this election in 2024 is taking place."
    h "The United States Supreme Court recently ruled that the former president would essentially be immune from any misconduct if he were to enter the White House again."
    h "Understand, this is someone who has openly said he would terminate, I'm quoting, terminate the Constitution of the United States."
    h "That he would weaponize the Department of Justice against his political enemies."
    h "Someone who has openly expressed disdain for members of our military."
    h "Understand what it would mean if Donald Trump were back in the White House with no guardrails."
    h "Because certainly, we know now the court won't stop him."
    h "We know JD Vance is not going to stop him."
    h "It's up to the American people to stop him."

    t "This is the one that weaponized. Not me. She weaponized."
    t "I probably took a bullet to the head because of the things that they say about me."
    t "They talk about democracy. I'm a threat to democracy."
    t "They're the threat to democracy."
    t "With the fake Russia Russia Russia investigation that went nowhere."

    p "We have a lot to get to."

    jump january6_next

label january6_next:
    $ harris_img = "harris default"
    $ trump_img = "trump default"
    $ january6_questions_asked += 1
    if january6_questions_asked < 2:
        $ followup = renpy.random.choice([
            "Thank you both. Let's continue with another question on this topic.",
            "All right, thank you. I have one more question about democracy.",
            "Thank you. I'd like to stay on this topic for one more question."
        ])
        p "[followup]"
        jump january6_menu
    return
