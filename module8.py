# import mysql.connector
#
# connection = mysql.connector.connect(
#     host="127.0.0.1",
#     port=3306,
#     database="flight_game",
#     user="root",
#     password="5769",
#     autocommit=True
# )

# icao = input("Enter ICAO code: ").upper()
#
# cursor = connection.cursor()
#
# sql = "SELECT name, municipality FROM airport WHERE ident = %s"
# cursor.execute(sql, (icao,))
#
# result = cursor.fetchone()
#
# if result:
#     print("Airport name:", result[0])
#     print("Location (town):", result[1])
# else:
#     print("Airport not found")
#
#
# #
# import mysql.connector
#
# # Connect to database
# connection = mysql.connector.connect(
#     host="127.0.0.1",
#     port=3306,
#     database="flight_game",
#     user="root",
#     password="5769",
#     autocommit=True
# )

# # Ask user for country code
# country = input("Enter area code (for example FI): ").upper()
#
# cursor = connection.cursor()
#
# # SQL query
# sql = """
# SELECT type, COUNT(*)
# FROM airport
# WHERE iso_country = %s
# GROUP BY type
# ORDER BY type
# """
#
# cursor.execute(sql, (country,))
# results = cursor.fetchall()
#
# # Print results
# if results:
#     for row in results:
#         print(f"{row[0]}: {row[1]} airports")
# else:
#     print("No airports found for this country.")
#
import mysql.connector
from geopy.distance import geodesic

# connect to database
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="5769",
    autocommit=True
)

cursor = connection.cursor()

# ask user for ICAO codes
icao1 = input("Enter first ICAO code: ").upper()
icao2 = input("Enter second ICAO code: ").upper()

# SQL query
sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"

# first airport
cursor.execute(sql, (icao1,))
result1 = cursor.fetchone()

# second airport
cursor.execute(sql, (icao2,))
result2 = cursor.fetchone()

if result1 and result2:
    coord1 = (result1[0], result1[1])
    coord2 = (result2[0], result2[1])

    distance = geodesic(coord1, coord2).kilometers

    print(f"Distance between airports: {distance:.2f} km")

else:
    print("One or both ICAO codes not found.")