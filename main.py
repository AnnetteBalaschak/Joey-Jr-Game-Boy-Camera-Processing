import os
from PIL import Image

input_dir = "/Users/annettebalaschak/Desktop/gb cam input"
output_dir = "/Users/annettebalaschak/Desktop/gb cam output"

input_colors = []
output_colors = [(27,42,9), (14,69,11), (73,107,34), (154,158,63)]  # Example output colors in RGB format
color_map = {}

def get_original_palette(image):
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            if pixel not in input_colors:
                input_colors.append(pixel)
    input_colors.sort()

# Apply the palette to the new image
def recolor_image(image):
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            if pixel in input_colors:
                index = input_colors.index(pixel)
                new_color = output_colors[index]
                image.putpixel((x, y), new_color)

if __name__ == "__main__":
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop over input directory files
    for file in os.scandir(input_dir):
        if file.is_file():
            with Image.open(file.path) as img:
                # Get the original palette from the image
                get_original_palette(img)
                recolor_image(img)
                
                img.resize
                img = img.resize((1024, 896), Image.Resampling.NEAREST)
                img.save(os.path.join(output_dir, file.name))

                # clear the palette
                input_colors.clear()