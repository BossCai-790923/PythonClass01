'''
There is a party to celebrate celebrities that you get to attend because you
won a ticket at your office lottery. Because of the high demand for tickets,
you only get to stay for one hour, but you get to pick which hour because
you received a special ticket. You have a schedule that lists exactly when
each celebrity is going to attend the party. You want to get as many pictures
with celebrities as possible to improve your social standing. This means you
wish to go for the hour when you get to hobnob with the maximum number
of celebrities and get selfies with each of them.

We are given a list of intervals that correspond to when each celebrity
comes and goes. Assume that these intervals are [i, j), where i and j
correspond to hours. That is, the interval is closed on the left side and open
on the right side. This means the celebrity will be partying on and through
the ith hour, but will have left when the jth hour begins. So even if you
arrive on the dot on the jth hour, you will miss this particular celebrity.
Here’s an example:

Celebrity   Comes   Goes
Beyoncé     6       7
Taylor      7       9
Brad        10      11
Katy        10      12
Tom         8       10
Drake       9       11
Alicia      6       8
'''

celebrities_arrival_schedule = [(6, 8), (6, 12), (6, 7), (7, 8),
                                (7, 10), (8, 9), (8, 10), (9, 12),
                                (9, 10), (10, 11), (10, 12), (11, 12)]

































































'''



# Data Preparation -----------------------------
# Step 1) I define a dict, which remembers how many celebrities will come for the hour.
# key: hour
# value: celebrities count
celebrities_count = {6:0, 7:0, 8:0, 9:0, 10:0, 11:0}


# Main logic -----------------------------------

# Step 2) Loop celebrities_arrival_schedule
# For each celebrity arrival schedule, I update my dict - celebrities_count
for time_interval in celebrities_arrival_schedule:
    for hour in range(*time_interval): # star unpacking which we learnt in 118, range function accepts 2 parameters: start / stop. So we can unpack the tuple.
        celebrities_count[hour] += 1

print("Here is my dict, which shows how many celebrities will come for each hour.")
print("Hour: Celebrities Count")
print(celebrities_count)
print("------------------------------------------------")


# Step 3) I find the hour which contains the maxmium count of celebrities

# Step 3.1) Data Preparation -------------
hour_i_should_go = 6
celebrities_i_can_see = 0

# Step 3.2) Loop the dict
for hour, count in celebrities_count.items():
    if count > celebrities_i_can_see:
        hour_i_should_go = hour
        celebrities_i_can_see = count

print(f"I should go to the party at {hour_i_should_go} pm")


'''