from bs4 import BeautifulSoup


class MySoupParser:
    github_url = ''
    header = ''
    title = ''
    sections = []
    pages = []

    def feed(self, source_html):

        self.sections = []
        self.pages = []

        soup = BeautifulSoup(source_html, 'html.parser')

        urls = soup.find().text.split('feedback link: ')
        if len(urls) > 1:
            self.github_url = urls[1].strip()

        self.header = soup.find('h1').text
        self.title = soup.find('h1').text

        h2tags = soup.find_all('h2')

        for h2tag in h2tags:
            self.sections.append(h2tag.text)

            page = [str(h2tag)]
            elem = self.next_element(h2tag)
            while elem and elem.name != 'h2':
                page.append(str(elem))
                elem = self.next_element(elem)
            self.pages.append('\n'.join(page))

    def next_element(self, elem):
        while elem is not None:
            elem = elem.next_sibling
            if hasattr(elem, 'name'):
                return elem
