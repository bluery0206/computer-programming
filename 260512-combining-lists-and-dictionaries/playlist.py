playlist = {
    "name": "Favorites",
    "songs": [
        {
            "title": "Hikari",
            "artist": "Utada Hikaru"
        },
        {
            "title": "Blue Bird",
            "artist": "Ikimono-gakari"
        }
    ]
}

# printing the first song in the playlist
song_1 = playlist["songs"][0]
print(song_1)

# updating the second songs title
print(f"Before: {playlist["songs"][1]}")
playlist["songs"][1]['title'] = "Blue nga langgam"
print(f"After: {playlist["songs"][1]}")