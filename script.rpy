image mountain = "mountain.jpg"
image river = "river.jpg"
image forest = "forest.jpg"
image cave = "cave.jpg"
image ship = "ship.jpg"
image miners = "miners.jpg"
image beach = "beach.jpg"
image pyramid = "pyramid.jpg"







# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Ghost")
define u = Character("Narrator", color="#c8ffc8")




init python:

    def verify(prompt, allowed_chars):
    # loop until a valid character is entered
        while True:
            # display prompt and get user input
            user_input = renpy.input(prompt)

            # check if user input is a valid character
            if user_input in allowed_chars:
                return user_input

                # if user input is not valid, display error message
                renpy.say("Invalid input. Please enter one of the following characters:")
                for char in allowed_chars:
                    renpy.say(f"- {char}")




# The game starts here.

label start_game:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene introduction

    # This displays lines of dialogue.


    # Wait for user input before continuing.

    pause

    # This displays more dialogue.

    u "The storm subsides and the crew decides you should be their new leader. Your goal is to find the forbidden treasure."

    # Wait for user input before continuing.

    pause

    # Display a decision point.

    menu:

        "Travel to the mountain":


            label start:

                show ship

                u "You wake up on a boat in the middle of a storm. Your captain is gone, and your crew is scrambling to survive."
                u "The storm subsides and the crew decides you should be their new leader. Your goal is to find the forbidden treasure."
                u "You and your crew have decided to embark on a journey to find the treasure. Your crew looks at you expecting a decision."
                u "The ship has been destroyed, and you are on an foreign island you decide that you only have one choice."
                $ d1 = verify("Enter M to begin your journey up the mountain.", ["M", "m"])
                hide ship
                show mountain

                if d1 == "m" or d1 == "M":
                    u "As you climb the mountain you start to get comfortable."
                    u "But when you are least expecting it, a cougar attacks you."
                    u "The crew needs you to handle this."
                    $ d2 = verify("Enter R to run from the cougar. T to fight the cougar.", ["R","r","t" "T"])
                    if d2 == "r" or d2 == "R":
                        u "You turn and run away from the cougar.  Your crewmate is unfortunately slower than you."
                        u "The crew continues to run without one of its members."
                        u "Your crewmates turn to you sadly.  But the journey must continue."
                        u "Would you like to regather your group in the cave, or resume your climb up the mountain?"
                        $ d3 = verify("Enter C if you want to go to the cave. Or enter M to climb the mountain.", ["c","m","C","M"])
                        if d3 == "M" or d3 == "m":
                            u "The crew continues to climb the mountain.  Hours have passed.  The crew starts to lose hope, when you hear a river flowing."
                            hide mountain
                            show river
                            u "The river is a sign of hope to the crew.  This is the first source of fresh water they have had in days."
                            u "The crew spots a vine tied to a tree.  The vine could be used as a way of transporting across the river.  The forest across the river has fruits growing on every tree."
                            u "You look across the river and think about how peaceful the land looks.  You hear the roaring river, and quickly gain awarness of the danger beneath you."
                            u "You have to decide.  You can either stay on your side of the river.  Or attempt to cross into the peaceful forest infront of you."



                            $ d4 = verify("Press V to swing on the vine.  Or S to stay on your side.",["v","s","V","S"])
                            if d4 == "S" or d4 =="s":
                                u "The dangers below you scare you."
                                u " You decide to stay on your side of the river."
                                u "You continue to walk up, and down the sides of the river hoping to cross at somepoint."
                                u "You eventually find a cave on the side of the mountain."
                                u "as your crew loses hope, you decide to enter as a change of scenery."
                                hide river
                                show cave
                                u "You wander through the cave for days."
                                u "You feel like you have left your crew hanging.  You feel like you should have risked it at the river."
                                u "You wander through the cave, and than you wander some more."
                                hide cave
                                u "You lose track of your steps as you lose hope."
                                u "You and your crew are lost."
                                u "You keep looking for an escape, until its too late."
                                u "You have gotten you and your crew killed."
                                $ renpy.quit()
                            if d4 == "V" or d4 == "v":
                                u "You tightly grip the vine.  You need to focus if you are going to make this jump."
                                u "Just dont look down, and hold on tight."
                                u "On the count of three.  Press enter to jump"
                                u "1"
                                u "2"
                                u "3"
                                u "JUMP"
                                u " That was super close!  Lets hope your crew can do the same."
                                u " The first member of your crew begins to cross."
                                u "He jumps on the vine, and trys to fling hiimself across the body of water."
                                u "The crew member lets go of the vine, and unfortunately falls into the water.  He hits a rock, and is washed away in the current."
                                u "Your final memeber of the ship hesitates.  He has seen you reach a beautiful forest, but he does not want to become a victim of the river."
                                u "The crew member tightly grips the vine.  He looks you in the eyes, and decides to follow you.  He launches himself across the river."
                                u "He makes it across safely. "
                                u "You and your last crewmate stay locked in.  All that matters now is finding the treasure."
                                hide river
                                show forest
                                u "You turn away from the river, and look into the forest behind you.  It is beautiful.  The trees are enormous, and covered with colorful fruit.  It smells like flowers."
                                u "You journey into the forest, and stumble upon a tree stump.  In the stump is an axe.  You and your crewmate look at eachother."
                                u "You feel angry you have lost two members of your crew.  You grab the axe and chop the stump.  "
                                u " Your friend attempts to calm you down but he i sunsuccesful.  You continue to destroy the stump, and find that the bottom of it is a box."
                                u " You talk to your crewmate about the box.  You both decide that the best idea is to destroy the box."
                                u "You hand your axe to the crewmate and he lets his anger out on the box."
                                u "the box shatters, and an abundance of jewels, currency, and swag fall to your feet."
                                u "You fall to your knees.  The happiness overcomes your grief, and physical exhaustion.  "
                                u "You notice the axe at your crewmates feet."
                                u "You think of how much more money you would have if your crewmate was not here."
                                $ df1=verify("Enter X to eliminate your crewmate and hoard the treasure.  Press F to split the prize.", ["f","x", "F", "X"])
                                if df1 == "F" or df1 == "f":
                                    u "You put your greed aside."
                                    u "You think about how far you and your friend have come."
                                    u "The memories you have made.  And those who you have lost."
                                    u "These thoughts flood your mind, as you pack your bags with treasure."
                                    u "You start to leave the forest with the treasure."
                                    u "You and your crewmate's lives will never be the same."
                                    u "The adventure of a lifetime has paid off."
                                    u " The two of you walk into the sunset, thankful for the journey.  You think of the lives ahead of you."
                                    u "You escape the island, and never see eachother again. "
                                    u "But you both know, you will never forget eachother."
                                    $ renpy.quit()
                                     # THE END
                                if df1 == "X" or df1 == "x":
                                     u " You dive on the axe and eliminate your final friend."
                                     u "You pack your bags with the treasure, and put on a ton of swag."
                                     u " You have been walking for miles.  Thinking of a way to escape when you realize."
                                     u "Your bags are getting lighter, your swag is dissapearing.  The treasure, is vanishing."
                                     u " Your eyes cannot believe what is ahead of you."
                                     g " I am here to haunt you.  You knew the forbidden treasure would only be worth it if you had others with you."
                                     g "But instead.  You decided to hoard the treasure for yourself."
                                     g "You will now spend the rest of your life with me.  I will haunt you until you die."
                                     g "You will never leave this island."
                                     u " The ghost has rattled you a little"
                                     u " You think about the ghost, and wonder if he is telling the truth."
                                     u " You then think about the ones you lost on the trip.  The people who made it happen... The people you let down."
                                     u " As this thought comes to mind.  You vanish with the ghost.  Forever."
                                     $ renpy.quit()
                                     #THE END
                        if d3 == "c" or d3 == "C":
                            hide mountain
                            show cave
                            u "You enter the cave.  You can hear the water dripping from the ceiling."
                            u "Bats fly close to your head.  You can't see anything, but part of you is glad that this is the case."
                            u "Your crew is exhausted.  The sun has started to set."
                            u "The cave splits to two paths.  One looks like a human made structure.  The other path is pitch black."
                            u "Your crew would like to either sleep in the cave, to try to let the light lead you through the dark path.  Or travel through the manmade secction."
                            $ dC = verify("Enter H to explore the structure, or Enter S to sleep.", ["H","h","S","s"])
                            if dC == "H" or dC == "h":
                                hide cave
                                show miners
                                u "You walk through the structure, tired and confused."
                                u " Minutes turn to hours, and the crew is losing hope.  Just when you thought nothing worst could come...."
                                u "The walls start to crumble, the ceiling collapses on you, and your crew."
                                u "You have failed to get the treasure, and killed your crew."
                                $ renpy.quit()
                                #THE END

                            if dC == "S" or "s":

                                u "You and your crew unpack your bags.  You decide to sleep."
                                hide cave
                                u "zzzzz"
                                u " You wake up to a loud noise.  The man made path has collapsed.  You are forced to continue down the dark path."
                                u " Bats fly everywhere.  The tunnel seems to just keep going."
                                u " As you start to lose hope, you see light against the wall."
                                u " It is a group of miners."
                                show miners
                                u " They explain to you that it has been a long time since they have had visitors."
                                u "These miners are so dedicated to there craft that they will not leave the cave without diamonds."
                                u "They explain to you there confusing backstory, and offer you a drink."
                                $ DD = verify("Enter D to have a couple of drinks with the miners, S to polietly decline to sleep.", ["d","s","D","S"])

                                if DD == "D" or DD == "d":
                                    u "The miners give you some of there oldest bottle."
                                    u " The bottle has been waiting for a visitor for longer than any of the miners had been alive."
                                    u " By the time you could count to five you had finished the bottle."
                                    u "1"
                                    u "2"
                                    u "3"
                                    u "4"
                                    u "5"
                                    u "damn the miners go hard."
                                    u " You start to feel so confident about finding the treasure."
                                    u " The crew leaves the cave.  As you leave you drop the bottle of wine you were gifted."
                                    u " You look down abruptly, before realizing that the label was a map."
                                    u  "There are 2 X's on the map. One on the beach, and one somewhere in the ocean on the other side of the island."
                                    $ dmap = verify("Enter B for Beach or Enter O for the ocean.", ["b","o","B","O"])
                                    hide miners


                                    if dmap == "O" or dmap =="o":
                                        show beach
                                        u "You travel across the island."
                                        u "Days pass, the journey remains peaceful."
                                        u "You reach what seems to be the X on the map, and start diving looking for treasure."
                                        u "After a couple dozen attempts, you find a box."
                                        u "You get a grip on the box, but you cant pull it out."
                                        u "You spend every last breath trying to obtain this potential treasure."
                                        u "But it is no use."
                                        u "You have killed yourself, and your crew."
                                        u "Game over"
                                        $ renpy.quit()
                                        #THE END

                                    if dmap == "B" or dmap == "b":
                                        show beach
                                        u "You travel all day to get to the beach.  The crew is exhausted.  But you decide to continue the journey."
                                        u "Hours go by, and just when you thought it couldn't get any worst, a giant crab approaches you."
                                        u " The crew sighs.  They are exhausted.  No one in the group has ever seen a crab as big as this one.  It appears to be a little bigger than 25 feet tall."
                                        u "Should you attempt to fight this crab, or hope it does not see you."
                                        $ crab = verify("Enter F to fight the crab or P to pray the crab does not see you.", ["f","p", "P", "F"])

                                        if crab == "P" or crab  == "p":
                                            u "you decide to lead your crew away from the crab."
                                            u "the crab sees you out of the corner of his huge eye."
                                            u "You and the crew runs, and escapes the enormous creature."
                                            u "You continue to follow the map"
                                            u "You see a pyramid on the beach."
                                            u "The pyramid towers over you and your crew."
                                            u " You dont understand why the pyramid isnt on the map, but you go in anyways."
                                            hide beach
                                            show pyramid
                                            u " You decide to enter the pyramid. It seems like it could be full of traps."
                                            u "As you get deeper into this structure You realize this is not the case."
                                            u "You continue to walk when you see a tree stump with an axe in it."
                                            u " You destroy the stump."
                                            u "it shatters, and an abundance of jewels, currency, and swag fall to your feet."
                                            u "You fall to your knees.  The happiness overcomes your grief, and physical exhaustion.  "
                                            u "You notice the axe at your crewmates feet."
                                            u "You think of how much more money you would have if your crewmate was not here."
                                            $ df2 = verify("Enter X to eliminate your crewmate and hoard the treasure.  Press F to split the prize.", ["x","f","F","X"])
                                            if df2 == "F" or df2 == "f":
                                                u "You put your greed aside."
                                                u "You think about how far you and your friend have come."
                                                u "The memories you have made.  And those who you have lost."
                                                u "These thoughts flood your mind, as you pack your bags with treasure."
                                                u "You start to leave the forest with the treasure."
                                                u "You and your crewmate's lives will never be the same."
                                                u "The adventure of a lifetime has paid off."
                                                u " The two of you walk into the sunset, thankful for the journey.  You think of the lives ahead of you."
                                                u "You escape the island, and never see eachother again. "
                                                u "But you both know, you will never forget eachother."
                                                $ renpy.quit()
                                                 # THE END

                                            if df2 == "X" or df2 == "x":
                                                 u "dive on the axe and eliminate your final friend."
                                                 u "You pack your bags with the treasure, and put on a ton of swag."
                                                 u " You have been walking for miles.  Thinking of a way to escape when you realize."
                                                 u "Your bags are getting lighter, your swag is dissapearing.  The treasure, is vanishing."
                                                 u " Your eyes cannot believe what is ahead of you."
                                                 g " I am here to haunt you.  You knew the forbidden treasure would only be worth it if you had others with you."
                                                 g "But instead.  You decided to hoard the treasure for yourself."
                                                 g "You will now spend the rest of your life with me.  I will haunt you until you die."
                                                 g "You will never leave this island."
                                                 u " The ghost has rattled you a little"
                                                 u " You think about the ghost, and wonder if he is telling the truth."
                                                 u " You then think about the ones you lost on the trip.  The people who made it happen... The people you let down."
                                                 u " As this thought comes to mind.  You vanish with the ghost.  Forever."
                                                 $ renpy.quit()
                                                 #THE END

                                        if crab == "F" or crab == "f":
                                            u " I dont know what you expected."
                                            u " Just wow. "
                                            u " A 25 foot tall crab... And you thought you could fight him."
                                            u "You put a ton of energy into hurting this crab."
                                            u "Unfortunately a 25 foot tall crab is a enormous crab so he hardly feels it."
                                            u "You have killed you, and your crew."
                                            $ renpy.quit()
                                            #THE END

                                if DD == "S" or DD == "s":
                                    u "The miners show you to your room.  They sleep in bunk beds so you and the whole crew stays in the same room."
                                    u "You get a good sleep, until you wake up to 15 miners in your room.  They loot your bags, and kill you and your crew."
                                    u "The miners take it very disrespectfully when you turn down a gift."
                                    u "You have gotten yourself, and your crew killed."
                                    u "Game Over."
                                    $ renpy.quit()
                                    # THE END

                    if d2 == "t" or d2 == "T":
                        u "There is no way you thought you could take a cougar."
                        u "The cougar puts in work on you, and the crew."
                        u "With home court advantage, and the physical advantages he has on you he kills you."
                        u "You have gotten you and your crew killed."
                        $ renpy.quit()
                        #THE END

    pause

    # This ends the game.

    return
