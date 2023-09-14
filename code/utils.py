#!/usr/bin/env python
# coding: utf-8

"""
@title: 
@author: Jaren Haber, PhD
@description: 

------------------------------------------------------------------------------------------------

@usage: python3 ...

@args:
-  --> path to folder containing raw text files (with .txt file ext)
-  --> path to folder containing article list
-  --> path to folder to save preprocessed text data

------------------------------------------------------------------------------------------------

@inputs:
- X (from Y)
- X (from Y)

@outputs:
- something (such and such format)
- something (such and such format)

"""


###############################################
# Initialize                 
###############################################

# Import packages
import requests
import shutil
from os.path import join


###############################################
# Define function(s)                 
###############################################

def get_unzip(URL, fpath):
    """
    Downloads zip-formatted file from specified URL and extracts it.
    
    Args:
        URL (str) -- points to zipped file
        fpath (str) -- path to folder in which to save output
    Returns:
        extracted zip file in main directory (one level up)
        (returns nothing directly)
        
    """
    
    zip_html = requests.get(URL)
    zip_bytes = zip_html.content
    
    fname = URL.split('/')[-1] # Get name for extraction folder using URL
    with open(join(fpath, fname), "wb") as outfile:
        outfile.write(zip_bytes)

    shutil.unpack_archive(fname, extract_dir=fpath, format = 'zip')
    
    return
