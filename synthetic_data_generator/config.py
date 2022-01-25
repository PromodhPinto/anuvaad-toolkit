import os
from os import listdir
from os.path import isfile, join
import re


####### MAKE_CORPUS
lang_code = "as"
# Language
lang = 'Assamese'
#LINE_SOURCES
inptxt=f"line_txt/{lang_code}/"

num_lines=6000 # To generate dataset        
out_txt_file=f"outcorpus_{lang_code}.txt"


########## DATA GENERATION
#PROCESS=58
#FILEPATH='/home/ubuntu/data-generator'
#OUTPATH='/home/ubuntu/data/ocr'
PROCESS=2
OUTPATH=f"output/{lang}/"
gentxt=f"line_txt/outcorpus_{lang_code}.txt"

# Backgournds
bgs_path = 'BG_PAPER/**'
real_imgs = f"real-data/{lang_code}/old/*.png"
curated = f"output/{lang}/{lang_code}-synt-data/*.png"
real_txt = f"real-data/{lang_code}/*.gt.txt"
font_path = f"font_files/{lang_code}/"



#FONT SIZES
font_sizes=[22, 23, 24, 25, 26, 27, 30, 36, 40, 45]
#Noices
noices = ['gauss','edge','poisson','median','none','non','non','non','non','non','non','non','non', 'no', 'edges', 'edges', 'edges', 'edges','contour','contour','smooth']
#FONT COLOUR
font_colour=[(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(25,25,25),(65,65,65),(0,0,0),(0,0,0),(0,0,0),(128,0,0),(0,0,128),(0,200,23),(255,0,0),(107, 17, 69),(11, 15, 6),(12, 12, 6),(33, 22, 35),(349, 33, 34),(37, 40, 21)]
# Backgrounds of class type 3
class3_bgs = ['old-brown-vintage-parchment-paper-texture',
          'paper-squares-background-hd',
          'paper-texture-document',
          'pexels-milo-textures-2850515',
          'pexels-pixabay-235985',
          'wolfgang-hasselmann-oKnBPj4xfiA-unsplash',
          'abstract-photocopy-texture-background-paper-95960065',
          'Natural-Paper-Background-Texture',
          'nordwood-themes-R53t-Tg6J4c-unsplash',
          'annie-spratt-BIn3m_DDSJE-unsplash',
          'gray-cardboard-paper-texture-hd',
          'dirty-photocopy-grey-paper-texture-background-dark-grunge-dirty-photocopy-grey-paper-texture-useful-as-background-129710148',]
# Noices of class type 3
class3_noices = ['gauss', 'median','smooth']
class1_noices = ['none', 'non', 'no', 'edges']
# Background color
bgs_color = ['pexels-milo-textures-2850515',
             'pexels-pixabay-235985',
             'photocopy-texture-background-close-up-90771302',
             'dirty-photocopy-grey-paper-texture-background-dark-grunge-dirty-photocopy-grey-paper-texture-useful-as-background-129710148',
             'wolfgang-hasselmann-oKnBPj4xfiA-unsplash',
             'simple-old-paper-3',
             'gray-cardboard-paper-texture-hd',
             'old-brown-vintage-parchment-paper-texture',
             'abstract-photocopy-texture-background-paper-95960065',
             'annie-spratt-BIn3m_DDSJE-unsplash',
             'paper-texture-document']
bgs_white = ['ricepaper2',
             'ricepaper20',
             'ricepaper21',
             'ricepaper22',
             'ricepaper23',
             'ricepaper24',
             'annie-spratt-BcGoZXjyPzA-unsplash',
             'annie-spratt-BcGoZXjyPzA-unsplash0',
             'annie-spratt-BcGoZXjyPzA-unsplash1',
             'annie-spratt-BcGoZXjyPzA-unsplash2',
             'marjanblan-_kUxT8WkoeY-unsplash',
             'marjanblan-_kUxT8WkoeY-unsplash0',
             'marjanblan-_kUxT8WkoeY-unsplash1',
             'marjanblan-_kUxT8WkoeY-unsplash2',
             'marjanblan-_kUxT8WkoeY-unsplash3',
             'paper',
             'paper0',
             'paper1',
             'paper2',
             'aPLQ4',
             'aPLQ40',
             'aPLQ41'
             ]
bgs_class3 = ['old-brown-vintage-parchment-paper-texture',
             'abstract-photocopy-texture-background-paper-95960065',
             'dirty-photocopy-grey-paper-texture-background-dark-grunge-dirty-photocopy-grey-paper-texture-useful-as-background-129710148',
             'pexels-milo-textures-2850515',
             'pexels-pixabay-235985',
             'wolfgang-hasselmann-oKnBPj4xfiA-unsplash']
# Parameters Json
params = {
    "datasetType": "ocr-corpus",
    "languages": {
        "sourceLanguage": lang_code
    },
    "collectionSource": [
        "All domain"
    ],
    "domain": [
        "general"
    ],
    "license": "cc-by-4.0",
    "submitter": {
        "name": "Project Anuvaad",
        "aboutMe": "Open source project run by ekStep foundation.",
        "team": [
            {
                "name": "Promodh Pinto J",
                "aboutMe": "Associate Software Engineer from the team OCR at Tarento Technologies"
            }
        ]
    },
    "format": "png",
    "dpi": "72_dpi",
    "imageTextType": "computer-typed-text"
    }  

