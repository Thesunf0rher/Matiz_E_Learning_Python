def make_album(author: str, album: str, track: int=None) -> dict:
    info = {'Author': author.title(), 'ALbum': album}
    if track is not None:
        info['Track'] = track
    return info

album1 = make_album('the weeknd', 'after hours')
album2 = make_album('bruno mars', '24k magic')
album3 = make_album('lil nas x', 'montero', 4)

print(album1)
print(album2)
print(album3)