class Track:
    def __init__(self, name, duration):
        self.name = name
        self.duration = int(duration)

    def show(self):
        print(f'{self.name} - {self.duration} min.')


class Album:
    def __init__(self, album_name, group, all_tracks):
        self.album_name = album_name
        self.group = group
        self.track_list = all_tracks

    def get_tracks(self, album):
        for tracks in album:
            tracks.show()

    def get_add(self, album, track):
        album.append(track)

    def get_duration(self, albom, total_duration=0):
        for tracks in albom:
            total_duration += tracks.duration
        print(f'Общая длительность альбома: {total_duration} min.')


numb = Track('Numb', 3)
in_the_end = Track('In The End', 3)
faint = Track('Faint', 2)

believer = Track('Believer', 3)
deep = Track('Deep Water', 3)
best_day = Track('Best Day of my Life', 3)

numb.show()
in_the_end.show()
faint.show()
believer.show()
deep.show()
best_day.show()

linkin = []
american = []

album1 = Album('linkin', 'Linkin Park', linkin)
album2 = Album('american', 'American author', american)

album1.get_add(linkin, numb)
album1.get_add(linkin, in_the_end)
album1.get_add(linkin, faint)
album2.get_add(american, believer)
album2.get_add(american, deep)
album2.get_add(american, best_day)

print(linkin)
print(american)

album1.get_tracks(linkin)
album2.get_tracks(american)

album1.get_duration(linkin)
album2.get_duration(american)
