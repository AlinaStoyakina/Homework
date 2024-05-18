def bank(X, Y):
    for year in range(1, Y+1):
        count = X + (X/10)
        X = count
    print(round(count, 4))
bank(5000, 10)