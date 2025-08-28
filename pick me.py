

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("The Pick Me Test: Are YOU a pick me?")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

Yes = 0
No = 0
Maybe = 0

#Question 1

print ("Have you ever fished for compliments?")
print ("Definition: putting yourself down to make someone feel bad in order to compliment you")
print ("1) Yes, many times")
print ("2) Maybe once or twice...  ")
print ("3) No, I would never")
print ("4) I haven't, but I would")

answer = int(input ('Enter your answer 1-4 '))

if answer == 1: 
    Yes += 2
elif answer == 2: 
    Maybe += 2
elif answer == 3: 
    No += 2
elif answer == 4:
    Maybe += 1
else:
    print ('Wrong Input')


#Question 2

print ('Have you ever exlcuded, ignored, or put down other girls to make yourself look better in front of a guy?')
print ('1) Yes, various times.')
print ('2) A couple times, but not recently.')
print ('3) Never, gals before pals')
print ("4) I haven't, but it's crossed my mind")

answer = int (input ('Enter your answer 1-4 '))

if answer == 1: 
    Yes += 2
elif answer == 2: 
    Maybe += 2
elif answer == 3: 
    No += 2
elif answer == 4:
    Maybe += 1
else:
    print ('Wrong Input')


#Question 3

print ('Do you pretend to like male-oriented interests just for attention?')
print ('1) Yes, various times.')
print ('2) A couple times, but not recently.')
print ("3) Nope I don't have time to be fake.")
print ("4) I haven't, but it's crossed my mind.")

answer = int (input ('Enter your answer 1-4 '))

if answer == 1: 
    Yes += 2
elif answer == 2: 
    Maybe += 2
elif answer == 3: 
    No += 2
elif answer == 4:
    Maybe += 1
else:
    print ('Wrong Input')


#Question 4

print ('Do you put down hobbies and interests that women like to be "different than the other girls", intentionally or unintentinally? ')
print ('1) Yes, sometimes')
print ('2) A couple times in the past, but not recently')
print ('3) Never')
print ("I haven't, but I've thought it before.")

answer = int (input ('Enter your answer 1-4 '))

if answer == 1: 
    Yes += 2
elif answer == 2: 
    Maybe += 2
elif answer == 3: 
    No += 2
elif answer == 4:
    Maybe += 1
else:
    print ('Wrong Input')

#Final Question

print ("Is your name Audri?")
print ('Yes?')
print ('No?')

int(input('Enter your answer: '))

if answer == 1: 
    Yes += 1000000
elif answer == 2: 
    No += 2

#Outro Code

most_points = max(Yes, No, Maybe)

if Yes == most_points: 
    print ('You are a certified pick-me! You display the most common pick-me traits and should really look into changing your personality.')
elif No == most_points: 
    print (' You passed! You are not a pick-me and most of the time, always put being kind above the attention of guys.')
else:
    print ("You're somewhere in between. You aren't a very obvious pick me. You might exhibit some common pick me traits, but generally, you aren't unbearable.")