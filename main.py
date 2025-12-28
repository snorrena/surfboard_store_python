from inventory import surfboard_list
from display import print_surfboard_data
from products import Surfboard

surfboard: Surfboard
for surfboard in surfboard_list:
    print(
        f"Brand: {surfboard.brand}, Model: ${surfboard.model}, Length: {surfboard.length}, Width: {surfboard.width}"
    )

print_surfboard_data(surfboard_list)
