from abc import ABC,abstractmethod
from collections.abc import Container

# Abstract Class

class MusicPlayer(ABC):

    @abstractmethod
    def play_song(self):
        print("Enjoy the music.")
        

    @abstractmethod
    def pause_song(self):
        print("Thank you for playing this song.")

    @abstractmethod
    def go_forward(self):
        print("Forwarded.")

    @abstractmethod
    def go_backward(self):
        print("Reversed")

    def give_feedback(self):
        input("Enter your feedback here: ")
        print("Thanks for your feedback. We appreciate it.")

#Child class

class Spotify(MusicPlayer):

    def __init__(self,format):
        self.format = format

    def play_song(self):
        super().play_song()
        print("Dive into the world of music without any distraction.")

    def pause_song(self):
        return super().pause_song()
    
    def go_forward(self):
        return super().go_forward()
    
    def go_backward(self):
        return super().go_backward()
    
obj = Spotify("mp3")
obj.play_song()
obj.pause_song()
obj.go_forward()
obj.go_backward()
obj.give_feedback()

#================================================================================================================

# class Bowl:
#     def __init__(self, liquid):
#         self.liquid = liquid

#     def __contains__(self, x):
#         return isinstance(x, Bowl) and self.liquid == x.liquid

# b1 = Bowl("water")
# b2 = Bowl("water")
# print(b1 in b2)  # Output: True

