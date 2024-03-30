#Task 1

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
#track_number = 1
'''
for x in genres:
    if x == "Jazz":
        print("This is track " + str(track_number) + ", it is " + x)
        print("This genre has a groovy vibe.")
    elif x == "Rock":
        print("This is track " + str(track_number) + ", it is " + x)
        print("This genre rocks your soul.")
    elif x == "Hip-hop":
        print("This is track " + str(track_number) + ", it is " + x)
        print("This genre will get you moving and make you dance.")
    elif x == "Classical":
        print("This is track " + str(track_number) + ", it is " + x)
        print("This genre will make you feel like you have gone back in time.")
    track_number += 1
'''


#Task 2
    
track_number = 1
is_hiphop = False

while track_number <= 4 and is_hiphop == False:
    if genres[track_number-1] == "Hip-hop":
        print("I don't really feel like listening to Hip-hop today.")
        is_hiphop = True
    else:
        if genres[track_number-1] == "Jazz":
            print("This is track " + str(track_number) + ", it is " + genres[track_number-1])
            print("This genre has a groovy vibe.")
        elif genres[track_number-1] == "Rock":
            print("This is track " + str(track_number) + ", it is " + genres[track_number-1])
            print("This genre rocks your soul.")
        elif genres[track_number-1] == "Hip-hop":
            print("This is track " + str(track_number) + ", it is " + genres[track_number-1])
            print("This genre will get you moving and make you dance.")
        elif genres[track_number-1] == "Classical":
            print("This is track " + str(track_number) + ", it is " + genres[track_number-1])
            print("This genre will make you feel like you have gone back in time.")
    track_number += 1


#Task 3
    

for x in range(len(genres)):
    if genres[x] == "Classical":
        print("There is no light show for the Classical Genre")
    else:
        if genres[x] == "Jazz":
            print("This is track " + str(x) + ", it is " + genres[x])
            print("The light show is ready.")
        elif genres[x] == "Rock":
            print("This is track " + str(x) + ", it is " + genres[x])
            print("The light show is ready.")
        elif genres[x] == "Hip-hop":
            print("This is track " + str(x) + ", it is " + genres[x])
            print("The light show is ready.")

