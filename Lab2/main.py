class Song:
    # self este echivalentul lui this din Java
    # __init__ este constructorul unei clase din Python
    def __init__(self, artist, title, year):
        self.artist = artist
        self.title = title
        self.year = year


    # echivalentul toString() din Java
    def __str__(self):
        return self.title + " by " + self.artist


    def play(self):
        print('Now playing %s by %s, released in %d' %(self.title, self.artist, self.year))


def main():
    song = Song('Eminem', 'Killshot', 2018)
    print(song)
    # calling a method
    song.play()


if __name__ == '__main__':
    main()
    