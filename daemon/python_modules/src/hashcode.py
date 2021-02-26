import random
import string
import os
from tinytag import TinyTag
from checksumdir import dirhash
from hashlib import sha1

def get_file_hashcode(path):
    video = TinyTag.get(path)
    video = video.__dict__
    video.pop('_filehandler')
    video = str(video).encode('utf-8')
    hashcode = sha1(video)
    return hashcode.hexdigest()


def get_dir_hashcode(path):
    check_and_create_random_ID_file(path)
    ID_path = os.path.join(path, "ID.txt")
    opened_ID_file = open(ID_path, "r", encoding='utf-8')
    read_file = opened_ID_file.read()
    hashcode = sha1(str(read_file).encode('utf-8'))
    return hashcode.hexdigest()


def check_and_create_random_ID_file(path):
    file_path = os.path.join(path, 'ID.txt')
    if not os.path.isfile(file_path):
        f = open(file_path, 'w')
        file_content = get_random_alphanumeric_string(50)
        f.write(file_content)
        f.close()


def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str
