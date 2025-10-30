li = input("Enter elements separated by space: ").split()

for li in li:
    if int(li) < 0:
        print("List:", li)