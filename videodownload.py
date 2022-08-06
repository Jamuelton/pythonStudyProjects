import webbrowser 

url =input('Enter your Youtube Url: ')

url = url[:12] + 'ss' + url[12:]

webbrowser.open(url)