class Playlist:
    def __init__(self, title: str, songs: list) -> None:
        self.title = title
        self.songs = songs

    def __len__(self):
        return len(self.songs)
