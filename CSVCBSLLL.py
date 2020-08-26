import csv
import os

save = "/group/p00259/structural/"
basepath = "/group/p00259/structural/"

for root, dirs, files in os.walk(basepath):
  for f in files:
    if (f.endswith("_L.nii.gz.txt") or f.endswith("_R.nii.gz.txt"))  and len(dirs) == 0:
      print("f", f, "root", root, "dirs", dirs)
      file = open(os.path.join(basepath, root, f) , "r")
      content1 = file.read()
      print(content1)
      file.close()
      row = (str(f) + " " + content1).replace('\n', '').replace("  ", ' ').split()
      print(row)
      with open(save + 'LLLCBSvolumesFinal.csv', 'a') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerow(row)
        
