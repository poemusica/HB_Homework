def main():

    sales_data = {}

    f = open("sales_report.csv")
    for line in f:
        line = line.rstrip()
        entries = line.split(",")
        salesperson = entries[0]
        melons = int(entries[2])

        if salesperson in sales_data:
            sales_data[salesperson] += 1
        else:
            sales_data[salesperson] = 1


    for key in sorted(sales_data):
        print "%s sold %d melons" % (key, sales_data[key])


if __name__ == "__main__":
    main()