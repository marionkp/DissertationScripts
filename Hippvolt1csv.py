import csv

patients=[13258, 25568, 25655, 25669, 25680, 25713, 25746, 25768, 25866, 25907, 26027, 26117, 26184, 26221, 26386, 26457, 26567, 26712, 27295, 27841, 28502, 13500, 25569, 25656, 25670, 25681, 25714, 25747, 25769, 25883, 26003, 26038, 26144, 26185, 26284, 26410, 26458, 26578, 26899, 27352, 27920, 28553, 20169, 25611, 25657, 25671, 25682, 25726, 25748, 25832, 25884, 26024, 26050, 26154, 26194, 26297, 26411, 26459, 26579, 26900, 27353, 27921, 28677, 23008, 25653, 25666, 25678, 25684, 25728, 25749, 25833, 25885, 26025, 26097, 26155, 26208, 26298, 26428, 26460, 26619, 26984, 27462, 28424, 28764, 24838, 25654, 25667, 25679, 25712, 25733, 25767, 25834, 25906, 26026, 26098, 26158, 26220, 26358, 26452, 26464, 26690, 27040, 27840, 28499, 28813]

basepath = "/data/mkp42/Manual_Hipp_T1/MEMCLINIC/"

endpathL = "/hipp_manseg_l.txt"
endpathR = "/hipp_manseg_r.txt"


for patient in patients:
    f1 = open(basepath + str(patient) + endpathL , "r")
    content1 = f1.read()
    f1.close()
    f2 = open(basepath + str(patient) + endpathR , "r")
    content2 = f2.read()
    f2.close()
    row = (str(patient) + " " + content1 + " " + content2).replace('\n', '').replace("  ", ' ').split()
    print(row)
    with open(basepath + 'volumes.csv', 'a') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerow(row)
