# Created by Shekhar Jha
# Tested in Python 2.7.13

import urllib
import re

symbols_file = open("symbols.txt")
symbols_list = symbols_file.read()
new_symbols_list = symbols_list.split(";")
new_symbols_list_sym = new_symbols_list[0].split(",")
new_symbols_list_name = new_symbols_list[1].split(",")

i = 0

print ("Stock prices of Fortune 50 comapnies listed at NASDAQ Stock Exchange")
print ("--------------------------------------------------------------------")

while i < len(new_symbols_list_sym):

    if new_symbols_list_sym[i] == '--':
        print ("Stock price of " + new_symbols_list_name[i] + " [----]")
    else:
        url = "http://www.nasdaq.com/symbol/" + new_symbols_list_sym[i]
        htmlfile = urllib.urlopen(url)
        htmltext = htmlfile.read().decode('utf-8')
        regex = '<div id="qwidget_lastsale" class="qwidget-dollar">(.+)*</div>'
        pattern = re.compile(regex)
        price = re.findall(pattern, htmltext)
        print ("Stock price of " + new_symbols_list_name[i] + " ",price)

    i+=1
