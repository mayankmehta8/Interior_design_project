import replicate
import os
import 
os.environ["REPLICATE_API_TOKEN"] = 
image = open("Empty Living Room.jpg", "rb")
output = replicate.run(
    "jagilley/controlnet-hough:854e8727697a057c525cdb45ab037f64ecca770a1769cc52287c2e56472a247b",
    input={
        "image": image,
        "prompt": "Professional Living room Editorial Style Photo, Symmetry, Straight On, Modern Living Room, Large Window, Leather, Glass, Metal, Wood Paneling, Neutral Palette, Ikea, Natural Light, Apartment, Afternoon, Serene, Contemporary, 4k",
        "a_prompt": "best quality, extremely detailed, photo from Pinterest, interior, cinematic photo, ultra-detailed, ultra-realistic, award-winning"
    }
)
print(output)