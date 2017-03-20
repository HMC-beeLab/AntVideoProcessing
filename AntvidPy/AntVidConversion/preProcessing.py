# This will use what we learned for writing in shell to reproduce the same code and then build up a code base to ultimatly batch process vids
import numpy as np
class DivideVid():

    def __init__(self, filePath, row, width=300, height=50):
        """
        Will read in line of CSV file
        :param filePath: absolute path to csv file
        :param row: the row of csv to read in
        """
        self.inputPath = np.loadtxt(filePath,dtype=str, delimiter=',', skiprows=row, usecols=range(0))[0]
        self.data = np.loadtxt(filePath ,dtype=float, delimiter=',', skiprows=row, usecols=range(1, 13))
        self.width =  width
        self.height = height
        self.cmd = ['avconv',#vid converter were using
                     '-i',#paramas
                     self.inputPath,#input path for comand
                     '-vf',#what command are we going to run
                     'crop=out_w=162:out_h=50:x=1197:y=311',#place holder for crop command
                     '']#outupt file path

    def cropVidIndividual(self):
        """

        :return: will create 6 vids with naming schema out-FilePath
        """

        
        outPath =  "out-" + self.inputPath



    def cropVidDirectory(self):
        """

        :return: will create 6 vids for every vid in dir
        """


# avconv -i $path_to_vid -vf crop=out_w=162:out_h=50:x=1197:y=311 $Out_I_A

#Test

print(np.loadtxt('test.csv',dtype=float,delimiter=',',skiprows=1, usecols=range(1,13)))
import csv

