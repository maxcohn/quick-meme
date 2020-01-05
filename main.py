from PIL import Image

f = open('test-images/dog.jpg', mode='rb')
img = Image.open(f)

img.show()

f.close()
