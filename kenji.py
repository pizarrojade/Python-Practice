print ('~~~~~~~~~~~~~~~~~~~~~~~~~~')
print ("Are you Kenji's Soulmate?")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~")


Yes = 0
Maybe = 0
No = 0

# Question 1

print ("When faced with a challenge, do you usally tackle it head-on or take time to plan your approach?")
print ("1) I tackle it head-on, no matter what.")
print ("2) I take time to plan my approach.")
print ("3) I try to avoid the challenges altogether.")

answer = int(input ('Enter your answer 1-3 '))

if answer == 1: 
    Yes += 2
elif answer == 2: 
    Maybe += 1
elif answer == 3: 
    No += 2
else:
    print ('Wrong Input')

# Question 2

print ("Do you enjoy quiet nights in, energetic adventures, or a mix of both?")
print ("1) A mix of both!")
print ("2) I enjoy energetic adventures more.")
print ("3) I prefer quiet nights in.")

answer = int (input ('Enter your answer 1-3 '))

if answer == 1: 
    Yes += 2
elif answer == 2: 
    Maybe += 1
elif answer == 3: 
    No += 2
else:
    print ('Wrong Input')

# Question 3

print ("Are you more of a thinker or a feeler when making decisions?")
print ("1) I'm a thinker, I analyze everything.")
print ("2) I'm a feeler, I trust my instincts.")
print ("3) I try to balance both.")

answer = int (input ('Enter your answer 1-3 '))

if answer == 1: 
    Maybe += 1
elif answer == 2: 
    Maybe += 1
elif answer == 3: 
    Yes += 2
else:
    print ('Wrong Input')

# Question 4

print ("Would you rather have deep one on-one conversations or be in a group setting?")
print ("1) I prefer deep one-on-one conversations.")
print ("2) I enjoy group settings more.")
print ("3) I like both equally.")

answer = int (input ('Enter your answer 1-3 '))

if answer == 1: 
    Yes += 2
elif answer == 2: 
    No += 2
elif answer == 3: 
    Maybe += 1
else:
    print ('Wrong Input')


# Question 5

print ("Is your name Alana?")
print ("1) Yes, it is.")
print ("2) No, it's not.")


answer = int (input ('Enter your answer 1-3 '))

if answer == 1: 
    Yes += 1000000000000000
elif answer == 2: 
    No += 1
else:
    print ('Wrong Input')

# Final Result

most_points = max(Yes, No, Maybe)

if Yes == most_points: 
    print ('You are Kenji\'s soulmate! You have a deep connection and understanding of each other.')
elif No == most_points: 
    print ('You are not Kenji\'s soulmate. You might have some differences, but that\'s okay! Everyone has their own unique connections.')
else:
    print ('You might be Kenji\'s soulmate, but there are still some uncertainties. Keep exploring your connection!')