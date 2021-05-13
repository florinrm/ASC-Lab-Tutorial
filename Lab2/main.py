from threading import Thread

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
        print('Now playing %s by %s, released in %d' % (self.title, self.artist, self.year))

    @staticmethod
    def class_method():
        print('static method')

    def second_class_method():
        print('another static method')
    second_class_method = staticmethod(second_class_method)


def main():
    song = Song('Eminem', 'Killshot', 2018) # nu avem keyword-ul new aici
    print(song)
    # calling a method
    song.play()
    Song.class_method()
    Song.second_class_method()


if __name__ == '__main__':
    main()
