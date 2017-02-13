# AntVideoProcessing
Process video clips into format for optimal processing

Path to do this:
use avconv to cut clips and figure out how to capture the correct areas then write clips and write script for this then figure out how to run a batch process on kunth 

Bellow are the cordinates and output values for each video. These were found by taking a screen capture form Avconv and then passing that screen shoot to python where scikit learn and matplot lib were used to convert the picture (.jpg) to a plot where the x,y pixle cordinates were vieable at any given point. Next I located the cordinates for the right most nest entance. Using the cordinates and some basic graph theory I then derived the arguments for avconv to process the video to extract the 6 nest entances.  

Cordinates:
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
Commands

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
