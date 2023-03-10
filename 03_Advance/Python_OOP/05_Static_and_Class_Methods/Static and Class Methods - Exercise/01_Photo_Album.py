from math import ceil


class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for i in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        for row in range(self.pages):
            for col in range(len(self.photos)):
                if len(self.photos[col]) < 4:
                    self.photos[col].append(label)
                    return f"{label} photo added successfully on page " \
                           f"{col + 1} slot {len(self.photos[col])}"
            return f"No more free slots"

    def display(self):

        dashes = ('-' * 11)
        result = ["-----------", ]
        for row in range(len(self.photos)):
            pics_on_row = len(self.photos[row])
            if pics_on_row > 0:
                pic = "[] " * pics_on_row
            else:
                pic = ""
            result.append(pic.rstrip())
            result.append(dashes)
        return '\n'.join(result)

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

