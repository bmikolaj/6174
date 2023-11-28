import csv


def main():
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
        tabs = 0
        current = start  # Retains original start
        #print(f'Starting at:\n{int("".join(start))}')
        while diff != 6174:
            high = [i for i in reversed(sorted(current))]
            low = sorted(current)
            high_int = int("".join(high))
            low_int = int("".join(low))

            diff = high_int-low_int
            if diff < 1000:
                break
            current = [str(i) for i in str(diff)]
            count += 1
            tabs = count
            #print('\t' * tabs, f'{high_int}-{low_int}={diff}')

        if diff != 6174:
            results[num] = 'Unsolvable'
        else:
            results[num] = count
        #print(f'Total Iterations: {count}')

    with open('Results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for k, v in results.items():
            writer.writerow([k, v])


if __name__ == '__main__':
    main()
