#importing image from pillow library
from PIL import Image

#open an image
image = Image.open('C:\\Users\\98919\\Desktop\\Computational Data Minig\\Projects 1\\Image-.png')

#convert image ro black / gray and white
black_white=image.convert('1')
gray=image.convert('L')

#save black and white / gray image
black_white.save("imagebw.png")
gray.save("imagegry.png")