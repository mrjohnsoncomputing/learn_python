# 2 - Numbers.py
*Skills: Variables, Integers, Math, Output*

Now that we have learnt how to print an output to the screen, let us do something useful with it.

We can use variables to store the result of a calculation like so:
`result = 1 + 1`

## 2.1
In `main.py`, create an appropriately named **variable** and set its value to the calculation `300` divided by `19`. *(In programming the forward slash character `/` is used to represent divide, and the asterix character* `*` *is used to represent multiply)*

## 2.2
Now you can use the `print()` command to output the result of this calculation, remembering to put the **variable** name in the brackets `()` of the `print()` function.

## 2.3
Numbers in programming can fall into many different categories, but keeping it simple we have **integer** `int` and **floating point** `float`.

An **integer** represents a whole number, and a **floating point** number represents any number with a decimal point, even things such as `10.0`
The way a computer stores and performs calclations on an `int` is different to that of a `float`, and so it is important we understand the difference.
#### What number type is the result from 2.2 - float or int?
*Type your answer as a **string** in a `print()` command in the `main.py` file*

## 2.4
We can convert one type of number to another. Putting a `float` inside the brackets `()` of `int()` will convert our `float` into an `int`.

Try updating the code you wrote in 2.2 to have the answer `print()` out as an **integer** rather than a **floating point**.

*(If you get stuck, read the next section for the answer)*

#### Breakdown of answer to 2.4

Let us break down the code for the solution for the last section.
Your answer should have looked like this:
```print(int(result))``` 
*(Your variable name might not be result, that's fine!)*

The way the computer will execute this code will be to first take whatever is inside of the brackets `()` of `print()` and resolve it.

In order to resolve what is in the brackets, it performs the conversion from the command `int(result)`

The result of this is then printed.

## 2.5
As a final activity, create an appropriately named **variable** and assign it to this calculation: `4 + 4 * 8`
`print()` the **variable** so that you can see what the result is.
Before running the code, see if you can predict what the answer will be. 

## 2.6
What mathemathical principle is the computer following?

How might you use brackets `()` in the calculation in order to get the result of `64` printing to the screen?
