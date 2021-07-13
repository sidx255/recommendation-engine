# obtain titles
import requests
from bs4 import BeautifulSoup
import csv
'''
url = "https://www.google.com"

file1 = open('www.bajajfinserv.in_internal_links.txt', 'r')

file2 = open("www.bajajfinserv.in_internal_links.txt", "r")

list_of_lists = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_lists.append(line_list)

a_file.close()
 
# print(list_of_lists)

list2 = []
while True:
    url = file1.readline()
    if not url:
        break
    reqs = requests.get(url, timeout=10)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    
    metas = soup.find_all('meta') #Get Meta Description
    list2=[ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description' ]
'''
import urllib.request
from bs4 import BeautifulSoup

# here we have to pass url and path
# (where you want to save ur text file)
urllib.request.urlretrieve("https://www.geeksforgeeks.org/grep-command-in-unixlinux/?ref=leftbar-rightbar",
						"text_file.txt")

file = open("text_file.txt", "r")
contents = file.read()
soup = BeautifulSoup(contents, 'html.parser')

f = open("test1.txt", "w")

# traverse paragraphs from soup
for data in soup.find_all("p"):
	sum = data.get_text()
	f.writelines(sum)

f.close()
