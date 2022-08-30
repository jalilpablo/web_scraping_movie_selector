import random
from urllib import response
import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4

url='https://www.imdb.com/chart/top'

def main():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html,'html.parser')
    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    rating_tags = soup.select('td.posterColumn span[name=ir]')
    
    def get_year(movie_tag):      #get the movie year function
       moviesplit = movie_tag.text.split()
       year = moviesplit[-1] #year is always the last element
       return year


    years = [get_year(tag) for tag in movietags]
    actors_list = [tag['title'] for tag in inner_movietags]
    titles = [tag.text for tag in inner_movietags]
    ratings = [float(tag['data-value']) for tag in rating_tags]

    n_movies = len(titles) #number of movies

    while(True):
        index = random.randrange(0,n_movies)
        break

    print(f'The random movie is {titles[index]} {years[index]}, rating: {ratings[index]}, starring: {actors_list[index]}')
    
    user_input = input('Tipe "another" if you want another movie ')
    if user_input == 'another':
        main()


        
if __name__ == '__main__':
    main()