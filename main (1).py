import random

#1
def getUserChoice():
  print('Choose rock, paper, or scissor:')
  user_choice = input()
  return user_choice

def getComputerChoice(): 

  Options = ['rock','paper','scissor']

  comp_choice = random.choice(Options) 
  return comp_choice

def compareChoice(user_choice,comp_choice): 
  if user_choice and comp_choice == 'paper':  
    return('Its a tie!')
    
  elif user_choice == 'scissor':
    return('You win!') 
    
  return 'User'

def printChoice(user_choice,comp_choice,result): 
  print(compareChoice(result))  

def updateScores(wins,losses,ties,winner): 
  user = 0
  comp = 0 

if user > 1: 
  print(wins) 

else: 
  print(losses)

def printScores(win,loss,tie): 
  print(win) 
  print(loss) 
  print(tie) 


##############################
#print(getUserChoice())

#print(getComputerChoice())

#print(random.choice(letters))