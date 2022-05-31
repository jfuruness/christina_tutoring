import csv

with open("task2_1.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "year"])
    writer.writeheader()
    for i in range(100):
        writer.writerow({"name": f"name{i}", "year": "21"})

with open("task2_2.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "disease"])
    writer.writeheader()
    for i in range(100):
        writer.writerow({"name": f"name{i}", "disease": f"disease{i}"})
