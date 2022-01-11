import csv
import os
#Assign a variable for the file to load the path.
file_to_load = os.path.join('election_results.csv')
#Assign variable to save the file to a path
file_to_save = os.path.join('election_analysis.txt')
#initialize total votes counter
total_votes = 0
candidate_options=[]
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#open the election results and read the file
with open(file_to_load) as election_data:
 #read the file object with the reader function
    file_reader = csv.reader(election_data)
    #print header row
    headers = next(file_reader)
     #print each row in the csv file
    for row in file_reader:
        #add to total vote count
        total_votes +=1
        #print candidate name each row
        candidate_name=row[2]

        #if candidate does not match existing candidate
        if candidate_name not in candidate_options:
            #add the candidate name to candidate list
             candidate_options.append(candidate_name)
             #begin tracking that candidate's vote count
             candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] +=1

#save results to our text file
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------\n")

    print(election_results, end="")
    #save final vote count to the text file
    txt_file.write(election_results)

#determine the percent of votes each candidate
# iterate through candidate list
    for candidate_name in candidate_votes:
    #retrieve vote count
        votes = candidate_votes[candidate_name]
    #calculate percentage
        vote_percentage = float(votes)/float(total_votes) * 100
    #print the candidate name and percent of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # print candidate, their count, and percentage in terminal
        print(candidate_results)
    #save candidate results to file
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # if true then set winning_count = votes and wiing_percent=#vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
        # set winning equal to candidates name
            winning_candidate = candidate_name
    #print winning results to terminal
    winning_candidate_summary = (f'--------------------\n'
                 f'winner: {winning_candidate}\n'
                 f'winning vote count: {winning_count:,}\n'
                 f'winning percentage: {winning_percentage:.1f}%\n'
                 f'----------------------\n')
    print(winning_candidate_summary)
    #save winning name to text file
    txt_file.write(winning_candidate_summary)

   













