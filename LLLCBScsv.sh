


patients=(sub-16316 sub-18474 sub-18907 sub-19735 sub-21621 sub-22632 sub-23377 sub-24523 sub-26471 sub-27045 sub-28141 sub-29290 sub-16317 sub-18802 sub-19056 sub-20110 sub-21680 sub-22645 sub-23386 sub-25198 sub-26562 sub-27186 sub-28294 sub-29456 sub-10977 sub-16671 sub-18804 sub-19211 sub-20869 sub-21833 sub-22728 sub-23526 sub-25876 sub-26633 sub-27291 sub-28595 sub-29927 sub-14268 sub-17726 sub-18829 sub-19389 sub-20926 sub-21980 sub-22730 sub-23674 sub-25955 sub-26678 sub-27308 sub-28822 sub-30167 sub-16313 sub-17875 sub-18830 sub-19454 sub-21020 sub-21993 sub-22834 sub-23773 sub-26037 sub-26686 sub-27398 sub-28881 sub-16314 sub-18340 sub-18831 sub-19533 sub-21123 sub-22553 sub-23004 sub-24033 sub-26353 sub-27001 sub-27399 sub-29121 sub-16315 sub-18451 sub-18902 sub-19663 sub-21395 sub-22631 sub-23315 sub-24156 sub-26384 sub-27012 sub-27526 sub-29207)


for patient in "${patients[@]}"
do 
  echo "$patient"
  for f in `find /group/p00259/structural/$patient -name "*_R.nii.gz"`
  do 
    touch ${f}.txt
    fslstats $f -V >> $f.txt
  done

  for f in `find /group/p00259/structural/$patient -name "*_L.nii.gz"`
  do
    touch ${f}.txt
    fslstats $f -V >> $f.txt
  done
  
 
  
 
done
