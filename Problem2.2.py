def generate_fib(max_value):
    series = [1, 1]
    while True:
        next_last = series[-1] + series[-2]
        if next_last > max_value:
            break
        series.append(next_last)
    return series

series = generate_fib(4000000)
evens = [series[x] for x in range(2, len(series), 3)]
print(sum(evens))
