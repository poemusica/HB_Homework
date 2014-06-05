
def underpaid(cost, parsed):
    bad_customers = []
    num_under = 0
    for data_list in parsed:
        customer_id, customer, qty, paid = data_list
        expected = qty * cost
        if expected > paid:
            num_under += 1
            shortage = expected - paid
            result = "%s (id %d) underpaid by $%.2f. expected $%.2f, paid $%.2f" % (customer, customer_id, shortage, expected, paid)
            result = result.upper()
            bad_customers.append(result)
    total = ("\n%d customers underpaid\n" % num_under).upper() 
    return total, bad_customers


def parse_file(my_file):
    parsed = []
    for line in my_file:
        line = line.rstrip()
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

    msg, bad_list = underpaid(cost, p)

    print msg
    print '\n'

    for b in bad_list:
        print b


    my_file.close()


if __name__ == "__main__":
    main()