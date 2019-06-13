from pyfy import Spotify
import time


spt = Spotify('Your-acess-code')

playlist_list = spt.user_playlists()

counter = 0
for pl in playlist_list['items']:
    print(counter,".)" ,pl['name'])
    counter +=1

user_Choice = int(input("choose a playlist by typing the number"))
print("Your chose",user_Choice,"which is", playlist_list['items'][user_Choice]['name'])
#6user_choice_two = input("Is this the correct playlist? Y for yes, N for No")
user_choice_pl_id = playlist_list['items'][user_Choice]['id']
user_choice_pl_name = playlist_list['items'][user_Choice]['name']




def add_tracks_archived(archivedTrackList, selectedPL_ID,selectedPL_Name):
    #check to see if an archived playlist exists
    foundPlaylist = False
    users_playlists = spt.user_playlists()
    archived_PL_ID= 0


    for playlists in users_playlists['items']:
        if selectedPL_Name+str("_archived") == playlists['name']:
            archived_PL_ID = playlists['id']
            print("playlist exists")
            foundPlaylist = True
            break


    if foundPlaylist == False:
        print("Creating Playlist")
        archived_PL_ID =spt.create_playlist(selectedPL_Name+str("_archived"))['id'] #creates the new playlist and grabs the id

    spt.add_playlist_tracks(archived_PL_ID, archivedTrackList)
    spt.delete_playlist_tracks(selectedPL_ID, archivedTrackList)




trackCounter =0
tracks_on_selected_pl = spt.playlist_tracks(user_choice_pl_id)

print(tracks_on_selected_pl)

for track in tracks_on_selected_pl['items']:
    print(trackCounter, track['track']['name'])
    trackCounter+=1

user_deleted_tracks_chose = input("Enter in the tracks you want archived. Ex: 1,7,8,10,23")










# setting the max parameter to 1, will return a list with 2 elements!
x = user_deleted_tracks_chose.split(",")


archived_song_list = []
for archived in x:
    if archived=="":
        pass
    else:
        archived_song_list.append(tracks_on_selected_pl['items'][int(archived)]['track']['id'])



print(archived_song_list)

add_tracks_archived(archived_song_list,user_choice_pl_id, user_choice_pl_name)




