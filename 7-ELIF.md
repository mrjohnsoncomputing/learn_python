# Elif.py
*Skills: Selection, Variables, Strings, Input & Output*

We are going to build on what we know about selection, by adding more conditions. 

Let us consider this scenario: 

### Program Description
We have a program which asks the user for their name
- A user called Bob should be greeted by the program saying "Hello Bob"
- A user called Sharon should be greeted by the program saying "Oh hi Sharon!"
- A user called Dr. Evil should be greeted by the program saying "Unauthorised access!"
- A user called Derek should be greeted by the program saying "Welcome boss."
- Any other user should be greeted by "Successful log on"

## 7.1
In order to implement that, we need more than just `IF` and `ELSE`, and that is where `ELIF` comes in.

Look at the code below, see how I have laid out my `IF` statement.

In this, I am testing four conditions, and `IF` nothing matches any of those conditions, we shall end up in the `ELSE` section.

`ELIF`, if you haven't figured it out already, is short for *else if*.

``` Python
# v 7.1 - Code v #
if CONDITION:
    # print something here I guess...  
elif CONDITION:
    # print something different here I guess...
elif CONDITION:
    # print something else here I guess
elif CONDITION:
    # print unique string here I guess...
else:
    # print generic greeting
### ^^^^^^^^^^ ###
```

In the code above, add user `input()`, replace the `CONDITION`s with proper conditions and insert the correct `print()` statement for each user described in the program description at the start.

Remember to get your single equals `=` and double equals `==` signs round the right way!

Once complete, make sure you run your program a few times, testing that it works properly for all the different users.
