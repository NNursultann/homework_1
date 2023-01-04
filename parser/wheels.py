import requests
from bs4 import BeautifulSoup

class ParserWheels:
    __URL = 'https://shina.kg/'
    __HEADERS = {'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

    @classmethod
    def __get_html(cls, url=None):
        if url is not None:
            req = requests.get(url=url, headers=cls.__HEADERS)
        else:
            req = requests.get(url=cls.__URL, headers=cls.__HEADERS)
        return req

    @staticmethod
    def __get_data(html):
        soup = BeautifulSoup(html, "html.parser")
        items = soup.find_all("div", class_="col-lg-9")
        wheels = []

        for item in items:
            title = item.find("div", class_="pl-item-info-expandable").find("a").getText().split(" ")
            wheels.append({
                "link": f"https://shina.kg{item.find('a').get('href')}",
                "size": title[1],
                "logo": title[2],
                "price": item.find("div", class_="price-wrapper").find("span").getText()

        })
        return wheels

    @classmethod
    def parser(cls):
        html = cls.__get_html()
        if html.status_code == 200:
            anime = []
            for i in range(1, 2):
                html = cls.__get_html(f"{cls.__URL}page/{i}/")
                current_page = cls.__get_data(html.text)
                anime.extend(current_page)
            return anime
        else:
            raise Exception("Bad request!")