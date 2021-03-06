class Song:
    static_member = 420 # membru static

    # self este echivalentul lui this din Java
    # __init__ este constructorul unei clase din Python
    def __init__(self, artist, title, year):
        self.artist = artist
        self.title = title
        self.year = year

    # echivalentul toString() din Java
    # ca sa ne referim la membri ai clasei, trebuie sa folosim self
    def __str__(self):
        return self.title + " by " + self.artist

    def play(self):
        print('Now playing %s by %s, released in %d' % (self.title, self.artist, self.year))

    # metodele statice nu au parametrul self
    @staticmethod
    def class_method():
        print('static method')


def main():
    song = Song('Eminem', 'Killshot', 2018)
    print(song)
    # calling a method
    song.play()
    Song.class_method()
    print(Song.static_member)


if __name__ == '__main__':
    main()
