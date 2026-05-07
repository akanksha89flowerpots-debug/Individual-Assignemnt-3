

fastest_time = 999999
fastest_route = 0
route = 1

while True:
    distance = float(input(f"Enter route {route} distance (miles): "))
    speed = float(input(f"Enter route {route} speed (miles/hour): "))

    # validate inputs
    if distance <= 0 or speed <= 0:
        print("Invalid input. Try again.\n")
        continue

    time = (distance / speed) * 60
    print("Time:", round(time, 2), "minutes\n")

    if time < fastest_time:
        fastest_time = time
        fastest_route = route

    more = input("More routes (y/n)?: ")
    if more != "y":
        break

    route += 1

print("\nRoute", fastest_route, "is fastest;", round(fastest_time, 2), "minutes")
