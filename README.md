surfboard_store_python is a simple python application.

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
