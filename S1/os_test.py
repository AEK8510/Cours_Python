import sys
import os


print(os.getcwd())
print(os.listdir())
if os.path.exists("toto.pdb"):
    print("The file is present.")
else:
    sys.exit("The file is absent.")