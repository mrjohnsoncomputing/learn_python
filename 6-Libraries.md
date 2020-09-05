# Title: 6 - Libraries.py
*Skills: Modules, Variables, Output*

A **library**, or **module**, is a file of code that you can load into your project in order to access extra commands which have been written by other people. 

We have seen some of the commands that come as standard in python already, such as: 
- `print()`
- `input()`
- `int()`
- `str()` 

These commands come as standard in python as they are common to almost all programming projects.

However, some commands are not always neccessary, and to save loading millions of lines of code when you run your program, these commands are kept separate for you to `import` as and when you need to.

## 6.1
Let us `import` our first library - the `time` **library**. 

To do this, we can use the line: 
`import time`
Add that into the relevant space in `main.py`

## 6.2 - a

The `time` **module** unsuprisingly deals with lots of things to do with time.

Paste the the code below into `main.py` and run it, paying close attention to how quickly each `print()` statement happens.

``` Python
# v 6.2 - Code v #
print(1)

print(2)

print(3)

print(4)

print(5)
### ^^^^^^^^^^ ###
```
## 6.2 - b
We are now going to use the `time` **library** to add some delay, so that the numbers **print()** out more slowly.

The `time` **library** has a `sleep()` function, where we can give an amount of seconds, as either an **integer** or a **float**, and our program will pause for that amount of time.

To access that function, we need to tell python that it belongs to the `time` **module**, and so we would write it as: 
`time.sleep()`

Add this command, with an amount of seconds in the brackets, between each print line that we pasted into `main.py` in 6.2 - a. 

Run the code and see if you can see the effect these additions have had.

Try changing the values in the brackets `()` of `time.sleep()` and take note of its effect.

## 6.3
Fantastic! We have now imported extra code to help us in our program.

Lets look at another library that could be useful to us. This library is called `random`.


Using what you have learnt already, try importing the `random` library into `main.py`

## 6.4
The `random` **library** allows us to generate *pseudo-random* numbers. Pseudo means false/fake and this might seem odd.

However, computers cannot be truly random, as they have to be programmed by humans, who are not random.

For me and you though, these random numbers will be just fine.

The `random` **module** has a function in it called `randint()`, which will return to us a random **integer**. 

We have to put two values in the `randint()` command:
1) The lowest we want out random number to be
2) The highest we want it to be.

It should look something like this: 
`random.randint(1,10)`

This will give us a random **integer** between 1 and 10, including 1 and 10.

Add this command to the `main.py` file, assign it to a **variable** and `print()` that **variable** out. 

Change the numbers so that it is picking numbers between -100 and 100.

Run the code a few times, is it giving you a different number each time?

## End
Well done! You have used two separate **libraries**!

There are a whole host of **libraries** that come as standard with python, as well as a lot which you can download and `import` into your project.

Using a **library** saves you lots of time, as you don't have to program something yourself, you can use code that someone else has already written.

Remember these **libraries** for future use - they might come in handy!
