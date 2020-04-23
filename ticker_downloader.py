import urllib.request, urllib.error, urllib.parse

import numpy as np

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

download = False


for j in range(0,len(letters)):
    letter = letters[j]

    if download == True:
        url = "http://eoddata.com/stocklist/NYSE/" + letter +".htm"

        response = urllib.request.urlopen(url)
        webContent = response.read()

        f = open("ticker_html_pages\\" +letter +'.html', 'wb')
        f.write(webContent)
        f.close

    else:
        f = open("ticker_html_pages\\" +letter +'.html', 'rb')
        webContent = f.read()
        f.close

    table = str(webContent).split("ctl00_cph1_divSymbols")
    table = table[1]
    table = table.split("</div>")
    table = table[0]
    table = table.split("<tr ")
    table = table[1:]

    ticker_list = [""]*len(table)
    name_list = [""]*len(table)
    for i in range(0, len(table)):
            row = table[i]
            row = row.split("Chart for NYSE")
            ticker = row[1]
            ticker = ticker.split("\"")

            ticker_list[i] = ticker[0]
            ticker_list[i] = ticker_list[i][1:]

            name = ticker[1]
            name = name.split("<td>")
            name = name[1]
            name = name.split("</td>")
            name_list[i] = name[0]

            if j ==0 and i==0:
                f= open("data.txt","w")
            else:
                f= open("data.txt","a+")
            f.write(ticker_list[i] + ", " + name_list[i] + "\r\n")
            f.close

#    data = np.column_stack((ticker_list, name_list))
