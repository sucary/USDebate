# Ending sequence - closing statements, transition, and winner announcement

label ending_sequence:
    # Closing statements
    $ harris_img = "harris default"
    $ trump_img = "trump default"

    p "The time has come for closing statements."
    p "Each candidate will have two minutes. Vice President Harris, we begin with you."

    $ harris_img = "harris smile"
    h "So I think you've heard tonight two very different visions for our country."
    h "One that is focused on the future and the other that is focused on the past. And an attempt to take us backward."
    h "But we're not going back."
    h "And I do believe that the American people know we all have so much more in common than what separates us."
    h "And we can chart a new way forward. And a vision of that includes having a plan, understanding the aspirations, the dreams, the hopes, the ambition of the American people."
    h "Which is why I intend to create an opportunity economy, investing in small businesses, in new families, in what we can do around protecting seniors."
    h "I believe in what we can do together that is about sustaining America's standing in the world."
    h "And ensuring we have the respect that we so rightly deserve including respecting our military."
    h "I will be a president that will protect our fundamental rights and freedoms including the right of a woman to make decisions about her own body."
    h "I started my career as a prosecutor. I was a D.A. I was an attorney general. A United States senator. And now vice president."
    h "I've only had one client. The people."
    h "And I'll tell you, as a prosecutor I never asked a victim or a witness are you a Republican or a Democrat. The only thing I ever asked them, are you okay?"
    h "And that's the kind of president we need right now. Someone who cares about you and is not putting themselves first."
    $ harris_img = "harris default"
    h "I intend to be a president for all Americans."

    p "Vice President Harris, thank you. President Trump, your closing statement."

    $ trump_img = "trump attack"
    t "So, she just started by saying she's going to do this, she's going to do that, she's going to do all these wonderful things."
    t "Why hasn't she done it? She's been there for three and a half years."
    t "They've had three and a half years to fix the border. They've had three and a half years to create jobs and all the things we talked about."
    t "Why hasn't she done it?"
    t "She should leave right now, go down to that beautiful White House, go to the Capitol, get everyone together and do the things you want to do."
    t "But you haven't done it. And you won't do it. Because you believe in things that the American people don't believe in."
    t "You believe in things like we're not going to frack. We're not going to take fossil fuel. Things that are going to make this country weak."
    t "We're a failing nation. We're a nation in serious decline."
    t "We're being laughed at all over the world. All over the world, they laugh."
    t "I know the leaders very well. They're coming to see me. They call me. We're laughed at all over the world."
    t "They don't understand what happened to us as a nation. We're not a leader. We don't have any idea what's going on."
    t "We have wars going on in the Middle East. We have wars going on with Russia and Ukraine."
    t "We're going to end up in a third World War. And it will be a war like no other because of nuclear weapons, the power of weaponry."
    t "I rebuilt our entire military. She gave a lot of it away to the Taliban. She gave it to Afghanistan."
    t "What these people have done to our country, and maybe toughest of all is allowing millions of people to come into our country, many of them are criminals."
    t "And they're destroying our country."
    $ trump_img = "trump default"
    t "The worst president, the worst vice president in the history of our country."

    $ harris_img = "harris default"
    $ trump_img = "trump default"

    p "President Trump, thank you."
    p "And that concludes tonight's debate from the National Constitution Center in Philadelphia."

    # Transition to results
    "The candidates shake hands as the debate ends."
    "Across the nation, Americans are casting their votes..."

    p "Ladies and gentlemen, the votes are now being counted."

    "Minutes pass as the nation waits with bated breath..."

    p "We are now ready to announce the results of tonight's debate."

    return

label winner_announcement:
    p "The American people have spoken."

    "A pause as the tension builds..."

    "The results appear on screens across the country..."

    "The crowd erupts as the winner is announced."

    p "The winner of tonight's presidential debate..."

    # Announce winner
    if harris_score > trump_score:
        $ show_score_strip = True
        p "Vice President Kamala Harris!"
        $ harris_img = "harris smile"
        h "Thank you, America. Together, we will chart a new way forward."
        h "We're not going back!"
    elif trump_score > harris_score:
        $ show_score_strip = True
        p "Former President Donald Trump!"
        $ trump_img = "trump smile"
        t "Thank you. We're going to make America great again."
        t "Greater than ever before!"
    else:
        $ show_score_strip = True
        p "In a historic outcome... tonight's debate is a tie."
        p "The American people remain divided."
        h "The fight continues."
        t "We'll see you at the next one."

    "And so concludes the presidential debate of September 10th, 2024."
    "The fate of the nation now rests in the hands of the voters."

    p "Thank you for watching."
    p "We'll see you four years from now for the next debate."
    p "Good night, America!"

    return
