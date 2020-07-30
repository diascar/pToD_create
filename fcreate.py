import os
import sys
import re
import shutil

base_dir = os.getcwd()
fext = sys.argv[1]

try:
    fpatrn = sys.argv[2]
except:
    fpatrn = ' '


pattern = re.compile(f'\.{fext}$')
flist = os.listdir(base_dir)

for f in flist:
    if re.findall(pattern, f) and fpatrn not in f:
        tmp_name = os.path.splitext(f)[0]
        print(f'creating directory:{tmp_name}')
        try:
            os.mkdir(tmp_name)
            shutil.move(f, os.path.join(base_dir, tmp_name))

        except FileExistsError:
            print(f'Directory {tmp_name} already exists!')
        except:
            print(f'something went wrong when creating directory: {tmp_name}')
       


