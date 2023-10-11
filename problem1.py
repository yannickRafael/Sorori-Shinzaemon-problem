def nr_of_grains():
    total = 1
    amounts = []
    amounts.append(total)
    
    for i in range(0, 100):
        total = 2 * total
        amounts.append(total)

    return amounts    




amounts = nr_of_grains()

print(f'the amount of grains after 100 days is {amounts[-1]}')