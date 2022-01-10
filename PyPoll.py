import csv
import os
#Assign a variable for the file to load the path.
file_to_load = os.path.join('election_results.csv')
#Assign variable to save the file to a path
file_to_save = os.path.join('election_analysis.txt')

#open the election results and read the file
with open(file_to_load) as election_data:
    #to do: read and analyze the data here

    #read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    #print header row
    headers = next(file_reader)
    print(headers)
    









