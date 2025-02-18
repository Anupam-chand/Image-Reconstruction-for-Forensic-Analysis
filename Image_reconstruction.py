from PIL import Image
import numpy as np

# Load the scrambled image (replace 'scrambled_image.png' with your file path)
scrambled_img = Image.open("C:\\Users\\anupa\\Downloads\\jigsaw.png")
width, height = scrambled_img.size

# Define grid size (5x5 tiles)
grid_size = 5
tile_width = width // grid_size
tile_height = height // grid_size

# Initialize a blank reconstructed image
reconstructed_img = Image.new("RGB", (width, height))

# Define the mappings (Original Row, Original Column, Scrambled Row, Scrambled Column)
mappings = [
    (2, 1, 0, 0), (1, 1, 0, 1), (4, 1, 0, 2), (0, 3, 0, 3), (0, 1, 0, 4),
    (1, 4, 1, 0), (2, 0, 1, 1), (2, 4, 1, 2), (4, 2, 1, 3), (2, 2, 1, 4),
    (0, 0, 2, 0), (3, 2, 2, 1), (4, 3, 2, 2), (3, 0, 2, 3), (3, 4, 2, 4),
    (1, 0, 3, 0), (2, 3, 3, 1), (3, 3, 3, 2), (4, 4, 3, 3), (0, 2, 3, 4),
    (3, 1, 4, 0), (1, 2, 4, 1), (1, 3, 4, 2), (0, 4, 4, 3), (4, 0, 4, 4)
]

for o_row, o_col, s_row, s_col in mappings:
    # Extract tile from scrambled position
    left = s_col * tile_width
    upper = s_row * tile_height
    right = left + tile_width
    lower = upper + tile_height
    tile = scrambled_img.crop((left, upper, right, lower))

    # Paste tile into original position
    paste_left = o_col * tile_width
    paste_upper = o_row * tile_height
    reconstructed_img.paste(tile, (paste_left, paste_upper))

# Save or display the result
reconstructed_img.save("reconstructed_image.png")
reconstructed_img.show()

