import os
import sys
import shutil
import datetime
import glob

def sync_folder(source_folder, destination_folder, full=False):
    print('source folder: ' + source_folder)
    print('destination folder: ' + destination_folder)
    filenames= os.listdir(source_folder)
    print('source folder file count: ' + str(len(filenames)))
    file_type = r'\*.*'
    files = glob.glob(destination_folder + file_type)
    max_file = max(files, key=os.path.getmtime)
    print(max_file)
    max_file_timestamp = os.path.getmtime(max_file)
    max_file_date_time = datetime.datetime.fromtimestamp(max_file_timestamp)
    print(max_file_date_time)
    copied_file_count = 0
    destination_filenames = os.listdir(destination_folder)
    for filename in filenames:
        full_path_source  = os.path.join(os.path.abspath(source_folder), filename)
        full_path_destination  = os.path.join(os.path.abspath(destination_folder), filename)
        if full :
            find_filename = [file for file in destination_filenames if filename == file]
            if len(find_filename) > 0 :
                modified_time_source = os.path.getmtime(full_path_source)
                modified_time_destination = os.path.getmtime(full_path_destination)
                if modified_time_source > modified_time_destination :
                    copied_file_count += 1
                    copy_file(copied_file_count, full_path_source, full_path_destination)
                else :
                    print('same file exsited : ' + filename)
            else :
                copied_file_count += 1
                copy_file(copied_file_count, full_path_source, full_path_destination)
        else :
            modified_time_source = os.path.getmtime(full_path_source)
            if modified_time_source >= max_file_timestamp :
                copied_file_count += 1
                copy_file(copied_file_count, full_path_source, full_path_destination)
            else :
                print('no need to copy: ' + filename)

def copy_file(copied_file_count, full_path_source, full_path_destination):
    shutil.copy(full_path_source, full_path_destination)
    print('copied: ' + full_path_source)
    print('copied count: ' + str(copied_file_count))


# python sync-folder.py D:\folder1 b D:\folder2 true|false
if __name__ == '__main__':
    try:
        print('start to sync folder')
        source_folder = sys.argv[1]
        destination_folder = sys.argv[2]
        full = False
        if len(sys.argv) > 3 :
            full = True if sys.argv[3] == 'true' else False
        sync_folder(source_folder, destination_folder, full)
        print('stop to sync folder')
    except Exception as ex:
        print(ex)