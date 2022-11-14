from PIL import Image, ImageFilter
filename = "myImage.jpg"
with Image.open(filename) as img:
    img.load()
    #loads the image into memory
#displaying the image, 
#img.show()

#properties when dealing with images, the Image class attributes
print(img.mode)#whether rgb or cymk
print(img.size)#image in pixels(1600 * 800)
#print(img.format)#either a jpg or a png

#cropping and resizing images
#The Image class has two methods that can be used to perform these operations
#.crop() and .resize():

"""
The argument to .crop() must be a 4-tuple that defines the left, upper, right, and bottom
edges of the region that you wish to crop. 
"""
cropped_img = img.crop((300, 150, 700, 1000))
print(cropped_img.size)
#cropped_img.show()

"""
.resize() allowes a turple of the new image width and height as specified
if we need aquarter the intilal image width and height, we use the floor_division_operator
"""
low_res_img = cropped_img.resize(
    (cropped_img.width // 4, cropped_img.height // 4)
)
#low_res_img.show()

#similar scalling can be archieved using the reduce() method as below 
low_res_img = cropped_img.reduce(4)
#low_res_img.show()

#thumbnail can equally be used when dealing withimages 
"""
If you prefer to set a maximum size rather than a scaling factor, then you can use .thumbnail().
The size of the thumbnail will be smaller than or equal to the size that you set.

Note: The .thumbnail() method changes the Image object in place and doesn’t 
return a new object. However, .crop(), .resize(), and .reduce() 
all return a new Image object. 
Not all methods in the Pillow library behave in the same way.
"""
MAX_SIZE = (100, 100)
cropped_img.thumbnail(MAX_SIZE, resample=3)#resampling is optional
#cropped_img.show()

#once all is okay with the retuened object, you can then save the new image using the save() method
#cropped_img.save("lessImage.jpg")
#cropped_img.save("lessImage.png")


#Transaformations | Basic image manipulations
#converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)#returns a warning for deprecation
converted_img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
#converted_img.show()
mirrorImage = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
#mirrorImage.show()
"""
Image.FLIP_LEFT_RIGHT: 
Flips the image left to right, resulting in a mirror image

Image.FLIP_TOP_BOTTOM: 
Flips the image top to bottom

Image.ROTATE_90:
Rotates the image by 90 degrees counterclockwise

Image.ROTATE_180:
Rotates the image by 180 degrees

Image.ROTATE_270:
Rotates the image by 270 degrees counterclockwise, which is the same as 90 degrees
clockwise

Image.TRANSPOSE: 
Transposes the rows and columns using the top-left pixel as the origin, 
with the top-left pixel being the same in the transposed image as in the original image

Image.TRANSVERSE:
Transposes the rows and columns using the bottom-left pixel as the origin, 
with the bottom-left pixel being the one that remains fixed between the original
and modified versions
"""

"""
All the rotation options above define rotations in steps of 90 degrees. 
If you need to rotate an image by another angle, then you can use .rotate():
"""
rotated_img = img.rotate(45)
#rotated_img.show()
"""
The Image object returned is the same size as the original Image. 
Therefore, the corners of the image are missing in this display. 
You can change this behavior using the expand named parameter:
"""
rotated_img = img.rotate(45, expand=True)
#rotated_img.show()


#Bands and Modes of an Image using pillow
"""
An image is a two-dimensional array of pixels, where each pixel corresponds to a color.
Each pixel can be represented by one or more values. For example, in an RGB image, each pixel is 
represented by three values corresponding to the red, green, and blue values for that pixel.

Therefore, the Image object for an RBG image contains three bands, one for each color. 
An RGB image of size 100x100 pixels is represented by a 100x100x3 array of values.

RGBA images also include the alpha value,
Therefore, an RGBA image of size 100x100 pixels is represented by a 100x100x4 array of values.
"""

cmyk_img = img.convert("CMYK")
gray_img = img.convert("L")  # Grayscale
#cmyk_img.show()
#gray_img.show()
rgb_bands = img.getbands()
print(rgb_bands)
cmyk_bands = cmyk_img.getbands()
print(cmyk_bands)

#splitting an image
red, green, blue = img.split()
print(red)# returns a grey scale image here
"""
The mode of the object that .split() returns is 'L', indicating this is a grayscale image
"""

#merging and returning single color band from rgb image 
"""
The first argument in merge() determines the mode of the image that you want to create. 
The second argument contains the individual bands that you want to merge into a single image.

To create the image showing only the red channel, you merge the red band from the original 
image with green and blue bands that only contain zeros. To create a band containing zeros
everywhere, you use the .point() method.
"""
zeroed_band = red.point(lambda _: 0)

red_merge = Image.merge(
    "RGB", (red, zeroed_band, zeroed_band)
    )

green_merge = Image.merge(
    "RGB", (zeroed_band, green, zeroed_band)
    )

blue_merge = Image.merge(
    "RGB", (zeroed_band, zeroed_band, blue)
    )

#ed_merge.show()

#Image Blurring, Sharpening, and Smoothing
blur_img = img.filter(ImageFilter.BLUR)
#blur_img.show()

"""
The displayed image is a blurred version of the original one. You can zoom in to
observe the difference in more detail using .crop() and then display the images again using .show():
"""
#img.crop((300, 300, 500, 500)).show()
#blur_img.crop((300, 300, 500, 500)).show()


"""
You can customize the type and amount of blurring that you need using
ImageFilter.BoxBlur() or ImageFilter.GaussianBlur():
"""

#img.filter(ImageFilter.BoxBlur(5)).show()
#img.filter(ImageFilter.BoxBlur(20)).show()
#img.filter(ImageFilter.GaussianBlur(20)).show()

#sharpeninig an image 
sharp_img = img.filter(ImageFilter.SHARPEN)
#img.crop((300, 300, 500, 500)).show()
#sharp_img.crop((300, 300, 500, 500)).show()

"""
Perhaps instead of sharpening an image, you need to smooth it.
You can achieve this by passing ImageFilter.SMOOTH as an argument for .filter():
"""
smooth_img = img.filter(ImageFilter.SMOOTH)
#img.crop((300, 300, 500, 500)).show()
#smooth_img.crop((300, 300, 500, 500)).show()

#Edge Detection, Edge Enhancement, and Embossing
#It’s also possible for an algorithm to detect edges automatically using edge detection kernels.
#The ImageFilter module in Pillow has a predefined kernel to achieve this.
img_gray = img.convert("L")
edges = img_gray.filter(ImageFilter.FIND_EDGES)
#edges.show()

"""
You can obtain a better outcome by applying the ImageFilter.SMOOTH filter before finding the edges:
"""
img_gray_smooth = img_gray.filter(ImageFilter.SMOOTH)
edges_smooth = img_gray_smooth.filter(ImageFilter.FIND_EDGES)
#edges_smooth.show()

"""
You can also enhance the edges of the original image with the ImageFilter.EDGE_ENHANCE filter:
"""

edge_enhance = img_gray_smooth.filter(ImageFilter.EDGE_ENHANCE)
#edge_enhance.show()
edge_enhance.save("enhanced.jpg")

#embossing
emboss = img_gray_smooth.filter(ImageFilter.EMBOSS)
#emboss.show()