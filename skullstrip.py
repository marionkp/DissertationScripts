import os
from subprocess import call
for subdir, dirs, files in os.walk("/lustre/scratch/wbic-beta/mkp42/Hippocampus"):
	for file in files:
		if file.endswith("nii.gz") and "mprage" in file and "sub-" in file:
			print(file)
			filepath= subdir + os.sep + file
			saved_name = filepath[:-len(".nii.gz")]
			#/applications/fsl/fsl-5.0.10/bin/bet /lustre/scratch/wbic-beta/mkp42/Hippocampus/25906/sub-25906_ses-20170622_acq-mprageipat2str_run-02_T1w /lustre/scratch/wbic-beta/mkp42/Hippocampus/25906/sub-25906_ses-20170622_acq-mprageipat2str_run-02_T1w_brain  -f 0.5 -g 0
			args = ["/applications/fsl/fsl-5.0.10/bin/bet", saved_name, saved_name + "_brain", "-f", "0.45", "-R", "-g", "-0.1"]
      			print(args)
			call(args)

