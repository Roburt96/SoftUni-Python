from project.song import Song


class Album:

    def __init__(self, name: str, *args):
        self.name = name
        self.published = False
        self.songs = [*args]

    def add_song(self, song_obj: Song):
        if song_obj.single:
            return f"Cannot add {song_obj.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        if song_obj in self.songs:
            return "Song is already in the album."

        self.songs.append(song_obj)
        return f"Song {song_obj.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."

        if song_name not in (x.name for x in self.songs):
            return "Song is not in the album."

        self.songs.remove(song_name)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for songs in self.songs:
            result += f"== {songs.get_info()}\n"
        return result
