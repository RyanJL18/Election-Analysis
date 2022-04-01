# How many votes did you get?
my_votes = int(input("How many votes did you get in the election?"))
# Total votes in the election
total_votes = int(input("What is the total votes in the election?"))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes/total_votes)*100
print("I received " + str(percentage_votes) + "% of total votes.")


counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

x = 0
while x <= 5:
    print(x)
    x = x + 1