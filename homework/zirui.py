def juice_cost(juice, container, material, supermarket):
    cost = 0
    if container == "ball":
        if material == "plastic":
            cost += 4*3.14*6**2 * 0.08
            if juice == "orange":
                cost += 4/3*3.14*6**3 * 0.14
            elif juice == "apple":
                cost += 4/3*3.14*6**3 * 0.11
        elif material == "metal":
            cost += 4*3.14*6**2 * 0.18
            if juice == "orange":
                cost += 4/3*3.14*6**3 * 0.14
            elif juice == "apple":
                cost += 4/3*3.14*6**3 * 0.11
    elif container == "cube":
        if material == "plastic":
            cost += 10**2*6 * 0.08
            if juice == "orange":
                cost += 10**3 * 0.14
            elif juice == "apple":
                cost += 10**3 * 0.11
        elif material == "metal":
            cost += 10**2*6 * 0.18
            if juice == "orange":
                cost += 10**3 * 0.14
            elif juice == "apple":
                cost += 10**3 * 0.11
    cost = cost * 1.3
    if supermarket == "ntuc":
        cost = cost * 1.1
    elif supermarket == "cold storage":
        cost = cost * 1.15
    cost = cost / 100
    print(f"Price of {juice} juice, container shape {container}, material {material}, sold at {supermarket}: ${round(cost, 2)}")


juices = ["apple", "orange"]
containers = ["cube", "ball"]
materials = ["plastic", "metal"]
supermarkets = ["ntuc", "cold storage"]
surface_area = 0
volume = 0

for i in range(2):
    for j in range(2):
        for k in range(2):
            for m in range(2):
                juice_cost(juices[i], containers[j], materials[k], supermarkets[m])