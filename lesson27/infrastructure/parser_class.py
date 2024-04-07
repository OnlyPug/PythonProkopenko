import json
from bs4 import BeautifulSoup
import requests


class ParserClass:

    def __init__(self):
        self.category_url = "https://geekach.com.ua/zhanry/na-udachu/"

    def fetch_page(self, url):
        response = requests.get(url)
        return BeautifulSoup(response.content, 'html.parser')

    def this_page_board_game(self, url):
        soup = self.fetch_page(url)
        logo = soup.find_all('img', class_='header-logo-img')
        if logo:
            return True
        else:
            return False

    def all_product_on_page(self, url):
        soup = self.fetch_page(url)
        logo = soup.find_all('div', class_='catalogCard-title')
        return len(logo)

    def save_all_products_to_file(self, url):
        soup = self.fetch_page(url)
        find_link = soup.find_all('div', class_='catalogCard-view')
        base_url = 'https://geekach.com.ua'
        links = [base_url + div.find('a')['href'] for div in find_link if div.find('a')]
        with open('Links_for_product_first_page.json', 'w') as writer:
            json.dump(links, writer, indent=4)

    def collect_product_links(self):
        product_links = []
        pagination_links = self.collect_pagination_links()

        for page_url in pagination_links:
            soup = self.fetch_page(page_url)
            find_link = soup.find_all('div', class_='catalogCard-view')
            page_links = ['https://geekach.com.ua' + div.find('a')['href'] for div in find_link if div.find('a')]
            product_links.extend(page_links)
        with open('ALL_links_with_pagination.json', 'w') as writer:
            json.dump(product_links, writer, indent=4)
        # return product_links

    def collect_pagination_links(self):
        base_url = 'https://geekach.com.ua'
        current_page = self.category_url
        pagination_list = [current_page]

        while current_page:
            soup = self.fetch_page(current_page)
            pag_div = soup.find('div', class_="pager__container")
            if not pag_div:
                break

            pag_links = pag_div.find_all('a', class_="pager__item j-catalog-pagination-btn")
            for pagin_link in pag_links:
                # додаю https://geekach.com.ua бо лінки без них
                href = pagin_link.attrs.get('href')
                if href and href.startswith('/zhanry/na-udachu/'):
                    full_link = base_url + href
                    if full_link not in pagination_list:
                        pagination_list.append(full_link)

            # переходимо по лінкам
            next_page_link = pag_div.find('a', class_="pager__item j-catalog-pagination-btn", text='>')
            current_page = base_url + next_page_link['href'] if next_page_link else None
        return pagination_list

    def information_about_product(self):
        list_of_results = []
        with open('ALL_links_with_pagination.json') as reader:
            list_of_links = json.load(reader)
            for link in list_of_links:
                list_of_results.append(self.return_parameters(link))
            # Слава могучему дяді інтрнету який допомогі мені вирішиту проблему з декодуванням цього проклятого сайту
        with open('All_game_result.json'.format(1), 'w', encoding='utf-8') as writer:
            json.dump(list_of_results, writer, indent=4, ensure_ascii=False)

    def return_parameters(self, url):
        soup = self.fetch_page(url)
        header = soup.find('h1', class_="product-title").text
        price = soup.find('div', class_="product-price").text
        status = soup.find('div', class_="product-header__availability").text
        article = soup.find('div', class_="product-header__code").text
        return {'link': url, 'header': header.strip(), 'price': price.strip(), 'status': status.strip(),
                'article': article.strip()}
