#Task 1

import random

moods = ["Happy", "Sad", "Stressed", "Calm", "Energetic"]
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
time_of_day = ["Morning", "Afternoon", "Evening"]

for d in range(7):
    for t in range(3):
        print("On " + days_of_week[d] + " " + time_of_day[t] + " you were " + random.choice(moods))



