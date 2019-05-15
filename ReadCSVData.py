from urllib import request

csvData = 'http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv'


def downloadCsvData(csv_url):
    # Take data from the url and read it
    response = request.urlopen(csv_url)
    csv = response.read()
    csvString = str(csv)
    # Separate the data into lines
    lines = csvString.split("\\n")
    # Create a destination file
    destUrl = r'calendar.csv'
    fx = open(destUrl, "w")
    for line in lines:
        # Write everything on its own line in the destination file
        fx.write(line + "\n")
    fx.close()


downloadCsvData(csvData)
