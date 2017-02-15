#!/bin/bash

# echo "Hello this is a script to take an ant video and turn it into a video displaying only the entrances to the nest"
# echo "Please enter the path of the file you would like to convert:"
# read path_to_vid
path_to_vid=$1
vidDir="Out-"
vidName=$(basename $path_to_vid) 
mkdir $vidDir$vidName
OutputPath=$(dirname "${path_to_vid}")"/"$vidDir$vidName

Out_I_A=$OutputPath"/Out_I-A.avi" 
Out_I_B=$OutputPath"/Out_I-B.avi" 
Out_II_A=$OutputPath"/Out_II-A.avi" 
Out_II_B=$OutputPath"/Out_II-B.avi" 
Out_III_A=$OutputPath"/Out_III-A.avi" 
Out_III_B=$OutputPath"/Out_III-B.avi" 

avconv -i $path_to_vid -vf crop=out_w=162:out_h=50:x=1197:y=311 $Out_I_A
avconv -i $path_to_vid -vf crop=out_w=162:out_h=50:x=1369:y=311 $Out_I_B
avconv -i $path_to_vid -vf crop=out_w=148:out_h=50:x=511:y=332 $Out_II_A
avconv -i $path_to_vid -vf crop=out_w=178:out_h=50:x=659:y=332 $Out_II_B
avconv -i $path_to_vid -vf crop=out_w=132:out_h=50:x=624:y=580 $Out_III_A
avconv -i $path_to_vid -vf crop=out_w=132:out_h=50:x=786:y=580 $Out_III_B
