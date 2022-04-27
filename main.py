"""main.py"""

from etl import dbload

def main():
    """Main function"""
    dbload.create_tables()
    dbload.clean_tables()
    dbload.load_data()

if __name__ == '__main__':
    main()
