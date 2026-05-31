print("Program Started")

import pandas as pd
from database import get_connection

df = pd.read_csv("business_data.csv")
print("CSV Loaded:", len(df))

print("Before DB Connection")

conn = get_connection()

print("After DB Connection")

cursor = conn.cursor()

print("Connected to MySQL")

count = 0

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO listing_master
        (business_name, category, city, address, phone, source)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        row["business_name"],
        row["category"],
        row["city"],
        row["address"],
        row["phone"],
        row["source"]
    ))
    count += 1

print("Rows Processed:", count)

conn.commit()

print("500 records inserted successfully!")

cursor.close()
conn.close()

input("Press Enter to exit...")