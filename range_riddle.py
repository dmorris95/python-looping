#Task 1

import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for d in range(7):
    print("On " + days_of_week[d] + ", you were feeling " + random.choice(moods))
