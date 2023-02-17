import time

ans_A = ['A', 'a']
ans_B = ['B', 'b']
ans_C = ['C', 'c']
yes = ['Y', 'y', 'Yes', 'YES', 'yes']
no = ['N', 'n', 'No', 'NO', 'no']
required = "\nUse only A, B or C\nLet's do this again."
required_1 = "\nType 'Yes' or 'No'.\nLet's do this again."

sword = 0
axe = 0
rock = 0
shield = 0
helmet = 0
armor = 0
experience = 0
strength = 0


def intro():
    print("You are sitting in your armchair before the fireplace and read the book.")
    time.sleep(1)
    print("Your children play with wooden toys.")
    time.sleep(1)
    print("Suddenly, a long distant sound of the guard watcher's horn breaks the evening family peace.")
    time.sleep(1)
    print("Enemy is close to village.")
    time.sleep(1)
    print("You're going to...")
    time.sleep(2)
    print("""
          A: Go out to see what's going on in the village.
          B: Take your family and hide under the table.
          C: Take an axe.
          """)

    choice = input("Your choice is: ")
    if choice in ans_A:
        going_out()
    elif choice in ans_B:
        hide_under_table()
    elif choice in ans_C:
        house_axe()
    else:
        print(required)
        intro()


def going_out():
    global sword
    global experience
    global strength
    print("You say to your wife to take care of children while you're out.")
    time.sleep(1)
    print("There is smell of burning houses chaos in the street. A dead soldier lies leaned against the wall.")
    time.sleep(1)
    print("His sword shine in the dark. A voice in your soul tells you to pick the sword.")
    time.sleep(1)
    print("""
          Will you pick up the sword?
          """)
    time.sleep(1)
    print("""
          Yes, you need it now!
          NO, sword of the soldier belongs to him even if he's dead.
          """)

    choice = input("Yes/No: ")
    if choice in yes:
        sword += 1
        experience += 1
        strength += 1
    elif choice in no:
        pass
    else:
        print(required_1)
        going_out()
    print("You're going further if to see is something happens in the streets.")
    time.sleep(1)
    print("Group of Orcs goes towards you. You stand close to tree if they can't see you.")
    time.sleep(1)
    print("""
          What are you going to do now?
          """)
    time.sleep(1)
    print("""
          A: Find way out of town.
          B: Lay down and wait them to pass away.
          C: Go home as quick as you can.
          """)
    choice = input(">>> ")
    if choice in ans_A:
        out_of_town()
    elif choice in ans_B:
        if sword > 0:
            lay_down_sword()
        else:
            lay_down()
    elif choice in ans_C:
        run_home_01()
    else:
        print(required)
        going_out()


def hide_under_table():
    print("You take your family with you and hide under the table hoping the Orcs to ignore your house.")
    time.sleep(1)
    print("Screams on the streets are louder. Sounds of metal hits are more frequent.")
    time.sleep(1)
    print("Door slams! Orcs get in your house!")
    time.sleep(1)
    print("They found you under the table!")
    time.sleep(1)
    print("You're captured.")
    time.sleep(1)
    print("You will spend the rest of your life in slavery.")
    time.sleep(2)
    print("""
          GAME OVER
          """)
    time.sleep(2)
    print("Retry?\nYes/No")
    choice = input(">>>")
    if choice in yes:
        intro()
    elif choice in no:
        print("Bye, bye! Coward.")
    else:
        print(required)
        hide_under_table()


def house_axe():
    global axe
    print("No way to leave your family alone in this dangerous situation.")
    time.sleep(1)
    print("You're not a warrior, but time has come to be.")
    time.sleep(1)
    print("The only useful weapon in your house is an axe you use to cut logs.")
    time.sleep(1)
    print("The Orcs are close, take your family into the safe corner and...")
    time.sleep(1)
    print("""
          A: Stand before the door and make them an axe welcome.
          B: Stand in front of corner to secure your family.
          C: Stand next to the door making an ambush surprise.""")
    choice = input("What's your choice: ")
    if choice in ans_A:
        door_axe_welcome()
    elif choice in ans_B:
        axe_corner()
    elif choice in ans_C:
        axe_ambush()
    else:
        print(required)
        house_axe()


def lay_down_sword():
    global sword
    # print("Orcs pass the street unrecognized you.")
    print("This is good opportunity to attack them from behind")
    time.sleep(1)
    print("""
          A: Stand up and sneak to the last Orc in the group.
          B: Wait for a while. Maybe there is another group of Orcs.
          C: Take a look around, maybe there is some more people ready to fight.
          """)
    choice = input("So, your choice is: ")
    if choice in ans_A:
        sword_attack_01()
    elif choice in ans_B:
        wait_while()
    elif choice in ans_C:
        look_around()
    else:
        print(required)
        lay_down_sword()


def lay_down():
    global rock
    print("They passed away. What are you going to do now?")
    time.sleep(1)
    print("Looks like you should pick up the sword.")
    time.sleep(1)
    print("So you could kill them now.")
    time.sleep(1)
    print("Maybe you can pick some rock to use as a weapon.")
    time.sleep(1)
    print("Why not? There's one, next to you.")
    time.sleep(1)
    print("Pick it up?")
    time.sleep(1)
    print("Yes/No")
    choice = input(">>> ")
    if choice in yes:
        rock += 1
        rock_attack()
    elif choice in no:
        pass
    else:
        print(required_1)
        lay_down()


def rock_attack():
    print("You hit the rock towards the Orcs.")
    time.sleep(1)
    print("It strikes the Orc's helmet.")
    time.sleep(1)
    print("Another Orc turns back and shoots tha arrow into you.")
    time.sleep(1)
    print("The arrow pierces your chest.")
    time.sleep(1)
    print("You fall down dead.")
    time.sleep(2)
    print("""
            GAME OVER
            """)
    time.sleep(1)
    print("""
             Play again?
             """)
    choice = input("""
                      Yes or No: 
                      """)
    if choice in yes:
        intro()
    elif choice in no:
        print("""
                 Lay in peace brave one.
                 """)
    else:
        print(required_1)
        out_of_town()


def sword_attack_01():
    print("You sneak to the last Orc in the group. He wears helmet and armour.")
    time.sleep(1)
    print("He didn't smell you.")
    time.sleep(1)
    print("Now, you have to use the sword for the first time in your life.")
    time.sleep(1)
    print("""
          A: Pierce his neck
          B: Hit his helmet, maybe it's not as hard as it looks.
          C: Cut his leg
          """)
    choice = input("So, what are you going to do: ")
    if choice in ans_A:
        pierce_neck_01()
    elif choice in ans_B:
        helmet_hit_02()
    elif choice in ans_C:
        cut_leg_02()
    else:
        print(required)
        sword_attack_01()


def wait_while():
    print("You breath becomes harder.")
    time.sleep(1)
    print("Fear starts to shake your body.")
    time.sleep(1)
    print("You stand up to find some better shelter.")
    time.sleep(1)
    print("An Orc's arrow hits your chest.")
    time.sleep(1)
    print("You're dead")
    time.sleep(1)
    print("""
              GAME OVER
              """)
    time.sleep(2)
    print("Retry?\nYes/No")
    choice = input(">>>")
    if choice in yes:
        intro()
    elif choice in no:
        print("Rest in peace. You tried to be brave.")
    else:
        print(required)
        wait_while()


def look_around():
    print("You stand up and run down the street.")
    time.sleep(1)
    print("Dead bodies lay down before burning houses.")
    time.sleep(1)
    print("Looks like there's no hope to find any company to face the Orcs.")
    time.sleep(1)
    print("A horse runs out from the corner heading to somewhere.")
    time.sleep(1)
    print("It's your son riding the horse.")
    time.sleep(1)
    print("His clothing is blood stained.")
    time.sleep(1)
    print("Looks like he's heavy wounded. He falls down without signs of life.")
    time.sleep(1)
    print("It means the Orcs attacked your house and killed your family.")
    time.sleep(1)
    print("All is lost.")
    time.sleep(1)
    print("""
              GAME OVER
              """)
    time.sleep(2)
    print("Retry?\nYes/No")
    choice = input(">>>")
    if choice in yes:
        intro()
    elif choice in no:
        print("What to say? You made a wrong decision.")
    else:
        print(required)
        look_around()


def out_of_town():
    print("Looks like the dark street is clear.")
    time.sleep(1)
    print("It leads to the creak, you can hide in the forest till the morning.")
    time.sleep(1)
    print("You stand up and run to the street, some screams pierce the air.")
    time.sleep(1)
    print("The street is dark and quiet.")
    time.sleep(1)
    print("The Orcs didn't pass here. There's no dead bodies and houses on fire.")
    time.sleep(1)
    print("Finally, you reached the creak.")
    time.sleep(1)
    print("You're saved!")
    time.sleep(1)
    print("""
          But, unfortunately, you lose because...
          """)
    time.sleep(1)
    print("""
          You're a coward!!!
          """)
    time.sleep(2)
    print("""
          GAME OVER
          """)
    time.sleep(1)
    print("""
          Play again?
          """)
    choice = input("""
                 Yes or No: 
                 """)
    if choice in yes:
        intro()
    elif choice in no:
        print("""
              Bye, bye, asshole!
              """)
    else:
        print(required_1)
        out_of_town()


def run_home_01():
    print("It was such a dumb decision to get out of house leaving your family unprotected.")
    time.sleep(1)
    print("You must do something to save the family.")
    time.sleep(1)
    print("But, what?!")
    time.sleep(1)
    print("The windows and door in your house are broken! ")
    time.sleep(1)
    print("As you get into the house you realize it's empty. ")
    time.sleep(1)
    print("All the things in the house are broken. ")
    time.sleep(1)
    print("Orcs got into your hose and took your wife and children away. ")
    time.sleep(1)
    print("What have you done?!")
    time.sleep(2)
    print("""
          You lose.
          Because you're dumb.
          """)
    time.sleep(2)
    print("""
          GAME OVER
          """)
    time.sleep(2)
    print("""
          Try again?
          Yes/No
          """)
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        print("""
              Bye, bye stupid.
              """)
    else:
        print(required_1)
        run_home_01()


def pierce_neck_01():
    global experience
    global sword
    global strength
    print("You find a tiny unprotected part on the Orc's neck and pierce the sword into the.")
    time.sleep(1)
    print("The Orc drops down dead.")
    time.sleep(1)
    print("Other Orcs turn back staring at you.")
    time.sleep(1)
    print("You...")
    experience += 1
    strength += 1
    time.sleep(1)
    print("""
          A: Run towards them with war yell.
          B: Stand at your place waiting for them to attack.
          C: Run to the closest corner to make an ambush.
          """)
    choice = input("What are you going to do: ")
    if choice in ans_A:
        pierce_neck_01_charge()
    elif choice in ans_B:
        pierce_neck_01_stand()
    elif choice in ans_C:
        pierce_neck_01_run()
    else:
        print(required)
        pierce_neck_01()


def helmet_hit_02():
    print("You hit his head with the sword.")
    time.sleep(1)
    print("The sword bounced off the helmet.")
    time.sleep(1)
    print("The Orc turns back and cut you down.")
    time.sleep(1)
    print("""
          GAME OVER
          """)
    time.sleep(1)
    print("""
          Try again?
          """)
    time.sleep(1)
    choice = input("Yes or No: ")
    if choice in yes:
        intro()
    elif choice in no:
        print("""
              Rest in peace brave man.
              """)
    else:
        print(required_1)
        helmet_hit_02()


def cut_leg_02():
    print("Back side of Orc's legs are unprotected by armour.")
    time.sleep(1)
    print("You cut his leg and he screams falling down, then you pierce the sword into his face.")
    time.sleep(1)
    print("An arrow hits your chest.")
    time.sleep(1)
    print("You should look around before you cut the Orc.")
    time.sleep(1)
    print("""
          GAME OVER
          """)
    print("""
          Try again?
          """)
    time.sleep(1)
    choice = input("Yes or No: ")
    if choice in yes:
        intro()
    elif choice in no:
        print("""
              The brave lives forever.
              """)
    else:
        print(required_1)
        cut_leg_02()


def pierce_neck_01_charge():
    global sword

    print("You have killed the first Orc. More of them will get one way ticket to hell.")
    time.sleep(1)
    print("You scream the war yell, then charge towards them.")
    time.sleep(2)
    print("An Orcs' arrow pierces into your chest.")
    time.sleep(1)
    print("You're dead.")
    time.sleep(2)
    print("""
          GAME OVER
          """)
    time.sleep(2)
    print("""
          Wanna try again?
          Yes/No
          """)
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        print("""
              There's a place for brave in eternity.
              """)
    else:
        print(required_1)
        pierce_neck_01_charge()


def pierce_neck_01_stand():
    global sword
    global experience
    print("A dead Orc is lying under your feet.")
    time.sleep(1)
    print("You hold the sword firmly waiting the next Orc to taste your sword.")
    time.sleep(1)
    print("But, they're not in hurry to die.")
    time.sleep(1)
    print("An arrow pierces you.")
    time.sleep(1)
    print("You're dead.")
    time.sleep(2)
    print("""
          GAME OVER
          """)
    time.sleep(1)
    print("""
          Try again?
          Yes?No
          """)
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        print("""
              Rest in peace brave warrior.
              """)
    else:
        print(required_1)
        pierce_neck_01_stand()


def pierce_neck_01_run():
    global sword
    global shield
    global experience
    global strength
    global armor
    # axe=0
    print("While you run towards the nearest corner, you feel an arrow flew close to you.")
    time.sleep(1)
    print("You hear a loud war yell of the Orcs.")
    time.sleep(1)
    print("Their heavy steps come to the corner.")
    time.sleep(1)
    print("You cut the neck of the first Orc that appears on the corner.")
    time.sleep(1)
    print("The second one that appeared on the corner found his death.")
    time.sleep(1)
    print("He had a shield on his back.")
    time.sleep(1)
    print("Maybe it's good to take his shield.")
    choice = input("So? Yes or No: ")
    if choice in yes:
        shield += 1
        experience += 1
        strength += 1
    elif choice in no:
        pass
    else:
        print(required_1)
        pierce_neck_01_run()

    if shield > 0:
        experience += 1
        print("You take the shield and step back to the position.")
        time.sleep(1)
        print("An Orc with an axe comes to the corner and hit his axe.")
        time.sleep(1)
        print("Fortunately, you have the shield to block the strike, so you cut the Orc with sword.")
        time.sleep(1)
        print("You step out of corner and see an Orc fires an arrow towards you.")
        time.sleep(1)
        print("Thanks to shield you have taken, an arrow doesn't kill you.")
        time.sleep(1)
        print("An bow and arrow Orc runs away.")
        time.sleep(1)
        print("There's dead armoured soldier lying, you can take his armour.")
        time.sleep(1)
        print("So, will you?")
        time.sleep(1)
        print("""
              Yes or Not
              """)
        choice = input(">>> ")
        if choice in yes:
            armor += 1
            experience += 1
            strength += 1
            print("An Orc with an axe comes to the corner and hit his axe on you.")
            time.sleep(1)
            print("Fortunately, you have a shield, so his axe hit against it.")
            time.sleep(1)
            print("You cut his neck killing him.")
            time.sleep(1)
            print("Other Orcs run away, so you decide to came beck to your home.")
            time.sleep(1)
            print("After you arrive to the home, you realize that Orcs robbed your house and took your family away.")
            time.sleep(1)
            print("You should stay there.")
            time.sleep(1)
            print("Now, you just can drop on your knees and cry.")
            time.sleep(2)
            print("""
                     GAME OVER
                     """)
            print("""
                     Try again?
                     """)
            time.sleep(1)
            choice = input("Yes or No: ")
            if choice in yes:
                intro()
            elif choice in no:
                print("""
                         Cry, dumb one. Cry...
                         """)
            else:
                print(required_1)
                pierce_neck_01_run()

        elif choice in no:
            pass

        else:
            print(required_1)
            pierce_neck_01_run()

    else:
        print("An Orc with an axe comes to the corner, hit his axe and cut you down.")
        time.sleep(1)
        print("You should take the shield.")
        time.sleep(1)
        print("You're dead now.")
        time.sleep(1)
        print("""
              GAME OVER
              """)
        time.sleep(2)
        print("""
              Wanna try again?
              Yes/NO
              """)
        choice = input(">>> ")
        if choice in yes:
            intro()
        elif choice in no:
            print("""
                  You have found your death in the first battle.
                  Brave lives forever.
                  """)
        else:
            print(required_1)
            pierce_neck_01_run()


def door_axe_welcome():
    global axe
    print("The door slams down.")
    time.sleep(1)
    print("The armoured Orc with a blood stained sword and round shield gets into your hose.")
    time.sleep(1)
    print("You attack him with an axe, but he rises a shield against you axe and pierce you with a sword.")
    time.sleep(1)
    print("You fall down dead.")
    time.sleep(2)
    print("""
          GAME OVER
          """)
    time.sleep(2)
    print("""
          Try again?
          Yes/No
          """)
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        print("""
              Rest in peace.
              """)
    else:
        print(required_1)
        door_axe_welcome()


def axe_corner():
    print("Your wife braces children while you wait for Orcs to get into the house.")
    time.sleep(1)
    print("Rumor outside becomes louder.")
    time.sleep(1)
    print("You hold the axe firmly.")
    time.sleep(1)
    print("Door slams and armoured Orc with blood stained sword and round shield gets into the house.")
    time.sleep(1)
    print("Another Orcs get in making your children cry.")
    time.sleep(1)
    print("The first Orc swings the sword and you hit it back with the axe.")
    time.sleep(1)
    print("But he hits your head with shield.")
    time.sleep(1)
    print("He cuts you as you fall down. You're dead.")
    time.sleep(2)
    print("""
          GAME OVER
          """)
    print("""
          Try again?
          Yes/No
          """)
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        print("""
              Brave lives forever.
              Rest in peace.
              """)
    else:
        print(required_1)
        axe_corner()


def axe_ambush():
    print("Rumor of the Orcs outside becomes loader.")
    time.sleep(1)
    print("You take the position next to the door.")
    time.sleep(1)
    print("The door slams and an Orc gets into the house, but doesn't see you behind.")
    time.sleep(1)
    print("You...")
    time.sleep(2)
    print("""
          A: Hit his head with the axe.
          B: Hit his back.
          C: Hit his leg with the axe.
          """)
    time.sleep(2)
    choice = input("So...: ")
    if choice in ans_A:
        helmet_hit_01()
    elif choice in ans_B:
        hit_back_01()
    elif choice in ans_C:
        cut_leg_01()
    else:
        print(required)
        axe_ambush()


def helmet_hit_01():
    print("You hit his head with the axe, but it bounced back of the helmet.")
    time.sleep(1)
    print("The Orc quickly turns back and cut you down.")
    time.sleep(1)
    print("You're dead.")
    time.sleep(2)
    print("""
          GAME OVER
          """)
    time.sleep(2)
    print("""
          Wanna try again?
          Yes/No
          """)
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        print("God holds thee now, brave warrior in try.")
    else:
        print(required_1)
        helmet_hit_01()


def hit_back_01():
    print("You hit his back with the axe.")
    time.sleep(1)
    print("He turns back cutting you down.")
    time.sleep(1)
    print("You're dead.")
    time.sleep(2)
    print("""
          GAME OVER
          """)
    time.sleep(2)
    print("""
          Are you going to try again?
          Yes/No
          """)
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        print("Rest in peace warrior in try.")
    else:
        print(required_1)
        hit_back_01()


def cut_leg_01():
    global sword
    global shield
    global experience
    global axe
    print("Back side of Orc's leg is unprotected with armour.")
    time.sleep(1)
    print("You hit his leg with the axe, he screams and falls down.")
    time.sleep(1)
    print("You quickly close the door, than finish the Orc hitting the axe at his neck.")
    experience += 1
    time.sleep(2)
    print("Looks like it's a good opportunity to take Orc's shield.")
    time.sleep(1)
    print("So, will you?")
    time.sleep(1)
    print("Or you think it's wasting of time 'cause there's more Orcs outside that can get ino the house.")
    time.sleep(1)
    print("Yes/No")
    choice = input(">>> ")
    if choice in yes:
        shield += 1
        experience += 1
        print("You take the shield just at time the door slams again.")
        time.sleep(1)
        print("Two Orcs get into the house.")
        time.sleep(1)
        print("They are confused about you and their dead brother in arms.")
        time.sleep(1)
        print("You...")
        time.sleep(2)
        print("""
              A: Hit the axe into Orc's neck.
              B: Step back to cover your family.
              C: Try to talk to them.
              """)
        time.sleep(2)
        choice = input("What's your choice: ")
        if choice in ans_A:
            hit_neck()
        elif choice in ans_B:
            cover_family()
        elif choice in ans_C:
            talk_to_them()
        else:
            print(required)
            cut_leg_01()
    elif choice in no:
        print("The door slams again.")
        time.sleep(1)
        print("Two Orcs get into the house.")
        time.sleep(1)
        print("They are confused about you and their dead brother in arms.")
        time.sleep(1)
        print("You use the moment of their confusion and try to cut their necks.")
        time.sleep(1)
        print("But, you hit the shield.")

    else:
        print(required)
        cut_leg_01()


def hit_neck():
    if shield > 0:
        print("You hit Orc by the shield into the face.")
        time.sleep(1)
        print("He drops his sword down, than you cut his neck with the axe.")
        time.sleep(1)
        print("He falls down dead.")
        time.sleep(1)
        print("Your wife picks up the sword while you attack another Orc.")
        time.sleep(1)
        print("You hit the axe against Orc's shield.")
        time.sleep(1)
        print("Your wife pierces the sword into Orc's neck.")
        time.sleep(1)
        print("Orc falls down dead.")
        time.sleep(1)
        print("Another Orc was armed with bow and arrows. Your wife picks them up.")
        time.sleep(1)
        print("You and your wife take Orcs' armors and mount them.")
        time.sleep(1)
        print("Now you're heavy armored and armed. You can safely go to the town to alarm the army.")
        time.sleep(1)
        print("You succeed.")
        time.sleep(1)
        print("""
        CONGRATS!
        """)
        time.sleep(1)
        print("Play again?")
        time.sleep(1)
        choice = input("Yes or No: ")
        if choice in yes:
            intro()
        elif choice in no:
            print("""
                The brave lives forever.
                """)
        else:
            print(required_1)
            hit_neck()
    else:
        print("You hit Orc's neck with the axe.")
        time.sleep(1)
        print("He falls down dead.")
        time.sleep(1)
        print("Another Orc hits your head with shield.")
        time.sleep(1)
        print("After you fall down, he cuts your throat with knife.")
        time.sleep(1)
        print("You're dead.")
        time.sleep(1)
        print("""
              GAME OVER
              """)
        time.sleep(1)
        print("""
              Try again?
              Yes?No
              """)
        choice = input(">>> ")
        if choice in yes:
            intro()
        elif choice in no:
            print("""
                  Rest in peace brave warrior.
                  """)
        else:
            print(required_1)
            hit_neck()


def cover_family():
    print("You step back to cover your family")
    time.sleep(1)
    print("One Orc takes bow and arrow.")
    time.sleep(1)
    print("Just as you try to attack them, an arrow pierces your chest.")
    time.sleep(1)
    print("You're dead.")
    time.sleep(1)
    print("""
          GAME OVER
          """)
    time.sleep(1)
    print("""
          Try again?
          Yes?No
          """)
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        print("""
              Rest in peace brave warrior.
              """)
    else:
        print(required_1)
        hit_neck()


def talk_to_them():
    print("You think it is needed to give negotiations a chance.")
    time.sleep(1)
    print("You say:")
    print("Guys, maybe we can solve this without killing each other.")
    time.sleep(1)
    print("They don't understand your language.")
    time.sleep(1)
    print("They kill you.")
    time.sleep(1)
    print("""
             GAME OVER
             """)
    time.sleep(1)
    print("""
             Try again?
             Yes?No
             """)
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        print("""
              Rest in peace brave warrior.
              """)
    else:
        print(required_1)
        talk_to_them()


print("You have", experience, "experience.")

intro()
