# 4 - Selection.py
*Skills: Variables, Strings, Integers, Math, Selection, Input & Output*

There are three main things that affect the flow of a program:
- **Sequence**
- **Selection**
- **Iteration**

**Sequence** is ensuring that our code is in the correct order. By completing the first three files, you have already been unknowlingly dealing with sequence. 

**Selection** deals with running code only `IF` certain conditions are true.

**Iteration** is used `FOR` repeating lines of code over and over and over and over and over and over and over and over and over again.

In this section, we shall look at **selection**.

## IMPORTANT
For this section to go well for you, it is important that you remember this golden rule:
- A single equals sign `=` is used to assign a value to a variable.
- A double equals sign `==` is used to compare two values.

## 4.1
In order for us to use selection, we are going to reuse some of the code we wrote in the last section, I have included it below for you:

```Python
# v 3 - Code v #
current_year = 2020
birth_year = int(input("Please enter the year you were born"))
age = current_year - birth_year
### ^^^^^^^^^^ ###
```
We have a logic error in the program above - did you notice it?

---
### Errors

There are two main types of error in programming 
- **Syntax** error
- **Logic** error

#### Syntax Error
A syntax error is something like a spelling mistake, or forgetting to close your brackets or speech marks.

Your code will likely not run if it has syntax errors, instead it will shout weird scary programmy things at you. 

#### Logic Error
A logic error is more serious, and normally results in your code running, but getting the wrong results. 

---

Here's the logic error in the code above:

Let us imagine that the current date is February 2020 (before the end of the world began).

If you were born in March 2010, our program would do 2020 - 2010 and say that you are 10 years old. 

However `IF` your birthday is in *March* (and remember that in this scenario we are still in February) then you are still 9 - you haven't had your birthday this year yet!

This means our program doesn't work properly, and needs to be cleverer - our program needs to subtract 1 from the age we calculated.

Our program needs to be clever enough to take this into account, and that is where selection comes in!

We will do this by asking the user a simple yes/no question:
`"Have you had your birthday yet? y/n"`

Copy teh code I have included above from section 3 and paste it into section 4.1.

Then, use the above **string**, combined with the `input()` function and assign it to a **variable** with an appropriate name. 

## 4.2
Now we will use the answer given by the user to check whether they have had their birthday yet.

I have put in the structure of an `IF` statement below. 

You will need to delete `CONDITION` and replace it with what you want to compare.

Copy the code below and paste it into `main.py`.

```Python
# v 4.2 - Code v #
if CONDITION:
    # This is where we shall put code if the person has had their birthday already this year
else:
    # This is where we shall put code if the person has NOT had their birthday already this year.
### ^^^^^^^^^^ ###
```
## 4.3
Hopefully you have replaced `CONDITION` with an actual condition - did you remember to use a double equals sign?. It should look something like this:

`if answer == "y":`

*Note: your* **variable** *might have a different name to* `answer`*, and that is fine.*

You should now replace the comments inside the `IF` and the `ELSE` with `print()` commands.

Please make sure you respect the four spaces that push the comments "into" the `IF` and the `ELSE`.

Python needs those spaces to know what is inside the `IF`, and what is outside of it. The same applies with the `ELSE` block.

If you don't use the right spacing, that will be a **syntax** error and won't run your code. 

**Test** your code with someone who has had their birthday already this year, and someone who hasn't - does it work for both of them?
