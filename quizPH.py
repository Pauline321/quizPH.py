# quiz.py by Pauline Harrell
# Question 1 - Correct Answer is (1)


#initialize variables
           
#question 1
q1 = """what is 3 + 3?
1) 6
2) 9
3) 5
4) 0
"""
a1 = int (0)
check1 = bool(False)
score = int(0)

#question 2
q2 = """what is Paulines's favorite color?
1) red
2) blue
3) purple
4) green
"""
a2 = int (0)
check2 = bool(False)
score = int(0)

# ask/answer Q1
print(q1)
while check1 == False:
  try:
        a1 =int(input(" choose the answer you think is correct. "))
        if a1 == 1:
           print("Thanks") #acceptable answer
           score = int(score+1)
           check1 = True
           
        elif 0 < a1 < 1: #acceptble answer
           print( "Thanks") 
           check1 = True
        else: 
           print(" Your choice needs to be between 1 and 4.") #unacceptable answer
  except ValueError:
           print("Your answer has to be a whole number")

# ask/answer Q2
print(q2)
while check2 == False:
  try:
        a2 =int(input(" choose the answer you think is correct. "))
        if a2 == 2:
           print("Thanks") #acceptable answer
           score = int(score+1)
           check2 = True
           
        elif 0 < a2 < 2: #acceptble answer
           print( "Thanks") 
           check2 = True
        else: 
           print(" Your choice needs to be between 1 and 4.") #unacceptable answer
  except ValueError:
           print("Your answer has to be a whole number")           

        

#score
print("quiz score: " , score* 50, "%")
                 

