import os
import shutil

root_curdir = os.path.curdir

def move_files_to_curdir(curdir):
    filenames= os.listdir (curdir)
    for filename in filenames:
        full = os.path.join(os.path.abspath(curdir), filename)
        if os.path.isdir(full):
            print('directory: ' + full)
            move_files_to_curdir(full)
            print('remove directory: ' + full)
            os.rmdir(full)
        else:
            destination_dir = os.path.join(root_curdir, filename)
            print('move file: from {} to {}'.format(full, destination_dir))
            shutil.move(full, destination_dir)

if __name__ == '__main__':
    try:
        print('start to move files')
        move_files_to_curdir(root_curdir)
        print('stop to move files')
    except Exception as ex:
        print(ex)