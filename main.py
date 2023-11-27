import random


def main():
    start = []

    # Ensure non-repeating digits
    while len(set(start)) < 2:
        start = []
        for _ in range(4):
            start.append(str(random.randint(0, 9)))

    count = 0
    diff = 0
    tabs = 1
    current = start  # Retains original start
    print(f'Starting at:\n{int("".join(start))}')
    while diff != 6174:
        high = [i for i in reversed(sorted(current))]
        low = sorted(current)
        high_int = int("".join(high))
        low_int = int("".join(low))

        diff = high_int-low_int
        current = [str(i) for i in str(diff)]
        count += 1
        tabs = count
        print('\t' * tabs, diff)

    print(f'Total Iterations: {count}')


if __name__ == '__main__':
    main()
