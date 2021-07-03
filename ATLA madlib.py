#ATLA Intro Mad Lib Generator - binitaz (7/1/21)


#Loop back to this point once code finishes
loop = 1
while (loop < 10):
#All the questions that the program asks the user
    name = input("Enter your name: ")
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    p_noun2= input("Choose another plural noun: ")
    number = input("Enter a large number: ")
    celebrity = input("Enter a celebrity's name: ")
    noun2 = input("Choose another noun: ")
    noun3 = input("Choose one more noun: ")
    verb = input("Choose a verb ending in -ing: ")
#Displays the intro based on the users input
    print ("------------------------------------------")
    print ("Long ago, the",p_noun,"lived together in harmony.")
    print ("Then, everything changed when the",noun,"attacked.")
    print ("Only the",noun2,", master of all four",p_noun2,", could stop them,")
    print ("but when the world needed them the most, they vanished.")
    print ()
    print (number,"years passed and", celebrity,"and I discovered the new", noun2,)
    print ("a(n)",noun3,"bender", "named", name,",")
    print ("and although their",verb, "skills are great,")
    print ("they have a lot to learn before they're ready to save anyone.")
    print ("But I believe",name, "can save the world.")
    print ("------------------------------------------")
#Loop back to "loop = 1"
    loop = loop + 1
