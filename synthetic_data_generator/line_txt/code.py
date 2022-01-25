import numpy as np
import random
from PIL import ImageFont, ImageDraw, Image, ImageFilter
from os import listdir
from os.path import isfile, join
import string
import langdetect
from tqdm import tqdm
import uuid
import json
from config import OUTPATH
import config
import cv2 
import numpy as np
import os

data_jsonf = []
ocr_jsonf = []
os.system('mkdir -p ' +OUTPATH+"data/")
os.system('mkdir -p ' +OUTPATH+"class1/white_bgr/images/")
os.system('mkdir -p ' +OUTPATH+"class1/color_bgr/images/")
os.system('mkdir -p ' +OUTPATH+"class1/white_bgr/txt/")
os.system('mkdir -p ' +OUTPATH+"class1/color_bgr/txt/")
os.system('mkdir -p ' +OUTPATH+"class2/white_bgr/images/")
os.system('mkdir -p ' +OUTPATH+"class2/color_bgr/images/")
os.system('mkdir -p ' +OUTPATH+"class2/white_bgr/txt/")
os.system('mkdir -p ' +OUTPATH+"class2/color_bgr/txt/")
os.system('mkdir -p ' +OUTPATH+"class3/white_bgr/images/")
os.system('mkdir -p ' +OUTPATH+"class3/color_bgr/images/")
os.system('mkdir -p ' +OUTPATH+"class3/white_bgr/txt/")
os.system('mkdir -p ' +OUTPATH+"class3/color_bgr/txt/")


def file_list(mypath):
    onlyfiles = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles


def create_image(background,font,symbol,font_size,col,font_colour):
    image = Image.open(background)
    if image.mode in ("RGBA", "P"):
        image = image.convert("RGB")
    #image=image.resize((200,200))
    font_pil = ImageFont.truetype(font, font_size, layout_engine=ImageFont.LAYOUT_RAQM)
    ascent, descent = font_pil.getmetrics()  
    try:
        if symbol==" ":
            a=font_pil.getmask('-').getbbox()[2]
        else:
            a=font_pil.getmask(symbol).getbbox()[2]
    except TypeError:
        print("TYPEERROR handled due to",symbol)
        #a=font_pil.getmask('M').getbbox()[2]
        return None
    text_width = a
    text_height = ascent+descent
    text_width+=int(0.03*(text_width))
    text_height+=int((0.10*text_height))
    image=image.resize((text_width+8,text_height),Image.ANTIALIAS)
    a=text_width//2
    b=ascent+int(0.05*(ascent))
    #image=image.crop((2,2,20+text_width,20+text_height))
    draw=ImageDraw.Draw(image)
    draw.text((8,text_height//2),symbol,col,font=font_pil,anchor="lm")
    #randomly select noise type
    #image=Image.open(image)
    noice = random.choice(config.noices)
    image = noisy(noice,image)
    #image.thumbnail([100,100], Image.ANTIALIAS)
    image_id=str(uuid.uuid4())
    #image.save(join(config.OUTPATH+"data/",image_id)+".png")
    #with open(join(config.OUTPATH,image_id)+".gt.txt", 'w') as f:
        #f.write(symbol)
    src = "synthetic"
    bg = background.split(".")[0].split("/")[1]
    font = font.split(".")[0].split("/")[-1].lower()
    if font.split("-")[-1] == "nonunicode":
        code = "non-unicode"
        font = listToString(font.split("-")[:-1])
    else: code = "unicode"
    version = "new"
    if bg in config.class3_bgs and noice in config.class3_noices:
        class_type = "class3"
        if bg in config.bgs_color:
            bg_color = "color"
        #elif noice == "edges":
           # bg_color = "color"
        else:
            bg_color = "white"
        if bg_color == "white":
            image.save(join(config.OUTPATH+f"{class_type}/white_bgr/images/",image_id)+".png")
            image.save(join(config.OUTPATH+"data/",image_id)+"_"+class_type+"_"+bg_color+"_"+src+"_"+font+"_"+code+"_"+version+".png")
            with open(join(config.OUTPATH+f"data/",image_id)+"_"+class_type+"_"+bg_color+"_"+src+"_"+font+"_"+code+"_"+version+".gt.txt", 'w') as f:
                f.write(symbol)
            with open(join(config.OUTPATH+f"{class_type}/white_bgr/txt/",image_id)+".gt.txt", 'w') as f:
                f.write(symbol)
        else: 
            image.save(join(config.OUTPATH+f"{class_type}/color_bgr/images/",image_id)+".png")
            image.save(join(config.OUTPATH+"data/",image_id)+"_"+class_type+"_"+bg_color+"_"+src+"_"+font+"_"+code+"_"+version+".png")
            with open(join(config.OUTPATH+f"data/",image_id)+"_"+class_type+"_"+bg_color+"_"+src+"_"+font+"_"+code+"_"+version+".gt.txt", 'w') as f:
                f.write(symbol)
            with open(join(config.OUTPATH+f"{class_type}/color_bgr/txt/",image_id)+".gt.txt", 'w') as f:
                f.write(symbol)
    elif bg in config.bgs_white and noice in config.class1_noices and font_colour==(0,0,0):
        class_type = "class1"
        if bg in config.bgs_color:
            bg_color = "color"
        #elif noice == "edges":
           # bg_color = "color"
        else:
            bg_color = "white"
        if bg_color == "white":
            image.save(join(config.OUTPATH+f"{class_type}/white_bgr/images/",image_id)+".png")
            image.save(join(config.OUTPATH+"data/",image_id)+"_"+class_type+"_"+bg_color+"_"+src+"_"+font+"_"+code+"_"+version+".png")
            with open(join(config.OUTPATH+f"data/",image_id)+"_"+class_type+"_"+bg_color+"_"+src+"_"+font+"_"+code+"_"+version+".gt.txt", 'w') as f:
                f.write(symbol)
            with open(join(config.OUTPATH+f"{class_type}/white_bgr/txt/",image_id)+".gt.txt", 'w') as f:
                f.write(symbol)
        else: 
            image.save(join(config.OUTPATH+f"{class_type}/color_bgr/images/",image_id)+".png")
            image.save(join(config.OUTPATH+"data/",image_id)+"_"+class_type+"_"+bg_color+"_"+src+"_"+font+"_"+code+"_"+version+".png")
            with open(join(config.OUTPATH+f"data/",image_id)+"_"+class_type+"_"+bg_color+"_"+src+"_"+font+"_"+code+"_"+version+".gt.txt", 'w') as f:
                f.write(symbol)
            with open(join(config.OUTPATH+f"{class_type}/color_bgr/txt/",image_id)+".gt.txt", 'w') as f:
                f.write(symbol)
    else:
        if bg in config.bgs_class3 and noice in config.class3_noices:
            class_type = "class3"
        elif bg in config.bgs_white and noice in config.class1_noices and font_colour==(0,0,0):
            class_type = "class1"
        elif noice in config.class3_noices:
            class_type = "class3"
        elif bg in config.class3_bgs:
            class_type = "class3"
        #elif bg in config.bgs_white: class_type = "class1"
        #elif bg not in config.bgs_color and noice in config.class1_noices:
            #class_type = "class2"
        else: class_type = "class2"
        if bg in config.bgs_color:
            bg_color = "color"
        #elif noice == "edges":
           # bg_color = "color"
        else:
            bg_color = "white"
        if bg_color == "white":
            image.save(join(config.OUTPATH+f"{class_type}/white_bgr/images/",image_id)+".png")
            image.save(join(config.OUTPATH+"data/",image_id)+"_"+class_type+"_"+bg_color+"_"+src+"_"+font+"_"+code+"_"+version+".png")
            with open(join(config.OUTPATH+f"data/",image_id)+"_"+class_type+"_"+bg_color+"_"+src+"_"+font+"_"+code+"_"+version+".gt.txt", 'w') as f:
                f.write(symbol)
            with open(join(config.OUTPATH+f"{class_type}/white_bgr/txt/",image_id)+".gt.txt", 'w') as f:
                f.write(symbol)
        else: 
            image.save(join(config.OUTPATH+f"{class_type}/color_bgr/images/",image_id)+".png")
            image.save(join(config.OUTPATH+"data/",image_id)+"_"+class_type+"_"+bg_color+"_"+src+"_"+font+"_"+code+"_"+version+".png")
            with open(join(config.OUTPATH+f"data/",image_id)+"_"+class_type+"_"+bg_color+"_"+src+"_"+font+"_"+code+"_"+version+".gt.txt", 'w') as f:
                f.write(symbol)
            with open(join(config.OUTPATH+f"{class_type}/color_bgr/txt/",image_id)+".gt.txt", 'w') as f:
                f.write(symbol)
    width, height= image.size
    gen_ulca_json(image,symbol,image_id,width,height,class_type,bg_color,src,font,code,version)

    return image

def gen_ulca_json(imge,line,image_id,width,height,class_type,bg_color,src,font,code,version):

        data_json = (
                            {
                                "groundTruth" : line,
                                "imageFilename": image_id+"_"+class_type+"_"+bg_color+"_"+src+"_"+font+"_"+code+"_"+version+".png",
                                "boundingBox":{
                                "vertices":[
                                {
                                    "x": 0,
                                    "y": 0
                                },
                                {
                                    "x": width,
                                    "y": 0
                                },
                                {
                                    "x": width,
                                    "y": height
                                },
                                {
                                    "x": 0,
                                    "y": height
                                }
                                ]
                            }
                            }
                        )
        
        ocr_json = (
                            {
                                "classType": class_type,
                                "backgroundColor": bg_color,
                                "source": src,
                                "fontName": font,
                                "fontType": code,
                                "fontVersion": version,
                                "groundTruth" : line,
                                "imageFilename": image_id+"_"+class_type+"_"+bg_color+"_"+src+"_"+font+"_"+code+"_"+version+".png",
                                "boundingBox":{
                                "vertices":[
                                {
                                    "x": 0,
                                    "y": 0
                                },
                                {
                                    "x": width,
                                    "y": 0
                                },
                                {
                                    "x": width,
                                    "y": height
                                },
                                {
                                    "x": 0,
                                    "y": height
                                }
                                ]
                            }
                            }
                        )
        #data_jsonf.append(data_json)
        #ocr_jsonf.append(ocr_json)
        with open(OUTPATH+"data/"+"data-ocr"+".json", 'a') as outfile:
            json.dump(ocr_json, outfile)
        with open(OUTPATH+"data/"+"data"+".json", 'a') as outfile:
            json.dump(data_json, outfile)

def noisy(noise_typ,image):
   if noise_typ == "gauss":
      noisy = image.filter(ImageFilter.GaussianBlur(radius = 1))
      return noisy
   elif noise_typ == "edge":
      noisy = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
      return noisy
   elif noise_typ == "emboss":
      noisy = image.filter(ImageFilter.EMBOSS)
      return noisy
   elif noise_typ =="median":
      noisy = image.filter(ImageFilter.MedianFilter(size = 3)) 
      return noisy
   #elif noise_typ =="edges":
    #  noisy = image.filter(ImageFilter.FIND_EDGES) 
     # return noisy
   elif noise_typ =="contour":
      noisy = image.filter(ImageFilter.CONTOUR) 
      return noisy
   elif noise_typ =="smooth":
      noisy = image.filter(ImageFilter.SMOOTH_MORE) 
      return noisy
   else: return image

# Function to convert  
def listToString(s): 
    
    # initialize an empty string
    str1 = " "
    # return string  
    return (str1.join(s))

def generator():
    bgs=file_list('BG_PAPER/')
    font_pack=file_list(config.font_path)
    #font_colour=[(0,0,0),(25,25,25),(65,65,65)]
    #font_sizes=range(15,116,10)
    #font_sizes=[35,55,75,95,115]   ###range(15,116,10)
    #symbols=list(string.printable[:94])
    #symbols.append(u"\u00A9")
    #symbols.append(u"\u2122")
    #symbols.append(" ")
    symbols=[]
    with open(config.gentxt, 'r') as f:
        for lines in f:
            if any(c.isalpha() for c in lines):
                if len(lines.split())>13:
                    text =  lines
                    text = text.split()
                    n = 13
                    symbl = [' '.join(text[i:i+n]) for i in range(0,len(text),n)]
                    for i in symbl:
                        symbols.append(i)
                else: symbols.append(listToString(lines.split()))

    for symbol in tqdm(symbols):
        try:
            if len(symbol.split())>=3 and langdetect.detect(symbol) != 'en':
                font_color=config.font_colour
                font_colour=random.choice(font_color)
                font_sizes=config.font_sizes
                col = random.choice(font_colour)
                font_size = random.choice(font_sizes)
                background = random.choice(bgs)
                font = random.choice(font_pack)
                yield background,font,symbol,font_size,col,font_colour
            #print("Percent Completed : ",((k+1)/len(font_pack))*100)  
        except langdetect.lang_detect_exception.LangDetectException:
            pass
