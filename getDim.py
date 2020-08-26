import nibabel as nib

img = nib.load('/scratch/hphi/mkp42/Hippocampus/25681/sub-25681_ses-20170324_acq-repcoronalt2hippocampus_run-01_T2w.nii.gz')

print(img.shape)

volume= img.get_fdata()

print(volume.shape)

