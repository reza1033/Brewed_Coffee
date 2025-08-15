while True:
    quantity_input = input("Choose your coffee quantity between 14 and 17 grams: (or type exit to quit): ")
    if quantity_input.lower() == "exit":
        print("Bye")
        break
    try:
        quantity = float(quantity_input)
        num = quantity / 10
        FS = 30 * num
        SS = 70 * num
        TS = 20 * num
        TCE = FS + SS + TS
        print(f"total time: 2m & 30s\ttemp:89C\nfirst step: {FS}ML\n1 minute break \nsecond step: {SS}ML\n"
              f"1 minute break \nthird step: {TS}ML\n30second break \nTotal coffee extract: {TCE}ML")
    except ValueError:
        print("enter number or exit")