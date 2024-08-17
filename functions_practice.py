age = 23
name = "jon doe"
likes_to_code = True


## Section 1 - variables and functions: 

# Question 1: Create two variables. One should be a string data type, and the other should be of type int.
age = 23
name = "jon doe"

# Use a single print statement to print both variables:
print(age, name)

# Question 2: Create a Python function that prints a greeting with a name as the parameter.
def greeting(name):
    print(f"Hello, {name}!")

# Invoke the function with a name argument of your choosing:

def greeting(name):
    print(f"Hello, {name}!")

## Section 2 - lists:

# Question 3: Create a list of your favorite movies with  at least 4 elements:

movie_list = ["batman", "starwars", "SPR", "terminator", "NOES",]

# Question 4: Use a print statement to print the list item at the index of 1:

print(movie_list[1])

# Question 5: Append a movie to the end of your list:

movie_list.append("inception")

# Use a print statement to print this ammended list:

print(movie_list)

## Section 3 - dictionaries:

# Question 6: Create a dictionary named 'cellphone' with 2 key:value pairs that are the properties of your cellphone.
#The keys should be: "color" and "number".
#Fill out the values on your own:

cellphone = {
    "color": "blue",     # Replace "blue" with the color of your cellphone
    "number": "123-456-7890"  # Replace "123-456-7890" with your cellphone number
}

# Question 7: Access a value from inside the dictionary (Try to print the value of the 'color' property).

print(cellphone.get("color"))


## Section 4 - strings:

# Question 8: Create a variable and store a string with multiple words in it:

# my_string = "this is a string with multiple words"

# # Question 9: Utilize the method that capitalizes the first letter of each word in your string - store this new string in a new variable:
# capitalized_sentence = sentence.title()

# # Use a print statement to print the new string:


# print(capitalized_sentence)

#Bonus:

# Question 10: Uncomment and look into this nested dictionary - try to relate your knowledge of objects and arrays in JavaScript.

students_in_order = {
  1: {'name': 'Esteban', 'age': '27', 'eye color': 'blue'},
  2: {'name': 'Jackson', 'age': '22', 'eye color': 'brown'},
  3: {'name': 'Zayn', 'age': '26', 'eye color': 'green'}
}

# Question 10 A: Write a print function that outputs the second student in the dictionary
print(students_in_order[2])

# Question 10 B: Write a print statement that outputs the name "Zayn" using the dictionary
print(students_in_order[3]['name'])

# Question 10 C: Write a print statment that outputs the age of Esteban from the dictionary
print(students_in_order[1]['age'])





#Section 1 - sets and tuples:
#Pre-Question: Take a look at this JavaScript Array:
# let javaScriptArray = [12, 55, 33, 40, 55, 33, 20, 12]

# How would you remove duplicates from this JavaScript Array? Take a few minutes to consider what steps are necessary to iterate through this array in JavaScript and remove the duplicates values.

# What advantages are available when we're working with Python? If this Array was instead a set, we wouldn't be able to store multiple values in it. Uncomment the identical set below and run the print statement. What did you notice in the console return?

# my_set = {12, 55, 33, 40, 55, 33, 20, 12}

# print(my_set)

#Question 1a: Create a set of your own with at least 3 different elements.
my_set = {"apple", "banana", "strawberries"}

#Question 1b: Add an item to the set that you just created.
my_set.add("blueberries")

#Question 1c: Print the set with the new data that you added to it:
print(my_set)

#Question 2a: Create a tuple with at least 3 elements inside of it.

my_tuple = (1, 'apple', 3.14)

#Question 2b: Print the tuple you just created.

print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: 'apple'
print(my_tuple[2])  # Output: 3.14


#Section 2 - loops:

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# Question 3: Use a for loop to iterate through the 'days' list above and print the days of the week:
for day in days:
    print(day)

x = 10
add_list = [10, 6, 12, 4, 5]
# Question 4: Uncomment the list and variable x above.  Loop through add_list and add each value to x. Print the value of x at each increment:

for i in add_list:
    # x += i
    print(x+i)  # Print the updated value of x at each increment



# Question 5: While Loops 

#Declare an iterator variable (set to the number 1) and write a While loop that adds 5 to the value of the variable starting_value as long as the iterator is under 10:

#starting_value = 5
# Initialize the variables
starting_value = 5
iterator = 1

# While loop to add 5 to starting_value as long as iterator is less than 10
while iterator < 10:
    starting_value += 5
    print(starting_value)  # Print the updated value of starting_value
    iterator += 1  # Increment the iterator

#Section 3 - conditionals: if, elif, else statements

# favorite_movie = "insert here"    
#Question 6a: Uncomment the favorite_movie variable above and change the value to the title of your favorite movie
#Below, write a conditional statement that prints the string "that's a great movie" if the favorite_movie variable equals your favorite movie.
#Otherwise (else), print the string "that's not my favorite movie".  
#Mess around with the value of the favorite_movie variable and trigger both conditional responses:



#Question 6b: Uncomment the movie_list variable below and implement a for loop that iterates through each item in the list. 
#If the item is a blueberry (or another fruit), print "item is a fruit and not movie"; 
#if the item is a car manufacturing company like Toyota, print "item is a car and not a movie"; 
#otherwise, just print the movie in the list:

# movie_list = ["Inception", "blueberries", "Toyota", "Good Will Hunting"]




#BONUS - conditional and operators practice:
# a = 5
# b = 5
# c = 12
#Question 7a: Use the correct operator to add variables a & c:

#Question 7b: Use the correct operator to subtract variables b & c:

#Question 7c: Use the correct comparison operator that shows if variables a & b equal each other:

#Question 7d: Use the correct operator to find the quotient of variables c & a

#Question 7e: Use the correct operator to find if variables c & b are not equal to each other:

# Function Definition Practice:
# Define functions according to the following prompts. Run the Replit to verify correct output.


# 1. Function that accepts no arguments. It's called say_hello and returns nothing, just prints 'hello'.
def say_hello():
  print("hello")

# 2. a 'sum' function that accepts two integers and returns the sum.
def sum(x,y):
  return x+y

# 3. an 'average' function that accepts two numbers and returns the average.
def average(x,y):
  return (x+y)/2

# 4. A function that accepts a first name and a last name and formats it to "{last_name}, {first_name}" (returns a string).
def format(first_name, last_name):
  return f"{last_name}, {first_name}"

# 5. A function that accepts a first name, last name, graduation year, and student number and returns those four items together in a list.
def grad_list(first, last, year, student_number):
  return [first, last, year, student_number]

# 6. A function that accepts an integer and returns whether it is above 18 or not (Boolean).
def over_18(x):
  return x > 18

#7. A function that accepts a string and prints the string in reverse (no return value).
def reverse(str):
  print(str[::-1])

  def hello():
    print("Hello!")

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

def eat_lunch(lunch_list):
    if not lunch_list:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {lunch_list[0]}")
        for item in lunch_list[1:]:
            print(f"Next I eat {item}")