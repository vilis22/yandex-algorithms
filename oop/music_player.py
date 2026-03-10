class MusicPlayer:
    def __init__(self):
        self._volume = 10

    def get_volume(self):
        return self._volume

    def set_volume(self, new_volume):
        if isinstance(new_volume, (int, float)) and 0 <= new_volume <= 100:
            self._volume = new_volume
