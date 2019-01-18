
# quiz.py by Pauline Harrell

#Defining a function
#ID and name all var.s the function needs to run.
#question string

def run_quest(quest,check,ansU,ansR):
  #
  #loop check varible          correct option

  # ask/answer q
  print(quest)
  while check == False:
    try:
      ansU =int(input(" choose the answer you think is correct. "))
      if ansU == ansR:
         print("Thanks") #acceptable answer
         #score = int(score+1)
         check = True
      elif 0 < ansU < 1: #acceptble answer
         print( "Thanks") 
         check = True
      else: 
         print(" Your choice needs to be between 1 and 4.") #unacceptable answer
    except ValueError:
             print("Your answer has to be a whole number")

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
cor1 = 1

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
cor2 = 2
           
#"Call" function for each question
#Question 1-2
run_quest(q1,check1,a1,cor1)
run_quest(q2,check2,a2,cor2)

   
#score
print("quiz score: " , score* 50, "%")
                 

