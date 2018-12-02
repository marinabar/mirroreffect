from PIL import Image
img = Image.open("avantages-quil-y-a-a-grandir-dans-un-petit-village.jpg")
pixels=img.load()
for i in range(img.width//2+1):
    for j in range(img.height):
        pixels[img.width-1-i, j]=pixels[i, j]
img.show()
