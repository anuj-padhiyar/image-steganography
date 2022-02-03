# image-steganography
simple algorithm for image steganography

install all the required modules using below command
```
$ pip install -r requirement.txt
```

## Introduction
Steganography is a technique of secret data hiding within some file or message.There are so many type of staganography is available like 
- image-steganography
- text-steganography
- video-steganography
- audio-steganography

image-steganography is an art of hiding data behind the image.
`steganography.py` will hide the data for image and `dataRetrive.py` will extract data from the image.
before run this program, just replace your path for image and text in both files.

## Short Descrition on algorithm
```
read the image
read the text
convert text to upper case
convert upper text to binary (7 bit )
store length of text at first location of image
calculate positions at where we want to store character 
	suppose we have 5 char and shape of image is [10x10]
	then we can store next char after skipping (100-1)/5 = 20 pixels
remove 1 MSB from binary character and devide 6 digit into 3 parts (each with 2 bit)
convert each value of R,G,B from decimal to binary and cut last 2 digit
append 1st part(2 bit) of that character to R
append 2nd part(2 bit) of that character to G
append 3rd part(2 bit) of that character to B
store the modified image
```


## Limitation
- This program is **run for only PNG images**. so before starting, just convert your image to png. Note that, This program **not work for JPG/JPEG.**
 - If you have large data, then you have to compress it or you have to choose image with high dimention
