# Use this file to test your repository functions 

from models.album import Album
from models.artist import Artist
import repositories.artist_repository as rep_rep
import repositories.album_repository as penseive

#load test artist data
# test_artist_1 = Artist("Louisianana")
# test_artist_2 = Artist("Shania Twain")
# test_artist_3 = Artist("The Olllam")
# art_rep.save(test_artist_1)
# art_rep.save(test_artist_2)
# art_rep.save(test_artist_3)

#get artists from SQL database
test_artist_1 = rep_rep.select_single(4)
test_artist_2 = rep_rep.select_single(5)
test_artist_3 = rep_rep.select_single(6)

# art_rep.delete_all()

# full_list_of_artists = art_rep.select_all()
# for artist in full_list_of_artists:
#     print(artist.__dict__)

# artist = art_rep.select_single(4)
# print(artist.__dict__)

# load test albums
# test_album_1 = Album("Come on Over", "Country/pop", test_artist_2)
# print(f"Console: test_album_1 = {test_album_1.__dict__}")
# test_album_2 = Album("With Pure Crystal Teeth", "Neo-Irish Folk", test_artist_3)
# test_album_3 = Album()
# penseive.save(test_album_1)
# penseive.save(test_album_2)

# Q: Find album by id
# print("Q: Find album by id")
# test_album_1 = penseive.select_album(10)

#create & save albums
# print("Q: Create and save albums")
# print(test_album_1.__dict__)

#show all albums
# print("Q: select all albums")
# print(penseive.select_all_albums())


# test rep_rep.find_artist_id_by_name()
# print("debug: find_artist_id_by_name():")
# print(rep_rep.find_artist_id_by_name("Shania Twain"))

# find all albums by artist
print("Q: find all albums by artist")
print(penseive.select_albums_by_artist("Shania Twain"))

