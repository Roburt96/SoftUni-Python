def add_songs(*args):
    song = {}
    for author, lyric in args:
        song[author] = song.get(author, [])
        for lyrics in lyric:
            song[author].append(lyrics)
    result = ""
    for key, value in song.items():
        result += f"- {key}\n"
        for text in value:
            result += f"{text}\n"
    return result










print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))