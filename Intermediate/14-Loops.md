# 14 - Loops

There are lots of times when we are programming where we will want to do something over and over again.

We refer to this process of doing something over and over again as **iteration**. We can also refer to it as a loop. 

There are two main types of loops:
1. Count Controlled
2. Condition Controlled

## Count controlled loops
A count controlled loop is given a number of times to repeat. In the example below, we are telling python that `FOR` every number in the `range()` of 0 - 10, including 0 and 10, it should run the code inside itself.

```python3
for i in range(0, 10):
  print(str(i), "Hello!")
```

A loop is a very handy tool for a programmer!

Copy the code above into a new file and run it - can you tell what is happening to `i` on each iteration of the loop?

It is standard practise to have a variable called `i` in a count controlled loop (as always, this `i` could be called anything, but it best practise to call it `i`), having this helps us keep track while our program is running of how many times the loop has run. 

You should be able to see when running the above code that `i` increments each time "Hello!" is printed out from 0 all the way up to 10. 

We use the **variable** name `i` because it stands for **iterator**, and **iterate** means to do something over and over again, which is what a loop does. 

## 14.1
Create a new python file and write some code that will print out the entirety of the 12 times table. 

Do this however you see fit, but without trying to use a loop.

## 14.2
I am assuming that you did something like the following for the last activity:

```python3
print("12")
print("24")
print("36")
# etc...
```

We can use a loop to make this much more efficient:

```python3
for i in range(1,12):
  print(i * 12)
```

Every time the loop runs, `i` increments by 1 and so we end up going through the whole times table, from `1 * 12` all the way up to `12 * 12`

Take this code, put it in a new file, and change it so that it asks the user what times table they would like displayed, and then outputs the first 12 numbers in that times table.

## Condition Controlled Loops
There are times in our programs that we don't know how many times we want some code to run. In fact, we want it to run over and over again until a certain thing happens. 

We call this a condition controlled loop. 
```python3
secret = "password123"
password = ""
while secret != password:
  password = input("Please enter your password: ")
```

The loop above is not set to run a certain amount of times, in fact it is going to keep running until the condition becomes false. 

So all the time `while` the `password` is not the same as the `secret`, the line of code inside the `while` loop will run, asking the user for their password. 

Copy this code into a new file and test it by putting in lots of wrong passwords and then putting in the correct one.

See how the program immediately ends once you put in the correct password, but you stay in the loop all the time you are entering wrong passwords. 

## 14.3
Create a new file.
You are going to write a program that does the following:
- Has a variable storing the correct username
- Has a variable storing the correct password
- Asks the user for their username
- Asks the user for their password
- Keeps asking until the correct combination is given
- IF the user gets their username wrong, the program should tell them.
- If the user gets their password wrong, the program should tell them
- Once the correct username and password are entered, a personalised welcome message should display before the program ends. 
