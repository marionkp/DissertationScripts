#!/bin/bash
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mkp42@medschl.cam.ac.uk
#SBATCH --time=120:00:00

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


time=$(date +%s) 

for f in $(find /data/mkp42/ADNI_data/ADNI -name "*.nii" | awk "FNR >= 1231  && FNR <= 1260");
do 
  #hippR=${f%.*}_R.nii.gz
  hippL=${f%.*}_L.nii.gz
  #echo "${bindir}/LLL $bindir $temp_dir $atlasdirR $f $hippR 1 20"
  #${bindir}/LLL $bindir $temp_dir $atlasdirR $f $hippR 1 20 
  echo "${bindir}/LLL $bindir $temp_dir $atlasdirL $f $hippL 1 20"
  ${bindir}/LLL $bindir $temp_dir $atlasdirL $f $hippL 1 20
done
