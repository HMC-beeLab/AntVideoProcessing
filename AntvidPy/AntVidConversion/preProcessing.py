# This will use what we learned for writing in shell to reproduce the same code and then build up a code base to ultimatly batch process vids
import numpy as np
import glob, os
import subprocess, shutil
class DivideVid():

    def __init__(self, filePath, row, width=300, height=50):
        """
        Will read in line of CSV file
        :param filePath: absolute path to csv file
        :param row: the row of csv to read in
        """
        self.inputPath = np.loadtxt(filePath,dtype='str', delimiter=',', skiprows=row, usecols=range(1))
        self.data = np.loadtxt(filePath ,dtype=float, delimiter=',', skiprows=row, usecols=range(1, 13))
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

        :return: will create 6 vids for every vid in dir
        """
        for path in self.inputPath: # iterate throught each of the paths in the csv
            cleanPath = str(path)[2:-1]
            try:
                os.mkdir(cleanPath + '/out') #make out put dir
            except:
                print('dir Already exsists')
            files_in_dir = os.listdir(cleanPath) #get paths to all files in dir
            files_in_dir.pop(0) #remove first elment which is dir name out
            for vidFile in files_in_dir:#itterate over each file
                outname = "out-" + os.path.basename(vidFile) #create out-filename
                outPath =  cleanPath + '/out/' + outname# create path to out dir for out file
                self.cmd['inputPath'] = cleanPath + '/' +vidFile #set paths
                self.cmd['outPath'] = outPath
                subprocess.call(self.convertCMD())# execute the crop comant

    def convertCMD(self):
        """
        Converts dict to execuatable command
        :return:
        """
        out = [self.cmd['vidProcessor'], self.cmd['parama'], self.cmd['inputPath'],
               self.cmd['args'], self.cmd['crop'], self.cmd['outPath']]
        return out


# avconv -i $path_to_vid -vf crop=out_w=162:out_h=50:x=1197:y=311 $Out_I_A

#Test
# filePath = 'test.csv'
# row = 1
# print(np.loadtxt(fname='/Users/alasdairjohnson/Code/AntVideoProcessing/AntvidPy/AntVidConversion/test.csv',dtype=float,delimiter=',',skiprows=1, usecols=range(1,13)))
a = DivideVid('test.csv', 1)
# print( a.data, a.inputPath)
# print(str(a.inputPath[0])[2:-1])
a.cropVidDirectory()

# print(np.loadtxt('test.csv',dtype=float,delimiter=',',skiprows=1, usecols=range(1,13)))
# import csv

