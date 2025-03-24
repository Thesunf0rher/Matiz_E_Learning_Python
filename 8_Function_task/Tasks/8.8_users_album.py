def make_album(author: str, album: str, track: int=None) -> dict:
    info = {'Author': author.title(), 'ALbum': album}
    if track is not None:
        info['Track'] = track
    return info

while True:
    print("(To exit, write q)")

    author = input("\nEnter the author performer: ")
    if author.lower() == 'q':
        break
    album_name = input("\nEnter the artist's album: ")
    if album_name.lower() == 'q':
        break
    tracks = input("\nNumber of tracks (press Enter if you don't know):")
    if tracks.lower() == 'q':
        break

    if tracks.isdigit():
        tracks = int(tracks)
        result = make_album(author, album_name, tracks)
    else:
        result = make_album(author, album_name)

    print(f"\n{result}\n")
#179