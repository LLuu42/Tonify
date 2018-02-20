import unirest
import operator

def top_emotion(sentiment_values):
    emotion = max(sentiment_values.iteritems(), key=operator.itemgetter(1))[0]
    return emotion

def artist_seed(emotion):
    seed = "3wyVrVrFCkukjdVIdirGVY"
    if emotion == "anger":
        seed = "7dGJo4pcD2V6oG8kP0tJRR"
    elif emotion == "fear":
        seed = "26bcq2nyj5GB7uRr558iQg"
    elif emotion == "joy":
        seed = "5YGY8feqx7naU7z4HrwZM6"
    elif emotion == "sadness":
        seed = "3TVXtAsR1Inumwj472S9r4"
    return seed


def song_seed(emotion):
    seed = "43ZyHQITOjhciSUUNPVRHc"
    if emotion == "anger":
        seed = "6PPRKnwToRK9GjTCV03vlG"
    elif emotion == "fear":
        seed = "2KH16WveTQWT6KOG9Rg6e2"
    elif emotion == "joy":
        seed = "5Q0Nhxo0l2bP3pNjpGJwV1"
    elif emotion == "sadness":
        seed = "2z3htsNRuhDN923ITatc56"
    return seed



def generatePlaylist(sentiment_values, auth_token):
    valence = sentiment_values["joy"]
    top = top_emotion(sentiment_values)
    seed_artist = artist_seed(top_emotion)
    seed_song = song_seed(top_emotion)

    url = "https://api.spotify.com/v1/recommendations"
    params = {"min_energy" : valence,"max_mode" : "5", "market" : "US", "min_danceability" : valence, "seed_tracks" : seed_song , "seed_artists" : seed_artist , "target_popularity" : "30", "min_valence" : valence, }
    headers = {"Authorization": "Bearer " + auth_token}

    res = unirest.get(url, headers=headers, params=params)
    print res.body
    return res.body
