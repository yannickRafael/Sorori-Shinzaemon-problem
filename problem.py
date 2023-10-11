def nr_of_grains(days):
    total = 1
    amounts = []
    amounts.append(total)
    
    for i in range(0, days):
        total = 2 * total
        amounts.append(total)

    return amounts    


days = int(input('Insert the number of days: '))

amounts = nr_of_grains(days)

print(f'the amount of grains after {days} days is {amounts[-1]}')