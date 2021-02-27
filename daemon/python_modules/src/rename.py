import os
from tinytag import TinyTag
from videoprops import get_video_properties


def list_files(path):
    all_files = []
    for (repertoire, sous_repertoires, fichiers) in os.walk(path):
        for file in fichiers:
            all_files.append(file)

    return all_files


def get_quality(file):
    video = get_video_properties(file)

    if video['width'] >=3800 :
        video_quality = "4K"
    elif video['width'] >= 2000 and video['width'] < 3800:
        video_quality = "2K"
    elif video['width'] >= 1700 and video['width'] < 2000:
        video_quality = "FullHD"
    elif video['width'] >= 1000 and video['width'] < 1700:
        video_quality = "HD"
    elif video['width'] < 1000:
        video_quality = "SD"

    return video_quality


def find_file(filename, search_path):
    for root, dir, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    
    return None


def quality_in_name_file(file_name):
    split_name = file_name.split('[')

    if len(split_name) == 1:
        return False
    
    return True


def add_quality_in_all_file_name(path):
    all_files = list_files(path)

    for file in all_files:
        if not quality_in_name_file(file) and file != "ID.txt":
            add_quality_in_file_name(file, path)


def add_quality_in_file_name(file, path):
    full_path = find_file(file, path)
    quality = get_quality(full_path)

    split_name = os.path.splitext(full_path)
    file_path = split_name[0]
    file_extension = split_name[1]

    new_path = file_path + "[" + quality + "]" + file_extension

    print("Last path : " + full_path)
    print("New path : " + new_path)

    os.rename(full_path, new_path)
