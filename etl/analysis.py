"""Make simple data analysis"""

import sqlite3

con = sqlite3.connect('data/etl.db')
cur = con.cursor()


def top_artist():
    """Select artist with most listenings"""
    cur.execute("SELECT artist_name, sum(listen_count) " \
                "FROM tracks INNER JOIN " \
                "(SELECT track_id, count(*) as listen_count " \
                "FROM listenings GROUP BY track_id) USING(track_id) " \
                "GROUP BY artist_name " \
                "ORDER BY sum(listen_count) DESC LIMIT 1;")
    return cur.fetchone()


def top_tracks():
    """Select 5 most popular tracks"""
    cur.execute("SELECT title FROM tracks INNER JOIN " \
                "(SELECT track_id, count(*) as listen_count " \
                "FROM listenings GROUP BY track_id) USING(track_id) " \
                "ORDER BY listen_count DESC LIMIT 5;")
    return cur.fetchall()
