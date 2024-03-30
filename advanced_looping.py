#Task 1

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
sublist_genres = []
for x in genres[1:4]:
    print(x)
    sublist_genres.append(x)

print(sublist_genres)


#Task 2

new_genres = [x + " Music" for x in genres]
print(new_genres)


#Task 3

for x in range(10, 0, -1):
    print(x)
print("The beat drops now!")
