from db.run_sql import run_sql

from models.artist import Artist

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

#our favourite function
#deleteing the values from table artists
def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def select_all():
    artists_list = []
    sql = "SELECT * FROM artists"
    query_results = run_sql(sql)
    for row in query_results:
        artist = Artist(row['name'], row['id'])
        artists_list.append(artist)
    
    return artists_list


def select_single(artist_id):
    artist = None
    sql = "SELECT * FROM artists WHERE id=%s"
    values = [artist_id]
    query_results = run_sql(sql, values)
    #check we have a result
    if query_results:
        #only one result but always in list format so need to access thorugh index [0]
        new_result = query_results[0]
        artist = Artist(new_result['name'], new_result['id'])
    # None if 'if' block doesn't run
    return artist

