#necesito:    
# ancho(1920)= imagen.png
# alto(1080) =imagen.png
# mcd = mcd(1920,1080)
# aspect ratio ancho = ancho/mcd
# aspect ratio alto = alto/mcd
# 
# rpta: aspect ratio ancho:aspect ratio alto

#region error
# Fuente: https://bobbyhadz.com/blog/python-no-module-named-pil
# Error que encontre al tratar de importar PIL
# Error Solventado:

# shell
# 👇️ Before installing Pillow, uninstall PIL.
# pip uninstall PIL

# 👇️ in a virtual environment or using Python 2
# pip install Pillow

# 👇️ for python 3 (could also be pip3.10 depending on your version)
# pip3 install Pillow

# 👇️ if you get permissions error
# sudo pip3 install Pillow
# pip install Pillow --user

# 👇️ if you don't have pip in your PATH environment variable
# python -m pip install --upgrade Pillow

# 👇️ for python 3 (could also be pip3.10 depending on your version)
# python3 -m pip install --upgrade Pillow

# 👇️ using py alias (Windows)
# py -m pip install --upgrade Pillow

# 👇️ for Anaconda
# conda install -c conda-forge pillow

# 👇️ for Jupyter Notebook
# !pip install Pillow               

# Tenga en cuenta que nos aseguramos de desinstalar PIL antes de
# instalar Pillow porque Pillow y PIL no pueden coexistir en el mismo entorno.
#endregion

# region Testeo abrimos una imagen
#from PIL import Image

#Cargamos la imagen  
#img =Image.open('images/bochi.jpg')
#img.show()


#Otra froma de hacerlo:

#import PIL.Image
#fp = open("images/bochi.jpg","rb") # rb: lei algo corto de que era (read only in binary)
#img = PIL.Image.open(fp)
#img.show()

#endregion

from PIL import Image
import requests
import io

# Abirendo la url para leer sus dimensiones
img = requests.get("https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png",stream=True)
aux_img = Image.open(io.BytesIO(img.content))
# Hallando su ancho y alto
width = aux_img.width
height = aux_img.height

# Funcion para hallar el maximo común divisor(mcd) de los 2 numeros
def mcd(a,b):
    temp=0
    while b!=0:
        temp =b
        b=a%b
        a=temp
    
    return a

# Llamamos a la funcion
maximocd = mcd(width,height)

# Calculamos el aspect ratio
aspectRatioWidth = width/maximocd
aspectRatioHeight = height/maximocd

print ("el ratio de la imagen es:",int(aspectRatioWidth),":",int(aspectRatioHeight))


