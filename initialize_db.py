import sqlite3

def initialize_db():
    with sqlite3.connect("ClassroomBooking.db") as db:
        cursor = db.cursor()

        # TODO: get a database structure
        cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
SchoolID text PRIMARY KEY,
Name text NOT NULL)
""")

if __name__ == "__main__":
    initialize_db()