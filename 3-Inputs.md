# 3 - Inputs.py
*Skills: Variables, Strings, Integers, Math, Input & Output*

So far we have been programming in a very static manner - all the values are "hard coded" into the program

But this is not how you normally interact with software!

And this does not make for a very dynamic, user friendly program.

To rectify this, we can take **input** from a user and use this in our code to perform a calculation. 

## 3.1

To take **input** from the user, we can use the `input()` function. 

Inside the brackets `()` of the `input()` function, we can include a **string** to tell the user what they should be entering
For example:
```input("Please enter your username")```
In `main.py`, use the `input()` command and ask the user for the year they were born.


## 3.2

The trouble with this is that we are not storing the value the user enters, which means we can't do anything with it.

To correct this, we shall take our code from above and assign it to a **variable** called `birth_year`.

Do this in `main.py`, and remember - **variable** names on the left of the equals sign `=` and values on the right.

Once written, make sure you run your code and see what happens - will it let you write and enter a response?

## 3.3
You should hopefully have something like this written inside 3.2
```birth_year = input("Please enter the year you were born")```

Regardless of what the user types, when we use the input command it always gives us the response as a **string**. 

This is important because the following: 
- `"2" * "2"`
- `"2" * 2`
- `2 * 2`

all give different results.

We are going to perform a mathematical calculation on what the user enters, and so we want it to be an **integer**.

Use the `int()` command, like we did in the previous file, to convert the `input()` from a **string**, such as `"2001"`, to an integer, such as `2001`.

Combine `int()` with your code from 3.2 and put it in `main.py`.

## 3.4
Well done if you managed to get the following solution!
```birth_year = int(input("Please enter the year you were born"))```

We now have code which can take an **input** from the user, and puts it into the correct format for us to work with.

Now we are going to tell the user how old they are based on what has been entered.

To do this, we need to create a **variable** which stores the current year.

Create a **variable** in `main.py`, using an appropriate **variable** name, and assign the value of the current year to it.

## 3.5
To get the user's age, we simply subtract the year the user was born from the current year.

Make sure you get this round the right way!

Using two existing **variables**, and storing the result in a new **variable**, write a line of code to calculate the user's age.

## 3.6
We shall now print out the result to the user.

In order to do this, we need to add together some strings, like this:

```print("You are " + age + "years old")```
*(age is what i would have called the variable in 3.5, you might have called it something different and that is fine)*

When we add strings together, we refer to it as **concatenation**. This is an important word for you to understand and to be able to use.

We do not say `"add two strings"`, we say `"concatenate two strings"`.

However, there is a problem. Our **variable** `age` *(or whatever you called it)* is an **integer**. We cannot **concatenate** **strings** and **integers** together.

If we try to do this, python will give us an error. 

However, just like we used the `int()` command to change a **string** to an **integer**...

...we can use the `str()` command to convert an **integer** into a **string**.

Add the final line of code, printing how old they are in years. 

*(The number by itself is not enough, you must be using additional strings like in my example above)*

Well done! You have taken another huge step on your journey to becoming a programmer!
