# EDIT IMAGES USING PYTHON
# p="Edit IMAGES using PYTHON"
# print(p.upper())
# installation of pillow library
# resize image files
# resize multiple img using for loop
# sharpness -> import ImageEnhance
# brightness
# color
# contrast
# image blur, gaussianblur

# What does the "Most likely due to a circular import" error mean in Python? 
# This error in Python signifies a circular dependency among two or more modules,
# where they try to import each other, creating an infinite loop and leading to the error. 
# It's important to restructure your code to avoid such circular dependencies.

from PIL import Image, ImageEnhance, ImageFilter
import os

# img1=Image.open('zman.png')
# # img1.save('zman.png')
# img1.show()
# img2=Image.open('zat.jpg')

# Resizing image 
# maxsize=(200,210)
# img1.thumbnail(maxsize)
# img1.save('zmansmallsize.png')
# img1.show()

# for resizing many images
for item in os.listdir():
    if item.endswith('.jpg'):
        img1=Image.open(item)
        filename,extension = os.path.splitext(item)
        img1.save(f'{filename}.png')

 #-----Sharpness-----#
        
# img1=Image.open('zman.png')
# enhancer = ImageEnhance.Sharpness(img1)
# enhancer.enhance(5).save('zmansharpeedby5.jpg')

 #-----Color----#
        
img1=Image.open('zman.jpg')
enhancer = ImageEnhance.Color(img1)
enhancer.enhance(8).save('zmancolorwitho8.jpg')

 #-----Brightness----#
        
img1=Image.open('zman.jpg')
enhancer = ImageEnhance.Brightness(img1)
enhancer.enhance(2).save('zmanBrightness2.jpg')

 #-----Contrast----#
        
img1=Image.open('zman.jpg')
enhancer = ImageEnhance.Contrast(img1)
enhancer.enhance(7).save('zmanContrast7.jpg')



#--------image blur, gaussianblur---------#
img1.filter(ImageFilter.GaussianBlur(radius=3)).save('zmaneditedtoblurr3.jpg')











