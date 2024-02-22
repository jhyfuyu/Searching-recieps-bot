import requests
import random
from typing import List, Any

URL_EDAMAM = 'https://api.edamam.com/search'
URL_THE_MEAL = 'https://www.themealdb.com/api/json/v1/1/filter.php?a='


def get_ingredients(req: str) -> Any:
    """ Поиск рецепта в API Edamam"""
    params = {
        'q': req,
        'app_id': 'efaca7f3',
        'app_key': '2a6559b4ab73ad7b243373ef1409346d',
    }
    response = requests.get(url_edamam, params=params)
    final_response_data: List = list()
    images_urls: List[str] = list()

    if response.status_code == 200:
        data = response.json()
        hits = data['hits']
        if hits:
            for i, hit in enumerate(hits[:3]):
                recipe = hit['recipe']
                images_urls.append(recipe['image'])
                ingridients = recipe['ingredientLines']
                label = recipe['label']
                final_response_data.append(f'{label}\nIngridients: {ingridients}\n')          
    return [final_response_data, images_urls[0]]


def get_random_meal(cuisine: str) -> str:
    """ Рандомное блюдо запрашиваемой кухни"""
    all_data_cuisine = requests.get(f'{url_the_meal}{cuisine}')
    data = (all_data_cuisine.json())['meals']
    meal_name = random.choice(data)['strMeal']
    return meal_name
