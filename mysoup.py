from bs4 import BeautifulSoup

from custom_extensions import slugify


class MySoupParser:
    github_url = ''
    header = ''
    title = ''
    sections = []
    subsections = []
    sommaire = {}
    pages = []
    subpages = []

    def feed(self, source_html):

        self.sections = []
        self.subsections = []
        self.pages = []
        self.subpages = []
        self.sommaire = {}

        soup = BeautifulSoup(source_html, 'html.parser')

        urls = soup.find().text.split('feedback link: ')
        if len(urls) > 1:
            self.github_url = urls[1].strip()

        self.header = soup.find('h1').text
        self.title = soup.find('h1').text

        h2tags = soup.find_all('h2')

        i = 0
        for h2tag in h2tags:
            self.sections.append(h2tag.text)

            page = [str(h2tag)]
            section_content = ''

            elem = self.next_element(h2tag)

            while elem and elem.name != 'h2':
                page.append(str(elem))
                section_content += str(elem)
                elem = self.next_element(elem)

            self.pages.append('\n'.join(page))
            self.subsections = []

            soup2 = BeautifulSoup(section_content, 'html.parser')
            h3tags = soup2.find_all('h3')
            for h3tag in h3tags:
                self.subsections.append(h3tag.text)
                page = [str(h3tag)]
                elem = self.next_element(h3tag)
                while elem and elem.name != 'h3':
                    page.append(str(elem))
                    elem = self.next_element(elem)
                self.subpages.append('\n'.join(page))

            self.sommaire[i] = self.subsections
            i = i+1
    def next_element(self, elem):
        while elem is not None:
            elem = elem.next_sibling
            if hasattr(elem, 'name'):
                return elem

    def subsections_update_ids(self, page):
        soup2 = BeautifulSoup(page, 'html.parser')
        h3tags = soup2.find_all('h3')

        for h3tag in h3tags:
            sup = soup2.new_tag('h3')
            sup['id'] = slugify(h3tag.text)
            sup.string = h3tag.text
            h3tag.insert_after(sup)
            h3tag.replaceWith('')

        return soup2
