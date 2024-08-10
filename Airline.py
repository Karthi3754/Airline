import sqlite3
from datetime import datetime

conn = sqlite3.connect('airline_db.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS flights
(id INTEGER PRIMARY KEY,
flight_number TEXT,
destination TEXT,
departure_time DATETIME,
available_seats INTEGER)''')

flights = [
('AA101', 'New York', datetime.strptime('2024-05-20 10:00:00', '%Y-
%m-%d %H:%M:%S'), 150),
('BA202', 'London', datetime.strptime('2024-05-21 12:00:00', '%Y-%m-
%d %H:%M:%S'), 200),
('CA303', 'Paris', datetime.strptime('2024-05-22 14:00:00', '%Y-%m-%d 
%H:%M:%S'), 180),
]

c.executemany("INSERT INTO flights VALUES (NULL, ?, ?, ?, ?)", flights)
conn.commit()

def sort_by_available_seats(ascending=True):
 query = "SELECT * FROM flights ORDER BY available_seats ASC" if ascending else "SELECT * FROM flights ORDER BY available_seats DESC"
 c.execute(query)
 rows = c.fetchall()
 for row in rows:
  print(row)

def sort_by_departure_time(ascending=True):
 query = "SELECT * FROM flights ORDER BY departure_time ASC" if ascending else "SELECT * FROM flights ORDER BY departure_time DESC"
 c.execute(query)
 rows = c.fetchall()
 for row in rows:
  print(row)

print("Flights sorted by available seats (ascending):")
sort_by_available_seats(ascending=True)
print("\n")
print("Flights sorted by departure time (ascending):")
sort_by_departure_time(ascending=True)
conn.close()