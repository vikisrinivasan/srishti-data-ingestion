import os
import glob
import shutil
def clear_dir(dir_path):
    try:
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
        os.makedirs(dir_path)
        return True
    except Exception as e:
        raise "Please Check the Directory"
