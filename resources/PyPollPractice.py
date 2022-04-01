# The data we need to retrieve
import os
import csv
dir(csv)

myPath = os.path.join("election_results.csv.csv")

if os.path.exists(myPath):
    print("On Target")

#Open the election results and read the file
with open(myPath, "r", newline='') as election_data:

     # To do: read and analyze the data here.

        # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
     # Print each row in the CSV file.
    for row in file_reader:
        print(row)
    # to do: perform analysis
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:



 # Write three counties to the file.
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
## Create a filename variable to a direct or indirect path to the file.
##file_to_load = os.path.join("election_results.csv.csv")
## Using the open() function with the "w" mode we will write data to the file.
##open(file_to_load, "r")

# to do: perform analysis

# Close the file
#election_data.close()
#  1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.