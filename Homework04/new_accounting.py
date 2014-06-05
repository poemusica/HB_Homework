
def underpaid(cost, parsed):
    num_under = 0
    for data_list in parsed:
        customer_id, customer, qty, paid = data_list
        expected = qty * cost
        if expected > paid:
            num_under += 1
            shortage = expected - paid
            result = "%s (id %d) underpaid by $%.2f. expected $%.2f, paid $%.2f" % (customer, customer_id, shortage, expected, paid)
            print result.upper()
    return ("\n%d customers underpaid\n" % num_under).upper()


def parse_file(my_file):
    parsed = []
    for line in my_file:
        data = line.split(',')
        customer_id = int(data[0])
        customer = data[1]
        qty = int(data[2])
        paid = float(data[3])
        parsed.append([customer_id, customer, qty, paid])
    return parsed


def main():
    my_file = open("customer_orders.csv")

    cost = 1

    p = parse_file(my_file)

    print underpaid(cost, p)

    my_file.close()


if __name__ == "__main__":
    main()