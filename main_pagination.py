import requests
import json
from config import headers, cookies
import os
import math


# Отправляем запрос и собираем Ids товаров (с сайта м-видео listing запрос, копируем cURL(bush), на сайте
# https://curlconverter.com/#python конвертируем cURL запрос для Python, копируем)
def get_data():
    params = {
        # Id категории (здесь указана категория планшеты)
        'categoryId': '101',
        'offset': '0',
        # лимит товаров поступающих на страницу
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    # проверка если директория не существует, то создаем ее
    if not os.path.exists('data'):
        os.mkdir('data')

    # далее создадим сессию
    # s объект сессии
    s = requests.Session()

    # запрос с параметрами, печеньками и заголовками. Получаем Json
    response = s.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                     headers=headers).json()
    # print(response)

    # задаем перменную, чтобы узнать значение ключа total
    total_items = response.get('body').get('total')

    # пишем проверку и если все окей, то вычисляем кол-во страниц (помним, что лимит товаров на страницу = 24 шт.)
    if total_items is None:
        return '[!] Нет товаров :('

    # вычисляем кол-во страниц с помощью функции ceil (округление вверх)
    pages_count = math.ceil(total_items / 24)
    print(f'[INFO] Количество позиций: {total_items}, Количество страниц: {pages_count}')

    # создаем три словаря, которые булем наполнять данными
    # словарь с ID товаров
    products_ids = {}
    # словарь для товаров с детальным описанием
    products_description = {}
    # словарь для прайсов
    products_prices = {}

    # пишем цикл в котором будем пробегаться по всем полученным страницам, в той или иной категории товаров
    for i in range(pages_count):
        # делаем смещение которое с каждой итерацией будет кратно 24, т.к. отображается только 24 товара на 1 странице
        offset = f'{i * 24}'
        # вставляем параметры, используемые выше
        params = {
            # Id категории (здесь указана категория планшеты)
            'categoryId': '101',
            'offset': offset,
            # лимит товаров поступающих на страницу
            'limit': '24',
            'filterParams': [
                'WyJza2lka2EiLCIiLCJkYSJd',
                'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
            ],
            'doTranslit': 'true',
        }
        response = s.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                         headers=headers).json()

        # забираем список с айдишниками
        products_ids_list = response.get('body').get('products')
        # на каждой итерации будем поплнять созданный нами ранее словарь для id
        products_ids[i] = products_ids_list
        # формируем параметры для второго запроса



    # # сохраним ответ в Json
    # with open('1_products_ids.json', 'w') as file:
    #     json.dump(products_ids, file, indent=4, ensure_ascii=False)
    # # print(products_ids)
    #
    # # Отправляем запрос и собираем IDs товаров(с сайта м-видео list запрос, копируем cURL(bush), на сайте
    # # https://curlconverter.com/#python конвертируем cURL запрос для Python, копируем с json_data и запрос
    # # вместо скопированного списка из productIds вставляем нашу переменную products_ids, в ответе получаем json
    # json_data = {
    #     'productIds': products_ids,
    #     'mediaTypes': [
    #         'images',
    #     ],
    #     'category': True,
    #     'status': True,
    #     'brand': True,
    #     'propertyTypes': [
    #         'KEY',
    #     ],
    #     'propertiesConfig': {
    #         'propertiesPortionSize': 5,
    #     },
    #     'multioffer': False,
    # }
    #
    # # в ответе получаем json
    # response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
    #                          json=json_data).json()
    #
    # # сохраняем результат (здесь мы получили данные по первым 24 продуктам(планшетам)
    # with open('2_items.json', 'w') as file:
    #     json.dump(response, file, indent=4, ensure_ascii=False)
    #
    # # распечатаем длину списка
    # # print(len(response.get('body').get('products')))
    #
    #
    # # Cобираем цены скидки и бонусы на товар
    # # (с сайта м-видео prices запрос, копируем cURL(bush), на сайте
    # # https://curlconverter.com/#python конвертируем cURL запрос для Python, копируем с params и запрос
    #
    # # до params склеем список с Ids в строку с помощью метода join
    # products_ids_str = ','.join(products_ids)
    #
    # # подставляем строку products_ids_str в params
    # params = {
    #     'productIds': products_ids_str,
    #     'addBonusRubles': 'true',
    #     'isPromoApplied': 'true',
    # }
    #
    # # отправляем запрос, в ответе получаем json
    # response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
    #                         headers=headers).json()
    #
    # # сохраняем результат в файл (здесь мы получили файл с ценниками, скидками бонусами и описанием акций)
    # with open('3_prices.json', 'w') as file:
    #     json.dump(response, file, indent=4, ensure_ascii=False)
    #
    # # создаем словарь под наши данные
    # items_prices = {}
    #
    # # получаем список со словарями в котором хранятся объекты с данными
    # material_prices = response.get('body').get('materialPrices')
    #
    # # пробегаемся по нему циклом
    # for item in material_prices:
    #     item_id = item.get('price').get('productId')
    #     item_base_price = item.get('price').get('basePrice')
    #     item_sale_price = item.get('price').get('salePrice')
    #     item_bonus = item.get('bonusRubles').get('total')
    #
    #     # на каждой итерации записываем в словарь новую пару, ключом будет ID товара, а значением словарь с данными в
    #     # виде базового прайса, прайса со скидкой и бонусами
    #     items_prices[item_id] = {
    #         'item_basePrice': item_base_price,
    #         'item_salePrice': item_sale_price,
    #         'item_Bonus': item_bonus
    #     }
    #
    #     # после выходим из цикла и записываем данные в json
    #     with open('4_items_prices.json', 'w') as file:
    #         json.dump(items_prices, file, indent=4, ensure_ascii=False)



# объединение словарей с данными выносим в отдельныую функцию
def get_result():
    # читаем словарь с данными по планшетам
    with open('2_items.json') as file:
        products_data = json.load(file)

    # и следом словарь с прайсами
    with open('4_items_prices.json') as file:
        products_prices = json.load(file)

    # забираем из словаря с данными только данные по планшетам
    products_data = products_data.get('body').get('products')

    # пробегаемся циклом по списку словарей и первым делом получаем id продукта
    for item in products_data:
        product_id = item.get('productId')

        # далее нужно найти совпадения в словаре с прайсами и если id там существует, сохраняем словарь с данными по
        # базовой цене, цене со скидкой и бонусами
        if product_id in products_prices:
            prices = products_prices[product_id]

        # создаем новые пары в итоговом словаре с данными
        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_Bonus'] = prices.get('item_Bonus')

    # выходим из цикла и записываем данные в json
    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    # get_result()


if __name__ == '__main__':
    main()
