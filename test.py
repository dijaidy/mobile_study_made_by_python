import json
import csv

with open("information\교재_카테고리_csv.csv", "r") as csv_in_file:
    filereader = csv.reader(csv_in_file)
    header = next(filereader)
    print(header)
    depth1_dict = {}
    with open("information\교재_카테고리_dict.json", "w", encoding="UTF-8") as out_file:
        for row in filereader:
            if row[5] == "":
                depth1_dict[row[4]] = {"CID": row[0], "item": {}}
            else:
                depth1_dict[row[4]]["item"][row[5]] = row[0]
        print(depth1_dict)
        json.dump(depth1_dict, out_file, ensure_ascii=False)
