import re
import os
import bs4

textos = []

directory = 'html_data'

with open('raw_data.txt', 'w') as outfiledata, open('raw_signo.txt','w') as outfilesigno:
    for filename in os.listdir(directory):
        if filename.endswith('html'):

            # abre y parsea el archivo
            with open(os.path.join(directory, filename)) as infile:
                html = bs4.BeautifulSoup(infile,'lxml')

            for tag in html.find_all('h6'):
                signo = tag.text.split()[0]
                texto = tag.findNext('p').text.strip()
                if texto == '':
                    texto = tag.findNext('p').findNext('p').text.strip()
                texto = re.sub('\n+',' ',texto)
                outfiledata.write(texto + '\n')
                outfilesigno.write(signo + '\n')
