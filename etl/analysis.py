"""Make simple data analysis"""

import sqlite3

con = sqlite3.connect('data/etl.db')
cur = con.cursor()


def top_artist():
    """Select artist with most listenings"""
    cur.execute("SELECT artist_name FROM tracks INNER JOIN listenings USING(track_id) GROUP BY artist_name ORDER BY count(id)") 
    return cur.fetchone()


def top_tracks():
    """Select 5 most popular tracks"""
    cur.execute("SELECT title FROM tracks INNER JOIN listenings USING(track_id) GROUP BY artist_name ORDER BY count(id) LIMIT 5") 
    return cur.fetchall()
