import sys
import os.path
from PIL import Image

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) >3:
    sys.exit("Too many command-line arguments")

as_input = sys.argv[1]
as_output = sys.argv[2]
allowed_extensions = ['.jpg', '.jpeg', '.png']
try:
    os.path.splitext(as_input)[1] in allowed_extensions
    os.path.splitext(as_output)[1] in allowed_extensions
    if os.path.splitext(as_input)[1] != os.path.splitext(as_output)[1]:
        sys.exit("Input and output have different extensions")
except FileNotFoundError:
    sys.exit('Invalid input')

# Open the input file and get its size
input_image = Image.open(as_input)
input_size = input_image.size

# Open the shirt file and resize it to match the input size
shirt_image = Image.open("shirt.png")
shirt_image = shirt_image.resize(input_size)

# Overlay the shirt image on top of the input image
input_image.paste(shirt_image, (0, 0), shirt_image)

# Save the resulting image to the output file
input_image.save(as_output)