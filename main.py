import argparse
import csv
import random


def user():
    start = int(input("Enter a number\n"))
    one(start)


def rand():
    start = []

    # Ensure non-repeating digits
    while len(set(start)) < 2:
        start = []
        for _ in range(4):
            start.append(str(random.randint(0, 9)))

    one(int("".join(start)))


def one(start):
    if start < 0 or start > 9999:
        raise ValueError(f'{start} is not between 0 and 10000')

    start = [i for i in str(start)]
    while len(start) != 4:
        start.insert(0, '0')

    count = 0
    diff = 0
    current = start  # Retains original start
    print(f'Starting at:\n{int("".join(start))}')
    while diff != 6174:
        high = [i for i in reversed(sorted(current))]
        low = sorted(current)
        high_int = int("".join(high))
        low_int = int("".join(low))

        diff = high_int - low_int
        current = [str(i) for i in str(diff)]

        # Append leading 0s if necessary
        while len(current) != 4:
            current.insert(0, '0')

        if len(set(start)) < 2:
            break

        count += 1
        print('\t' * count, f'{high_int} - {low_int} = {diff}')

    if diff != 6174:
        print('Unsolvable')
    else:
        print(f'Total Iterations: {count}')


def allNumbers():
    results = {}
    for num in range(0, 10000):
        start = [i for i in str(num)]
        while len(start) != 4:
            start.insert(0, '0')

        # Ensure non-repeating digits
        if len(set(start)) < 2:
            results[num] = 'Repeating'
            continue

        count = 0
        diff = 0
        current = start  # Retains original start
        while diff != 6174:
            high = [i for i in reversed(sorted(current))]
            low = sorted(current)
            high_int = int("".join(high))
            low_int = int("".join(low))

            diff = high_int-low_int
            current = [str(i) for i in str(diff)]

            # Append leading 0s if necessary
            while len(current) != 4:
                current.insert(0, '0')

            if len(set(start)) < 2:
                break

            count += 1

        if diff != 6174:
            results[num] = 'Unsolvable'
        else:
            results[num] = count

    with open('Results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for k, v in results.items():
            writer.writerow([k, v])

    print('Done!')


def main(**kwargs):
    if kwargs.get('all'):
        allNumbers()
    elif kwargs.get('num'):
        one(kwargs.get('num'))
    elif kwargs.get('input'):
        user()
    else:
        rand()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()

    group.add_argument('--all', '-a', action='store_true')
    group.add_argument('--input', '-i', action='store_true')
    group.add_argument('--num', '-n', type=int)

    main(**vars(parser.parse_args()))
