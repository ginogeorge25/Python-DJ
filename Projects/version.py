# import platform

# print (platform.python_version())


import pandas as pd
import urllib.request

# path to your csv file with the endpoint coordinates
coordinates = pd.read_csv('C:\DJ\Data gallery\De-Identified OP Utilization Locations\opul.csv')

# graphhopper API call building blocks. Check Graphhopper documentation how to modify these.
urlStart = 'http://localhost:8989/route?'
point = 'point='
urlEnd = '&type=gpx&instructions=false&vehicle=car'
separator = '%2C'

# The starting point for each query (lat, lon). Use e.g. QGIS to change these.
startY = '42.504851'
startX = '-71.195655'



# Make the API calls for each row in you CSV file and save the results to individual .gpx files.
for index, row in coordinates.iterrows():
    # print (row)
    # print("--------------")
    req = urlStart + point + startY + separator + startX + '&' + point + str(row['provLatitude']) + separator + str(row['provLongitude']) + urlEnd #fails here
    # print (req)

    resp = urllib.request.urlopen(req)
    gpxData = str(resp.read(), 'utf-8')
    fileName = 'opul' + str(index)
    saveFile = open('C:\DJ\Data gallery\graphhopper-web-0.9.0-bin\gpx_files\{0}.gpx'.format(fileName), 'w')
    print('processed index ' + str(index))
    saveFile.write(gpxData)
    saveFile.close()
