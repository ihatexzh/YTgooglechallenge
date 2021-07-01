"""A video player class."""
import random

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.isPlaying = False
        self.isPaused = False
        self.playlist_id = 0
        self.playlist_list = []
        self.videoflag = False



    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos = self._video_library.get_all_videos()
        print("A list of available videos: ")
        temp_list = []
        for vid in videos:
            tags = "["
            for tag in vid.tags:
                tags = tags + tag + " "
            tags += "]"
            if tags != "[]":
                tags = tags[0:len(tags)-2] + "]"

            temp_list += [f"{vid.title} ({vid.video_id}) {tags}"]
        sorted_list = sorted(temp_list)
        for li in sorted_list:
            print(li)


    def play_video(self, video_id):
        global is_playing
        global previous_played
        global now_playing
        global is_paused

        now_playing = self._video_library.get_video(video_id)

        if not now_playing:
            print("Video does not exist!")
        else:
            if is_playing:
                print(f"Stop playing: {previous_played}")
                print(f"Start playing: {now_playing.title}")
                is_paused = False
                previous_played = now_playing.title
            else:
                print(f"Start playing: {now_playing.title}")
                is_playing = True
                is_paused = False
                previous_played = now_playing.title

        """Plays the respective video.
        

        Args:
            video_id: The video_id to be played.
        """


    def stop_video(self):
        """Stops the current video."""
        global is_playing
        global previous_played
        global now_playing

        if is_playing:
            print(f"Now stopping: {now_playing.title}")
            is_playing = None
            previous_played = None
        else:
            if not is_playing:
                print("No video is playing now.")
                previous_played = None



    def play_random_video(self):
        """Plays a random video from the video library."""
        global is_playing
        global previous_played
        global now_playing
        global is_paused

        now_playing = random.choice(self._video_library.get_all_videos())
        if is_playing:
            print(f"Stopping video: {previous_played}")
            print(f"Playing video: {now_playing.title}")
            is_playing = True
            is_paused = False
        else:
            print(f"Now start playing: {now_playing.title}")
            is_playing = True
            is_paused = False

        previous_played = now_playing.title



    def pause_video(self):
        """Pauses the current video."""




    def continue_video(self):
        """Resumes playing the current video."""

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in (name.lower() for name in self.playlist_dict.keys()):
            pl = Playlist(playlist_name)
            self.playlist_dict[playlist_name] = pl
            print("Successfully created new playlist:", pl._name)
        else:
            print("Cannot create. It already exists.")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_name_old = playlist_name
        if playlist_name.lower() not in (name.lower() for name in self.playlist_dict.keys()):
            print("Cannot add video to", playlist_name + ":", "Playlist does not exist")
        else:
            for key in self.playlist_dict.keys():
                if key.lower() == playlist_name.lower():
                    playlist_name = key
            video_list = self.playlist_dict[playlist_name]._videos
            try:
                video_name = self._video_library.get_video(video_id)._title
            except:
                video_name = ""
            if not video_name:
                print("Cannot add video to", playlist_name_old + ":", "Video does not exist")
            elif video_id in video_list:
                print("Cannot add video to", playlist_name + ":", "Playlist does not exist")

        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """

        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
