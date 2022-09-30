#importing matplot library
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#a function use formula
def rgb2bw(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    bw = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return bw

#read an colour image and convert to black and white with function rbg2bw
image =mpimg.imread('C:\\Users\\98919\\Desktop\\Computational Data Minig\\Projects 1\\Image-.png')
black_white=rgb2bw(image)

#show black and white image using matplot
plt.imshow(black_white, cmap=plt.get_cmap('gray'))
plt.savefig('imagebw2.png')
plt.show()