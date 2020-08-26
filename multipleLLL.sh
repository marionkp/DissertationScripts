#!/bin/bash
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mkp42@medschl.cam.ac.uk
#SBATCH --time=24:00:00

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

patients=(13500  25569  25656  25670  25681  25714  25747  25769  25883  26003  26038  26144  26185  26284  26410  26458  26578  26899  27352  27920  28553 20169  25611)

time=$(date +%s) 

for patient in "${patients[@]}"
do 
  echo "$patient"
 
  img=/group/p00412/hippocampus/$patient/MPRAGE.nii.gz
  hippR=/data/mkp42/LLL_Results/$patient/LLL_R_MPRAGE.nii.gz
  hippL=/data/mkp42/LLL_Results/$patient/LLL_L_MPRAGE.nii.gz 
  echo "${bindir}/LLL $bindir $temp_dir $atlasdirR $img $hipp 1 20"
  `mkdir /data/mkp42/LLL_Results/$patient/`  
  ${bindir}/LLL $bindir $temp_dir $atlasdirR $img $hippR 1 20 >> /scratch/hphi/mkp42/Hippocampus/LLLlogs/logs${time}.txt
  echo "${bindir}/LLL $bindir $temp_dir $atlasdirL $img $hipp 1 20"
  ${bindir}/LLL $bindir $temp_dir $atlasdirL $img $hippL 1 20 >> /scratch/hphi/mkp42/Hippocampus/LLLlogs/logs${time}.txt
done
