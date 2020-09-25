# 12 - Arrays

`Array` is a fancy name for a list.

Sometimes, it is much better to store values in a single list, rather than lots of separate **variables**.

Take a look at this example, where we have 6 good people defined in 6 separate **variables** and 6 bad people defined in 6 separate **variables**. 

The program checks the user's inputted name to see whether they are on the good list or the bad list, or neither, and gives an appropriate response.

```python3
good_person1 = "Jim"
good_person2 = "Fred"
good_person3 = "Reginald"
good_person4 = "Barbara"
good_person5 = "Ethel"
good_person6 = "Sandra"

bad_person1 = "Andre"
bad_person2 = "Phillip"
bad_person3 = "Craig"
bad_person4 = "Skylar"
bad_person5 = "Whitney"
bad_person6 = "Amanda"

name = input("Please enter your name: ")

if name == good_person1 or name == good_person2 or name == good_person3 or name == good_person4 or name == good_person5 or name == good_person6:
  print("Welcome, oh mighty one!")
elif name == bad_person1 or name == bad_person2 or name == bad_person3 or name == bad_person4 or name == bad_person5 or name == bad_person6:
  print("Access denied.")
else:
  print("Sorry, we don't seem to have your name in our records.")

```

## 12.1
Copy the code from the example above and paste it into a new file.

Add an extra name to the good people, (`good_person7`) and an extra name to the bad people (`bad_person7`) - you can choose what their name values will be. 

Now **test** the program with your new names and make sure it gives the correct response for the good person and the bad. 

**Don't forget to update the** `IF` **statement to test for the new names you have added!**

## 12.2
Look at how long the conditions are in the `IF` statement! That is absolute madness - there must be a better way! 

And there is!

Here is the exact same program, but using `Arrays` rather than lots of **variables**. Notice how the **variable** names for the `arrays` are plural, because they contain multiple things. 

```python3
good_people = ["Jim", "Fred", "Reginald", "Barbara", "Ethel", "Sandra"]

bad_people = ["Andre", "Phillip", "Craig", "Skylar", "Whitney", "Amanda"]

name = input("Please enter your name: ")

if name in good_people:
  print("Welcome, oh mighty one!")
elif name in bad_people:
  print("Access denied.")
else:
  print("Sorry, we don't seem to have your name in our records.")
```


Now you are going to do the same as in `11.1`, but for the code block above here (the one that uses arrays), putting it in its own new file.

Add the names you chose in `11.1` correctly to their respectivce lists.

Is there anything you need to adjust in the `IF` statement to make it work?

## 12.3
Hopefully by adding to both code examples, you have got a feel for how arrays can be used to make your programming much more efficient and easier to read. 

We are now going to have a look at how arrays work in more detail.

There is one golden rule to remember when using arrays.

`The first thing in the array is at position 0`

Copy the code below into a new file. Each comment in the code below should have an accompanying line of code. Add lines of code below comments which do not have a line of code written underneath them.

```python3
# declare array of colours
colours = ["blue", "red", "yellow"]

# print whole array
print(colours)

# print just the second value in the array
print(colours[1])

# add a new colour to the array
colours.append("green")

# find the length of the array
len(colours)

# print the first value in the array

# print the second and third value in the array

# print the length of the array

# add a new colour to the array

# print the length of the array

# print the last item in the array

# print the last item in the array without using just an integer

```