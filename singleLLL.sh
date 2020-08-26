
bindir=/home/mkp42/Documents/LLL_package/LLL_bin       
PATH=${bindir}:$PATH
export PATH


MCRROOT=/scratch/hphi/mkp42/MATLAB_2014b   

LD_LIBRARY_PATH=.:/home/mkp42/Documents/MATLAB_Runtime/v84/runtime/glnxa64:${MCRROOT}/runtime/glnxa64:/home/mkp42/Documents/MATLAB_Runtime/v84/bin/glnxa64:/applications/matlab/matlab2013a/bin/glnxa64:/applications/matlab/matlab2013a/runtime/glnxa64:/home/mkp42/Documents/LLL_package/LLL_bin/added_modified_files
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${MCRROOT}/bin/glnxa64:${bindir}
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${MCRROOT}/sys/os/glnxa64
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${MCRROOT}/sys/opengl/lib/glnxa64



export LD_LIBRARY_PATH

atlasdirR=${bindir}/3T_R 
atlasdirL=${bindir}/3T_L 


####################################################################################################
temp_dir=/home/mkp42/Documents/LLiL_package/example/temp  
img=/group/p00412/hippocampus/13258/MPRAGE.nii.gz
hippR=/data/mkp42/LLL_Results/13258/LLL_R_sub-13258_ses-20181120_acq-mprageipat2str_run-01_T1w.nii.gz #replace it with your output file names
hippL=/data/mkp42/LLL_Results/13258/LLL_L_sub-13258_ses-20181120_acq-mprageipat2str_run-01_T1w.nii.gz 

#### run the segmentation and you will obtain a segmentation resutl similar to test_img_hippo_l.nii.gz
#### you should replace "3" with 20 for better segmentation performance

echo "${bindir}/LLL $bindir $temp_dir $atlasdirR $img $hipp 1 20"
${bindir}/LLL $bindir $temp_dir $atlasdirR $img $hippR 1 20 > /dev/null

echo "${bindir}/LLL $bindir $temp_dir $atlasdirL $img $hipp 1 20"
${bindir}/LLL $bindir $temp_dir $atlasdirL $img $hippL 1 20 > dev/null
