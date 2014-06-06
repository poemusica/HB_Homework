
def calculate_revenue(melon_tallies, melon_prices):
    total_revenue = 0
    txt_descriptions = []
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        msg = "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)
        txt_descriptions.append(msg)
    return txt_descriptions

def count_melons(fileobj):
    melon_tallies = {"Musk": 0, "Hybrid": 0, "Watermelon": 0, "Winter": 0}

    for line in fileobj:
        data = line.split(",")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count
    return melon_tallies

def count_sales(fileobj):
    sales = [0, 0]

    for line in fileobj:
        data = line.split(",")
        if data[1] == "0":
            sales[0] += float(data[3])
        else:
            sales[1] += float(data[3])
    
    person_msg =  "Salespeople generated %0.2f in revenue." % sales[1]
    internet_msg =  "Internet sales generated %0.2f in revenue." % sales[0]
    txt_descriptions = [person_msg, internet_msg]

    return sales, txt_descriptions


def eval_sales(sales_tallies):
    if sales_tallies[1] > sales_tallies[0]:
        return "Guess there's some value to those salespeople after all."
    else:
        return "Time to fire the sales team! Online sales rule all!"


def pretty_print_summaries(revenue_summaries, sales_summaries, sales_evaluation):
    print '*' * 40
    for msg in revenue_summaries:
        print msg
    print '*' * 40
    for msg in sales_summaries:
        print msg
    print sales_evaluation
    print '*' * 40    


def summarize_revenue_data(filename):
    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }

    f = open(filename)

    melon_tallies = count_melons(f)
    revenue_summaries = calculate_revenue(melon_tallies, melon_prices)

    f.close()

    return revenue_summaries


def summarize_sales_data(filename):
    f = open(filename)

    sales_tallies, sales_summaries = count_sales(f)

    sales_evaluation = eval_sales(sales_tallies)

    f.close()

    return sales_summaries, sales_evaluation


def main():

    orders = "orders_by_type.csv"
    revenue_summaries = summarize_revenue_data(orders)

    sales = "orders_with_sales.csv"
    sales_summaries, sales_evaluation = summarize_sales_data(sales)

    pretty_print_summaries(revenue_summaries, sales_summaries, sales_evaluation)



# count up the differerent types of melons that were sold.
# calculated revenue from those melon tallies.
# separated online sales from phone sales.
# produce a fancy report to summarize the information for our CEO

if __name__ == "__main__":
    main()