numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:

    if num > 500:
        break

    if num > 150:
        continue

    if num % 5 == 0:
        print(num)