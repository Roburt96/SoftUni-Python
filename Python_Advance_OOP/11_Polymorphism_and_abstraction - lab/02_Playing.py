def start_playing(sound):
    return sound.play()


class Guitar:
    def play(self):
        return "Playing the guitar"


guitar = Guitar()
print(start_playing(guitar))
