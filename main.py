from pyfy import Spotify
import time


spt = Spotify('your-code')




"""
Add_tracks_Archived
-checks to see if an archived playlist exists for the selected playlist
-If no playlist (pl) exists then create a new one
-Once pl situation is solved removed all songs from selected playlist and add them to archived
"""

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




"""
print_tracks
- literrally just prints tracks from the playlist that is selected
-Allows the user to choose which tracks to delete by seperating their number with commas EX: (1,6,78,)
-return the selected playlist id and the list of archived songs 
"""
def print_tracks():
    trackCounter =0
    tracks_on_selected_pl = spt.playlist_tracks(user_choice_pl_id)


    for track in tracks_on_selected_pl['items']:
        print(trackCounter, track['track']['name'])
        trackCounter+=1

    user_deleted_tracks_chose = input("Enter in the tracks you want archived. Ex: 1,7,8,10,23")
    x = user_deleted_tracks_chose.split(",")
    #Sends all the songs from selected playlist and the tracks the user selected to delete
    #method returns a list of id's of all the selected songs


    return [tracks_on_selected_pl, x]

"""
get_song_id
- Takes the song list and archived song list from the print function
-returns a list of the id's for each song selected
"""

def get_song__id(pl_track_list, selected_archive_tracks):
    archived_song_list = []
    for archived in selected_archive_tracks:
        if archived=="":
            pass
        else:
            archived_song_list.append(pl_track_list['items'][int(archived)]['track']['id'])

    return archived_song_list







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



print_tracks_return = print_tracks()
archived_track_ids= get_song__id(print_tracks_return[0],print_tracks_return[1])

add_tracks_archived(archived_track_ids,user_choice_pl_id, user_choice_pl_name)
