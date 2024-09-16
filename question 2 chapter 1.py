import time
from PIL import Image

# Step 1: Generate the number 'n'
current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

n = generated_number
print(f"Generated number (n): {n}")

# Step 2: Open the image
image_path = r"C:\Users\shara\Downloads\WhatsApp Image 2024-09-16 at 23.19.53_2207c23e.jpg"
image = Image.open(image_path)

# Step 3: Create a new image with the same size
new_image = Image.new('RGB', image.size)

# Step 4: Modify the pixels
pixels = image.load()
new_pixels = new_image.load()

for i in range(image.width):
    for j in range(image.height):
        r, g, b = pixels[i, j]
        new_pixels[i, j] = (min(r + n, 255), min(g + n, 255), min(b + n, 255))

# Step 5: Save the new image
new_image.save('chapter1out.png')

# Step 6: Sum all the red (r) pixel values in the new image
total_red_value = sum(new_pixels[i, j][0] for i in range(image.width) for j in range(image.height))

print("The sum of all red (r) pixel values in the new image is:", total_red_value)
