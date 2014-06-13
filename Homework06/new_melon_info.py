"""
melon_info.py - Prints out all the melons in our inventory

"""

from new_melons import melon_data


def print_data(data_dict):

	for name, info in data_dict.iteritems():
		price, seedless = info

		hashasnot = 'have'
		if seedless:
			hashasnot = "do not have"

		print "%ss %s seeds and are $%0.2f" % ( name, hashasnot, price)


def main ():
	print_data(melon_data)

if __name__ == '__main__':
	main()