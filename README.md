surfboard_store_python is a simple python application.

//TODO: this comment has been added to test lazyit

This app generates a list of surfboard in a store inventory. Each surfboard has a model, make, length and width.
The app loops through the inventory list and prints out the details for each surfboard in the inventory.


The surfboard data object is defined in the products.py file. The class: Surfboard defines an object
constructor that takes in all fields for the surfboard data object. The class also includes
a function that prints out the object field details.

The inventory.py imports the Surfboard class and uses it to instantiate a number of surfboard objects.
The surfboard objects created are add to a list.

The display.py file defines a function that will loop through the list of surfboard and call the print_info
method on each to dispay the surfboard details. This file imports the Surfboard class and uses it to 
type the function input argument as a list of type Surfboard.

The main.py imports the surfboard list from the inventory and the print_surfboard_data method from 
display. The surfboard list is passed into the print_surfboard_data function as argument. When the function 
is called, it loops through the surfboard inventory and calls the print_info method on each object.

The main.py file also includes a for loop that iterates over the inventory list and prints out 
the surfboard details for each item.

note: python used indentation to define code blocks. Indentation of four spaces after the end of a statement
with a colon:
ex.

if 5 > 2: //the : colon indicate the end of a statement
    #all code four spaces from the start of the statement are part of the code block

types annotations may be added as a colon followed by the type. Ofter the variable type is implied.
my_list_variable:[int]

functions, classes and variables can be imported from other files as needed

from file_name_without_extention import object_name  //the from keyword is first, then the file name and import
def - keyword used to define a function or class method

for items in items_array:[object_name] //for in keywords with a explicity type annotation

the print statement used parenthesis. Objects the in statment surrounded by curly brackets will be string interpolated. Dot notation
can be used to access object field data or functions.
print(f"my_object_value - {object.value}, function_return - {object.function_call()}")

def _init_  //constructor method for object instatiation
self // keyword used inside an object instance to reference encapsulated fields and/or functions

type annotation hints can be used but are not enforced
i: int
for i in range(5):
    print(f"value_of_i={i}")
