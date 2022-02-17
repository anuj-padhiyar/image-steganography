import skimage as si
import numpy as np
import math

class Picture:
    def __init__(self,path):
        self.img = si.io.imread(fname = path)
    
    def get_image_shape(self):
        return self.img.shape

    def get_image_lw(self):
        return list(self.get_image_shape())[:-1]
    
    def dec_bin(val):
        return np.binary_repr(val,width=8)

    def bin_dec(val):
        return int(val,2)
    
    def get_color_value(self,l,w):
        return [self.img[l][w][0],self.img[l][w][1],self.img[l][w][2]]
    
    def assign_color_value(self,value,l,w):
        for i,val in enumerate(value):
            self.img[l][w][i] = Picture.bin_dec(val)
    
    def calculate_jump(self,l):
        totalPixel = np.prod(self.get_image_lw())
        return math.ceil((totalPixel-1)/l)

    def store_data(self,value,l,w):
        colors = self.get_color_value(l,w)
        binColors = list(Picture.dec_bin(i) for i in colors)
        binValue = Picture.dec_bin(value)
        if l==0 and w==0:
            binValue= [binValue[0:3],binValue[3:6],binValue[6:]]
        else:
            binValue = binValue[2:]
            binValue = [binValue[0:2],binValue[2:4],binValue[4:]]
        
        finalColors = []
        for a,b in zip(binColors,binValue):    
            finalColors.append(a[:-len(b)] + b)
        self.assign_color_value(finalColors,l,w)
    
    def get_location(self,jump,l,w):
        originalL,originalW = self.get_image_lw()
        if (w+jump) < originalW:
            return [l,jump+w]
        
        l += math.floor(jump/originalW)
        w = (w+jump) % originalW
        return [l,w]
        
    def store_image(self,path):
        si.io.imsave(fname = path, arr = self.img)
                
if __name__ == "__main__":
    file= open("text/data.txt","r")
    image = Picture("./Images/animal.png")
    
    textInFile = file.read().upper()
    dataLength = len(textInFile)
    file.close()
    
    if np.prod(list(image.get_image_lw())) > dataLength:
        image.store_data(dataLength,0,0)
        jump = image.calculate_jump(dataLength)
        l,w = 0,1
        
        for i,val in enumerate(textInFile):        
            image.store_data(ord(val),l,w)
            l,w = image.get_location(jump,l,w)
        image.store_image("./Stagno/stagnoAnimal.png")
    else:
        print("Data is too big!!")
        print("compress the data or select big image.")
