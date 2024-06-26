import os
import pygame
import eyed3

class MusicPlayer:
    def __init__(self, music_folder):
        self.music_folder = music_folder
        self.music_files = [f for f in os.listdir(music_folder) if f.endswith(('.mp3', '.wav','.m4a'))]
        self.current_index = 0
        self.paused = False

        pygame.init()
        pygame.mixer.init()
    
    def get_current_track_name(self):
        if not self.music_files:
            return None
        return os.path.splitext(self.music_files[self.current_index])[0]
    def get_album_artwork(self):
        audiofile = eyed3.load(os.path.join(self.music_folder, self.music_files[self.current_index]))

        if audiofile.tag:
            if audiofile.tag.images:
                return audiofile.tag.images[0].image_data

        return None

    def play(self):
        pygame.mixer.music.load(os.path.join(self.music_folder, self.music_files[self.current_index]))
        pygame.mixer.music.play()
        print(self.get_current_track_name())

    def pause(self):
        if self.paused:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        self.paused = not self.paused

    def stop(self):
        pygame.mixer.music.stop()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)

    def next_track(self):
        self.current_index = (self.current_index + 1) % len(self.music_files)
        self.stop()
        self.play()

    def prev_track(self):
        self.current_index = (self.current_index - 1) % len(self.music_files)
        self.stop()
        self.play()

if __name__ == "__main__":
    music_folder = "media"
    player = MusicPlayer(music_folder)

    while True:
        command = input("Enter command (play/pause/stop/volume/next/prev/exit): ").lower()

        if command == "play":
            player.play()
        elif command == "pause":
            player.pause()
        elif command == "stop":
            player.stop()
        elif command == "volume":
            volume = float(input("Enter volume (0.0 to 1.0): "))
            player.set_volume(volume)
        elif command == "next":
            player.next_track()
        elif command == "prev":
            player.prev_track()
        elif command == "exit":
            break
        else:
            print("Invalid command. Try again.")
