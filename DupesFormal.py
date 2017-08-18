"""Duplicate image removal."""

import numpy as np
import numpy.linalg as alg
import scipy.misc as sp
import os

def image_process(path, image_name):
    formats = ['JPEG', 'JPG', 'PNG', 'GIF', 'BMP']
    file_type = image_name.split('.')
    return None if file_type[-1].upper() not in formats else sp.imread(path + '\\' + image_name, flatten = True)

def image_list(path, files):
    img_list = []

    for item in files:
        img_file = image_process(path, item)
        img_list.append(img_file)

    return img_list

def dupes():

    final_list = []

    #Path processing start
    try:
        path1 = input("Initial Path1 --> ")
        path2 = input("Check Path2 --> ")

        str_path1 = str(path1)
        str_path2 = str(path2)
    except:
        print('Faulty paths.')

    files1 = os.listdir(str_path1)
    files2 = os.listdir(str_path2)

    first_list = image_list(path1, files1)
    second_list = image_list(path2, files2)
    #Path processing end

    #Identifying 0s for uniques and 1s for duplicates
    for i in range(len(files1)):
        if first_list[i] is None:
            final_list.append(0)
        else:
            for k in range(len(files2)):
                if second_list[k] is None:
                    continue
                elif first_list[i].sum() == second_list[k].sum():
                    final_list.append(1)
                    break
                elif k == len(files2) - 1:
                    final_list.append(0)
    #Identification end

    if not final_list:
        print("No duplicates!")
        return

    #Image removal
    for i in range(len(files1)):
        if final_list[i] == 1:
            os.remove(str_path1 + '\\' + files1[i])
    #Image removal end

    print("Duplicates Removed!")

#dupes()
