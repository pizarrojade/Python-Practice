print ("Welcome...")
print ("To Untitled Document...")
print ('The Mini-Game...')

print () #blank line

print ("This is a fantasy, story-based game that highlights the importance of choosing your path wisely. You will be given two or more options that will alter the ending of the story.")
print ("But beware. Some endings are better than others. Take heed.")

print () #blank line

print (". . .")

print() #blank line

print ("It was a rainy day in the city while you're working your part-time job at the Library.") 
print ("Your boss, Alexa Levine, left you at the bookstore, locking the door while she went to an important buisness meeting.")
print ("It had been ages since anyone had come to the bookstore, but today, despite the rain, there came two solid knocks at the locked bookstore door.")

print () #blank line

#Will you open the door?

print ("Will you open it?")
print ( "1) Yes, it would be rude to leave a customer out in the rain.")
print ( "2) No, there's no way that someone is outside in the pouring rain.")

answer = int(input('Enter your answer 1-2: '))

if answer == 1: 
    print ("You decide to open the door, rain splatterin the front door as a handsome looking man walks into the library.")
elif answer == 2: 
    print ()
    print ("You decide not to open the door, not wanting to take chances alone in the library, but the man keeps knocking. Now, let me ask you again, will you open the door?")
    print ("1) Yes?")
    print ("2) YES!")
    int(input('Enter your answer 1-2: '))
    print () #blank space
    print ('Reclutantly, you open the door, rain splattering on the door mat as a handsome looking man walks into the library.')
else: 
    print ("That number was not an option. Please choose between option 1 and 2.")

print ()
#Will you help the strange man find the book he's looking for?

print ("The man walks in, completely ignoring you as he rounds the corner. You go back to your desk, watching him carefully.")
print ()
print ("He stands in the middle of the bookstore, seemingly looking for something. Becuase you're so kind, you start a warring mental debate. Will you ask him what he needs or let him wander?")
print ("1) I'll ask him. He might need something I can find quickly, then I can get him out of my hair.")
print ("2) I'll let him wander. I don't want to hold much conversation with him anyways.")

answer = int(input('Enter your answer 1-2: '))

if answer == 1: 
    print ("You decide to ask him whether he needs help, to which he replies he needs help finding a book called 'Song of the Chosen'. You type the book into your library computer, only to find that it doesn't exist. At least you don't have it.")
elif answer == 2:
    print ("You stay silent, watching warily as he stands around for a solid five minutes until eventually, he asks you for help. He says he's looking for a book called 'Song of the Chosen.'")
    print ("You type the book into your library computer only to find... it doesn't exist. At least you don't have it.")
else: 
    print ("That number was not an option. Please choose between option 1 and 2.")