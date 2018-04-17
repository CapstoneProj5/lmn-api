
import datetime

from songkick_api.sk_venue import Venue
from songkick_api.sk_artist import Artist


class Event(object):

    def __init__(

            self,
            sk_id:     int,
            date:      datetime.date,
            artist:    Artist,
            artist_id: int,
            venue:     Venue,
            venue_id:  int,
            city:      str,
            state:     str):

            self.sk_id = sk_id
            self.date = date
            self.artist = artist
            self.artist_id = artist_id
            self.venue = venue
            self.venue_id = venue_id
            self.city = city
            self.state = state

    def __str__(self):

        return "      \n" \
           "ID: {}    \n" \
           "Date: {}  \n" \
           "Artist: {}\n" \
           "Venue: {} \n".format(

            str(self.sk_id),
            self.date,
            self.artist.displayName,
            self.venue.displayName)

    def __dict__(self):

        return {
            'sk_id':     self.sk_id,
            'date':      self.date,
            'artist':    self.artist,
            'artist_id': self.artist_id,
            'venue':     self.venue,
            'venue_id':  self.venue_id,
            'city':      self.city,
            'state':     self.state}
