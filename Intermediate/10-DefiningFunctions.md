# 10 - Defining Functions

So far we have been writing code that just runs whenever we press `Run`. 

But this isn't how we typically write code. Often what we do is write code and store it in functions, and then when we want to use it, we can **call** the function. 

Look at this example:
```python3
def add(num1, num2):
  total = num1 + num2
  return total

score = 0
score = add(score, 3)
score = add(score, 5)
```

We have used the `def` keyword, short for **define**, to tell python that we are **defining** a function. 

We have given the function a descriptive name, `add`. We could have called it anything, so long as it wasn't already a function in python, like `print` for instance.

In the brackets `()` of add, we have put in two **variables** that we want the programmer to give to the function, `num1` and `num2`. When we have variables in the brackets `()` of a function, we call them **parameters**.

The code that we want to run when we use the function should be indented in, like in the example above, to show that the code is part of the function - Notice how `total` and `return` are not in line with `def`, but instead pushed in a little.

The code we have in the `add()` function adds its two **parameters** and stores them in a **variable** called `total`.

We then use the `return` keyword. This is a **REALLY** important word when working with functions, because this does something very helpful - it sends the value after it, in this case `total`, back to wherever the function was **called** from. 

When the above code is run, python will read the `add()` function, but it won't run it, because it is just a definition.

It will then move onto the next line `score = 0`, and store that **variable** in memory. 

Next, it moves onto the line `score = add(score, 3)`. This is the first time we have **called** the `add()` function that we defined above. By the order that `score` and `3` are inside the brackets, that tells the function that `num1` is the value of `score` (so, `0`) and `num2` is the value of `3`. 

The function will then calculate the total by adding the two values (0 + 3), and then `return` that total to where the function was **called**. 

So if we were to look behind the scenes, this line `score = add(score, 3)` once the function has run, will actually look like this `score = 3`, though of course you won't actually see that, but that is what is happening behind the scenes.

Finally, the last line works on the same principle.
We have `score = add(score, 5)`. This time, when we pass the value of `score` into the `add()` function, the value of `score` is now `3`, due to having updated the **variable** on the previous line. This gets passed into `num1` and we pass the `5` into `num2`.

So we are now passing in a `3` and a `5` to the `add()` function. 

It should hopefully be fairly obvious to you what the final result of `score` is.

Spoiler alert - It's `8`.

## 10 - Task

Now it is your turn!
Copy the below code into a new python file (see `09-PythonFiles.md` if unsure), and write functions for `square()` and `multiply()` so that the program can calculate the area of a circle with a radius of 10. Ensure your function definitinons are written at the top of your code, otherwise python will be trying to **call** the functions before it has read their definitions.
```python3
radius = 10
pi = 3.14
rSqrd = square(radius)
area = multiply(pi, rSqrd)
```

*Note: The code will throw an error if you try and run it before defining the two functions, as you are telling it to use functions (square() & multiply()) that don't exist.*