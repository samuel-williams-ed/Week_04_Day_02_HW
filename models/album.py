class Album():
    def __init__(self, input_title, input_genre, input_artist, generated_id=None):
        self.title = input_title
        self.genre = input_genre
        self.artist = input_artist
        self.id = generated_id
