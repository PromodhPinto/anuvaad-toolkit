# SYNTHETIC DATA GENERATION

Synthetic data generation is the process of generating images and corresponding ground truths with different font family, font colour, font size, background color, space between words and many more.

## Prerequisites
- python 3.7
- ubuntu 16.04

You need to install some libraries. I have specified the names and versions of python libraries in requirements.txt
```bash
pip install -r requirements.txt
```

# Configuration

We have here config settings that may help generate synthetic data for each languages:

* lang_code : language code
* lang      : language
* num_lines : the number of lines to generate dataset from raw corpus
* bgs_path  : background images path
* real_imgs : real data path
* real_txt  : real data ground truth path
* font_ path: font files path
* noices    : noise filters to be applied
* font_colour: font color codes
* ...

# Directories

The folder structure consists of the following files/directories
* the `synthetic_data_generator` directory holds all services, each with their files
* the `BG_PAPER` directory holds useful background images, needed to genereate the synthetic images
* the `real-data` directory holds real world data that is added along with the synthetic data
* the `line_txt` directory holds list of files containing text corpus for each language
* the `font_files` directory holds list of directories containing fonts for each language
* the `output` directory holds the generated data

## APIs and Documentation
After successful installation of prerequisites, you will have to run run.py

```bash
python run.py
```
This service is used to generate synthetic images from a text corpus specific to each language. After initiating this service,
the images are being generated under the directory `output` and the specific language.

### Request Format
```txt
POST/Synthetic data generation
Accept list of files

Text corpus is added to the directory line_txt
	filename structure: outcorpus_<language code>.txt
Collected font files are added to this directory
	folder & filename structure: font_files/<language code>/filename.ttf
Background images are added to the directory BG_PAPER
	filename structure: <name>.jpg

```
### Response
```
POST/Synthetic data generation
Returns jpg files and corrsponding txt files which have ground truth
Returns json files containing the details for each image

```
#### Input & Output Structure
```

"inputFile": "input txt file",
"outputFile": "jpg files and corrsponding txt files which have ground truth and json files which have list of attributes mention below",
"outputLocale": "en",
"outputType": "jpg, txt and json"

```
##### Json Structure
```
* data-ocr.json

{[
{
    "classType": "class1",
    "backgroundColor": "white",
    "source": "real",
    "fontName": "timesroman",
    "fontType": "unicode",
    "fontVersion": "old",
    "groundTruth": "\u0905\u0932\u094d\u092a\u0915\u093e\u0932\u0940\u0928 \u0915\u092e\u0940\u0936\u0928",
    "imageFilename": "a527aa1a-6f8c-4217-892b-c7c311f0e987_class1_white_real_timesroman_unicode_old.png",
    "boundingBox": {
        "vertices": [
            {
                "x": 0,
                "y": 0
            },
            {
                "x": 331,
                "y": 0
            },
            {
                "x": 331,
                "y": 43
            },
            {
                "x": 0,
                "y": 43
            }
        ]
    }
},

{....},
{....}
        ]}
        
* params.json

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
                "name": "Naresh Kumar Saini",
                "aboutMe": "AI Engineer at Tarento Technologies"
            },
            {
                "name": "Promodh Pinto J",
                "aboutMe": "Associate Software Engineer at Tarento Technologies"
            }
        ]
    },
    "format": "png",
    "dpi": "72_dpi",
    "imageTextType": "computer-typed-text"
    }  

For more information about api documentation, please check @ ```https://github.com/project-anuvaad/anuvaad``

## License
[MIT](https://choosealicense.com/licenses/mit/)
