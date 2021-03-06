# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#characters
define mus = Character("Mustafa")
define fird = Character("Firdaus")
define arif = Character("Arif")
define khai = Character("Khai")
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
image m1_1 = im.Scale("GS1.PNG",1279,720)
image m1_2 = im.Scale("GS2.PNG",1279,720)
image m2 = im.Scale("Designer.PNG",1279,720)
image m3 = im.Scale("upload.PNG",1279,720)
image m4 = im.Scale("mobileBlocks.PNG",1279,720)
image m5_1 = im.Scale("mobileConnect.PNG",1279,720)
image m5_2 = im.Scale("AICompanion.PNG",1279,720)
image m6_1 = im.Scale("build1.PNG",1279,720)
image m6_2 = im.Scale("build2.PNG",1279,720)
image m6_3 = im.Scale("build3.PNG",1279,720)
image ea1 = im.Scale("arduino.jpg",1279,720)
image ea2_1 = im.Scale("arduinoFullKit.webp",1279,720)
image ea2_2 = im.Scale("arduinoIDE.PNG",1279,720)
image ea2_3 = im.Scale("arduinoIDE2.PNG",1279,720)
image ea3 = im.Scale("ArduinoParts.png",1279,720)
image ea4_1 = im.Scale("arduinoPort.png",1279,720)
image ea4_2 = im.Scale("arduinoCode.PNG",1279,720)
image ea5 = im.Scale("blocklyduino.PNG",1279,720)
image ea6 = im.Scale("instructables.PNG",1279,720)
image ea7_1 = im.Scale("portGreys.jpg",1279,720)
image ea7_2 = im.Scale("sparksGogo.PNG",1279,720)
image erp1 = im.Scale("RPI.jpg",1279,720)
image erp2_1 = im.Scale("RaspPiStarterKit.PNG",1279,720)
image erp2_2 = im.Scale("NOOBS.PNG",1279,720)
image erp3_1 = im.Scale("RaspiParts.png",1279,720)
image erp3_2 = im.Scale("RPIGPIO.png",1279,720)
image essh1 = im.Scale("ESSH1.PNG",1279,720)
image essh2 = im.Scale("ESSH2.PNG",1279,720)
image essh3 = im.Scale("ESSH3.PNG",1279,720)
image essh4 = im.Scale("ESSH4.PNG",1279,720)
image evnc = im.Scale("VNC.PNG",1279,720)
image erp6 = im.Scale("raspPiProjects.PNG",1279,720)
image erp7 = im.Scale("crontab.PNG",1279,720)
image bb = im.Scale("breadboard.jpg",1279,720)

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

    arif "Oh yeahhh, time for mobile. I will be teaching on some MIT App Inventor, but basic ones as you really need to try it to understand"

    arif "What do you want to learn about?"

    jump MobileTopics

label MobileTopics:
    menu:
        "I want to learn more about you":
            jump lblArifIntro
        "Getting Started":
            jump lblGS
        "Designer Phase":
            jump lblDesigner
        "Uploading files":
            jump lblUpload
        "Block Phase":
            jump lblBlock
        "Connecting the Companion":
            jump lblConnect
        "Putting the app on your phone":
            jump lblExport

label lblArifIntro:
    hide arif_happy

    show arif_shocked:
        center
        yalign 0.2
    if arifIntro == 0:
        arif "Hmm, well... I guess a short intro won't hurt"

    elif arifIntro == 1:
        arif "Forreals?"


    if firdIntro == 1 and arifIntro == 0:
        show fird_test with moveinright:
            right
            yalign 0.2
        fird "I told you, this kid is a bit weird"
        hide fird_test with moveoutright
    if musIntro == 1 and arifIntro == 0:
        show mus_smirk with moveinright:
            right
            yalign 0.2
        mus "Ahh, you are a victim as well!"
        hide mus_smirk with moveoutright
    if khaiIntro == 1 and arifIntro == 0:
        show khai_smirk with moveinright:
            right
            yalign 0.2
        khai "WOHOOO go ahead! It is your time now!"
        hide khai_smirk with moveoutright

    $ arifIntro = 1

    hide arif_shocked

    show arif_happy:
        center
        yalign 0.2

    arif "My name is Arif, but you can call me Rif or Rip for short"
    arif "Not death rip okay hahaha"
    arif "I study with Fird from the start...like since 2015. We started our journey here together"
    arif "Who knows, one day I get to see you working here"

    arif "Well, that's all from me. What else you want to learn about?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another mobile topic":
            jump MobileTopics
        "I need to go now :/ ":
            hide arif_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblGS:

    scene m1_1 with dissolve

    arif "Alright, first enter the website given. If you can't see it clearly, the link is"
    arif "https://appinventor.mit.edu/"
    arif "Then press create apps. You will then have to login with your gmail account"
    arif "If you have a kidosol account, login with that email as it will be easier for us to track you and if you lose information on your email"
    arif "Else, you can ask the trainer to create one for you"

    scene m1_2 with dissolve

    arif "You will then come to the main screen after accepting all the agreements"
    arif "Press start new project to create a new project"
    arif "If you have a project before, or many projects before, they will be listed below on the webpage"
    arif "The website will automatically open the latest project you are working on, but you can always return to the main page and pick a different project"
    arif "You can pick a different project by pressing the project name"
    arif "So about creating a new project, once you click on it, you have to put a name"
    arif "If your name have spaces, it will be replaced with underscores ( _ )"

    scene bg_kroom with dissolve

    show arif_happy:
        center
        yalign 0.2

    arif "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another mobile topic":
            jump MobileTopics
        "I need to go now :/ ":
            hide arif_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblDesigner:
    scene m2 with dissolve

    arif "I'll compile most of the basic stuff in the designer here"
    arif "Let's start with number 1"
    arif "You can Add more screens to your app using the Add Screen button, then remove the extra screens using the Remove Screen button"
    arif "However, you cannot remove the first screen as that is your main screen"
    arif "You can navigate through your different screens by pressing the Screen 1 button"
    arif "Of course, it will show a different screen name based on the screen you are on"
    arif "Publish to Gallery is you publish your app to the gallery, which is like an online MIT repository to store all the apps published"
    arif "This allows other users to find your project through that gallery"

    arif "Now let's see number 2"
    arif "The pallette consists of the GUI(Graphical User Interface) components you can put in your app"
    arif "Almost every app needs a user interface in this modern times, it really helps make your app user friendly depending on how you use it"
    arif "I will go briefly on what some of them do"
    arif "User interface consists of the main interface in an app like textboxes and buttons"
    arif "Layout consists on how you want to organise your interface, such as putting four buttons in a single row"
    arif "Media consists of all those media components such as camera, sound for your app, a player to play songs maybe? Sound recorders and even text to speech are there!"
    arif "Drawing and animation is more to animating sprites"
    arif "Sensors contain components that app will use your phone to detect. Example, accelerometer sensor will execute a function if your phone is moving"
    arif "Storage is mostly for database, storing your item's information. Really handy for games!"
    arif "There are more I did not explain, go ahead and explore them!"

    arif "Number 3, halfway there dude, kinda!"
    arif "The viewer here will show you all the components you put in earlier."
    arif "Here is where you will drag your components from the pallette and change their properties using the the properties tab on the right"
    arif "Sometimes the display is not 100% accurate, but it is almost there"
    arif "Since some components are hidden like the sensors, they are by default unticked when you put them in"
    arif "The hidden components will not disturb the appearance of your application"
    arif "You can also change the responsiveness of the viewer to that of a tab and so, by default it is this phone size"

    arif "Number 4 is the components you input earlier from the pallette, and it have a lot in common with number 7"
    arif "You can select the component you insert, and change the properties as well"
    arif "Different components have different properties, but components of the same type can be given different properties"
    arif "Example, you have two buttons, the first button can have a font size of 30 pixels, while the second have 15 pixels"
    arif "You can also rename your components and delete them"
    arif "I recommend you to rename each component with a proper name as it will help you greatly in your coding"

    arif "Number 5 is to upload your files, I will teach you more on that in that specific section"
    arif "Number 6 is to switch between your designer phase and your block phase, where you will do your coding"
    arif "Phew, finally done! hahaha"


    scene bg_kroom with dissolve

    show arif_happy:
        center
        yalign 0.2

    arif "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another mobile topic":
            jump MobileTopics
        "I need to go now :/ ":
            hide arif_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd
label lblUpload:
    scene m3 with dissolve

    arif "Upload is used to upload assets like images and music"
    arif "First, click on the upload button"
    arif "You will then be greeted by this popup box"
    arif "DISCLAIMER: YOU CANNOT UPLOAD A FILE BIGGER THAN 4MB OR SO"
    arif "Keep that in mind when uploading an asset"
    arif "Ohh...how to upload? Click on choose file and pick the file you need to upload"
    arif "Then press okay. Easy!"

    scene bg_kroom with dissolve

    show arif_happy:
        center
        yalign 0.2

    arif "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another mobile topic":
            jump MobileTopics
        "I need to go now :/ ":
            hide arif_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblBlock:
    scene m4 with dissolve

    arif "Blocks are your coding"
    arif "MIT App Inventor makes it simple where you don't need to write code, but use the blocks based on how you want it to function"
    arif "Of course, this comes with limitation, but it is really good in introducing the concepts of mobile development"
    arif "And you can make some good apps with this as well!"
    arif "Alright, first of all, to access the blocks section, press the blocks button on the top right"
    arif "Now there are few types of blocks, the most common you will use are the built in ones and the ones you added from the components in the designer"
    arif "Remember, most components you used from the pallette actually has blocks for their coding"
    arif "The media shows the files you uploaded and you can even upload the files you uploaded"
    arif "Example, you can do it so that when you press a button, the background image and song change. Cool, amirite?"
    arif "Let's go through some of the built in blocks"
    arif "I will briefly explain on some of those that you will usually use"
    arif "Control is the condition blocks like if else"
    arif "Logic is boolean, like true, false, or if a condition is equal to a desired outcome"
    arif "This means that if the condition is satisfied, the app will do something, if not it will do something else or so"
    arif "Math contains mathematical operations from addition and substraction all the way to trigonometry"
    arif "Text is used to show a text, join texts together and even compare texts"
    arif "Lists are to store many data and use as well as link them together"
    arif "Example, you make a game, where each enemy will have different scores when killed. You can set one list for the enemy, another for the score"
    arif "And then implement them together"
    arif "Dictionaries usually store value with their keys. It is usually a pair, example, you can store like something like 'school : kidocode;'"
    arif "Of course, in blocks manner. The school is the value and kidocode is the key"
    arif "Colours are used to change the colour of something or so when your app does something. You can also mix colours together"
    arif "Variables are something you can use to store data, then manipulate it to make your app more functional"
    arif "Procedures are like functions, you can put your codes inside there, and call it and places you prefer."
    arif "It makes the blocks neater and not that messy as you can store a big chunk of code in one function block, and just use that function block for all those functions."
    arif "The components you use have their own specific blocks too, see how the example made a block where if you press the button, your app will talk and greet you!"
    arif "This is why I mentioned in the designer section to always rename your components to a name that defines its functions"
    arif "The backpack at the top right is where you can put your code in, and take it out. The concept is like copy pasting a big chunk of code"
    arif "The trash can at the bottom right is what you can use to delete your blocks"
    arif "There is even a warning and error provider at the bottom left near the media tab so that you can find your errors and solve them"
    arif "Warnings don't need to be solved, but on some occasions you need to fix them to make the app better"

    scene bg_kroom with dissolve

    show arif_happy:
        center
        yalign 0.2

    arif "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another mobile topic":
            jump MobileTopics
        "I need to go now :/ ":
            hide arif_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblConnect:

    arif "Imagine you code your app, but you did not realise there is an error"
    arif "Or if the app functioned as you want it to be."

    hide arif_happy

    show arif_smirk:
        center
        yalign 0.2
    arif "That would suck, wouldn't it HAHAH"

    hide arif_smirk

    show arif_happy:
        center
        yalign 0.2
    arif "That is why you need to connect your phone to the MIT App Inventor. I know what you are thinking, what if you don't have a smartphone?"
    arif "Well, you can use an emulator, there are a few steps, so I will give you the tutorial link here"
    arif "https://appinventor.mit.edu/explore/ai2/setup-emulator.html"

    arif "Now for those who have a smartphone and can support the app, search and download"
    arif "MIT App Companion"
    hide arif_happy

    show arif_shocked:
        center
        yalign 0.2
    show fird_test with moveinright:
        right
        yalign 0.2
    fird "Good news, last time the app is only on Android, now iOS users can enjoy it too!"
    arif "OI DON'T STEAL MY SCREENTIME!"
    fird "HEHEHEH SORRYYYYYY"
    hide fird_test with moveoutright

    hide arif_shocked

    show arif_happy:
        center
        yalign 0.2

    arif "So, where were we?"
    arif "A'ha"

    scene m5_1 with dissolve

    arif "Once you download the app, press on Connect, then AI Companion"

    scene m5_2 with dissolve

    arif "You will be greeted with this screen. Now here are the steps"
    arif "1. Make sure your phone and the device you are running the MIT AI2 website are using the same Internet connection"
    arif "2. Open your app and insert the code, but RECOMMENDED to scan the QR code"
    arif "3. ONCE YOU SCAN, DON'T PRESS ANYTHING OR IT WILL GLITCH AND YOU WILL HAVE TO RECONNECT"
    arif "4. IF CONNECTION PROBLEMS PERSISTS, RESET THE CONNECTION BY PRESSING CONNECT, RESET CONNECTION"
    arif "5. ALSO TRY ENABLING LEGACY MODE IF YOU CAN'T CONNECT"

    arif "The connection may reset and your app won't run the updated blocks on your phone"
    arif "If that happens, just reset the connection and click on AI Companion again(both done by pressing the connect button)"

    scene bg_kroom with dissolve

    show arif_happy:
        center
        yalign 0.2

    arif "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another mobile topic":
            jump MobileTopics
        "I need to go now :/ ":
            hide arif_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblExport:
    arif "When you finished your app, of course you might want it on your phone"
    arif "So how do we do it?"

    scene m6_1 with dissolve

    arif "First press the Build button, and you will have two options"
    arif "One is to built from a QR Code, where you will need a QR scanner app on your phone"
    arif "The second is through an apk, where you need to transfer through your phone(usually by cable) and install"
    arif "Note that you might have to disable some security on your smartphone to put the apps on your phone"

    scene m6_2 with dissolve

    arif "If you press either of them, you will see the progress bar building to either download the APK or show the QR code"

    scene m6_3 with dissolve

    arif "If you build with QR code, you will have to scan the QR code with your QR scanner, NOT YOUR MIT APP ALRIGHT?! Ahaha"

    scene bg_kroom with dissolve

    show arif_happy:
        center
        yalign 0.2

    arif "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another mobile topic":
            jump MobileTopics
        "I need to go now :/ ":
            hide arif_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd
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

    mus "Yooooo, I will teach about electronics"
    mus "Most notably, the Raspberry Pi and Arduino, as they are really useful in programming"
    mus "So, what are you interested in learning"

    jump ElecTopics

label ElecTopics:
    menu:
        "I want to know more about you!":
            jump lblMusIntro
        "I want to more about Arduino":
            jump ArduinoMenu
        "I want to more about Raspberry Pi":
            jump RaspberryPiMenu
        "What is the breadboard?":
            jump lblBreadboard
label lblBreadboard:
    scene bb with dissolve

    mus "This is a breadboard"
    mus "It is like an extension for your GPIO pins explained in the Arduino and Raspberry Pi sections"
    mus "It also works as a base for a circuit"
    mus "It is labeled with coordinates to make the circuit components easier to map"
    mus "Oh, the extension, imagine you used an Arduino and have many components that need Ground pins"
    mus "But your arduino have only 3 Ground pins"
    mus "You can use a jumper cable from your arduino and connect to the breadboard and you will have many Ground pins!"
    mus "But how do we know which pins are effected by the jumper cable?"
    mus "For the + and -, they are horizontal(left to right)"
    mus "Ideally, you will use the - for Ground pins and + for power (Example: the 5V of the Arduino)"
    mus "For the coordinates, it is vertical(top to bottom) BUT ONLY UNTIL THE MIDDLE"
    mus "Notice the middle line? The breadboard is split to two parts there"
    mus "So the top and bottom are two separate connections when you use the jumper cable"
    mus "But you can link them together. I wonder how. Hmm..."

    scene bg_kroom with dissolve

    show mus_happy:
        center
        yalign 0.2

    mus "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another electronic topic":
            jump ElecTopics
        "I need to go now :/ ":
            hide mus_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd
label ArduinoMenu:
    menu:
        "Introduction to Arduino":
            jump lblArduinoIntro
        "Getting Started":
            jump lblGSA
        "Arduino parts":
            jump lblArduinoPart
        "Some coding explanation":
            jump lblArduinoCode
        "Blocks":
            jump lblArduinoBlocks
        "Combine with other hardware":
            jump lblArduinoHardware
        "Troubleshoot greyed port":
            jump lblTroubleshootArduino

label lblArduinoIntro:
    scene ea1 with dissolve

    mus "Time to explain about the arduino!"
    mus "Arduino is a microcontroller"
    mus "Do you know what a microcontroller is?"

    menu:
        "I do!":
            call iKnowMC from _call_iKnowMC
        "Sorry, I don't":
            call iXKnowMC from _call_iXKnowMC
    mus "Arduino can be programmed using the Arduino IDE which uses C and C++ languages, which I will get into in the getting started section"
    mus "There are also many peripherals and hardware that can be combined with the Arduino that I will explain in more detail in the other sections"
    mus "Arduino have different models, make sure to research them before using the one you want for your project"
    mus "Each of them have their perks and disadvantages while some of them have different ways to connect to the computer to code"

    scene bg_kroom with dissolve

    show mus_happy:
        center
        yalign 0.2

    mus "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another electronic topic":
            jump ElecTopics
        "I need to go now :/ ":
            hide mus_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblGSA:

    mus "How do we get started with the Arduino? Well first of all, you need the kit"
    mus "You kidocode students will soon get the kbox, which will have all the equipment needed"
    mus "But if you want to buy them and you don't know what to buy, well..."

    scene ea2_1 with dissolve

    mus "You can buy the kit online from https://my.cytron.io/?r=1 or so"
    mus "They usually have the full set. The most important thing is"
    mus "The Arduino, breadboard, jumper cables, the electric components you need for your project like LED, buzzer and the USB cable(USB cable type A/B Standard USB 2.0 cable)"
    mus "Now, you need to download the software to code the Arduino"

    scene ea2_2 with dissolve

    mus "The website to download is"
    mus "https://www.arduino.cc/en/software"
    mus "Then pick the download option based on what Operating System you use (Windows/Linux/macOS) and version"

    scene ea2_3 with dissolve

    mus "You can then pick just download to download"
    mus "Or you can contribute to the creators and send them some money for their hard work"

    scene bg_kroom with dissolve

    show mus_happy:
        center
        yalign 0.2

    mus "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another electronic topic":
            jump ElecTopics
        "I need to go now :/ ":
            hide mus_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblArduinoPart:


    mus "I'll explain the important parts of the Arduino"
    mus "The External Power Supply is what you will use to give your Arduino power, through a power supply like a plug."
    hide mus_happy

    show mus_smirk:
        center
        yalign 0.2
    mus "Make sure the power supply you use is enough, or else you will burn the Arduino. LIKE A CERTAIN TRAINER HERE"
    show fird_test with moveinright:
        right
        yalign 0.2

    hide fird_test with moveoutright

    hide mus_smirk
    show mus_happy:
        center
        yalign 0.2

    scene ea3 with dissolve

    mus "You can also supply it with power through the USB plug when you connect to your device like a laptop or PC"
    mus "Through that, you can also upload your code to the Arduino and execute your code"
    mus "The pins with the black holders are called GPIO pins, short for General Purpose Input Output and it usually use male-to-male or male-to-female jumper cables"
    mus "The ground pins are where the negative of the components will usually go, like the short leg of an LED or a wire connecting to the short leg on the breadboard"
    mus "The digital input output pins are used to connect to the digital electronic components such as the long leg of an LED, the legs of an ultrasonic sensor, etc"
    mus "Kinda like the positives of the digital electronic components"
    mus "The TX and RX mean serial out and serial in(transceiver and receiver) and can be used to communicate with other hardware as well"
    mus "The Serial Ports vary from arduino models, example, some have one(like Arduino Uno) and others have three(like Arduino Mega ADK)."
    mus "The analog pins are like the digital input output pins but for analogue electronic components like temperature sensors"
    mus "The voltage in pin(Vin) is where you can put in the wire connector of a battery(with the negative going to ground)"
    mus "Making your project portable"
    mus "The 3.5 and 5V pins are to power other electronic components like a GPS Module, ultrasonic sensor and so"

    scene bg_kroom with dissolve

    show mus_happy:
        center
        yalign 0.2

    mus "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another electronic topic":
            jump ElecTopics
        "I need to go now :/ ":
            hide mus_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblArduinoCode:


    mus "First of all connect your Arduino to your coding device using the USB cable"
    scene ea4_1 with dissolve
    mus "Then open your Arduino IDE"
    mus "Then go to ports and always pick the last port on Windows. If on Linux or Mac, pick the port that shows the USB being used"
    mus "If those ports don't work, you can try the other ports"
    mus "If the port is greyed out or there are other problems, you need to do some troubleshooting, I will explain more about that in the troubleshooting topic"
    scene ea4_2 with dissolve
    mus "Now I will explain some of the basic coding"
    mus "Arduino IDE uses C and C++ coding."
    mus "void setup() is where you will define what pins you are using. OUTPUT means the component is using the output command(display or show something)"
    mus "INPUT will mean that it is accepting something, example, an ultrasonic sensor receiving the wave back or light sensor receiving the light to measure"
    mus "pinMode is to define which pin, in this case 13, will be used for what function, in this case output"
    mus "Please take note of the curly braces and semicolon ;, Thank you!"
    mus "void loop is where your programming will go, note that it will endlessly loop"
    mus "digitalWrite is for digital pins, where you define the pin you want to use and its function"
    mus "In this case, it is HIGH meaning the switch is closed and LOW means the switch is open"
    mus "Eh, switch, okay that might be a bit hard to understand"
    mus "Imagine you put an LED light. HIGH means the LED will turn on, LOW means it will turn off"
    mus "delay is like a pause, it uses milliseconds"
    mus "1000 milliseconds is 1 second, so 500 milliseconds is 0.5 seconds"
    mus "If you are using an LED, the pause will make the LED light up for 5 seconds, then turn off for 5 seconds, and repeat, making it blinking"
    mus "Remember, digitalWrite is for OUTPUT, digitalRead is for INPUT"
    mus "Once you done your code, you can verify if the code is correct with the tick button"
    mus "If there is a mistake, it will return an error message for you to fix it"
    mus "It will also tell you an error message if you upload your code(the arrow button near the tick)"
    mus "When you upload, it will prompt you to save your code. This is optional but please save it if you are doing a personal project"
    mus "This will put the code in your arduino and will execute it within the Arduino, making your device functional"
    mus "If you use the serial coding like printing text and so, you can see the output at the serial monitor(top right button that looks like a magnifying glass)"


    scene bg_kroom with dissolve

    show mus_happy:
        center
        yalign 0.2

    mus "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another electronic topic":
            jump ElecTopics
        "I need to go now :/ ":
            hide mus_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblArduinoBlocks:
    mus "So imagine you want to code BASIC arduino programs but don't know C or C++"
    scene ea5 with dissolve
    mus "Good news, there are blocks to help you!"
    mus "However, I need to repeat, this is for BASIC PROGRAMS"
    mus "Not everything will be on blocks"
    mus "Anyways, let's start. First, you can login kportal, press app studio and press electronics to access the blocks for arduino"
    mus "Or you can go to the blocklyduino website which is"
    mus "https://blocklyduino.github.io/BlocklyDuino/blockly/apps/blocklyduino/"
    mus "You can ignore the XML tab."
    mus "Instead, have a look at the left and right picture, the left shows the blocks tab where you combine the blocks"
    mus "The right shows the Arduino tab that converts the blocks to code"
    mus "You can then copy your code and paste it in Arduino IDE!"
    mus "Let me briefly explain some of the block types"
    mus "Logic is the condition like if else"
    mus "Control is to control your code's execution like delay and loops"
    mus "Math is to input math operators and numbers"
    mus "Text is to input string, usually it is to show the output on the Serial Monitor"
    mus "Variables have variable blocks to store, manipulate and call your code"
    mus "Functions have function blocks where you can store your code and call them many times"
    mus "Input/Output is where you will find the input blocks like digitalRead and output blocks like digitalWrite, the most important blocks"
    mus "Servo has some blocks to control the servo motor"
    mus "Grove Analog have some blocks to control certain analog electronic components"
    mus "Grove have some blocks to control certain digital electronic components"
    mus "Grove LCD have some blocks for the Arduino LCD Screen(separate hardware)"
    mus "Grove motor have a block with some commands for a DC Motor"

    scene bg_kroom with dissolve

    show mus_happy:
        center
        yalign 0.2

    mus "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another electronic topic":
            jump ElecTopics
        "I need to go now :/ ":
            hide mus_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblArduinoHardware:
    mus "Arduino can be combined with other hardware"
    mus "How? It depends on the hardware"
    mus "And it depends on everything you've learned so far"
    mus "All the ports, all the code"
    mus "I can't explain more on this part, it is something you have to experiment on your own"
    mus "As each hardware (Arduino compatible only) has different pins and ways to connect and function"
    mus "I can however, tell you where you can practice"
    scene ea6 with dissolve
    mus "https://www.instructables.com/circuits/arduino/projects/"
    mus "Here is where you can browse arduino projects"
    mus "Start by picking some easy projects, then keep on moving on to harder projects."
    mus "Keep on doing this and you will be really really REALLY good in arduino"
    mus "ALL THE BEST"

    scene bg_kroom with dissolve

    show mus_happy:
        center
        yalign 0.2

    mus "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another electronic topic":
            jump ElecTopics
        "I need to go now :/ ":
            hide mus_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblTroubleshootArduino:
    mus "Arduino, as most items, will sometimes run into a problem"
    mus "Most of the time it is the Arduino IDE"
    scene ea7_1 with dissolve
    mus "The main diagnosis is when your Arduino IDE ports are greyed or the USB connected to the Arduino is not detected"
    mus "Here are some ways to troubleshoot it"
    mus "The first is through the Arduino itself, check these conditions."
    mus "1. MAKE SURE THE USB CABLE IS WORKING, CHECK IF THE ARDUINO IS LIT UP WHEN CONNECTED TO YOUR CODING DEVICE"
    mus "2. IF YOU CONNECT TO DIFFERENT HARDWARE OR BREADBOARD, MAKE SURE YOUR GROUND IS NOT CONNECTED TO POSITIVE AND POWER IS NOT CONNECTED TO NEGATIVE"
    mus "3. MAKE SURE YOUR BREADBOARD AND ARDUINO ARE WORKING"
    scene ea7_2 with dissolve
    mus "Now let's check the Arduino IDE"
    mus "Sometimes your Arduino maybe a different version and doesn't include a built in driver"
    mus "First of all, connect your arduino."
    mus "Second, enter this website"
    mus "https://sparks.gogo.co.nz/ch340.html"
    mus "And follow the instruction based on your operating system"
    mus "Keep on doing this and you will be really really REALLY good in arduino"

    scene bg_kroom with dissolve

    show mus_happy:
        center
        yalign 0.2

    mus "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another electronic topic":
            jump ElecTopics
        "I need to go now :/ ":
            hide mus_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd
label iKnowMC:
    mus "Good! Alright, let's move on"

label iXKnowMC:
    mus "It's okay. Let me explain"
    mus "A microcontroller is a small computer on a single metal-oxide-semiconductor(the material) integrated circuit chip"
    mus "Semiconductor means it can partly condcut current"
    mus "A microcontroller contains one or more CPUs (Central Processing Units) along with memory and programmable input/output peripherals"
    mus "I will explain the input and output in the ports section later on"

label RaspberryPiMenu:
    menu:
        "Introduction to Raspberry Pi":
            jump lblRaspPiIntro
        "Getting Started":
            jump lblGSRP
        "Raspberry Pi parts":
            jump lblRaspPiParts
        "Controlling from Afar!":
            jump SSHMenu
        "Some coding explanation":
            jump lblRaspPiCode
        "Combine with other hardware":
            jump lblRaspPiHardware
        "Continuously run your Python Script":
            jump lblCron

label lblGSRP:
    mus "Oh boi this is going to be long"
    mus "I just try to cut it short"
    scene erp2_1 with dissolve
    mus "These are some things you need for your Raspberry Pi"
    mus "Note that some of these items will differ based on your Pi model"
    mus "Please research them first before buying"
    mus "The main things you need are:"
    mus "1. THE RASPBERRY PI"
    mus "2. MICROSD CARD (RECOMMENDED 32GB OR 16GB/8GB IF LIGHT USE)"
    mus "3. MICROSD CARD ADAPTER(DEPENDS ON YOUR LAPTOP) OR CARD READER"
    mus "4. HDMI CABLE"
    mus "5. HDMI CONVERTERS BASED ON YOUR RASPBERRY PI AND LAPTOP"
    mus "6. POWER CABLE(DEPENDS ON YOUR RASPBERRY PI MODEL)"
    mus "7. PERIPHERALS LIKE MOUSE, KEYBOARD"
    mus "8. USB HUB IF YOU ARE USING RASPBERRY PI OR NEED MORE USB PORTS"
    mus "9. USB CONVERTERS DEPENDING ON YOUR RASPBERRY PI"
    mus "10. DISPLAY (EXAMPLE: MONITOR)"
    mus "11. DEVICE LIKE LAPTOP OR COMPUTER"

    mus "Your HDMI cable is the important part as it will connect to a display like a monitor to use, like a computer haha."

    scene bg_kroom with dissolve

    hide mus_happy

    show mus_smirk:
        center
        yalign 0.2
    mus "Well, it is a microcomputer!"

    show fird_test with moveinright:
        right
        yalign 0.2

    fird "Lame joke"

    hide mus_smirk

    show mus_shocked:
        center
        yalign 0.2
    mus "Here comes the party pooper"
    mus "Please leave"

    fird "REEEEE"
    hide fird_test with moveoutright
    hide mus_shocked

    show mus_happy:
        center
        yalign 0.2

    mus "Alright, where were we?"
    mus "Ahh, alright, to setup!"
    mus "First take a micro SD card and use an adapter or card reader to connect it to your device"
    mus "First of all reformat the micro SD card if you have any items on it"
    mus "You can download any Operating System, but most recommended are Linux"
    mus "Mostly recommended is Debian OS"
    scene erp2_2 with dissolve
    mus "I usually like to use the noobs OS for my Raspberry Pi, you can follow this link"
    mus "https://www.raspberrypi.org/documentation/installation/noobs.md"
    mus "for the instructions"
    mus "Once you are done downloading the OS, extract it and transfer it to the SD Card or use an Imager"
    mus "Now insert the SD card in the Raspberry Pi, and power it up"
    mus "Connect your peripherals and display"
    mus "Follow the instructions given and you are done!"
    mus "Note that the update and installation will take a long time. If it gets frozen during installation, you can power off the Pi and power it on again"
    mus "Make sure your Pi has sufficient power and Internet Connection during this time"

    scene bg_kroom with dissolve

    show mus_happy:
        center
        yalign 0.2

    mus "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another electronic topic":
            jump ElecTopics
        "I need to go now :/ ":
            hide mus_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd
label lblRaspPiParts:
    scene erp3_1 with dissolve
    mus "These are parts of the Raspberry Pi"
    mus "Each Pi has different features, there are some similiar features like the GPIO pins and variant of the USB ports and so"
    mus "For this section, I will show you using a picture of the Raspberry Pi 3 Model B"
    mus "And I will explain the main features"
    mus "The USB ports are what you will use to connect your peripherals like your mouse"
    mus "The Camera Port is what you will use to connect a Raspberry Pi Camera for projects involving cameras like Computer Vision"
    mus "The Micro USB Power Input is what you will use to power the Pi"
    mus "They will give a power supply, but you can use your phone cable as well"
    mus "Just make sure there is sufficient power"
    mus "You can use the Ethernet slot to connect to the Internet via LAN Cable"
    mus "The MicroSD Card Slot is what you will use to put in your MicroSD card that has the Operating System as explained in the Getting Started section"
    mus "Then there are the GPIO pins which is universal for all the Raspberry Pi models"

    scene erp3_2 with dissolve
    mus "This picture already explains the GPIO pins. I just briefly explain it"
    mus "The jumper cables used for the GPIO pins are female-to-male or female-to-female"
    mus "The pins with V is to power other electronic components like a GPS Module, ultrasonic sensor and so"
    mus "Ground pins are wear the negative of the electronic components will use"
    mus "The GPIO pins are what you use to connect the pins of the electronic components, whether digital or analog"
    mus "The ID_SC and ID_SD pins can be used as normal GPIO pins"
    mus "Or attach EEPROM, which you need to research more on"
    mus "Or use an l2C bus(NOT POSSIBLE ON PI3"
    mus "They are known as GPIO pin 0 and pin 1"

    scene bg_kroom with dissolve

    show mus_happy:
        center
        yalign 0.2

    mus "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another electronic topic":
            jump ElecTopics
        "I need to go now :/ ":
            hide mus_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd
label lblRaspPiCode:
    mus "Honestly I can't say much bout this"
    mus "Why? Cause it is Python coding"
    mus "You will learn this in classes"
    mus "Also Firdaus have a section of it, as well as explaining on using other Python compilers"
    fird "WOW I GOT PRAISED"
    mus "Please, go away"
    fird ":("
    mus "Anyways, go to his section and look at the last topic to learn more about this"
    mus "All I can say is there are different Python libraries for different functions"
    mus "Heck, you can even use AI(Artificial Intelligence) with this"
    mus "If you are interested, try checking out something call Computer Vision"
    scene bg_kroom with dissolve

    show mus_happy:
        center
        yalign 0.2

    mus "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another electronic topic":
            jump ElecTopics
        "I need to go now :/ ":
            hide mus_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblRaspPiHardware:
    mus "Raspberry Pi can be combined with other hardware"
    mus "How? It depends on the hardware"
    mus "And it depends on everything you've learned so far"
    mus "All the ports, all the code, using it remotely to make it easier"
    mus "I can't explain more on this part, it is something you have to experiment on your own"
    mus "As each hardware (Raspberry Pi compatible only) has different pins and ways to connect and function if using GPIO pins"
    mus "You need to also take into account the coding, as Python has a lot of libraries and different codes"
    mus "Hence the projects are all dynamic"
    mus "I can however, tell you where you can practice"
    scene erp6 with dissolve
    mus "https://www.instructables.com/Raspberry-Pi-Beginner-Projects/"
    mus "Here is where you can browse beginner Raspberry Pi projects"
    mus "Start by picking some easy projects, then keep on moving on to harder projects."
    mus "Keep on doing this and you will be really really REALLY good in Raspberry Pi"
    mus "ALL THE BEST"

    scene bg_kroom with dissolve

    show mus_happy:
        center
        yalign 0.2

    mus "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another electronic topic":
            jump ElecTopics
        "I need to go now :/ ":
            hide mus_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd
label lblCron:
    mus "Imagine you want to make a project using your Raspberry Pi"
    mus "And you code it with Python"
    mus "Of course when you turn it on, you want it to run the Python script"
    mus "You don't want the user to always have to enter the Raspberry Pi and run the script manually...right?"
    mus "So how do we do that?"
    scene erp7 with dissolve

    mus "Thankfully, Raspberry Pi is usually Linux based, and it has a built in function called crontab"
    mus "crontab is like a scheduler"
    mus "So, how do we use the crontab?"
    mus "Firstly open the terminal"
    mus "Then input this code"
    mus "sudo crontab -e"
    mus "sudo means superuser do, it is like run with admin privileges"
    mus "You will be brought to this screen, now go to the very bottom and list:"
    mus "(Just in case the bottom part is not clear, here are the last two lines of the coding)"
    mus "@reboot python /home/pi/Desktop/PnCTracker/PnCTracker.py &"
    mus "* * * * * /home/pi/Desktop/PnCTracker/PnCTracker.py"
    mus "Anyways, at the bottom of the screen, list:"
    mus "1. When the python script will be executed, * * * * * is used for the time variables, it means always"
    mus "* means all"
    mus "2. The directory of the Python script"
    mus "This part of the code, I stole from Fird's final year project"
    fird "YOU WHAT?!"
    mus "Shh, CLASS IS IN SESSION!"
    fird "... :'("
    mus "Please ignore that guy, anyways, there are also some more keywords to explain"
    mus "@reboot means that the Python script with the full directory given will be executed everytime it reboots"
    mus "The & means forever"

    scene bg_kroom with dissolve

    show mus_happy:
        center
        yalign 0.2

    mus "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another electronic topic":
            jump ElecTopics
        "I need to go now :/ ":
            hide mus_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblRaspPiIntro:
    scene erp1 with dissolve

    mus "Time to explain about the Raspberry Pi!"
    mus "Raspberry Pi is a microcomputer"
    mus "Do you know what a microcomputer is?"

    menu:
        "I do!":
            call iKnowMComp from _call_iKnowMComp
        "Sorry, I don't":
            call iXKnowMComp from _call_iXKnowMComp
    mus "You need to setup the Raspberry Pi in order to make it work"
    mus "Then you can use the Pi itself since it is a computer."
    mus "The programming projects used is mostly Python, and there are already built in Python Editors there"
    mus "Raspberry Pi usually uses Debian, but it can use other operating systems, but mostly is Linux based"
    mus "I personally haven't seen windows(used to be able to) or MacOS on it, but you can search more on it"
    mus "There are many kinds of Raspberry Pi, and each have their own benefit and limitation"

    scene bg_kroom with dissolve

    show mus_happy:
        center
        yalign 0.2

    mus "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another electronic topic":
            jump ElecTopics
        "I need to go now :/ ":
            hide mus_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label iKnowMComp:
    mus "Good! Alright, let's move on"

label iXKnowMComp:
    mus "It's okay. Let me explain"
    mus "A microcomputer is a small, relatively inexpensive computer with a microprocessor as its central processing unit."
    mus "t includes a microprocessor, memory and minimal input/output circuitry mounted on a single printed circuit board."
    mus "It is useful for programming(especially Python) and working purposes"
    mus "You can also play some non-heavy games on it"
    mus "NON-HEAVY, so please for God's sake do not attempt to play PUBG or Fortnite on it"
    hide mus_happy

    show mus_smirk:
        center
        yalign 0.2

    mus "You don't want it to burn, do you?"
    mus "It won't really burn, but smoke might come out. If that happens, I will gradually show myself out"

    hide mus_smirk with moveoutright

    show mus_smirk with moveinright:
        center
        yalign 0.2

    mus "LOL"

label SSHMenu:
    mus "If you are like a certain someone"

    show fird_test with moveinright:
        right
        yalign 0.2

    hide fird_test with moveoutright

    hide mus_happy

    show mus_smirk:
        center
        yalign 0.2
    mus "You saw that?"

    hide mus_smirk
    show mus_happy:
        center
        yalign 0.2
    mus "You might be tired of always using your laptop and then changing the cable for using the Pi"
    mus "Hence, there are some methods you can use to remotely control the Raspberry Pi"

    menu:
        "VNC":
            jump lblVNC
        "SSH":
            jump lblSSH

label lblVNC:
    mus "This is Firdaus favourite"

    scene evnc with dissolve

    mus "To do this, you first need to make a VNC account. It is free, but you can only connect 5 devices"
    mus "For more, you have to pay"
    mus "VNC can be used to connect devices besides Pi as well, but we are only going to focus on Pi now"
    mus "Now, there are two types of VNC"
    mus "VNC Viewer and VNC Server"
    mus "VNC Viewer will be downloaded on the device you want to use to remotely control the Pi"
    mus "VNC Server will be downloaded on the Pi"
    mus "Once you are done, follow the instructions from here"
    mus "https://magpi.raspberrypi.org/articles/vnc-raspberry-pi"
    mus "for the Pi and the VNC Viewer"
    mus "And you can control your Pi from the VNC Server from just clicking the device's name"
    mus "PLEASE NOTE THAT THE PI AND DEVICE NEEDS WIFI FOR THIS TO WORK"
    mus "On certain Pis like Raspberry Pi Zero, the connection might be slower and laggier due to the RAM"

    scene bg_kroom with dissolve

    show mus_happy:
        center
        yalign 0.2

    mus "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another electronic topic":
            jump ElecTopics
        "I need to go now :/ ":
            hide mus_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblSSH:
    mus "SSH stands for Secure Shell Protocol where you control services securely over an unsecured network"
    mus "For this method, I am going to show you steps based on https://itsfoss.com/ssh-into-raspberry/"
    mus "NO COPYRIGHT PLZ THNX"
    mus "ALSO FOR SSH, YOUR DEVICE AND THE PI MUST USE THE SAME INTERNET CONNECTION"
    mus "AND YOU WILL CONTROL YOUR PI TERMINAL, NOT INTERFACE"


    scene essh1 with dissolve

    mus "First, go to the Raspberry Pi configuration window by pressing the Pi logo and then Preferences"

    scene essh2 with dissolve

    mus "Then press the interface tab"
    mus "Enable SSH then restart the Pi"
    mus "If you are like me and prefer doing this through the terminal like VNC as well, you can use"
    mus "sudo raspi-config"

    scene essh3 with dissolve

    mus "We need to find the ip address of the Pi"
    mus "Open the terminal (Me likey)"
    mus "Then use the command ifconfig"
    mus "The ip address will usually be the inet of eth0 (ethernet 0)"
    mus "Unless you use a broadband as well, then you need to use the ip address of that broadband"
    mus "Don't worry, you can easily know which ip address to use"
    mus "Just don't use the subnet mask"

    scene essh4 with dissolve
    mus "Open the terminal on your device if you are using Mac or Linux"
    mus "If you are using windows, download Putty and use that"
    mus "Then use the command ssh pi@ip address"
    mus "Example: ssh pi@192.168.0.0"
    mus "I don't know whose ip I just put in but...sorry"
    mus "LOL those who know networking will probably be laughing now. Or cringing"
    mus "When prompted, press yes"
    mus "The default username is pi"
    mus "The default password is raspberry"
    mus "Now you will be able to use the Raspberry Pi terminal"

    scene bg_kroom with dissolve

    show mus_happy:
        center
        yalign 0.2

    mus "That's all for this section, what do you wish to do now?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another electronic topic":
            jump ElecTopics
        "I need to go now :/ ":
            hide mus_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd
label lblMusIntro:
    hide mus_happy

    show mus_shocked:
        center
        yalign 0.2
    if musIntro == 0:
        mus "Whaaaattttt?"

    elif musIntro == 1:
        mus "You really want to hear me talk about myself again?"

    if firdIntro == 1 and musIntro == 0:
        show fird_test with moveinright:
            right
            yalign 0.2
        fird "I told you, this kid is a bit weird"
        hide fird_test with moveoutright
    if arifIntro == 1 and musIntro == 0:
        show arif_smirk with moveinright:
            right
            yalign 0.2
        arif "I had to intro myself so you have to as well"
        hide arif_smirk with moveoutright
    if khaiIntro == 1 and musIntro == 0:
        show khai_smirk with moveinright:
            right
            yalign 0.2
        khai "WOHOOO go ahead! It is your time now!"
        hide khai_smirk with moveoutright

    $ musIntro = 1

    hide mus_shocked

    show mus_happy:
        center
        yalign 0.2

    mus "The name's Mustafa, call me Mus though"
    mus "Well, if you want to haha"
    mus "As what Daus said earlier, I am usually his partner in projects, especially programming ones"
    mus "I started here a bit late though"
    mus "I've been involved in many programming projects as well"
    mus "So...If I can do it. What is stopping you from being as good as me? Actually no, you can be better!"

    mus "So that is all for this topic, what you wanna know about next?"

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another electronic topic":
            jump ElecTopics
        "I need to go now :/ ":
            hide mus_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

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
            jump lblCSSJS

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
    if musIntro == 1 and khaiIntro == 0:
        show mus_smirk with moveinright:
            right
            yalign 0.2
        mus "Ahh, you are a victim as well!"
        hide mus_smirk with moveoutright
    if arifIntro == 1 and khaiIntro == 0:
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
        "I want to learn another web topic":
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

    scene bg_kroom with dissolve

    show khai_happy:
        center
        yalign 0.2

    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another web topic":
            jump WebMenu
        "I need to go now :/ ":
            hide khai_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblBRP:
    scene w2 with dissolve
    khai "This is a simple part"
    khai "These two codes are used to put the next element(text, image, etc) on the next line"
    khai "Difference is br, short for break line, will put the next element immediately on the next line"
    khai "However, the p tag, short for paragraph, will usually skip a line before and after the element, making an extra space"
    khai "Simple, right?"

    scene bg_kroom with dissolve

    show khai_happy:
        center
        yalign 0.2
    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another web topic":
            jump WebMenu
        "I need to go now :/ ":
            hide khai_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblHeading:
    scene w3 with dissolve
    khai "Now let's get into headings"
    khai "Headings have built in paragraph and bold behaviours, making you not having to manually put a breakline or paragraph and change the boldness of the text"
    khai "There are only 6 headings, those after h6 will be counted as h6"
    khai "The sizing decreases from h1 to h6 where h1 is the largest and h6 is the smallest"
    khai "Simple, right?"

    scene bg_kroom with dissolve

    show khai_happy:
        center
        yalign 0.2
    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another web topic":
            jump WebMenu
        "I need to go now :/ ":
            hide khai_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblImages:
    scene w4 with dissolve
    khai "Wow Images! Beautiful, amirite?"
    khai "Images are important in most websites. Not only do they make the website looks nicer, but they also explain information that is easier to understand for a certain audience"
    khai "The basic code of inserting an image is <img src='' /> The / is optional as seen in the image"
    khai "But it is a good practice to make it /> . Why the pic doesn't show that? Well... wrong screenshot moment"
    khai "src stands for source, which is where the image is. If you are using a custom compiler, you can download the image and insert the path in the src"
    khai "For example, <img src='khai/somepic.png'>"
    khai "But you can also use the image link. For example"
    khai "Go to google images, find an image you like and click it. You can click it again to go to the website that has that image"
    khai "Sometimes you need to click it to get its true resolution(the width and height of the image)"
    khai "Then right click the image, copy the image link / address/ location and you will get the link as shown in the example"
    khai "Of course the links will be different, and have different lengths as well"
    khai "You can also change the height and width of the image by adding a height and width attributes respectively"
    khai "You can also put an alt attribute, which will show text if the image is broken(wrong link or no Internet)"
    khai "It is important to put a brief keyword of what the image for the alt attributes so that the user will understand what the image is about if they can't see it"

    scene bg_kroom with dissolve

    show khai_happy:
        center
        yalign 0.2
    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another web topic":
            jump WebMenu
        "I need to go now :/ ":
            hide khai_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblLinks:
    scene w5 with dissolve
    khai "Alrighttt let's talk about links! We call them hyperlinks!"
    khai "These are used to navigate to different webpages or different sections of the same page. Uuu convenient!"
    khai "Let's have a look at the example. I did not complete the link to explain further about the code(Let's just stick with that, it is not like I forget or anything)"
    khai "Let's break it down one by one"
    khai "a stands for anchor, which is a placeholder to define a hyperlink."
    khai "href is like reference to the URL(Uniform Resource Locator) which it the link you put between the ''"
    khai "For example, I want to go to <a href='https://www.facebook.com'>Facebook</a>"
    khai "Yo yo hold up, why do we have something between the a tags? Like Facebook or Fire Emblem from the picture?"
    khai "Well those will be the words that when click, will navigate to the link given"
    khai "You can also use pictures instead of text between there. Try it!"

    scene bg_kroom with dissolve

    show khai_happy:
        center
        yalign 0.2
    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another web topic":
            jump WebMenu
        "I need to go now :/ ":
            hide khai_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblStyle:
    scene w6 with dissolve
    khai "There is a lot to explain about this, so I'll just keep it short and sour. Just kidding, short and sweet"
    khai "They are also commonly known as CSS files"
    khai "So styles are used to make your websites nicer. Like how HTML is the skeleton, styles are your features, your skin, hair etc etc"
    khai "There are many different ways for you to use styles but I will only touch on the style tag for now. The rest, you have to explore!"
    khai "There are 3 basics in styling using the style tag"
    khai "The first is using the tag name followed by the curly brackets, and put the styles you want inside"
    khai "This will make all of the tags with the same name have the same style. But what if you want only a specific tag?"
    khai "You can use the class or id"
    khai "Define the tag with a class or id followed by a name as shown in the example"
    khai "To link a class with the class name style, put a . before the class name"
    khai "For id, use #"
    khai "Again, there are many styles and many ways to do so, but you need to explore and test them yourself to fully grasp the concept"

    scene bg_kroom with dissolve

    show khai_happy:
        center
        yalign 0.2
    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another web topic":
            jump WebMenu
        "I need to go now :/ ":
            hide khai_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblScript:
    scene w7 with dissolve
    khai "Another main part of making a website besides the style is the scripts. Scripts have many functions. Too much to list"
    khai "Some of them are animations, changing the code so that one code can display different text based on certain conditions"
    khai "It is a very powerful tool. It uses Javascript"
    khai "If HTML is the skeleton, Javascript is how the body works"
    khai "In this example, I will show you how to manipulate an id using this"
    khai "First, define an empty paragraph tag(You can use headings or so if you want) with an id"
    khai "Now add a script tag."
    khai "Notice the code written, document usually represents the web page."
    khai "getElementById is followed by the name of the ID you want to change."
    khai "innerHTML returns the HTML content of an element"
    khai "This is only basic use of Javascript."
    khai "Please study more on it, it will help you a lot in the future(alongside TypeScript)"

    scene bg_kroom with dissolve

    show khai_happy:
        center
        yalign 0.2
    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another web topic":
            jump WebMenu
        "I need to go now :/ ":
            hide khai_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd

label lblCSSJS:
    scene w8 with dissolve
    khai "When you use a programming editor, it is best practice to separate your files as shown to make it more organised"
    khai "It looks like a small matter but trust me, it will greatly help"
    khai "Now in the previous parts I explained about styles and scripts, it is recommended you read that first if you haven't"
    khai "Let's separate the style codes and script codes to different files"
    khai "Style codes will go in a file with the .css extension, and scripts with the .js extension(Nowadays, also .ts)"
    khai "And the main html codes will go in a file with a .html extension"
    khai "See how they are linked with each other?"
    khai "CSS is linked to the HTML by using the <link rel='stylesheet' href='css file name'/>"
    khai "Yes I forgot the / again"
    khai "To link Javascript, you will use the script tag as shown, and put the name of your .js file in the src. Don't forget your quotations '' !"
    khai "You can link different HTML files with each other, and each file can be linked to different CSS and JS files"
    khai "With this knowledge, you have a basic idea of making a simple website"
    khai "What are you waiting for? Go and try it for yourself! "

    scene bg_kroom with dissolve

    show khai_happy:
        center
        yalign 0.2
    menu:
        "I wish to learn a different topic":
            jump topicsToLearn
        "I want to learn another web topic":
            jump WebMenu
        "I need to go now :/ ":
            hide khai_happy with moveoutright
            show fird_test with moveinright:
                center
                yalign 0.2
            jump lblEnd
label lblEnd:
    stop music fadeout 3.0
    play music "audio/DFInstrumental.mp3" fadein 3.0
    fird "I see you finish your classes."
    hide fird_test with moveoutright
    show arif_happy with moveinright:
        center
        yalign 0.2
    arif "Hope to see you again!"
    hide arif_happy with moveoutright
    show mus_happy with moveinright:
        center
        yalign 0.2
    mus "Remember to keep on learning and improving!"
    hide mus_happy with moveoutright
    show khai_happy with moveinright:
        center
        yalign 0.2
    khai "All the best!"
    hide khai_happy with moveoutright
    show fird_test with moveinright:
        center
        yalign 0.2
    fird "See you! Hope you enjoy today and hope to see you again! ^_^"
    stop music fadeout 3.0
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
            call iKnowCT from _call_iKnowCT
        "What is Computational Thinking??":
            call whatIsCT from _call_whatIsCT

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
