import csv

with open("task1.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "year"])
    writer.writeheader()
    for i in range(100):
        writer.writerow({"name": f"name{i}", "year": "21"})
