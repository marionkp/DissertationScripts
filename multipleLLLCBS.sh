#!/bin/bash
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mkp42@medschl.cam.ac.uk
#SBATCH --time=20:00:00

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
temp_dir=/home/mkp42/Documents/LLL_package/example/temp

#sub-23004 sub-29207 sub-23315 sub-19056 sub-26037 sub-26353 sub-25876 sub-27291 sub-16313
#sub-16314 sub-27186 sub-28881 sub-19454 sub-29456 sub-18340 sub-16315 sub-19735 sub-22631
#sub-27526 sub-27399 sub-26562 sub-21123 sub-29290 sub-21833 sub-28141 sub-26633 sub-22553
#sub-27045 sub-26686 sub-21395 sub-20869 sub-28595 sub-23377 sub-30167 sub-18829 sub-23526
#sub-22645 sub-24156 sub-18831 sub-22834 sub-20926 sub-26471 sub-18830 sub-25198 sub-19389
#sub-21993 sub-18451 sub-22632 sub-21621 sub-19663 sub-24033 sub-27012 sub-23773
#sub-16316 sub-26678 sub-25955 sub-27308

patients=(sub-28294 sub-20110 sub-18804 sub-29121 sub-19211 sub-23674 sub-17726 sub-22730 sub-17875 sub-21680)

for patient in "${patients[@]}"
do 
  echo "$patient" 

  for f in $(find /group/p00259/structural/${patient} -name "*.nii.gz");
  do 
    fnii=${f%.*} 
    hippL=${fnii%.*}_L.nii.gz
    hippR=${fnii%.*}_R.nii.gz
    echo "${bindir}/LLL $bindir $temp_dir $atlasdirR $f $hippR 1 20"
    ${bindir}/LLL $bindir $temp_dir $atlasdirR $f $hippR 1 20 
    echo "${bindir}/LLL $bindir $temp_dir $atlasdirL $f $hippL 1 20"
    ${bindir}/LLL $bindir $temp_dir $atlasdirL $f $hippL 1 20
  done
done

