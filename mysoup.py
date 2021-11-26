import re

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

    languages = ['java', 'kotlin', 'php', 'c#', 'js', 'html', 'css', 'python']
    keywords = ['return', 'abstract', 'continue', 'for', 'new', 'switch', 'assert', 'default', 'goto*', 'package',
                'synchronized', 'boolean', 'do', 'if', 'private', 'this', 'break', 'double', 'implements', 'protected',
                'throw', 'byte', 'else', 'import', 'public', 'throws', 'case', 'enum', 'instanceof', 'transient',
                'catch', 'extends', 'int', 'short', 'try', 'char', 'final', 'interface', 'static', 'void', 'class',
                'finally', 'long', 'strictfp**', 'volatile', 'const', 'float', 'native', 'super', 'while']

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

        pre_blocs = soup.findChildren('pre', recursive=True)
        for pre_bloc in pre_blocs:
            children = pre_bloc.findChildren("span", recursive=False)
            nb_deleted = 0
            for child in children:
                if child.text.strip() == '':
                    child.replaceWith('')
                    nb_deleted = nb_deleted + 1
                    if nb_deleted > 2:
                        break

        code_blocs = soup.findChildren('div', attrs={'class': 'codehilite'}, recursive=True)
        code_head_handle = False
        code_comment_handle = False
        code_comments = []

        # code_within_brackets = ''
        last_opened_child = None
        last_within_brackets_child = None

        for code_bloc in code_blocs:
            children = code_bloc.findChildren("span", recursive=True)

            for child in children:

                if child.text == '[':
                    code_head_handle = True
                    last_opened_child = child
                    # code_within_brackets = ''
                    last_within_brackets_child = None

                if child.text == '//':
                    code_comment_handle = True

                if code_head_handle and child.text == ']':
                    # print('code_within_brackets: ' + code_within_brackets)
                    # print('code_within_brackets: ' + last_within_brackets_child.text)

                    # if code_within_brackets == 'python':
                    if last_within_brackets_child.text  in self.languages:  # == 'python':
                        child.replaceWith('')
                        last_opened_child.replaceWith('')
                        last_within_brackets_child.replaceWith('')

                    code_head_handle = False

                if code_head_handle:
                    # print('child to delete : ' + str(child))
                    # child.replaceWith('')
                    pass
                else:
                    if child.text in self.keywords:
                        child.attrs['class'] = 'k'

                if code_head_handle and child.text != '[':
                    # code_within_brackets = child.text
                    last_within_brackets_child = child

                if child.text.strip() != '' and child.text.strip() != '//' and code_comment_handle:
                    child.attrs['class'] = 'c'
                    # print('add comment : ' + str(child))
                    # code_comments.append(child)

                if child.text == '' and code_comment_handle:
                    # code_comments = []
                    code_comment_handle = False

        # for code_comment in code_comments:
        #     print('comment : ' + str(child))
        #     code_comment.attrs['class'] = 'c'

        i = 0
        for h2tag in h2tags:
            self.sections.append(h2tag.text)

            page = [str(h2tag)]
            section_content = ''
            elem = self.next_element(h2tag)
            while elem and elem.name != 'h2':
                # elem2 = re.sub(code_header_txt,"", str(elem))

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
            i = i + 1

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

    def clean_code_header(self, page):
        soup2 = BeautifulSoup(page, 'html.parser')
        spans = soup2.find_all(lambda tag: tag.name == "span" and "```" in tag.text)  # ('span[text=```]')

        for span in spans:
            span.replaceWith('')
        return soup2
