film = ["title1", "title2", "title3", "title4", "title5"]
file = open('filmy.txt', 'w', encoding="utf-8")
for i in  film:
    file.write(f"{i}\n")
file.close()
