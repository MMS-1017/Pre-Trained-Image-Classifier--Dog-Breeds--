#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Mohamed Mohsen
# DATE CREATED:  11/28/2022                     
# REVISED DATE: 

# PURPOSE: Create the function get_pet_labels that creates the pet labels from the image's filename. This function inputs: 
# - The Image Folder as image_dir within get_pet_labels function and as in_arg.dir for the function call within the main function. 

# This function creates and returns the results dictionary as results_dic within get_pet_labels function and as results within main.

# The results_dic dictionary has a 'key' that's the image filename and a 'value' that's a list. This list will contain the following item at index 0 : pet image label (string).

# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    in_files = listdir(image_dir)
    results_dic = dict()
    
    for idx in range(0, len(in_files), 1):
        if in_files[idx][0] != ".":
            low_pet_image = in_files[idx].lower()
            word_list_pet_image = low_pet_image.split("_")
            pet_name = ""
            
# Loops to check if word in pet name is only alphabetic characters, if true append word to pet_name separated by trailing space: 
            
            for word in word_list_pet_image:
                if word.isalpha():
                    pet_name += word + " "
# Strip off starting/trailing whitespace characters:

            pet_name = pet_name.strip()
    
# Adds new key-value pairs to dictionary ONLY when key doesn't already exist. This dictionary's value is a List that contains only one item - the pet image label:

            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] =  [pet_name]
            else:
                print("** Warning: Duplicate files exist in directory:", in_files[idx])
 
    return results_dic