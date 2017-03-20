#!/bin/bash

# echo "Hello this is a script to take an ant video and turn it into a video displaying only the entrances to the nest"
# echo "Please enter the path of the file you would like to convert:"
# read path_to_vid
echo $1
echo "$(< $1)"
# echo "read"

# while IFS=',' read col1 col2
# do
#     echo "I got:$col1|$col2"
# done < $1

variable="$(< $1)"
	for i in $(echo $variable | sed "s/,/ /g")
	do
	    # call your procedure/other scripts here below
        arr=(${line//,/ })
        echo $arr[0]
	    echo "$i"
	done

# while IFS= read -r line;do
#     fields=($(printf "%s" "$line"|cut -d',' --output-delimiter=' ' -f1-))
#     command "${fields[1]}" -x "${fields[2]}"
# done < $1
# while IFS="," read f1 f2 f3 f4 f5 f6 f7 f8 f9 f10 f11 f12 f13
# do
# 	echo "$f1" :
#     echo "$f2" :
#     echo "$f3" :
#     echo "$f4" :
#     echo "$f5" :
#     echo "$f6" :
#     echo "$f7" :
#     echo "$f8" :
#     echo "$f9" :
#     echo "$f10" :
#     echo "$f11" :
#     echo "$f12" :
#     echo "$f13" :
# done < "$1"





# path_to_vid=$1
# vidDir="Out-"
# vidName=$(basename $path_to_vid) 
# mkdir $vidDir$vidName
# OutputPath=$(dirname "${path_to_vid}")"/"$vidDir$vidName

# Out_I_A=$OutputPath"/Out_I-A.avi" 
# Out_I_B=$OutputPath"/Out_I-B.avi" 
# Out_II_A=$OutputPath"/Out_II-A.avi" 
# Out_II_B=$OutputPath"/Out_II-B.avi" 
# Out_III_A=$OutputPath"/Out_III-A.avi" 
# Out_III_B=$OutputPath"/Out_III-B.avi" 

# avconv -i $path_to_vid -vf crop=out_w=162:out_h=50:x=1197:y=311 $Out_I_A
# avconv -i $path_to_vid -vf crop=out_w=162:out_h=50:x=1369:y=311 $Out_I_B
# avconv -i $path_to_vid -vf crop=out_w=148:out_h=50:x=511:y=332 $Out_II_A
# avconv -i $path_to_vid -vf crop=out_w=178:out_h=50:x=659:y=332 $Out_II_B
# avconv -i $path_to_vid -vf crop=out_w=132:out_h=50:x=624:y=580 $Out_III_A
# avconv -i $path_to_vid -vf crop=out_w=132:out_h=50:x=786:y=580 $Out_III_B
