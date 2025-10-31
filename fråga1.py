artist_and_albums = {

  "Stevie Wonder": ["Talking book", "Hotter then July"],

  "Pink Floyd": ["The Wall", "Whish you were here", "Pulse"],

  "Lady Gaga": [],

  "Elvis Presley": []

}

while True:

    print("1. Lägg till artist")

    print("2. Lägg till album till artist")

    print("3. Avsluta")

    choice = input(">>>")

    if choice == "1":
        ny_artist = input("Artist: ").title().strip()
        if ny_artist in artist_and_albums:
            print("Oh no, den finns redan!!!")
            continue
        artist_and_albums[ny_artist] = []




    elif choice == "2":
        artist_namn = input("Artist: ").title().strip()
        if artist_namn in artist_and_albums:
            album = input("Album: ").title().strip()
            if album in artist_and_albums[artist_namn]:
                continue
            artist_and_albums[artist_namn].append(album)

        else:
            print("Artist saknas!")



    elif choice == "3":
        break

    else:

        print("Ogiltigt val")