import csv

with open("business_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "business_name",
        "category",
        "city",
        "address",
        "phone",
        "source"
    ])

    for i in range(1, 501):
        writer.writerow([
            f"Business {i}",
            "Restaurant" if i % 2 == 0 else "Hospital",
            "Delhi" if i % 3 == 0 else "Mumbai",
            f"Address {i}",
            f"900000{i:04d}",
            "Google" if i % 2 == 0 else "Justdial"
        ])

print("500 records generated successfully!")