#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# follow instructions in this page to prepare darknet environment
# https://towardsdatascience.com/custom-object-detection-using-darknet-9779170faca2

import os
import shutil

def copy_labled_image(file_name, trainset_dir, images_dir, labels_dir):
    image_name = file_name.replace('.txt', '.png')
    image_path = os.path.join(trainset_dir, image_name)
    label_path = os.path.join(trainset_dir, file_name)
    shutil.copyfile(image_path, os.path.join(images_dir, image_name))
    print("Copied " + image_path)
    shutil.copyfile(label_path, os.path.join(labels_dir, file_name))
    print("Copied " + label_path)
    return image_name

stage_dir = '/mnt/c/cygwin64/home/Edward/.virtualenvs/github/darknet'
images_dir = os.path.join(stage_dir, 'data/baa/images/')
labels_dir = os.path.join(stage_dir, 'data/baa/labels/')
train_txt_path = os.path.join(stage_dir, 'data/baa/train.txt')
val_txt_path = os.path.join(stage_dir, 'data/baa/val.txt')

# get a list of all yolo label txt files
#archive_base_dir = '/mnt/c/cygwin64/home/Edward/.virtualenvs/hualiang/bone_age_algorithm/Sdk/archive'
#archive_base_dir = '/mnt/hualiang_dev_shared/darknet/archive'
#trainset_dir = os.path.join(archive_base_dir, 'boneage-training-dataset/boneage-training-dataset')

trainset_dir = '/mnt/c/cygwin64/home/Edward/.virtualenvs/github/rsna_images'

images_relpath_list = []

os.mkdir(images_dir)
os.mkdir(labels_dir)

for filename in os.listdir(trainset_dir):
    f = os.path.join(trainset_dir, filename)
    if os.path.isfile(f) and filename.endswith('.txt'):
        if filename == 'classes.txt':
            shutil.copyfile(f, os.path.join(labels_dir, filename))
            print("Copied classes.txt")
        else:
            image_name = copy_labled_image(filename, trainset_dir, images_dir, labels_dir)
            images_relpath_list.append('data/baa/images/' + image_name)

print(images_relpath_list)

with open(train_txt_path, 'w') as f:
    for i in range(len(images_relpath_list) - 1):
        f.write("%s\n" % images_relpath_list[i])
print("Updated " + train_txt_path)

with open(val_txt_path, 'w') as f:
    for i in range(len(images_relpath_list) - 1, len(images_relpath_list)):
        f.write("%s\n" % images_relpath_list[i])
print("Updated " + val_txt_path)
