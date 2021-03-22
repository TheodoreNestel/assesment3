"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relation, relationship

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = 'playlist'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable = False)
    desc = db.Column(db.Text,)

    songs = db.relationship('Song',secondary='playlistsong',backref='playlist')
    #so to clarify how this works it want secondary to br the bridge. Itll hook up playlist to song 
    #based on the foreign key contraints of playlistsong 

    #need to add a relationship here 
    
   
    #from my understanding this lets me access all my tables using . calls from playlist objects 

    


class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE

    __tablename__ = 'song'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text,nullable = False)
    artist = db.Column(db.Text,nullable = False)

    


    




class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = 'playlistsong'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))
    
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'))

    
    #we made both foreign keys this table's primary key to prevent being able to add songs 
    


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
