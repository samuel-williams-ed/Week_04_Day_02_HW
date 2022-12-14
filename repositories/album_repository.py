from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist
import repositories.artist_repository as rep_rep
# from repositories.album_repository import penseive
# ^ just banter

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    #value passed in SQL db for artist is the id only
    #when we pull data dfrom db we use id
    #to create an instance of artist that is within the instance of album
    # print("############## penseive #############")
    # print("")
    # print(f"penseive: value, album.artist = {album.artist.__dict__}")
    # print(f"penseive: value, album.artist.id = {album.artist.id}")
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    # print(f"results of SQL query = {results}")
    id = results[0]['id']
    # print(f"penseive: id = {id}")
    album.id = id
    return album

def select_album(album_id):
    album = None

    sql = " SELECT * FROM albums WHERE id=%s"
    values = [album_id]
    
    #single album where matches album_id
    results = run_sql(sql, values)
    
    if results:
        result = results[0]
        artist = rep_rep.select_single(result['artist_id'])
        album = Album(result['title'], result['genre'], artist, result['id'])
    return album

def select_all_albums():
    sql = " SELECT * FROM albums"
    return run_sql(sql)

def select_albums_by_artist(artist_name_string):
# find the artist id in album table
    artist_id = rep_rep.find_artist_id_by_name(artist_name_string)
# find albums matching found artist_id
    sql = " SELECT * FROM albums WHERE artist_id=%s"
    values = [artist_id]
    return run_sql(sql, values)

# debug:
    # print(f"alb_rep: select_alb_by_art: sqp values passed: {values}")
    # print(f"alb_rep: select_alb_by_art: sqp query returned: {query_result}")
