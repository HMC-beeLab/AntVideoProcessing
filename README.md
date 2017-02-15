# AntVideoProcessing
Process video clips into format for optimal processing

Path to do this:
use avconv to cut clips and figure out how to capture the correct areas then write clips and write script for this then figure out how to run a batch process on server EC2, knuth, ect.

Bellow are the coordinates and output values for each video. These were found by taking a screen capture form Avconv and then passing that screen shoot to python where scikit learn and matplot lib were used to convert the picture (.jpg) to a plot where the x,y pixel coordinates were viewable at any given point. Next I located the coordinates for the right most nest entrance. Using the coordinates and some basic graph theory I then derived the arguments for avconv to process the video to extract the 6 nest entrances. 

![Ant ecosystem](/diagram00.jpg) 



### Coordinates:
```
	I:
		A: 
			out_w:162 
			out_h:50
			x:1197
			y:311
		B:
			out_w:162 
			out_h:50
			x:1369
			y:311
	II:
		A: 
			out_w:148 
			out_h:50
			x:511
			y:332
		B:
			out_w:178 
			out_h:50
			x:659
			y:332

	III:
		A: 
			out_w:132 
			out_h:50
			x:624
			y:580
		B:
			out_w:132 
			out_h:50
			x:786
			y:580

	IV:
		NA
```
### Commands:

```
I:
	avconv -i $path_to_vid -vf crop=out_w=162:out_h=50:x=1197:y=311 Out_I-A.avi
	avconv -i $path_to_vid -vf crop=out_w=162:out_h=50:x=1369:y=311 Out_I-B.avi

II:
	avconv -i $path_to_vid -vf crop=out_w=148:out_h=50:x=511:y=332 Out_II-A.avi
	avconv -i $path_to_vid -vf crop=out_w=178:out_h=50:x=659:y=332 Out_II-B.avi

III:
	avconv -i $path_to_vid -vf crop=out_w=132:out_h=50:x=624:y=580 Out_III-A.avi
	avconv -i $path_to_vid -vf crop=out_w=132:out_h=50:x=786:y=580 Out_III-B.avi

IV:
	NA
```

### Use:

This script is designed to take in a path to a file. It will then create a directory Out-(filename) in this directory there will be 6 .avi video files each of these will contain a video of the nest entrance for there respective entrances. The naming convention for these files is Out_(region)-(Nest) Where Region refers to the quadrant the nest is located and Nest references to the A or B marker assigned in the above diagram. 

## Example:
Do the following one time to give script permission to run.
```chmod -x getNestEntrances.sh```

Now we can execute the script now execute it:
```sh getNestEntrances.sh /Users/alasdairjohnson/code/AntVideoProcessing/shorttest.avi```

we can see above there are three components for execution we will look at them in order:
	sh - this reference to the fact we are running a shell script
	getNestEntrances.sh - this is the script to be executed
	/Users/alasdairjohnson/code/AntVideoProcessing/shorttest.avi - is the path to the desired file to convert 










