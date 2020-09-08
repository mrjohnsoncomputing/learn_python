# Python Files

So far we have been using a single file `main.py` to put all of our code in. 

This is a bit clunky, as a lot of the code is unrelated. It would be much better if we separated our code out into individual files. 

That is what we are going to do in this section.

## 9.1
Firstly, you will need to make sure you have the `Intermediate` folder selected on the left hand side. 

Now click on the three vertical dots on the right hand side of `Intermediate`, and click on `Add File`.

You are going to name this file `9.py`

Once the file is created, put a command in it so we can test it is working. 
I'd suggest using something like `print("9.py Loaded Successfully")`, but you can do whatever you like, so long as you print *something* out!

And press `Run`!

Ah. It's still running `main.py`...

**sigh**

## 9.2
To make sure the right file is run when we press the `Run` button, we need to tell repl.it which python file it should be looking for. At the moment it is set up to use `main.py`.

We can change this by going to the file on the left called `.replit`. *(Has that been there this whole time?!)*

Inside that file you will see this:
```
language = "python3"
run = "python3 main.py"
```
Hopefully it is obvious what you will need to change in order to get `9.py` running instead of `main.py`

## 9.3
In every section from here onwards, I will be expecting you to make a new python file for your code and changing the `.replit` file to the appropriate file name. 

It is therefore a very good idea to start every python file you create with some kind of `print()` statement telling you what file is being run. For instance, if we move onto 10, create our new python file, type our code and then press `Run`, we will know what we have forgotten to do if we see the following:
```
> 9.py Loaded Successfully
```

You can be as creative as you like with your startup message, as long as it remains helpful to you so you know what file is being run.

Right, now we've got all that out of the way, lets do some programming - see you in 10!