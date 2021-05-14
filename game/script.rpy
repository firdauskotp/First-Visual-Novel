# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#characters
define mus = Character("Mustafa")
define fird = Character("Firdaus")
define arif = Character("Arif")
define khai = Character("Khairi")
#images
image bg_kroom = im.Scale("kroom.jpg",1420,900)
image p1 = im.Scale("p1.PNG",1279,720)
image p2 = im.Scale("p2.PNG",1279,720)
image p3 = im.Scale("p3.PNG",1279,720)
image p4 = im.Scale("p4.PNG",1279,720)
image p5 = im.Scale("p5.PNG",1279,720)
image p6 = im.Scale("p6.PNG",1279,720)
image p7 = im.Scale("p7.PNG",1279,720)
image w1 = im.Scale("webBasic.PNG",1279,720)
image w2 = im.Scale("webParaBr.PNG",1279,720)
image w3 = im.Scale("webHeading.PNG",1279,720)
image w4 = im.Scale("webImage.PNG",1279,720)
image w5 = im.Scale("webLinks.PNG",1279,720)
image w6 = im.Scale("webStyle.PNG",1279,720)
image w7 = im.Scale("webScript.PNG",1279,720)
image w8 = im.Scale("webCJ.PNG",1279,720)

# image fird_main:
#     Character("Firdaus")
#     xpos 0.0
#     ypos 50.0
# The game starts here.

#variables
default askPersonalIntro = 0
default firdIntro = 0
default kidoIntro = 0
default arifIntro = 0
default khaiIntro = 0
default musIntro = 0
default firdToMove = 0
default arifToMove = 0
default khaiToMove = 0
default musToMove = 0


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_kroom with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show fird_test:
        center
        yalign 0.2
    # show fird_main

    play music "audio/TheTaskAtHand.mp3" fadein 3.0
    # These display lines of dialogue.

    fird "Welcome to Kidocode! I will be your trainer for today!"

    fird "Are you ready for your class? Or do you want an introduction?"

    jump firstChoice

label goodBye:
    fird "Ahh I see, it's okay. See you next time!"
    return

label imReady:
    $ firdToMove = 1

    fird "Alright, let's get started!"

    fird "So we offer a few classes here, and my friends, who are also trainers here, will teach you the different classes based on our speciality"

    fird "Of course, we will just go through it, not explain fully though, that is for when you study later!"

    fird "I will guide you through Python!"

    fird "Let's introduce the other three trainers shall we?"

    show arif_happy with moveinright:
        right
        yalign 0.2

    fird "This is one of my close friends, Arif, he will guide you through mobile!"
    arif "Glad to meetcha! You can call me Rif"
    hide arif_happy with moveoutright


    show mus_happy with moveinright:
        right
        yalign 0.2

    fird "This is another of my close friends and project partner usually, Mustafa, he will guide you through electronics!"
    mus "Howdy, just call me Mus, alright?"
    hide mus_happy with moveoutright

    show khai_happy with moveinright:
        right
        yalign 0.2

    fird "This is an old friend of mine, Khairi. He will guide you through web development"
    khai "WOHOOO, just call me khai for short. Can't wait to teach you!"

    hide khai_happy with moveoutright




    fird "Now that you have been introduced to the different trainers and classes, which one would you like to study first?"

    jump topicsToLearn

label lblPy:
    $ firdToMove = 1

    if musToMove == 1:
        hide mus_happy with moveoutright
        $ musToMove = 0
    elif arifToMove == 1:
        hide arif_happy with moveoutright
        $ arifToMove = 0
    elif khaiToMove == 1:
        hide khai_happy with moveoutright
        $ khaiToMove = 0
    show fird_test with moveinright:
        center
        yalign 0.2

    stop music fadeout 3.0
    play music "audio/fe4bothk.mp3" fadein 3.0

    fird "We have a few activities in Python. Which one do you want to learn about?"

    jump PythonMenu

label topicsToLearn:
    menu:
        "Python":
            jump lblPy
        "Mobile App":
            jump lblMob
        "Electronics":
            jump lblElec
        "Web Development":
            jump lblWeb
        "I am done learning!":
            jump lblEnd

label PythonMenu:
    menu:
        "Turtle Graphics!":
            jump lblp1
        "Loop":
            jump lblp2
        "Variables":
            jump lblp3
        "Functions":
            jump lblp4
        "Conditions":
            jump lblp5
        "Lists":
            jump lblp6
        "Python Editor":
            jump lblp7


label lblp1:
    scene p1 with dissolve

    fird "Let's have a look at the codes shall we?"
    fird "So this is how you make the turtle in Python"
    fird "You can use this for all kinds of graphics, these are just SOME of the basics"
    fird "The first part of the code is defining the Turtle object"
    fird "If you use another compiler, you need another line of code, but we will get into that in the Python Editor section"
    fird "tom = Turtle() is defining the name of the turtle, you can use any name, BUT NOT KEYWORDS!"
    fird "You can define the shape and colour of the turtle as well. Colour is spelled color as it follows the american syntax"
    fird "There are specific shapes and colours, where if you don't follow them, the turtle will just be a default arrow shape and black colour respectively"
    fird "You can set the turtle shapes, I heard, but that is for you to experiment"
    fird "Turtle has 4 directions, forward, backward, left and right. Notice the turtle drawing"
    fird "Where the turtle moves depend on its CURRENT position"
    fird "Also, the trainer will usually say MOVE for FORWARD and BACKWARD, and TURN for LEFT and RIGHT"
    fird "In the parantheses, the brackets that is, a number is written, right? That number for forward and backward is the pixel to move"
    fird "While for the left and right, it is the angles. You will learn about them soon enough"
    fird "Also notice those with the quotations, that are the  ' ', those are what we call strings"
    fird "Strings are what we use for text, don't use it for integers(numbers)!"
    fird "There is a code not included in the picture that is the penup() and pendown() feature. This is to make spaces between drawings"
    fird "There is also a code called goto, which is used for the coordinates"
    fird "There is another code there for the circle. In the parantheses, remember we use this name for brackets, is the radius of the circle"
    fird "Radius is half of the circle, that means the turtle drew from the halfway point"
    fird "Saves you the trouble of drawing a circle eh hahahaha"
    fird "Finally, there is also begin_fill() and end_fill() which are used to fill in the shape drawn between them. In this case, it fills in the circle"
    fird "Here are also some tips, a straight line has an angle of 180 degrees"
    fird "To get the exterior angle, you can use 180-interior angle"
    fird "Exterior angle is the angle outside the shape while interior angle is the angle inside the shape"
    fird "As you can see, you can draw a lot of things using the Python Turtle Graphics. Go ahead and use your creativity"

    scene bg_kroom with dissolve

    show fird_test:
        center
        yalign 0.2

    fird "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another python topic":
            jump PythonMenu
        "I need to go now :/ ":
            jump lblEnd


label lblp2:
    scene p2 with dissolve

    fird "Let's have a look at the codes shall we?"
    fird "So this is how you make loops in Python"
    fird "For now I will be explaining about loops using Turtle Graphics. I will explain using mathematics concepts in future steps as there is much to break down"
    fird "Let's make the speed 0 first. 0 is the fastest speed, like SONICCCCCC"
    fird "A loop is something we can make so that we don't have to write the same codes again."
    fird "To make a loop, we need to use the syntax where we use for count in (1,2,3,4) (It is square brackets actually. I can't put the closing square bracket due to the limitation of this software)"
    fird "That method is where we use a list, but in case we want to make 100 iterations(repetitions), you can use for x in range(100)"
    fird "Note that count, x, and all those after the keyword for is just a name, it can be anyname AS LONG AS IT IS NOT A KEYWORD"
    fird "I advise you to use different loop names for each loop to easily differentiate them and make it a good programming practice"
    fird "Notice the space after the for line? That is what we call indentation(it consists of 4 spaces per indentation) and it is important"
    fird "Indented codes under the loop are what will be repeated"
    fird "If you want to fill in the shape using a loop, please put the begin and end fill outside that loop, so that it will fill in the shape, not the line"
    fird "There are also nested loops, meaning loop in loop, where the first loop will be executed first, then the program will wait for the second and so on loops to be executed"
    fird "before going on with the rest of the codes. There can be more than two loops in a nested loop"
    fird "Also notice that you can calculate the angle using 360 / the number of sides. This is because 360 is the total exterior angle"

    scene bg_kroom with dissolve

    show fird_test:
        center
        yalign 0.2

    fird "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another python topic":
            jump PythonMenu
        "I need to go now :/ ":
            jump lblEnd

label lblp3:
    scene p3 with dissolve

    fird "Let's have a look at the codes shall we?"
    fird "So this is how you make variables in Python"
    fird "Variables are important as without them, you will have to write much longer codes"
    fird "Variables can also be manipulated, where you can use mathematical operations to manipulate them, hence making your program more dynamic and functional"
    fird "You can use any name for your variables as long as it fits the rules(no keywords, cannot start with numbers)"
    fird "The value is then assigned to the variable to be used for the future. Simple, right?"
    fird "You can also use input, which is where you ask the user for their value instead of defining it itself, making there be many answers to a single equation"
    fird "You will know that you have to use input if you see the keywords READ, USER, INPUT, KEYBOARD"
    fird "To use input, the syntax is datatype(input('message')) where the message is optional"
    fird "Some of commonly used datatypes are int (integer which is whole number), float(decimal) and string(text)"
    fird "When input is used, a box will appear. Input the value you desire and match the datatype of the input"
    fird "Print is used to print the output, but it only shows the output for the programmer, it is not really stored in the system"
    fird "How to store it in the system? Simple! Use return instead! I will explain more on that in the functions' section"

    scene bg_kroom with dissolve

    show fird_test:
        center
        yalign 0.2

    fird "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another python topic":
            jump PythonMenu
        "I need to go now :/ ":
            jump lblEnd

label lblp4:
    scene p4 with dissolve

    fird "This is an important lesson"
    fird "Functions are something you define once, but can call many times"
    fird "Imagine like your schoolbag that have many books, you only take out the book you need during the correct lesson"
    fird "That is how functions work, you only need to call the function when you need them, or else they won't be executed"
    fird "The syntax is def functionName(paramaters which are optional):"
    fird "Like loops, you need the indentation for functions to work"
    fird "The function name can be any name but needs to follow the rules like no keywords, cannot start with number etc"
    fird "You can also use parameters which act like variables when calling the function"
    fird "Note that parameters follow the order from left to right and separated by the commas"
    fird "You need to call the function to execute it"
    fird "I really advise you to make all the functions first then call it to make it look more orderly"
    fird "You will also learn how to use return"
    fird "See how return doesn't show the output unless you put it in print?"
    fird "That is because print is for the developer to see the process, but only see, not send the data to be processed"
    fird "return is used to send the data back to the program, where it will be processed to be used in the system"

    scene bg_kroom with dissolve

    show fird_test:
        center
        yalign 0.2

    fird "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another python topic":
            jump PythonMenu
        "I need to go now :/ ":
            jump lblEnd

label lblp5:
    scene p5 with dissolve

    fird "This is a fairly simple lesson"
    fird "Conditions are used to check whether a statement is true or false"
    fird "Actually even this program uses the if else when you see the dialogue changed hahaha"
    fird "Conditions are used to change how the program works when the statement is true or false"
    fird "As seen in the code, there are 3 basics to conditions that are if, elif and else"
    fird "if is used to check the first statement, elif is used to check the further statements, else is the default statement if all the above are false"
    fird "There are many operators that can be used in conditions like the greater than sign, lesser than, and, or, not"

    scene bg_kroom with dissolve

    show fird_test:
        center
        yalign 0.2

    fird "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another python topic":
            jump PythonMenu
        "I need to go now :/ ":
            jump lblEnd

label lblp6:
    scene p6 with dissolve

    fird "This is a bit hard at the start, but with much practice will be easy"
    fird "Lists are something that store data(called elements) in specified positions(called index)"
    fird "Index are seperated by , and starts from 0"
    fird "Example for the first list(lists use the square bracket), red is index 0, blue is index 1 and so on"
    fird "There are two basic ways to use the lists"
    fird "The first method is to make a loop with the range, then call the list by using the syntax listName(loopname) where the () is actually square brackets"
    fird "I can't put a complete square bracket here due to the limitations of this software"
    fird "The second is to use the listName itself as the range, that way, you just need to put the loopName when calling the list"
    fird "This is because you are directly using the list instead of before where you are using range and need to manually call the list"
    fird "The bottom part, notice how a variable is defined, but when printed, the variable changed value"
    fird "This is because the variable is added by the element of the next index until the list is completed"
    fird "0 is assigned as it will not effect the addition of the code"
    fird "So it will be something like 0=0+2, 2=2+3, 5=5+4 and so on until 6"
    fird "You need to always practice this, then it will become easy"

    scene bg_kroom with dissolve

    show fird_test:
        center
        yalign 0.2

    fird "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another python topic":
            jump PythonMenu
        "I need to go now :/ ":
            jump lblEnd

label lblp7:
    scene p7 with dissolve

    fird "This is using Python IDLE as an example"
    fird "Notice how there are two different files, one is the shell, another is a new file"
    fird "For the shell, you can just type in the code and press enter, and it will execute immediately"
    fird "Downside is if you make a mistake, you might have to redo some codes"
    fird "Also, in a different compiler, if you want to use the Turtle Graphics,"
    fird "You need to import the library using from turtle import *"
    fird "* means all, so you are importing all the functions of the turtle library"
    fird "You can also code freely in the file, using this, even if you make a mistake, you can easily correct it"
    fird "You have to save first before running the code though, and the output will usually be displayed on the Shell"
    fird "If you use the Turtle Graphics, a new window will be shown where the drawing is done"
    fird "Don't press that window as it can make the window go unresponsive"

    scene bg_kroom with dissolve

    show fird_test:
        center
        yalign 0.2

    fird "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another python topic":
            jump PythonMenu
        "I need to go now :/ ":
            jump lblEnd

label lblMob:
    $ arifToMove = 1

    if firdToMove == 1:
        hide fird_test with moveoutright
        $ firdToMove = 0
    elif musToMove == 1:
        hide mus_happy with moveoutright
        $ musToMove = 0
    elif khaiToMove == 1:
        hide khai_happy with moveoutright
        $ khaiToMove = 0


    show arif_happy with moveinright:
        center
        yalign 0.2
    stop music fadeout 3.0
    play music "audio/fe4dia.mp3" fadein 3.0

    fird "We have a few activities in Python. Which one do you want to learn about?"

    jump topicsToLearn
label lblElec:
    $ musToMove = 1

    if firdToMove == 1:
        hide fird_test with moveoutright
        $ firdToMove = 0
    elif arifToMove == 1:
        hide arif_happy with moveoutright
        $ arifToMove = 0
    elif khaiToMove == 1:
        hide khai_happy with moveoutright
        $ khaiToMove = 0

    show mus_happy with moveinright:
        center
        yalign 0.2
    stop music fadeout 3.0
    play music "audio/fe4r.mp3" fadein 3.0

    jump topicsToLearn


label lblWeb:
    $ khaiToMove = 1

    if firdToMove == 1:
        hide fird_test with moveoutright
        $ firdToMove = 0
    elif musToMove == 1:
        hide mus_happy with moveoutright
        $ musToMove = 0
    elif arifToMove == 1:
        hide arif_happy with moveoutright
        $ arifToMove = 0

    show khai_happy with moveinright:
        center
        yalign 0.2
    stop music fadeout 3.0
    play music "audio/fe4lnd.mp3" fadein 3.0

    khai "Yoo so there are a few topics to learn, I'll touch on some of the basics, alright?"

    khai "Soo, what do you want to learn about?"

    jump WebMenu

label WebMenu:
    menu:
        "I want to know more about you":
            jump lblKhaiIntro
        "The structure of making a HTML code":
            jump lblWebStructure
        "Break Lines and Paragraphs":
            jump lblBRP
        "Headings":
            jump lblHeading
        "Images":
            jump lblImages
        "Links":
            jump lblLinks
        "Style":
            jump lblStyle
        "Script":
            jump lblScript
        "CSS and JS Files":
            jump lblCSS

label lblKhaiIntro:
    show khai_shocked:
        center
        yalign 0.2
    if khaiIntro == 0:
        khai "Gee really?"

    elif khaiIntro == 1:
        khai "One more?"


    if firdIntro == 1 and khaiIntro == 0:
        show fird_test with moveinright:
            right
            yalign 0.2
        fird "I told you, this kid is a bit weird"
        hide fird_test with moveoutright
    elif musIntro == 1 and khaiIntro == 0:
        show mus_smirk with moveinright:
            right
            yalign 0.2
        mus "Ahh, you are a victim as well!"
        hide mus_smirk with moveoutright
    elif arifIntro == 1 and khaiIntro == 0:
        show arif_smirk with moveinright:
            right
            yalign 0.2
        arif "I had to intro myself so you have to as well"
        hide arif_smirk with moveoutright

    khai "Well I guess it is okay"

    $ khaiIntro = 1

    hide khai_shocked
    
    show khai_happy:
        center
        yalign 0.2

    khai "My full name is a bit long, so I usually go by the nickname Khairi, or Khai for short"
    khai "Well I am actually an Aerospace Engineering student, but I am also a full timer here"
    khai "Firdaus and I, we gooooo wayyyy back"
    khai "Anyways, if I can be a good programming teacher although I am not from a programming background, it means that you will be better than me someday"

    khai "That's from me on this topic, what do you want to do next?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another python topic":
            jump WebMenu
        "I need to go now :/ ":
            hide khai_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblWebStructure:
    scene w1 with dissolve
    khai "Alright, so this is the main web structure"
    khai "This is HTML coding"
    khai "Imagine HTML as the skeleton of the body. It is basic, but it is the foundation of a human body"
    khai "First of all, understand the tags. There are open tags, example <html> and end tags, example </html>"
    khai "Most tags have an opening and closing tag, like a container"
    khai "Now the main structure, first of all you need the html tag"
    khai "Usually nowadays most compilers have that built in, but you need to do it as practice. It is the best practice"
    khai "Now we have the head, this is where most of the importing happens"
    khai "The contents of the head won't usually be visible, except the title tag which is the name of the tab (PS: open a google tab, and look at the name at the top)"
    khai "You can also import and link files like link a CSS and JS file. I will explain a bit of that in the last section later on"
    khai "The content in the <body> tag is what will usually be displayed on the screen"
    khai "As stated before, usually compilers have the body built in, but it is best practice to write it anyways"
    khai "That's from me on this topic, what do you want to do next?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another python topic":
            jump WebMenu
        "I need to go now :/ ":
            hide khai_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblBRP:
    scene w2 with dissolve
    khai "This is a simple"
    khai "These two codes are used to put the next element(text, image, etc) on the next line"
    khai "Difference is br, short for break line, will put the next element immediately on the next line"
    khai "However, the p tag, short for paragraph, will usually skip a line before and after the element, making an extra space"
    khai "Simple, right?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another python topic":
            jump WebMenu
        "I need to go now :/ ":
            hide khai_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd
label lblEnd:
    fird "See you! Hope you enjoy today and hope to see you again! ^_^"
    return

label firdIntroduction:
    if firdIntro == 0:
        fird "Ehh? Really? Alright then I guess..."

    elif firdIntro == 1:
        fird "Seriously, again?"

    fird "Here is where I would put my shocked face but I need to pay to remove backgrounds. Sigh"

    fird "Anyways, I will be your trainer for today"

    fird "My name is Firdaus, just call me fir, or fird, or daus hahaha. I used to be an intern here but now working here"

    fird "I used to have no experience in coding Python, but after hard work and dedication, I managed to make many projects using Python"

    fird "This game is one of it as well"

    fird "So, if I could do it, I am sure you can as well!"

    fird "What do you want to know about next?"

    $ askPersonalIntro = 1
    $ firdIntro = 1

    jump firstChoice


label kidocodeIntroduction:

    if kidoIntro == 0:
        fird "Sure! Sit tight!"
    elif kidoIntro == 1:
        fird "Again? Sure!"

    fird "Kidocode is first established in 2015"

    fird "It's main purpose is to teach computational thinking to kids"

    fird "Do you know what computational thinking is?"

    menu:
        "I do!":
            call iKnowCT
        "What is Computational Thinking??":
            call whatIsCT

    fird "Kids of many ages come here to learn to code"

    fird "We teach a lot of languages here, but mainly Python, Electronics and mobile applications"

    fird "I'll teach you that during your class!"

    $ kidoIntro = 1

    fird "What do you want to know about next?"

    jump firstChoice

label firstChoice:
    menu:
        "I'm ready to start my class!":
            jump imReady
        "May I have an introduction to this place?":
            jump kidocodeIntroduction
        "May I have your introduction?":
            jump firdIntroduction
        "I need to leave :/":
            jump goodBye

label whatIsCT:
    fird "It means solving problems like computer scientists!"

    fird "Computational Thinking, or let's refer to it as CT for short, refers to thought processes required in understanding problems and formulating solutions"

    fird "Example, what is the shortest way to exit the room? Why is this specific building closed today?"

    fird "During that time, you will be thinking about the reasons through certain CT concepts"

    fird "CT usually involves logic, assessment, patterns, automation and generalisation"

    fird "Most of your thinking concepts in certain situations actually uses CT whether you realise it or not! Hahaha"

    fird "Do you want me to repeat that?"

    menu:
        "Yeah!":
            fird "Alrighty then"
            jump whatIsCT

        "Nah!":
            fird "Cool!"
            jump iKnowCT

label iKnowCT:
    fird "Ahh I see, kids these days sure are smart!"
