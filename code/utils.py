#!/usr/bin/env python
# coding: utf-8

"""
@title: Utility functions for data processing and analysis
@author: Jaren Haber, PhD
@date: September 16, 2023

"""


###############################################
# Initialize                 
###############################################

# Import packages
import requests
import shutil
import regex # supports recursion and unicode handling
from unicodedata import normalize # to clean up unicode
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
    
    zipped = requests.get(URL)
    zipped_bytes = zipped.content
    
    fname = URL.split('/')[-1] # Get name for extraction folder using URL
    outfile = join(fpath, fname)
    with open(outfile, "wb") as f:
        f.write(zipped_bytes)

    shutil.unpack_archive(outfile, extract_dir = fpath, format = 'zip')
    
    return


def clean_unicode(text, replace_spaces=True):
    """
    Cleans unicode from input text and standardizes spacing.
    
    Args:
        text (str) -- any raw text
        replace_tabs (bin) -- whether to replace consecutive spaces or tabs with single space
    Returns:
        text with unicode converted to readable format
        
    """
    
    if replace_spaces:
        # Replace all consecutive spaces (including in unicode), tabs, or "|"s with a single space
        text_cleaned = regex.sub(r"[ \t\h\|]+", " ", text)
    
    # Simplify unicode characters by normalizing
    text_cleaned = normalize('NFKC', text_cleaned)
    
    # Remove ascii (such as "\u00")
    text_cleaned = text_cleaned.encode('ascii', 'ignore').decode('ascii')
    
    return text_cleaned