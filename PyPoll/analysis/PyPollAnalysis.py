#columns: Voter ID, County, Candidate

#calculate the following:
#Total number of votes cast
#complete list of candidates who rec'd votes
#the percentage of votes each candidate won
#total number of votes each candidate won
#winner of election based on popular vote

import os
import csv

PyPoll_csv = os.path.join("..", "Resources", "election_data.csv")

#if os.path.isfile(PyPoll_csv) is True:
    #print("this file exists")

#else:
    #print("this file does not exist")

total_votes_cast = 0
candidate_list = []
candidate_total_votes = []
percent_votes_candidate = []
election_winner = []
popular_vote = []

with open(PyPoll_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ',')

    csv_header = next(csv_reader)
    #print(csv_header)

    for row in csv_reader:
        total_votes_cast = total_votes_cast +  1
        candidate_list ##Look at that names in names

    print("Election Results")
    print("---------------------")
    print("Total Votes:", total_votes_cast)
    print("---------------------")
    
