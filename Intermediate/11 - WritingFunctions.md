# 11 - Writing Functions

## 11.1
**Function Name:** say_hello_to
**Parameters:** name *(String)*
**Process:** Prints the phrase "Hello <Name>! Nice to see you."
**Returns:** Nothing

### Tests
|Input|Expected Output|
|-|-|
|Bob|Hello Bob! Nice to see you.|
|Clarence|Hello Clarence! Nice to see you.|
|Georgina|Hello Georgina! Nice to see you.|
|My Dude|Hello My Dude! Nice to see you.|

## 11.2
**Function Name:** is_bob
**Parameters:** name *(String)*
**Process:** Checks to see whether the given name is "bob"
**Returns:** Boolean

### Tests
|Input|Return Value|
|-|-|
|Bob|True|
|BOB|True|
|boB|True|
|Reginald|False|
|Freya|False|
|EdWiNA|False|

## 11.3
**Function Name:** check_username
**Parameters:** username *(String)*
**Process:** Checks to see whether the given username is "quentin32". Prints a message to the user.
**Returns:** Boolean

### Tests
|Input|Expected Output|Return Value
|-|-|-|
|quentin32|Valid Username|True|
|quentin23|User not recognised|False
|QUENTIN32|User not recognised|False
|Reginald|User not recognised|False
|Freya|User not recognised|False
|EdWiNA|User not recognised|False

## 11.4
**Function Name:** pick_a_number
**Parameters:** *nothing*
**Process:** Asks the user to pick a number between 1 and 10
**Returns:** Integer between 1 and 10

### Tests
|User Input|Return Value
|-|-|
|1|1|
|8|8|
|15|-1
|-10|-1
|10.1|10
|5.53|6
|1000|-1

## 11.5
**Function Name:** delay
**Parameters:** seconds *(integer)*
**Process:** Tells the user: "A pause of <seconds> seconds is about to happen". Counts the amount of seconds, printing each out in sequence every second. Tells the user: "The <seconds> second pause has completed."
**Returns:** *nothing*

### Tests
|Input|Process
|-|-|
|1|A pause of 1 seconds is about to happen. 0. 1. The 1 second pause has completed.|
|5|A pause of 5 seconds is about to happen. 0. 1. 2. 3. 4. 5. The 5 second pause has completed.|
|15|A pause of 15 seconds is about to happen. 0. 1... 14. 15. The 15 second pause has completed.|