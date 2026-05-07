#user input
target = float(input("Enter total sales target: "))
total = 0
#enhancement
while target <= 0:
print("invalid target")
target = float(input("Enter total target: "))
#loop
for day in range(1,6):
sales = float(input(f"enter day {day} sales: "))
while sales <= 0:
print("Invalid sales.")
sales = float(input(f"Enter day {day} sales: "))
#sales calculation
total += sales
percent = (total / target) * 100
print("Cumulative sales:", total, "(", percent, "%)")
