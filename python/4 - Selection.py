# There are three main things that affect the flow of a program
# Sequence, Selection and Iteration. 
# Sequence is ensuring that our code is in the correct order. By completing the first three files, you have already been unknowlingly dealing with sequence. 
# Selection deals with running code only if certain conditions are true.
# Iteration is used for repeating lines of code over and over and over and over and over and over and over and over and over again.
# In this section, we shall look at selection.

# For this section to go well for you, it is important that you remember this golden rule:
# A single equals sign is used to assign a value to a variable.
# A double equals sign is used to compare two values.

# In order for us to use selection, we are going to reuse some of the code we wrote in the last section, I have included it below for you:

# v 3 - Code v #
current_year = 2020
birth_year = int(input("Please enter the year you were born"))
age = current_year - birth_year
### ^^^^^^^^^^ ###

# There are two main types of error in programming - a syntax error and a logic error. 
# A syntax error is something like a spelling mistake, or forgetting to close your brackets or speech marks.
# Your code will likely not run if it has syntax errors
# A logic error is more serious, and normally results in your code running, but getting the wrong results. 
# We have a logic error in the program we wrote for section 3 - did you notice it?

# Lets imagine it is February 2020 (before the end of the world began).
# If you were born in March 2010, our program would do 2020 - 2010 and say that you are 10 years old. 
# However your birthday is in March, so you are still 9 and our program needs to subtract 1 from the age we calculated.
# Our program needs to be clever enough to take this into account, and that is where selection comes in!
# We will do this by asking the user a simple yes/no question - "Have you had your birthday yet? y/n"
# Use that, combined with the input function and assign it to a variable with an appropriate name. 

# v 4.1 - Code v #

### ^^^^^^^^^^ ###

# Now we will use the answer given by the user to check whether they have had their birthday yet.
# I have put in the structure of an IF statement below. 
# You will need to delete CONDITION and replace it with what you want to compare

# v 4.2 - Code v #
if CONDITION:
    # This is where we shall put code if the person has had their birthday already this year
else:
    # This is where we shall put code if the person has NOT had their birthday already this year.
### ^^^^^^^^^^ ###

# Once you have replaced the CONDITION with an actual condition (Did you remember to use a double equals sign?)...
# ...then replace the comments inside the if and the else with print commands.
# Please make sure you respect the four spaces that push the comments "into" the if and the else. 
# Python needs those spaces to know what is inside the if, and what is outside it. THe same with the else.

# Test your code with someone who has had their birthday already this year, and someone who hasn't - does it work for both of them?
