import repetitive

# Individual values of members to be used for comparisons
elizabeth = 1
marj = 2
rosanne = 3
ruthanne = 4
donnie = 5
patricia = 6
kim = 7
monica = 8
martin = 9
gabe = 10
john = 11
ben = 12
jerome = 13
johnG = 14
jamie = 15
julia = 16
phil = 17
alley = 18
anna = 19
steven = 20
ellane = 21
jake = 22
veera = 23
precila = 24
clarence = 25
lincoln = 26
mo = 27
alex = 28

# The list of members organized into groups based on generation

gen1 = [elizabeth] # 1

gen2 = [marj, rosanne, ruthanne, donnie, patricia] # 2, 3, 4, 5, 6

gen3 = [kim, monica, martin, gabe, john, ben, jerome] # 7, 8, 9, 10, 11, 12, 13

gen4 = [johnG, jamie, julia, phil, alley, anna, steven, ellane, jake, veera, precila, clarence] # 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25

gen5 = [lincoln, mo] # 26, 27

gen6 = [alex] # 28

# List of members who don't have children of their own
# The members in this list cannot be classified as parents, grandparents, etc.
hasNoChildren = [rosanne, ruthanne, donnie, patricia, martin, john, ben, jerome, johnG, jamie, julia, alley, anna, steven, jake, veera, precila, clarence, mo, alex]

# while loop
while(1):

  repetitive.list()
  
  # User inputs to be stored as a value
  userInput = int(input())
  userInput2 = int(input())
  
  if userInput == userInput2:
    print('You selected the same member twice! Please select 2 different members.')
  
  if userInput in gen1 and userInput != userInput2:
    print("Elizabeth")
  
  if userInput in gen2 and userInput != userInput2:
    if userInput == marj:
      print("Marj")
      
    if userInput == rosanne:
      print("Rosanne")
  
    if userInput == ruthanne:
      print("Ruthanne")
  
    if userInput == donnie:
      print("Donnie")
  
    if userInput == patricia:
      print("Patricia")
  
  if userInput in gen3 and userInput != userInput2:
    if userInput == kim:
      print("Kim")
  
    if userInput == monica:
      print("Monica")
  
    if userInput == martin:
      print("Martin")
  
    if userInput == gabe:
      print("Gabe")
  
    if userInput == john:
      print("John")
  
    if userInput == ben:
      print("Ben")
  
    if userInput == jerome:
      print("Jerome")
  
  if userInput in gen4 and userInput != userInput2:
    if userInput == johnG:
      print("John G")
  
    if userInput == jamie:
      print("Jamie")
  
    if userInput == julia:
      print("Julia")
  
    if userInput == phil:
      print("Phil")
  
    if userInput == alley:
      print("Alley")
  
    if userInput == anna:
      print("Anna")
  
    if userInput == steven:
      print("Steven")
  
    if userInput == ellane:
      print("Ellane")
  
    if userInput == jake:
      print("Jake")
  
    if userInput == veera:
      print("Veera")
  
    if userInput == precila:
      print("Precila")
  
    if userInput == clarence:
      print("Clarence")
  
  if userInput in gen5 and userInput != userInput2:
    if userInput == lincoln:
      print("Lincoln")
  
    if userInput == mo:
      print("Mo")
  
  if userInput in gen6 and userInput != userInput2:
    print("Alex")
  
  ######################################################
    
  # If both members are in generation 2, they are siblings 
  if userInput in gen2 and userInput2 in gen2 and userInput != userInput2:
    print("is the sibling of")
  
  # If both members are in generation 3, they are siblings 
  if userInput in gen3 and userInput2 in gen3 and userInput != userInput2:
    print("is the sibling of")
  
  # Checks the relationship using math
  if -2 < userInput - userInput2 < 0 and userInput and userInput2 not in hasNoChildren: # Gen 1
    print("is the parent of")
  if -6 < userInput - userInput2 < -1: # Gen 2
    print("is the parent of")
  if -13 < userInput - userInput2 < -5: # Gen 3
    print("is the parent of")
  if userInput - userInput2 < -12: # Gen 4
    print("is the parent of")
  if userInput - userInput2 < -24: # Gen 5
    print("is the parent of")
  if userInput - userInput2 < -26: # Gen 6
    print("is the parent of")
    
  ######################################################
  
  if userInput2 in gen1 and userInput != userInput2:
    print("Elizabeth")
  
  if userInput2 in gen2 and userInput != userInput2:
    if userInput2 == marj:
      print("Marj")
      
    if userInput2 == rosanne:
      print("Rosanne")
  
    if userInput2 == ruthanne:
      print("Ruthanne")
  
    if userInput2 == donnie:
      print("Donnie")
  
    if userInput2 == patricia:
      print("Patricia")
  
  if userInput2 in gen3 and userInput != userInput2:
    if userInput2 == kim:
      print("Kim")
  
    if userInput2 == monica:
      print("Monica")
  
    if userInput2 == martin:
      print("Martin")
  
    if userInput2 == gabe:
      print("Gabe")
  
    if userInput2 == john:
      print("John")
  
    if userInput2 == ben:
      print("Ben")
  
    if userInput2 == jerome:
      print("Jerome")
  
  if userInput2 in gen4 and userInput != userInput2:
    if userInput == johnG:
      print("John G")
  
    if userInput2 == jamie:
      print("Jamie")
  
    if userInput2 == julia:
      print("Julia")
  
    if userInput2 == phil:
      print("Phil")
  
    if userInput2 == alley:
      print("Alley")
  
    if userInput2 == anna:
      print("Anna")
  
    if userInput2 == steven:
      print("Steven")
  
    if userInput2 == ellane:
      print("Ellane")
  
    if userInput2 == jake:
      print("Jake")
  
    if userInput2 == veera:
      print("Veera")
  
    if userInput2 == precila:
      print("Precila")
  
    if userInput2 == clarence:
      print("Clarence")
  
  if userInput2 in gen5 and userInput != userInput2:
    if userInput2 == lincoln:
      print("Lincoln")
  
    if userInput2 == mo:
      print("Mo")
  
  if userInput2 in gen6 and userInput != userInput2:
    print("Alex")

print("")
print("")