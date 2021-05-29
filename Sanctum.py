import sys
import time

a = 1
b = 0.01
c = 0.1


def intro():
    print()
    print("(Everything is dark.)")
    time.sleep(a)
    print("You feel around, using your hands to see.")
    time.sleep(a)
    print("The ground is cold, damp, and covered in thick vines.")
    time.sleep(a)
    print("You feel a round rock that sinks into the floor when you press it.")
    time.sleep(a)
    print("The ground starts rumbling...")
    time.sleep(a)
    print("Light begins flooding in.")
    print()
    s = "I'm in a cave?.."
    for char in s:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(1)
    print()
    print()
    print("The rock released a boulder that was blocking the cave entrance.")
    time.sleep(a)
    print("Three paths are revealed:")
    time.sleep(a)
    print()
    print("Part #1: Exit forward through the caves entrance, into the light.")
    print("Part #2: Explore the depths of the rear of the cave, into the darkness.")
    print("Part #3: Climb down the vines into a bottomless hole in the ground.")
    print()
    first_path = input("Which path will you choose? (1/2/3): ")
    if first_path == '1':
        print()
        path1()
    elif first_path == '2':
        print()
        path2()
    else:
        print()
        path3()


def path1():
    print("You exit forward through the cave's entrance, into the light.")
    time.sleep(a)
    print("It's incredibly bright but your vision adjusts as you continue.")
    time.sleep(a)
    print("The cave exit closes, there's no going back now.")
    time.sleep(a)
    print("You look out and see that you're about halfway down an incredible mountain.")
    time.sleep(a)
    print("A man calls out to you")
    time.sleep(a)
    print()
    s1 = '"Hello there!...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s2 = "...My name is APOLLO. I thought you were my sister, ARTEMIS..."
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s3 = "...Ah, now I remember you! Yes, you're looking for CHRONOS..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...He's the one who trapped you in this time loop..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...Yet, I cannot bring you to him..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...Only HERMES can do that..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...However, I have heard that CHRONOS dwells at the base of this mountain.\""
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)

    time.sleep(1)
    print()
    print()
    print("There are two paths to take to the bottom of the mountain:")
    time.sleep(a)
    print("Path #1: Take the set path down the mountain.")
    print("Path #2: Scale down the side of the mountain.")
    print()
    secondPath = input("Which path will you choose? (1/2): ")
    if secondPath == '1':
        path1_1()
    elif secondPath == '2':
        path1_2()


def path1_1():
    print()
    print("You begin walking down the mountain toward the bottom.")
    time.sleep(a)
    print("The path is long and winding but the walk is not difficult.")
    time.sleep(a)
    print("The sky is bright and blue and a warm breeze hits your face.")
    time.sleep(a)
    s8 = '  "I could get used to this..."'
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself.')
    time.sleep(a)
    print("A boy calls out to you.")
    time.sleep(a)
    print()
    s1 = '"Hey! Wait up!...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s2 = "...My name is ARES. I was just coming down the mountain for some fresh air..."
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s3 = "...Mount OLYMPUS is the highest reaching mountain on Earth and the air is specially crisp..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...Anyhow, I see you're searching for the correct path, as we all are..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...It's not my place to tell you which path is correct..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...However, I will tell you this..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    print()
    print()
    s7 = '..."ONLY THROUGH DARKNESS WILL FREEDOM BE ATTAINED"'
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    intro()


def path1_2():
    print()
    print("You begin scaling down the side of the mountain toward the bottom.")
    time.sleep(a)
    print("It's a long way down but you soon grow strong enough to appreciate the view.")
    time.sleep(a)
    print("Although you're still about halfway up the mountain, clouds surround you and the world seems small.")
    time.sleep(a)
    s1 = '  "I don\'t believe my eyes..."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself')
    time.sleep(a)
    print()
    print("You continue down the mountain for days until you reach the bottom.")
    time.sleep(a)
    s2 = '  "Finally! I can face you, CHRONOS!"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('--You yell, entering the base of Mount OLYMPUS through the largest red and black doors you\'ve ever seen')
    time.sleep(a)
    print("The darkness consumes you as you enter, unable to see a thing.")
    time.sleep(a)
    print("A thunderous voice calls out to you...")
    time.sleep(a)
    print()
    s3 = "Ah... I've been expecting you. But you're far too early..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...It appears you've taken a fairly easy route..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...You can see through the light, but not the DARKNESS..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...You've developed some STRENGTH, but not enough..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...There is more you need to grow..."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s8 = "...More you need to LEARN"
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s9 = "...And learn you will"
    for character in s9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s10 = "...In time..."
    for character in s10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    intro()


def path2():
    print("You explore the depths of the rear of the cave, into the darkness.")
    time.sleep(a)
    print("It's incredibly dark but your vision adjusts as you continue forward.")
    time.sleep(a)
    print("A huge boulder slides into place behind you, blocking your path back.")
    time.sleep(a)
    print("You notice that the cave floor is declining to the left, like a spiral.")
    time.sleep(a)
    print("A woman calls out to you.")
    time.sleep(a)
    print()
    s1 = '"Hello there!...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s2 = "...My name is ARTEMIS... I thought you were my brother, APOLLO..."
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s3 = "...Ah, now I remember you! Yes, you're looking for CHRONOS..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...He's the one who trapped you in this time loop..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...However, I cannot bring you to him..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...Only HERMES can do that..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...However, I have heard that CHRONOS dwells at the base of this cave..."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    print()
    print()
    print("There are two paths to continue through the cave:")
    time.sleep(a)
    print("Path #1: Go to the left.")
    time.sleep(a)
    print("Path #2: Go to the right.")
    time.sleep(a)
    print()
    secondPath = input("Which path will you choose? (1/2): ")
    if secondPath == '1':
        path2_1()
    elif secondPath == '2':
        path2_2()


def path2_1():
    print()
    print("You take the fork in the cave to the left and continue walking.")
    time.sleep(a)
    print("The cave floor is still declining but is becoming much steeper than before.")
    time.sleep(a)
    print("It's so dark and the winding cave seems to go on forever.")
    time.sleep(a)
    s1 = "I have no choice, I must keep going..."
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself')
    time.sleep(a)
    print("Still going, fortifying your will, until finally, you reach the largest red and black door in existence.")
    time.sleep(a)
    print()
    s2 = '  "Finally! I can face you, CHRONOS!"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You erupt as you enter the doors at the base of the cave inside Mount OLYMPUS')
    time.sleep(a)
    print()
    print("Standing now in the largest room, in front of the largest man you've ever seen.")
    time.sleep(a)
    print("The room is dark, but you can see the source of the thunderous voice which calls out to you...")
    time.sleep(a)
    print()
    s3 = "Ah... I've been expecting you. But you're still too early..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...It appears you've taken a fairly easy route..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...Your vision is keen. You see through the darkness and the light..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...However, you haven’t developed quite enough strength..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...There is more you need to grow..."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s8 = "...More you need to learn..."
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s9 = "...And learn you will..."
    for character in s9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s10 = "...In time."
    for character in s10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    intro()


def path2_2():
    print()
    print("You take the fork in the cave to the right and continue walking.")
    time.sleep(a)
    print("The cave floor is now inclining and is becoming quite steep.")
    time.sleep(a)
    print("It's so dark but after what seems like days of walking, you see a glow in the distance.")
    time.sleep(a)
    s1 = '  "What in the world can that be...?"'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself')
    time.sleep(a)
    print("Approaching the brilliant light, you reach the end of this path and see an old book perched atop a pedestal")
    time.sleep(a)
    print()
    s2 = '  "THE SECRETS OF TIME"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You read the large inscription on the cover before opening the book.')
    print()
    time.sleep(a)
    s3 = '"If you stumble upon this tomb...'
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...It may save you from your doom..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...Your vision is keen, that much is clear..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...But you have yet to face your fear..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = '...The truest path is one of toil..."'
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s8 = "...Climb down vines beneath the soil..."
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s9 = "...Speak with MOIRAE, help her first..."
    for character in s9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s10 = "...Then you will complete your search..."
    for character in s10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    time.sleep(a)
    intro()


def path3():
    print("You climb down the vines into a bottomless hole in the ground")
    time.sleep(a)
    print("It's dark, damp, and hard to climb down the vines, but your vision and muscles eventually adjust.")
    time.sleep(a)
    print("A huge boulder slides into place above you, blocking your escape.")
    time.sleep(a)
    print("You continue climbing down the vines until you hear something whirring up at you.")
    time.sleep(a)
    print("Someone calls out to you.")
    time.sleep(a)
    print()
    s1 = "Hey, hey there!..."
    for char in s1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s2 = "My name is HERMES. I will be your guide to freedom..."
    for char in s2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s3 = "Yes, I know all about you. You are looking for Chronos..."
    for char in s3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s4 = "He is the one who trapped you in the time loop..."
    for char in s4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s5 = "I'm on my way to deliver a message, so I cannot escort you personally..."
    for char in s5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s6 = "However I can transport you there or anywhere else in his Sanctum on Mount Olympus."
    for char in s6:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s7 = "Chronos is just below and he will certainly test you when you meet him..."
    for char in s7:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(c)
    print()
    print("HERMES will transport you:")
    time.sleep(a)
    print("Path #1: Continue below to face Chronos.")
    time.sleep(a)
    print("Path #2: Read: 'The Secrets of time.'")
    time.sleep(a)
    print("Path #3: Speak with Ares.")
    time.sleep(a)
    print("Path #4: Speak with Artemis.")
    time.sleep(a)
    print("Path #5: Speak with Apollo.")
    time.sleep(a)
    print()
    second_path = input("Which path will you choose? (1/2/3/4/5): ")
    if second_path == '2':
        path2_2()
    elif second_path == '3':
        path1_1()
    elif second_path == '4':
        path1()
    elif second_path == '5':
        path2()
    else:
        print()

    print("You continue down the vines until you reach the bottom.")
    time.sleep(a)
    print("You see a small old woman next to the largest red and black iron-wrought double-doors you've ever seen.")
    time.sleep(a)
    print('The old woman calls out to you')
    time.sleep(a)
    s8 = "...Hello there, young traveler!"
    for char in s8:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    s9 = "...My name is Moirae, I am in great need of help..."
    for char in s9:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    s10 = "...I know who you seek, Chronos is just beyond this door."
    for char in s10:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    s11 = "...If you enter, you may speak with him and restore your freedom."
    for char in s11:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    s12 = "...But before you do so, would you take me home?..."
    for char in s12:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    s13 = "...I am unable to escape this cold, dark cave on my own."
    for char in s13:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    s14 = "...The choice is yours"
    for char in s14:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(c)
    print()
    print("Path #1: Forget the old woman. Enter the doors and speak with Chronos.")
    time.sleep(a)
    print("Path #2: Honor the woman's request. Help Moirae return home safely.")
    time.sleep(a)
    third_path = input("Which path would you like to take? (1/2): ")
    if third_path == '1':
        path3_1()
    elif third_path == '2':
        path3_2()


def path3_1():
    print()
    print("...You begin walking toward the doors, ignoring Moirae's request")
    time.sleep(a)
    print("...I would help you out, but I am in a bit of a hurry, you understand. ")
    time.sleep(a)
    print("...You pull open the massive doors with all of your might and enter")
    time.sleep(a)
    print("...Standing now in the largest room, in front of the largest man you've ever seen.")
    time.sleep(a)
    print("...The room is dark, but you can see the source of the thunderous voice which calls out to you...")
    time.sleep(a)
    print()
    s1 = "Ah... I've been expecting you. But you're somewhat early..."
    for char in s1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    s2 = "...It appears you've taken a fairly hard route..."
    for char in s2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    s3 = "...Your vision is keen. You see through the darkness and the light..."
    for char in s3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    s4 = "...And your strength has grown from your travels."
    for char in s4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    s5 = "...However, there is still just one..."
    for char in s5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    s6 = "...One more thing you need to learn:"
    for char in s6:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    s7 = "...And learn you will."
    for char in s7:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    s8 = "...in time."
    for char in s8:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(c)
    intro()


def path3_2():
    print('You begin walking toward Moirae, honoring her request')
    time.sleep(a)
    print("I understand. I know what it's like to miss home... That's why I need to get out of here...")
    time.sleep(a)
    print("But before I walk through those doors, I promise that I'll get you home safely.")
    time.sleep(a)
    print()
    print("You kneel down in front of Moirae, allowing her to climb easily onto your back.")
    time.sleep(a)
    print("Standing up, you make your way back to vine wall to make your ascent.")
    time.sleep(a)
    print("Just as you grab the vines, the enormous red and black iron doors thrust open, slamming to a halt.")
    time.sleep(a)
    print("The largest man you've ever seen steps out and his thunderous voice which calls out to you...")
    time.sleep(a)
    print()
    s1 = "Ah... I've been expecting you. And you're right on time!..."
    for char in s1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    s2 = "It appears you've taken a very difficult route."
    for char in s2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    s3 = "Your vision is keen. You see through the darkness and the light."
    for char in s3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    s4 = "And your strength has grown from your travels."
    for char in s4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    s5 = "You've even put others needs before your own."
    for char in s5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    s6 = "You have learned everything I have to teach you."
    for char in s6:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    s7 = "So you may finally be free."
    for char in s7:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    s8 = "It's time to return..."
    for char in s8:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(3)
    print()
    print('THANK YOU FOR PLAYING!')


print()
print("      ###################")
print("      ##               ##")
print("      ##    Sanctum    ##")
print("      ##               ##")
print("      ###################")
print()
time.sleep(a)
print('Wha... What happened? Where am I?')
time.sleep(a)
print("It's too dark to see anything...")
time.sleep(a)
print()
game_start = input("Would you like to start the game? (Y/N):  ")
if game_start == 'n'.lower():
    print("Maybe next time...")
else:
    intro()
