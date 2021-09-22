import requests
import bs4
import csv
base_url = 'https://www.iplt20.com/teams/men'
res = requests.get(base_url)
soup = bs4.BeautifulSoup(res.text,'lxml')

product_card = soup.select('.card__details')
product_title = soup.select('.card__title')
product_subtitle = soup.select('.card__subtitle')
product_year = soup.select('.team-card__wins')
ipl_data_dict = {}
index =0
for num in range(len(product_title)):
    temp_dict = {}
    title =product_title[num].getText()
    temp_dict['venue'] =product_subtitle[num].getText().strip()
    if product_card[num].find('div'):        
        if index < len(product_year):
            temp_dict['winning_year']  = product_year[index].getText().strip()
            index+=1
    else:
        temp_dict['winning_year']  =  "Never wins a Trophy"        
    ipl_data_dict[f'{title}'] =temp_dict
     
print(ipl_data_dict)
file_name = 'ipl_team_csv.csv'
fields = ['title', 'venue', 'winning_year']
def dict_to_csv():
    with open(file_name,'w') as csv_file:
            csv_writer_ = csv.DictWriter(csv_file,fields)
            csv_writer_.writeheader()
            for key in ipl_data_dict:
                csv_writer_.writerow({field: ipl_data_dict[key].get(field) or key for field in fields})

dict_to_csv() #function called
