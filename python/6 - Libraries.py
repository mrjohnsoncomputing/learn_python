# Title: 6 - Libraries.py
# Skills: Modules, Variables, Output

# A library, or module, is a file of code that you can load into your project in order to access extra commands which have been written by other people. 
# Commands such as print(), input(), int() and str() as we have seen already come as standard in python, as they are common to almost all programming projects.
# However, some commands are not always neccessary, and to save loading all of this code when you run your program...
# ...these commands are kept separate for you to import as and when you need to.

# Lets import our first library - the time library. 
# To do this, we can use the line: import time
# Add that in the space below

# v 6.1 - Code v #

### ^^^^^^^^^^ ###

# The time module unsuprisingly deals with lots of things to do with time.
# Run the code below, paying close attention to how quickly each print statement happens.

# v 6.2 - Code v #
print(1)

print(2)

print(3)

print(4)

print(5)
### ^^^^^^^^^^ ###

# We are now going to use the time library to add some delay, so that the numbers print out more slowly.
# The time library has a sleep() function, where we can give an amount of seconds, as either an integer or a float, and our program will pause for that amount.
# To access that function, we need to tell python that it belongs to the time module, and so we would write it as: time.sleep()
# Add this command, with an amount of seconds in the brackets, between each print line above. 
# Run the code again and see if you can see the effect it has had.
# Try changing the values in the brackets of time.sleep() and take note of its effect.


# Fantastic! We have now imported extra code to help us in our program.
# Lets look at another library that could be useful to us. This library is called: random
# Try importing it below

# v 6.3 - Code v #

### ^^^^^^^^^^ ###

# The random library allows us to generate pseudo-random numbers. Pseudo generally means false/fake and this might seem odd.
# However, computers cannot be truly random, as they have to be programmed by humans, who are not random.
# For me and you though, these random numbers will be just fine.
# The random module has a function in it called randint(), which will return to us a random integer. 
# We have to put two values in the randint() command, the first value is the lowest we want out random number to be, and the second is the highest we want it to be.
# It should look something like this: random.randint(1,10)
# This will give us a random integer between 1 and 10, including 1 and 10.
# Add this command to the space below, assign it to a variable and print that variable out. 
# Change the numbers so that it is picking numbers between -100 and 100.
# Run the code a few times, is it giving you a different number each time?

# v 6.4 - Code v #

### ^^^^^^^^^^ ###

# Well done! You have used two separate libraries!
# There are a whole host of libraries that come as standard with python, as well as a lot which you can download and import into your project.
# Using a library saves you lots of time, as you don't have to program something yourself, you can use code that someone else has written.
# Remember these libraries for future use - they might come in handy!
