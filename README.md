# Algorithm-Project
This program will display a list of members from a family tree. Depending on the 2 members the user selects, the program will show the relationship between them.

This program relies on splitting the list of members into many categories and comparing them using numerous "if" statements and the like.

For example, if Rosanne and Donnie are selected, the program will show that Rosanne is a sibling of Donnie, since they have the same parents. 

# Pseudo code
Assign members an individual value 

Make multiple lists, one for each generation

Make another list for the members with no children

Print out a list of members

Ask user to select 2 members and store the user input in 2 variables

Make ‘if’ statements for each member so that the program prints out the 2  members’ names if selected

Compare the values assigned to the members selected and compare them (Generation Number, Individual Number)

If user input’s gen is equal to user input2’s gen, check the parents of each member to determine if they’re siblings or cousins (Siblings if they come from the same parent/Cousins if they come from different parents/Half siblings if they share only one parent)

If user input’s gen is one higher or lower than user input2’s gen, check the lower gen to see if they’re a child of the higher gen. If not, then they’re a nephew/niece. If yes, then they’re a child of the higher gen.

Do the same thing for even higher/lower generations

Print out the first selected member’s name

Print out “is the (kinship term) of”

Print out the second selected member’s name

Repeat the code using a ‘while(1)’ loop
