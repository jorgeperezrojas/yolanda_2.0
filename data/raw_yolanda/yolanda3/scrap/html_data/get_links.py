import os
import bs4

textos = []

directory = '../html_menu/'
pref = 'https://www.lacuarta.com/horoscopo/noticia/horoscopo'
links = set()

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        with open(os.path.join(directory, filename)) as infile:
            html = bs4.BeautifulSoup(infile,'lxml')
            for tag in html.find_all('a'):
                link = tag['href']
                if link and link.startswith(pref):
                    links.add(link)

with open('wget.sh','w') as script_file:
    for link in links:
        out_name_data = link.split('/')
        out_name = out_name_data[-3] + '-' + out_name_data[-2]
        command = f'wget {link} -O {out_name}.html\n'
        script_file.write(command)