FILES = ["um-deliveries-20140519.csv",
        "um-deliveries-20140520.csv", "um-deliveries-20140521.csv"]


def print_log_data(filename):
    fileobj = open(filename)
    word_list = []
    for line in fileobj:
        line = line.rstrip()
        words = line.split(',')
        word_list.append(words)
    format_data(word_list)
    fileobj.close()
    print "\n"
    return

def format_data(word_list):
    for data in word_list:
        melon, count, amount = data
        pretty_data = "Delivered %s %ss for a total of: $%s" % (count, melon, amount)
        print pretty_data.upper()

def main():
    for f in FILES:
        day = str(FILES.index(f) + 1)
        print "Day %s" % day
        print_log_data(f)

if __name__ == "__main__":
    main()