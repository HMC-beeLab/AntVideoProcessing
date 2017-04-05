# This will use what we learned for writing in shell to reproduce the same code and then build up a code base to ultimatly batch process vids
import numpy as np
import subprocess, shutil, os
class DivideVid():

    def __init__(self, filePath, row=1, width=300, height=50):
        """
        Will read in line of CSV file
        :param filePath: absolute path to csv file
        :param row: the row of csv to read in
        """
        self.headers = np.genfromtxt(filePath,dtype='str', delimiter=',', usecols=range(1,13))[0][::2]
        self.inputPath = np.loadtxt(filePath,dtype='str', delimiter=',', skiprows=row, usecols=range(1))
        self.data = np.loadtxt(filePath ,dtype=int, delimiter=',', skiprows=row, usecols=range(1, 13))
        self.width =  width
        self.height = height
        self.cmd = {'vidProcessor':'avconv',#vid converter were using
                     'parama' :'-i',#paramas
                     'inputPath' : None,#input path for comand
                     'args' : '-vf',#what command are we going to run
                     'crop' : 'crop=out_w=162:out_h=50:x=1197:y=311',#place holder for crop command
                     'outPath' : None}#outupt file path

    def cropVidIndividual(self):
        """

        :return: will create 6 vids with naming schema out-FilePath
        """


        outPath =  "out-" + self.inputPath



    def cropVidDirectory(self):
        """
        This first for loop controls iterating over the rows of the csv file while
        the second controls operating on all files in the given dir
        the use case being I have an experiment that uses spesific paramas run a bach on them and then
        :return: will create 6 vids for every vid in dir
        """

        for index in range(len(self.inputPath)): # iterate throught each of the paths in the csv
            row =  self.inputPath[index]
            data = self.data[index]

            #get path of file
            cleanPath = str(row)[2:-1] # this is required becuse of the fact that we get a byte string, Weird
            #create output folder
            try:
                os.mkdir(cleanPath + '/out') #make out put dir
            except:
                print('dir Already exsists')
            print(len(self.inputPath))
            #get files in directory
            files_in_dir = os.listdir(cleanPath) #get paths to all files in dir
            files_in_dir.pop(0) #remove first elment which is dir name out

            #run avconv on all files in dir
            for vidFile in files_in_dir:#itterate over each file
                zones = [1,2,3,4,5,6]
                for zone in zones:
                    # print(data)
                    self.addCropingArgs(zone, data) # will set the area to be croped


                    outname = "out_"+ self.headers[zone-1][:-2]+ "_" + os.path.basename(vidFile) #create out-filename
                    # print(outname)
                    outPath =  cleanPath + '/out/' + outname# create path to out dir for out file
                    self.cmd['inputPath'] = cleanPath + '/' +vidFile #set paths
                    self.cmd['outPath'] = outPath # Sets output path

                    # subprocess.Popen(' '.join(self.convertCMD()))
                    # print(self.cmd)
                    subprocess.call(self.convertCMD())# execute the crop comant

    def convertCMD(self):
        """
        Converts dict to execuatable command
        :return:
        """
        out = [self.cmd['vidProcessor'], self.cmd['parama'], self.cmd['inputPath'],
               self.cmd['args'], self.cmd['crop'], self.cmd['outPath']]
        return out

    def addCropingArgs(self, zone, row):
        """
        zone is an int 2, 3, 4 which will indicate which zone to be sliced

        Will take in the self.width, self.height and self.data into the format:
            crop - area to crop
            out_w - Width dimesion of output vid
            out_h - Height dimesion of output vid
            x - Lataral cordinate used for begining of crop
            y - Vertical coordinate used for begining of crop

        will then take this data and construct a string similar to the format:

        crop=out_w=162:out_h=50:x=1197:y=311

        This will then be put into the self.cmd['crop'] dict so it can be used but fuck this all might be wrong
        :return: None
        """
        if zone not in [1,2,3,4,5,6]:
            raise Exception("Not in valid zone")
        else:
            out = "crop=out_w=" + str(self.width) + ":out_h=" + str(self.height) + ":x=" + str(row[2*zone-2]) + ":y=" + str(row[2*zone-1])
            self.cmd['crop'] = out

# avconv -i $path_to_vid -vf crop=out_w=162:out_h=50:x=1197:y=311 $Out_I_A

#Test
a = DivideVid('test.csv')
# print(a.headers)
# print( a.data, a.inputPath)
# print(str(a.inputPath[0])[2:-1])
a.cropVidDirectory()
# print(np.loadtxt('test.csv',dtype=float,delimiter=',',skiprows=1, usecols=range(1,13)))


