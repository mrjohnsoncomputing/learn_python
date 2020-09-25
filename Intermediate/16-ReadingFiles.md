# 16 - Reading Files
Reading files is a really important aspect in programming. 
It allows us to write programs that can work with big data sets, analyse that data, and then return a result. 
It also reduces the amount of data we have to *hard-code*, that is, store inside our python program.

For example, take a look at the file in this folder called `names.txt`. It should be a list of names. Imagine that this file is a list of valid usernames for our program. We could have anyone update that file, without them having to know how to read and write python. Plus, we don't have to jump into the code ourselves to update it AND our code is less cluttered because all of this data is stored elsewhere. 

## 16.1
We learnt to **define** functions in #10, and I always like to stick my file reading code inside a function, so that is where we are going to start.
Firstly, take a copy of the code below and put it in a new file. 
```python3
def read_file():
  # Code for reading file goes here - must be indented!
```

In order to open a file, we need to use the `open()` command.
The `open()` command should be given two **arguments**. The first should be the filename as a **string**, and the second should be the mode we want to open the file in, also as a **string**. 

---

### Arguments
An **argument** is the value that you put inside the brackets of a function. For instance, the `print()` function expects *at least* one **string** **argument**:
```python3
print("Hello World!")
```
But you can add a second argument:
```python3
print("Hello World!", "It's nice to see you!")
```
Or as many as you like:
```python3
print("Hello", "World!", "It's", "nice", "to", "see", "you")
```

We must put commas between **arguments** when we are using more than one, so that python can tell that they are separate.

---

Anyway! as I was saying, we need to give the `open()` function two **arguments**
- The name of the file as a **string** -  we will be opening `names.txt`
- The mode we want to open the file in as a **string**

We shall be opening the file in *read mode*, so we are going to use `"r"` as the second argument. 

We also need to assign the `open()` command to a suitably named **variable**.

So, enough of me yapping on!

Using everything I've told you, add in the `open()` command remembering to assign it and add in the arguments in the correct order.

You can get rid of the `# Code for reading file goes here - must be indented!` line in the code you copied across. 

Once you have done that, inside the function, `print()` out your variable.

If you get stuck, the solution is in the next section. 

**Stuck**: To have attempted and thought about the problem many times and many different ways, using all relevant information given to you, without success.

## 16.2
*We are going to continue working on this code, in the same file you created in #13.1 - you won't need to create any additional code files for the rest of #13.*

A big well done if you have something like the below:
```python3
def read_file():
  file = open("names.txt", "r")
  print(file)

read_file()
```

Make sure you are calling the function at the end of your program and testing it - are you seeing the names from the text file printed to the screen?

Probably not.

We need to do a three things in order to get our names from the file.
- Read the file
- Close the file
- Change the print statement

### 1
Firstly, we need to actually tell Python to *read* our file. We can do this by saying `file.read()` and assigning it to a variable - yes it is as simple as that (As long as you remember to assign it to a variable). 

I would recommend calling your variable something like `data`. We can put this new line of code under the line we have the `open()` command on.

### 2
Now we need to close the file. We can say `file.close()` to close our file. We **DO NOT** need to assign this to a variable, as it is just a command - it won't return any values to us.  This line should go after the line with `file.read()` on it. 

### 3
Finally we need to change what we are printing. Instead of printing the file, we need to `print()` the data we extracted from it. If you have been following carefully, you should have created a variable (maybe called `data`) and assigned `file.read()` to it. Use this variable in the brackets `()` of the `print()` command.

## 16.3
The first thing we are going to do is make our function usable for any file. This is a small tweak, but it is a good programming practise to get into. 

At the moment, whenever we call `read_file()`, we will always have the contents of `names.txt` read for us. But what if we wanted to read `numbers.txt`? 

We definitely DO NOT want to end up in the situation where we have functions like `read_file2()` and `read_file3()` cropping up! No our code has to be dynamic, it has to be clever, and so we shall use a **parameter** in our function definition in order to make our `read_file()` function more flexible. 

---

### Parameters
A **parameter** is the value that you put inside the brackets of a function **definition**. It is easily confused with an **argument**, which we looked at earlier in this document.

In order to see the difference effectively, here is an example. 
```python3
def add_one(number):
  result = number + 1
  return result

total = add_one(5)
```
In the above code, a function called `add_one()` has been defined and a **parameter** called `number` has been given in the brackets. This **parameter** is used inside the function in order to calculate the `result`.

We use a **parameter** to stand in for a value, so we can use the function with any value we give it when we call it. 

When we call the function on the last line of the code above, we put the **argument** of `5` in the brackets `()`. 

We can run the line `total = add_one(5)` in our heads by taking the **argument** given, `5`, and replacing `number` with it in the function **definition** at the top of the code.

So we would take `result = number + 1`, swap the **parameter** `number` for the **argument** `5` and end up with `result = 5 + 1`

---

In order to make our `read_file()` function more flexible, we are going to:
- Add a **parameter** into the brackets `()` of `def read_file()`
- Remove `"names.txt"` from the `open()` function and replace it with our **parameter**
- Add `"names.txt"` into the brackets when we call `read_file()`

Off you go, do the three tasks in the list above and I'll see you in 13.4!

And the solution is in the next step, if you do get stuck - try and give it a go first though before looking!

## 16.4
Okay, so I am really hoping you have **developed** your code into something like the following - don't worry if your **parameter** name is slightly different to mine. 
```python3
def read_file(filename):
  file = open(filename, "r")
  data = file.read()
  file.close()
  print(data)

read_file("names.txt")
```

If you do have something similar to the above - well done! If you don't, go in and make the appropriate changes.  

I would now like you to add one line of code to the end of your file that will print out the `numbers.txt` file after the `names.txt` file has printed. 

## 16.5

Okay, this is good! one thing we are missing from our function is the `return` keyword that we looked at in #10. It's all very well printing the values to the screen, but we can't use those values unless we `return` them from the function. 

Here's what I'd like you to do:
- Replace the `print(data)` with code which will `return` the **variable** instead of printing it. 
- Assign the two function calls at the bottom of your code to their own unique variable names, so that the returned data from the function can be stored somewhere
- Add two additional lines to the bottom of the code to print out your two variables storking the contents of the `numbers.txt` and `names.txt` files. 

Again, if you get really stuck, you can find the solution in the next section.

## 16.6
A big pat on the back if you have something that looks like the code below:
```python3
def read_file(filename):
  file = open(filename, "r")
  data = file.read()
  file.close()
  return data

names = read_file("names.txt")
numbers = read_file("numbers.txt")
print(names)
print(numbers)
```

Blimey, that was a lot of work! 

Take a deep breath and treat yourself to a smile - you're doing great!

Using files in python allows us to take a very difficult and boring task and complete it in seconds. 

See you in #14!