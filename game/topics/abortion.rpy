label abortion:
    $ abortion_questions_asked = 0
    $ abortion_q1_asked = False
    $ abortion_q2_asked = False
    $ abortion_q3_asked = False

label abortion_menu:
    menu:
        "Which question about abortion would you like to ask?"

        "\"Why should women trust you?\" (Ask Trump)" if not abortion_q1_asked:
            $ abortion_q1_asked = True
            jump abortion_q1
        "\"Would you support any restrictions?\" (Ask Harris)" if not abortion_q2_asked:
            $ abortion_q2_asked = True
            jump abortion_q2
        "\"Would you veto a national ban?\" (Ask Trump)" if not abortion_q3_asked:
            $ abortion_q3_asked = True
            jump abortion_q3

label abortion_q1:
    $ current_question_num = abortion_questions_asked + 1
    $ harris_score += 9
    $ trump_score += 3

    p "President Trump, you've often touted that you were able to kill Roe v. Wade."
    p "Last year, you said that you were proud to be the most pro-life president in American history."
    p "Then last month you said that your administration would be great for women and their reproductive rights."
    p "In your home state of Florida, you surprised many with regard to the six-week abortion ban."
    p "You initially said it was too short and then the very next day you reversed course and said you would vote to support the six-week ban."
    p "Vice President Harris says women shouldn't trust you on the issue of abortion because you've changed your position so many times."
    p "Why should they trust you?"

    t "Well, the reason I'm doing that vote is because the plan is, as you know, the vote is, they have abortion in the ninth month."
    t "They even have, and you can look at the governor of West Virginia, the previous governor of West Virginia, not the current governor who's doing an excellent job, but the governor before."
    t "He said the baby will be born and we will decide what to do with the baby. In other words, we'll execute the baby."

    h "That's not what anybody--"

    t "And that's why I did that, because that predominates. Because they're radical."
    t "The Democrats are radical in that."
    t "And her vice presidential pick, which I think was a horrible pick, by the way, for our country, because he is really out of it."
    t "But her vice presidential pick says abortion in the ninth month is absolutely fine."
    t "He also says execution after birth, it's execution, no longer abortion, because the baby is born, is okay."
    t "And that's not okay with me. Hence the vote."
    t "But what I did is something for 52 years they've been trying to get Roe v. Wade into the states."
    t "And through the genius and heart and strength of six Supreme Court justices we were able to do that."
    t "Now, I believe in the exceptions for rape, incest and life of the mother. I believe strongly in it."
    t "Ronald Reagan did also. 85%% of Republicans do."
    t "But we were able to get it. And now states are voting."
    t "For the first time you're going to see, look, this is an issue that's torn our country apart for 52 years."
    t "Every legal scholar, every Democrat, every Republican, liberal, conservative, they all wanted this issue to be brought back to the states where the people could vote."
    t "And that's what happened. And now states are voting."

    menu:
        "Fact-check Trump's claim about post-birth abortion?"

        "Fact-check him":
            jump abortion_q1_challenge
        "Let Harris respond":
            jump abortion_q1_harris_response

label abortion_q1_challenge:
    p "There is no state in this country where it is legal to kill a baby after it's born."
    p "Madam Vice President, I want to get your response to President Trump."

    t "Well, I don't think so--"

    p "President Trump, thank you."

    if renpy.random.random() > 0.5:
        jump abortion_q1_fumble
    else:
        jump abortion_q1_recover

label abortion_q1_fumble:
    $ trump_score -= 2
    $ trump_img = "trump defensive"
    jump abortion_q1_harris_response

label abortion_q1_recover:
    $ trump_score += 2
    $ trump_img = "trump attack"
    t "Wait a minute. Wait a minute. Let me respond to that."
    t "She's lying again. I believe in the three exceptions. Rape, incest, life of the mother. I've said it a hundred times."
    t "And what I did is give it back to the people. The people are voting now. Ohio voted. Kansas voted. That's democracy."
    t "She wants the federal government to control everything. I gave it to the states. That's what people wanted for 52 years."
    h "Women are bleeding out in parking lots--"
    t "That's a state issue. And the states are going to figure it out."
    jump abortion_next

label abortion_q1_harris_response:
    h "Well, as I said, you're going to hear a bunch of lies."
    h "And that's not actually a surprising fact."
    h "Let's understand how we got here."
    h "Donald Trump hand-selected three members of the United States Supreme Court with the intention that they would undo the protections of Roe v. Wade."
    h "And they did exactly as he intended."
    h "And now in over 20 states there are Trump abortion bans which make it criminal for a doctor or nurse to provide health care."
    h "In one state it provides prison for life."
    h "Trump abortion bans that make no exception even for rape and incest."
    h "Which understand what that means."
    h "A survivor of a crime, a violation to their body, does not have the right to make a decision about what happens to their body next."
    h "That is immoral."
    h "And one does not have to abandon their faith or deeply held beliefs to agree the government should not be telling a woman what to do with her body."
    h "And Donald Trump certainly should not be telling a woman what to do with her body."
    h "I have talked with women around our country."
    h "Pregnant women who want to carry a pregnancy to term suffering from a miscarriage."
    h "Being denied care in an emergency room because the health care providers are afraid they might go to jail."
    h "And she's bleeding out in a car in the parking lot."
    h "She didn't want that. Her husband didn't want that."
    h "A 12 or 13-year-old survivor of incest being forced to carry a pregnancy to term? They don't want that."
    h "And I pledge to you, when Congress passes a bill to put back in place the protections of Roe v. Wade, as president of the United States, I will proudly sign it into law."
    jump abortion_next

label abortion_q2:
    $ current_question_num = abortion_questions_asked + 1
    $ harris_score += 6
    $ trump_score += 6

    p "Vice President Harris, I want to give you your time to respond."
    p "But I do want to ask, would you support any restrictions on a woman's right to an abortion?"

    h "I absolutely support reinstating the protections of Roe v. Wade."
    h "And as you rightly mentioned, nowhere in America is a woman carrying a pregnancy to term and asking for an abortion."
    h "That is not happening. It's insulting to the women of America."
    h "And understand what has been happening under Donald Trump's abortion bans."
    h "Couples who pray and dream of having a family are being denied IVF treatments."
    h "What is happening in our country, working people, working women who are working one or two jobs, who can barely afford childcare as it is."
    h "They have to travel to another state to get on a plane sitting next to strangers, to go and get the health care she needs."
    h "And what you are putting her through is unconscionable."
    h "And the people of America have not, the majority of Americans believe in a woman's right to make decisions about her own body."
    h "And that is why in every state where this issue has been on the ballot, in red and blue states both, the people of America have voted for freedom."

    t "Excuse me, I have to respond."

    p "Vice President Harris--"

    t "Another lie. It's another lie."
    t "I have been a leader on IVF which is fertilization. The IVF -- I have been a leader."
    t "In fact, when they got a very negative decision on IVF from the Alabama courts, I saw the people of Alabama."
    t "And the legislature two days later voted it in."
    t "I've been a leader on it. They know that and everybody else knows it. I have been a leader on fertilization, IVF."
    t "And the other thing, they -- you should ask, will she allow abortion in the eighth month, ninth month, seventh month?"

    h "Come on."

    t "Would you do that? Why don't you ask her that question--"

    h "Why don't you answer the question would you veto--"

    t "That's the problem. Because under Roe v. Wade."

    h "Answer the question, would you veto--"

    t "You could do abortions in the seventh month, the eighth month, the ninth month--"

    h "That's not true."

    t "And probably after birth."
    t "Just look at the governor, former governor of Virginia."
    t "The governor of Virginia said we put the baby aside and then we determine what we want to do with the baby."

    p "President Trump, thank you."

    menu:
        "Press Harris on specific limits?"

        "Challenge her":
            jump abortion_q2_challenge
        "Move on":
            jump abortion_next

label abortion_q2_challenge:
    p "Vice President Harris, should there be any limit on abortion? 15 weeks? 20 weeks? Where do you draw the line?"

    if renpy.random.random() > 0.5:
        jump abortion_q2_fumble
    else:
        jump abortion_q2_recover

label abortion_q2_fumble:
    $ harris_score -= 2
    $ harris_img = "harris default"
    h "I believe in the protections of Roe v. Wade."
    h "The government shouldn't be making these decisions. Doctors and patients should."
    t "She won't answer! She won't answer because she's radical."
    jump abortion_next

label abortion_q2_recover:
    $ harris_score += 2
    $ harris_img = "harris attack"
    h "Let me be clear. Roe v. Wade had a framework that worked for 50 years."
    h "It allowed states to restrict abortion after viability, with exceptions for the life and health of the mother."
    h "That's the standard that doctors, patients, and families understood and relied upon."
    h "What we have now is chaos. Women bleeding out in parking lots. That's not pro-life. That's pro-cruelty."
    t "She still won't say--"
    h "I just told you. Viability, with exceptions. That's what Roe said. That's what I support."
    jump abortion_next

label abortion_q3:
    $ current_question_num = abortion_questions_asked + 1
    $ harris_score += 9
    $ trump_score += 2

    p "President Trump, would you veto a national abortion ban if it came to your desk?"

    t "Well, I won't have to because again -- two things."
    t "Number one, she said she'll go back to Congress. She'll never get the vote. It's impossible for her to get the vote."
    t "Especially now with a 50-50 -- essentially 50-50 in both Senate and the House."
    t "She's not going to get the vote. She can't get the vote. She won't even come close to it. So it's just talk."
    t "You know what it reminds me of?"
    t "When they said they're going to get student loans terminated and it ended up being a total catastrophe."
    t "The student loans -- and then her, I think probably her boss, if you call him a boss, he spends all his time on the beach."
    t "But look, her boss went out and said we'll do it again, we'll do it a different way."
    t "He went out, got rejected again by the Supreme Court."
    t "So all these students got taunted with this whole thing about this whole idea. Same thing with abortion."

    menu:
        "Press for a yes or no answer?"

        "Press him":
            jump abortion_q3_challenge
        "Let Harris respond":
            jump abortion_q3_harris

label abortion_q3_challenge:
    p "But if I could just get a yes or no. Because your running mate JD Vance has said that you would veto if it did come to your desk."

    if renpy.random.random() > 0.5:
        jump abortion_q3_fumble
    else:
        jump abortion_q3_recover

label abortion_q3_fumble:
    $ trump_score -= 2
    $ trump_img = "trump defensive"
    t "Well, I didn't discuss it with JD. In all fairness."
    t "JD -- And I don't mind if he has a certain view but I think he was speaking for me but I really didn't."
    t "Look, we don't have to discuss it because she'd never be able to get it, just like she couldn't get student loans."
    t "They didn't even come close to getting student loans."
    t "They taunted young people and a lot of other people that had loans. They can never get this approved."
    t "So it doesn't matter what she says about going to Congress. Wonderful. Let's go to Congress. Do it."
    p "So you won't say yes or no on the veto?"
    t "I told you. It doesn't matter. It'll never come to my desk."
    jump abortion_q3_harris

label abortion_q3_recover:
    $ trump_score += 2
    $ trump_img = "trump attack"
    t "Look. Let me be clear. I would not sign a national ban. I've said it before. I'm saying it again."
    t "We worked hard to give this to the states. I'm not going to take it away from the states. That's what we fought for."
    h "He won't commit--"
    t "I just committed! I just said it! No national ban. What part don't you understand?"
    jump abortion_q3_harris

label abortion_q3_harris:
    h "Understand, if Donald Trump were to be re-elected, he will sign a national abortion ban."
    h "Understand in his Project 2025 there would be a national abortion monitor."
    h "That would be monitoring your pregnancies, your miscarriages."
    h "I think the American people believe that certain freedoms, in particular the freedom to make decisions about one's own body, should not be made by the government."

    t "Well, there she goes again. It's a lie."
    t "I'm not signing a ban. And there's no reason to sign a ban."
    t "Because we've gotten what everybody wanted."
    t "Democrats, Republicans and everybody else and every legal scholar wanted it to be brought back into the states."
    t "And the states are voting."

    jump abortion_next

label abortion_next:
    $ harris_img = "harris default"
    $ trump_img = "trump default"
    $ abortion_questions_asked += 1
    if abortion_questions_asked < 2:
        $ followup = renpy.random.choice([
            "Thank you both. Let's continue with another question on this topic.",
            "All right, thank you. I have one more question about reproductive rights.",
            "Thank you. I'd like to stay on this topic for one more question."
        ])
        p "[followup]"
        jump abortion_menu
    return
