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
        print('Now playing %s by %s, released in %d' %(self.title, self.artist, self.year))

    @staticmethod
    def class_method():
        print('static method')

class MyThread(Thread):
    def __init__(self, tid):
        Thread.__init__(self)
        self.tid = tid

    def run(self):
        print("Thread with id %d" %(self.tid))

def main():
    song = Song('Eminem', 'Killshot', 2018)
    print(song)
    # calling a method
    song.play()
    Song.class_method()

    thread1 = MyThread(1)
    thread2 = MyThread(2)
    
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == '__main__':
    main()
    