import requests
import json

# Отправляем запрос и собираем Ids товаров (с сайта м-видео listing запрос, копируем cURL(bush), на сайте
# https://curlconverter.com/#python конвертируем cURL запрос для Python, копируем)
def get_data():

    cookies = {
        '_ym_d': '1652708957',
        '_ym_uid': '1633350827847902432',
        'ADRUM': 's=1652708962304&r=https%3A%2F%2Fwww.mvideo.ru%2Fproducts%2Felektrochainik-tefal-sense-ko693110-20074031%3F0',
        '__lhash_': '55f20dcca3db997a2db9fbd5b61ca004',
        'CACHE_INDICATOR': 'false',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_CATALOG_STATE': '1',
        # код города, если парсить несколько городов, нужно менять данный параметр
        'MVID_CITY_ID': 'CityCZ_1638',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GTM_DELAY': 'true',
        'MVID_GUEST_ID': '21160892652',
        'MVID_HANDOVER_SUMMARY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7800000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_HANDOVER': '0',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MOBILE_FILTERS': 'false',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_LOGIN': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_REGION_ID': '6',
        'MVID_REGION_SHOP': 'S904',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_SMART_BANNER_BOTTOM': 'true',
        'MVID_SUPER_FILTERS': 'true',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PICKUP_SEAMLESS_AB_TEST': '2',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'flacktory': 'no',
        'searchType2': '3',
        '_gid': 'GA1.2.1678000611.1659216988',
        '_ym_isad': '2',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'SMSError': '',
        'authError': '',
        'tmr_lvid': 'e38bb51f3b80537fdf51111fd2a74596',
        'tmr_lvidTS': '1633350822435',
        'gdeslon.ru.user_id': 'c307dea1-7141-46b3-8673-e8e33e7ca4df',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'advcake_track_id': 'e4e73721-faeb-5bea-c76c-4ee4d5c0167d',
        'advcake_session_id': 'f22b86be-d77c-0588-86da-0d2f8379e0db',
        'flocktory-uuid': '5c4338d8-9404-4a35-bd1c-fb7e6ce96950-5',
        'afUserId': '7b5b03de-70b3-4148-83a6-e6f340d24e86-p',
        'AF_SYNC': '1659216991358',
        '_ga': 'GA1.2.67721858.1659216988',
        'tmr_detect': '0%7C1659217211975',
        'tmr_reqNum': '40',
        '_ga_CFMZTSS5FM': 'GS1.1.1659216987.1.1.1659217245.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1659216987.1.1.1659217245.17',
        'mindboxDeviceUUID': '32bbeffc-cd62-4c16-900a-e74000af215a',
        'directCrm-session': '%7B%22deviceGuid%22%3A%2232bbeffc-cd62-4c16-900a-e74000af215a%22%7D',
        'MVID_ENVCLOUD': 'prod2',
        '_dc_gtm_UA-1873769-1': '1',
        '_dc_gtm_UA-1873769-37': '1',
        'JSESSIONID': 'hFvJvllVy1ZJtdtpc2NL34XVyr6pRyTh6QJ2vrTF6JKHhlTKs8pr!164902245',
        'bIPs': '1595647062',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ym_d=1652708957; _ym_uid=1633350827847902432; ADRUM=s=1652708962304&r=https%3A%2F%2Fwww.mvideo.ru%2Fproducts%2Felektrochainik-tefal-sense-ko693110-20074031%3F0; __lhash_=55f20dcca3db997a2db9fbd5b61ca004; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=1; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_MULTI_DELETE=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_1638; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GTM_DELAY=true; MVID_GUEST_ID=21160892652; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7800000000000; MVID_LAYOUT_TYPE=1; MVID_LP_HANDOVER=0; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=false; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_LOGIN=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_REGION_ID=6; MVID_REGION_SHOP=S904; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_SMART_BANNER_BOTTOM=true; MVID_SUPER_FILTERS=true; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PICKUP_SEAMLESS_AB_TEST=2; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; flacktory=no; searchType2=3; _gid=GA1.2.1678000611.1659216988; _ym_isad=2; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; SMSError=; authError=; tmr_lvid=e38bb51f3b80537fdf51111fd2a74596; tmr_lvidTS=1633350822435; gdeslon.ru.user_id=c307dea1-7141-46b3-8673-e8e33e7ca4df; gdeslon.ru.__arc_domain=gdeslon.ru; advcake_track_id=e4e73721-faeb-5bea-c76c-4ee4d5c0167d; advcake_session_id=f22b86be-d77c-0588-86da-0d2f8379e0db; flocktory-uuid=5c4338d8-9404-4a35-bd1c-fb7e6ce96950-5; afUserId=7b5b03de-70b3-4148-83a6-e6f340d24e86-p; AF_SYNC=1659216991358; _ga=GA1.2.67721858.1659216988; tmr_detect=0%7C1659217211975; tmr_reqNum=40; _ga_CFMZTSS5FM=GS1.1.1659216987.1.1.1659217245.0; _ga_BNX5WPP3YK=GS1.1.1659216987.1.1.1659217245.17; mindboxDeviceUUID=32bbeffc-cd62-4c16-900a-e74000af215a; directCrm-session=%7B%22deviceGuid%22%3A%2232bbeffc-cd62-4c16-900a-e74000af215a%22%7D; MVID_ENVCLOUD=prod2; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; JSESSIONID=hFvJvllVy1ZJtdtpc2NL34XVyr6pRyTh6QJ2vrTF6JKHhlTKs8pr!164902245; bIPs=1595647062',
        'pragma': 'no-cache',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-set-application-id': '1e312c52-d17b-4715-95b6-456c5e844eaf',
    }

    params = {
        # Id категории (здесь указана категория планшеты)
        'categoryId': '195',
        'offset': '0',
        # лимит товаров поступающих на страницу
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }
    # запрос с параметрами, печеньками и заголовками. Получаем Json
    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()
    # print(response)
    # нужные нам Ids лежат в body->products, достаем их
    products_ids = response.get('body').get('products')
    # сохраним ответ в Json
    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)
    # print(products_ids)

    # Отправляем запрос и собираем IDs товаров(с сайта м-видео list запрос, копируем cURL(bush), на сайте
    # https://curlconverter.com/#python конвертируем cURL запрос для Python, копируем с json_data и запрос
    # вместо скопированного списка из productIds вставляем нашу переменную products_ids, в ответе получаем json
    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    # в ответе получаем json
    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    # сохраняем результат (здесь мы получили данные по первым 24 продуктам(планшетам)
    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    # распечатаем длину списка
    print(len(response.get('body').get('products')))




def main():
    get_data()

if __name__ == '__main__':
    main()