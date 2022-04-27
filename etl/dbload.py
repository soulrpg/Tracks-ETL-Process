"""Create SQLite database and load data to it"""

import sqlite3

con = sqlite3.connect('data/etl.db')
cur = con.cursor()

TRACKS_FILEPATH = "data/unique_tracks.txt"
LISTENINGS_FILEPATH = "data/triplets_sample_20p.txt"


def create_tables():
    """Create tracks and listenings tables"""
    cur.execute("CREATE TABLE IF NOT EXISTS tracks (id TEXT PRIMARY KEY, "
                "track_id TEXT NOT NULL, artist_name TEXT NOT NULL, "
                "title TEXT NOT NULL);")
    cur.execute("CREATE TABLE IF NOT EXISTS listenings "
                "(user_id TEXT NOT NULL, track_id TEXT NOT NULL, "
                "listen_date INTEGER NOT NULL);")
    print("Tables created.")


def clean_tables():
    """Remove all records from tables"""
    cur.execute("DELETE FROM tracks;")
    cur.execute("DELETE FROM listenings;")
    print("Tables cleaned.")


def load_data():
    """Load data from txt files"""
    try:
        with open(TRACKS_FILEPATH, mode="r", encoding="ISO-8859-1") as tracks:
            for line in tracks:
                data = line.split("<SEP>")
                cur.execute("INSERT INTO tracks VALUES(?, ?, ?, ?);", \
                    (data[0], data[1], data[2], data[3]))
        with open(LISTENINGS_FILEPATH, mode="r", encoding="ISO-8859-1") \
            as listenings:
            for line in listenings:
                data = line.split("<SEP>")
                cur.execute("INSERT INTO listenings VALUES(?, ?, ?);", \
                    (data[0], data[1], data[2]))
        con.commit()
    except FileNotFoundError:
        print("Data loading failed. Place input files into data/ directory.")
    print("Data loaded.")
    con.close()
