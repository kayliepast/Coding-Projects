"""
A wes anderson style filter that emphasizes 
pastels and yellows and is grainy. 
"""

from PIL import Image, ImageEnhance
import numpy as np

# Specify the input and output image paths
input_image = "cute_yarn_robot.jpeg"  
output_image = "wes_anderson.jpeg"

# Open the image
img = Image.open(input_image)

# Ensure the image is in RGB mode
img = img.convert('RGB')

# Split the image into its RGB channels
r, g, b = img.split()

# Adjust the red channel to bring out warm orange tones
r_enhancer = ImageEnhance.Brightness(r)
# Increase red brightness by 25% for stronger warm tones
r = r_enhancer.enhance(1.25)  

# Adjust the green channel to add a soft yellowish tint (contributes to the orange feel)
g_enhancer = ImageEnhance.Brightness(g)
# Increase green brightness by 15% to blend with red and create orange hues
g = g_enhancer.enhance(1.15)  

# Reduce the blue channel slightly to mute cool tones and make the image feel warmer
b_enhancer = ImageEnhance.Brightness(b)
 # Decrease blue brightness by 15%
b = b_enhancer.enhance(0.85) 

# Merge the modified channels back into one image
wes_anderson_img = Image.merge('RGB', (r, g, b))

# Enhance the color saturation slightly to make the orange tones pop without being overwhelming
color_enhancer = ImageEnhance.Color(wes_anderson_img)
# Increase saturation by 10%
wes_anderson_img = color_enhancer.enhance(1.1)  

# Reduce contrast slightly for a softer, desert-like appearance
contrast_enhancer = ImageEnhance.Contrast(wes_anderson_img)
# Slightly reduce contrast by 10%
wes_anderson_img = contrast_enhancer.enhance(0.90)  

# Add a subtle grain effect for a vintage, film-like texture
def add_grain(image):
    width, height = image.size
    grain = np.random.normal(128, 20, (height, width, 3)).astype(np.uint8)  
    # Gentle grain for texture
    grain_img = Image.fromarray(grain, mode="RGB")
    # Blend the image with grain at 20% opacity for subtle texture
    return Image.blend(image, grain_img, 0.2)  

vintage_nevada_img = add_grain(wes_anderson_img)

# Save the final image with the subtle orangey Nevada-style filter
vintage_nevada_img.save(output_image)

print(f"wes anderson filter image saved as {output_image}")
