# 1. Create a list of favorite musicians
# Boom.
favorite_musicians = ['Sia', 'Pink Floyd', 'Bastille', 'Interpol']

# 2. Create a list of tuples, w ea containing lat and long of somewhere I've been.
# Sacramento, Fremont, Poughkeepsie
locations = [(38.5617251,-121.5833395), (37.5295018,-122.0786826), (41.6939603,-73.9362234)]

# Create a dictionary that contains different attributes about me
kitch = {'height': '5 ft 8', 'favorite author': 'Vonnegut','sign': 'Capricorn'}

question = input("Type 'height', 'favorite author' or 'sign' to find out about me.")
if question in kitch:
    answer = kitch[question]
    print(answer)


artists_songs = {"Jay-Z" : {"99 Problems", "Dirt Off Your Shoulder"}, "Pink Floyd": {"Another Brick in the Wall, PT II",
                                                                                  "Money"}}
print(artists_songs["Jay-Z"])
