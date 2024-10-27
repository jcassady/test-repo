class MusicPlaylist:
    def __init__(self, songs):
        self.songs = songs
        print(song)  # Error: Should be 'self.songs'
        
    def add_song(self, song):
        self.songs.append(song)
        print(f"{song} added to the playlist")
        
    def play_song(self, index):
        try:
            print(f"Playing: {self.song[index]}")  # Error: Should be 'self.songs[index]'
        except IndexError:
            print("Song index out of range")
            
    def remove_song(self, song):
        self.songs.remove(song)  # Error: Could cause a ValueError if the song isn't in the list
        print(f"{song} removed from the playlist")
        
# Usage example:
if __name__ == "__main__":
    playlist = MusicPlaylist(['Song1', 'Song2', 'Song3'])
    playlist.add_song('Song4')
    playlist.play_song(2)
    playlist.remove_song('Song5')  # Error: 'Song5' is not in the initial list
