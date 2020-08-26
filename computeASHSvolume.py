import os
import subprocess

print(os.getcwd())

for root, dirs, files in os.walk(os.getcwd()):
  patient = root.split("/")[-1]
  if patient.isdigit():
    args = ["$ASHS_ROOT/bin/ashs_main.sh"]
    args += ["-I", patient, "-a", "/home/mkp42/ashsT1_atlas_upennpmc_07202018"]
    matching1 = [s for s in files if "mprage" in s and "sub-" in s and "brain.nii" in s] 
    print("matching1", matching1)
    matching2 = [s for s in files if "hippocampus" in s and "sub-" in s] 
    print("matching2", matching2)
    args += ["-g", "/scratch/hphi/mkp42/Hippocampus/" + patient + "/" + matching1[0], "-f", "/scratch/hphi/mkp42/Hippocampus/" + patient + "/" + matching2[0]]
    
    args += ["-w", "/scratch/hphi/mkp42/Hippocampus/" + patient + "/ASHS_" + patient + "T1_Skull"]
    subprocess.call(["mkdir", "-p", "/scratch/hphi/mkp42/Hippocampus/" + patient + "/ASHS_" + patient + "T1_Skull"])
    print("args", args)
    print("patient", patient)
    subprocess.call(args, shell=True) #, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    break

#$ASHS_ROOT/bin/ashs_main.sh -I 26410 -a /home/mkp42/ashsT1_atlas_upennpmc_07202018 -g /scratch/hphi/mkp42/Hippocampus/26410/sub-26410_ses-20180508_acq-repmprageipat2str_run-01_T1w.nii.gz -f /scratch/hphi/mkp42/Hippocampus/26410/sub-26410_ses-20180508_acq-repcoronalt2hippocampus_run-01_T2w.nii.gz -w /scratch/hphi/mkp42/Hippocampus/26410

 

