from PIL import Image
import re
import glob
#import os
#import sys

OVERLAP = 12


filenames = glob.glob('*.PNG') + glob.glob('*.JPEG') + glob.glob('*.JPG')
if filenames:
    filename = filenames[0]
    name =  filename.split(".")[0]
    extension =  filename.split(".")[1]
    
    # These two following are intended to read the path of the executable, if the this program is executed from image-splitter.exe
    #application_path = os.path.dirname(sys.executable)
    #image = Image.open(application_path + "/" + filename)
    image = Image.open(filename)
    width, height = image.size

    imageaux = Image.new(image.mode, (width + OVERLAP, height + OVERLAP), color=0)
    imageaux.paste(image, (OVERLAP, OVERLAP))
    width, height = imageaux.size
    #imageaux.save("PROBANDO.PNG", "PNG")

    ## Cuadrante superior-izquierdo
    left = 0 + OVERLAP
    top = 0 + OVERLAP
    right = (width / 2) + OVERLAP
    bottom = (height / 2) + 2*OVERLAP
    img = imageaux.crop((left, top, right, bottom))
    img.save(name + " 1.PNG", "PNG")

    ## Cuadrante superior-derecho
    left = width / 2
    top = 0 + OVERLAP
    right = width
    bottom = (height / 2) + 2*OVERLAP
    img = imageaux.crop((left, top, right, bottom))
    img.save(name + " 2.PNG", "PNG")

    ## Cuadrante inferior-izquierdo
    left = 0 + OVERLAP
    top = (height + OVERLAP) / 2
    right = (width / 2) + OVERLAP
    bottom = height
    img = imageaux.crop((left, top, right, bottom))
    img.save(name + " 3.PNG", "PNG")

    ## Cuadrante inferior-derecho
    left = (width + OVERLAP) / 2 - OVERLAP
    top = (height + OVERLAP) / 2 
    right = width
    bottom = height
    img = imageaux.crop((left, top, right, bottom))
    img.save(name + " 4.PNG", "PNG")
