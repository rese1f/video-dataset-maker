

def download_resolution(h):
    for i in [144, 360, 480, 720, 1080, 1440, 2160]:
        if h <= i: return i
    return 2160