import csv
# with open("user.csv","r") as f:
#     # reader = csv.DictReader(f)
#     reader = csv.reader(f)
#     for user in reader:
#         # print(user['username'],user['email'])
#         print(user[0])
#         print(user[1])
#

with open("user.csv","r") as f:
    # reader = csv.DictReader(f)
    reader = csv.reader(f)
    for user in reader:
        # print(user['username'],user['email'])
        username = user[0]
        password = user[1]