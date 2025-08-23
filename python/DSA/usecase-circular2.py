# Circular Buffer for Music Playlist
# Series of Music: Playlist
class MusicPlaylist:
    def __init__(self, memorySize):
        # [None] => [] "empty list"
        self.memory = [None] * memorySize
        # size = 3 => ["", "", ""]
        self.size = memorySize
        self.start = self.stop = 0
        
    def add_song(self, song):
        self.memory[self.stop] = song
        self.stop = (self.stop + 1) % self.size
        if self.stop == self.start:
            self.start = (self.start + 1) % self.size
            
    def play_song(self):
        playlist = []
        song = self.start
        while song != self.stop:
            playlist.append(self.memory[song])
            song = (song + 1) % self.size
        return playlist
    
songs = MusicPlaylist(3) 
# songs.add_song("Salaam Rocky Bhai")
# songs.add_song("Tagaru Banthu Tagaru")
# songs.add_song("Bombe Heluthaithe")
# songs.add_song("Avane Srimmanarayana")
songs.add_song("Song 1")
songs.add_song("Song 2")
songs.add_song("Song 3")
songs.add_song("Song 4")
print(songs.play_song())

# Initial Step

# We are storing some songs and playing it, parallely we are checking the current and next songs
# memory = [], size = 3, start, stop = 0
#      [None, None, None]
#         0    1     2  
#    start/stop

# stop = 0, start = 0
# Add 1st song:  memory[0] = "Song 1"
# stop = (0 + 1) % 3 => (1) % 3 => 1
# stop == start => 1 == 0 => F

# stop = 1, start = 0
# Add 2nd song: memory[1] = "Song 2"
# stop = (1 + 1) % 3 => (2) % 3 => 2
# stop == start => 2 == 0 => F

# stop = 2, start = 0
# Add 3rd song: memory[2] = "Song 3"
# stop = (2 + 1) % 3 => (3) % 3 => 0
# stop == start => 0 == 0 => T
        # start = (0 + 1) % 3 => (1) % 3 => 1
        
# stop = 0, start = 1

# After adding 3 songs in the memory:
# memory = ["Song 1", "Song 2", "Song 3"]
        #      0          1        2
        
# ----------------------------------------
# stop = 0, start = 1
# Add 4th song: memory[0] = "Song 4"
# stop = (0 + 1) % 3 => (1) % 3 => 1
# stop == start => 1 == 1 => T
        # start = (1 + 1) % 3 => (2) % 3 => 2
        
# stop = 1, start = 2

# While adding 4th song, it has Replaced the "Song 1" with "Song 4" at the 0th position
# memory = ["Song 4", "Song 2", "Song 3"]
#         #      0          1        2
# --------------------------------------------

# While playing the song:

# stop = 1, start = 2

# playlist = []
# song = 2, stop = 1
# while song ! = stop => while 2 != 1 => T
            # playlist.append(memory[song]) => playlist.append(memory[2]) 
                                          # => playlist.append("Song 3") 
                                          # song = (song + 1) % size
                                          # song = (2 + 1) % 3 => 3 % 3 = 0
                                          # song = 0
# song = 0, stop = 1
# while song ! = stop => while 0 != 1 => T
            # playlist.append(memory[song]) => playlist.append(memory[0]) 
                                          # => playlist.append("Song 4") 
                                          # playlist = ["Song 3"] + ["Song 4"]  
                                          # song = (song + 1) % size
                                          # song = (0 + 1) % 3 => 1 % 3 = 1
                                          # song = 1
# song = 1, stop = 1
# while song ! = stop => while 1 != 1 => F
            # Stop
            # print(playlist)  
            # playlist = ["Song 3", "Song 4"]   