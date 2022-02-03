from steganography import Picture

class DataRetrive(Picture):
    def __init__(self,path):
        super().__init__(path)
    
    def extract_data(self,l,w):
        colors = self.get_color_value(l,w)
        binColors = list(Picture.dec_bin(i) for i in colors)
        if l==0 and w==0:
            character = [binColors[0][-3:],binColors[1][-3:],binColors[2][-2:]]
        else:
            character = [binColors[0][-2:],binColors[1][-2:],binColors[2][-2:]]
        return ''.join(character)

if __name__ == "__main__":
    file= open("text/retrivedData.txt","w")
    image = DataRetrive("./Stagno/stagnoAnimal.png")
    binDataLength = image.extract_data(0,0)
    dataLength = DataRetrive.bin_dec(str(binDataLength))
    jump = image.calculate_jump(dataLength)
    l,w = 0,1
    
    for i in range(dataLength):
        char = image.extract_data(l, w)
        char = ('1' if char[0]=='0' else '0')+char
        file.write(chr(DataRetrive.bin_dec(char)))
        l,w = image.get_location(jump,l,w)
    file.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    