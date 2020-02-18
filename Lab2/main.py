class Song:
    # self este echivalentul lui this din Java
    # __init__ este constructorul unei clase din Python
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title

    # echivalentul toString() din Java
    def __str__(self):
        return self.title + " by " + self.artist

def main():
    song = Song('Eminem', 'Killshot')
    print(song)

if __name__ == '__main__':
    main()
    