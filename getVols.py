from os import path
from glob import glob
import csv
from string import split

volfile = "raw_volumes.txt"

sides = ["left", "right"]
subjlist = [ v for v in glob("*") if path.isdir(v) if not v == "test" ]

# open output file
f = open("volumes.csv", "w")

headers = ["wbic", "manual_l", "manual_r", "ashs_l", "ashs_r"]

writer = csv.DictWriter(f, fieldnames = headers, delimiter = "\t")
writer.writeheader()

for subj in subjlist:
    # manual left
    try:
        ml = open(path.join(subj, "hipp_manseg_l.txt"))
        ml_vol_left = split(ml.readlines()[0].rstrip("\n"), " ")[1]
    except:
        ml_vol_left = "NA"

    # manual right
    try:
        mr = open(path.join(subj, "hipp_manseg_r.txt"))
        mr_vol_right = split(mr.readlines()[0].rstrip("\n"), " ")[1]
    except:
        mr_vol_right = "NA"

    # ashs left
    if path.exists(path.join(subj, "final", "_".join([subj, "left", volfile]))):
        try:
            mr = open(path.join(subj, "final", "_".join([subj, "left", volfile])))
            lines = mr.readlines()
            vol_ant = split(lines[0].rstrip("\n"), " ")[-1]
            vol_post = split(lines[0].rstrip("\n"), " ")[-1]
            vol_total_left = str(float(vol_ant) + float(vol_post))
        except:
            vol_total_left = "NA"
    else:
        vol_total_left = "NA"


    # ashs right
    if path.exists(path.join(subj, "final", "_".join([subj, "right", volfile]))):
        try:
            ml = open(path.join(subj, "final", "_".join([subj, "right", volfile])))
            lines = ml.readlines()
            vol_ant = split(lines[0].rstrip("\n"), " ")[-1]
            vol_post = split(lines[0].rstrip("\n"), " ")[-1]
            vol_total_right = str(float(vol_ant) + float(vol_post))
            print(' '.join([str(vol_ant), str(vol_post), vol_total_right]))
        except:
            vol_total_right = "NA"
    else:
        vol_total_right = "NA"

    outdict = {"wbic" : subj,
               "manual_l" : ml_vol_left,
               "manual_r" : mr_vol_right,
               "ashs_l" : vol_total_left,
               "ashs_r" : vol_total_right}

    writer.writerow(outdict)

f.close()
