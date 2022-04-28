"""main.py"""

import time

from etl import dbload, analysis


def main():
    """Main function"""
    start_time = time.time()
    dbload.create_tables()
    dbload.clean_tables()
    dbload.load_data()
    print("Top artist:", analysis.top_artist()[0])
    print("Top tracks:")
    top_tracks = analysis.top_tracks()
    for i, track in enumerate(top_tracks):
        print(i + 1, track[0])
    end_time = time.time()
    print("Time elapsed:", end_time - start_time)


if __name__ == '__main__':
    main()
