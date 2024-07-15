with open("hr_system.txt") as txtfile:
    for line in txtfile:
        item = line.split()
        name = item[0]
        id = item[1]
        title = item[2]
        salary = item[3]
        print(f"{name} (ID: {id}), {title} - ${salary}")