import webget
file_url = 'https://raw.githubusercontent.com/DaMexicanJustice/frantic_midnight/master/data%20sets/vgsales.csv'
file_name = 'sales.csv'
csv_file = webget.download(file_url, file_name)

csv_file
