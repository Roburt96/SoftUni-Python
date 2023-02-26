from project.album import Album
from project.song import Song


class Band:

    def __init__(self, name: str):
        self.name = name
        self.album = []

    def add_album(self, album: Album):
        if album not in self.album:
            self.album.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        else:
            return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name: str):
        if album_name not in (x.name for x in self.album):
            return f"Album {album_name} is not found."

        if album_name in (x.name for x in self.album):
            for x in self.album:
                if x.published:
                    return f"Album has been published. It cannot be removed."

        self.album.remove(album_name)
        return f"Album {album_name} has been removed."

    def details(self):
        result = f"Band {self.name}\n"
        for x in self.album:
            result += f"{x.details()}\n"
        return result

song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())