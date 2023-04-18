class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def cante(self):
        for line in self.lyrics:
            print(line)

    def caps(self):
        for line in self.lyrics:
            print(line.split(' '))

Happy_Day = Song(['''OHHHH, Happay Day !!!!
OHHHHH Happy Day
OHHHHHHHHH Happy Happy Day !!!'''])

Dance_To_Me = Song(['''Dance to me now, OHHHHH
 OHHHHHHHHHHHHHHH
 Dance to me now !!!'''])

Happy_Day.cante()
Dance_To_Me.cante()
Happy_Day.caps()
Dance_To_Me.caps()
 
