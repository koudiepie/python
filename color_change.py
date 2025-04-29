from PIL import Image

original = Image.open("pokemon.png").convert("RGB")

r, g, b = original.split()

new = Image.merge("RGB", (g, b, r))

new.show()