import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from PIL import Image
import os
from os import listdir
company_name = input("Enter company name: ")
folder_dir = "C:/Users/Sundas.Mohsin/Desktop/Project/images/"
images_list = []
for img in os.listdir(folder_dir):
    if(img.startswith(company_name) and img.endswith (".png")):
        images_list.append(img)
  
d = os.getcwd
os.chdir(folder_dir)
fig = plt.figure()
plt.title("RGB Intensity")
plt.axis("off")
for i in range(len(images_list)):
    file = images_list[i]
    im = Image.open(file)
    px = im.load()
    index = i+1
    rows = 1
    cols = 3    
    ax = fig.add_subplot(rows,cols,index, projection = "3d")
    ax.set_title(file,fontsize=6)

    x=[]
    y=[]
    z=[]
    c=[]

    for row in range(0,im.height):
        for col in range(0, im.width):
            pix = px[col,row]
            newCol = (pix[0]/255, pix[1]/255, pix[2]/255)
            if(not newCol in c):
                x.append(pix[0])
                y.append(pix[1])
                z.append(pix[2])
                c.append(newCol)

    ax.scatter(x,y,z,c=c)
plt.savefig("C:/Users/Sundas.Mohsin/Desktop/Project/"+ company_name +".png")
plt.show()