import re
import webbrowser

import markdown
from mako.template import Template
from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagPattern, Pattern

import unidecode

from mysoup import MySoupParser

XXX_RE = r'(Positive )(.*?)'


# POS_RE = r'(>Positive :)(.*?)--'
# NEG_RE = r'(>Negative :)(.*?)--'


class AttrTagPattern(Pattern):
    """
    Return element of type `tag` with a text attribute of group(3)
    of a Pattern and with the html attributes defined with the constructor.
    """

    def __init__(self, pattern, tag, attrs):
        Pattern.__init__(self, pattern)

        print(tag)
        self.tag = tag
        self.attrs = attrs

    def handleMatch(self, m):
        print('handleMatch: ', m)
        el = markdown.util.etree.Element(self.tag)
        el.text = m.group(3)
        print(el.text)
        for (key, val) in self.attrs.items():
            el.set(key, val)
        return el


class MyExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        pos_tag = AttrTagPattern(XXX_RE, 'aside', {'class': 'special'})
        md.inlinePatterns.add('aside1', pos_tag, '>not_strong')

        # neg_tag = AttrTagPattern(NEG_RE, 'aside', {'class': 'warning'})
        # md.inlinePatterns.add('aside2', neg_tag, '>not_strong')


def slugify(text):
    text = unidecode.unidecode(text).lower()
    return re.sub(r'[\W_]+', "-", text)


def generate(source_html):
    parser = MySoupParser()
    parser.feed(source_html)

    template_html_name = 'html/template.html'
    output = Template(filename=template_html_name, input_encoding='utf-8')

    nav = '<ul>'
    for section in parser.sections:
        nav += '<li class="toctree-l1"><a class="reference internal" href="#' + slugify(
            section) + '">' + section + '</a></li>'
    nav += '</ul>'

    main_content = ''
    class_name = 'active'
    i = 0
    for page in parser.pages:
        main_content += '<section id="' + slugify(
            parser.sections[i]) + '" class="article ' + class_name + '">' + page + '</section>'
        class_name = 'hidden'
        i += 1

    # global generated_html

    generated_path = 'html\\'
    generated_html = generated_path + slugify(parser.title) + ".html"
    f = open(generated_html, encoding='utf-8', mode="w+")

    f.write(output.render(
        title=parser.header,
        doc_title=parser.title,
        page_name="Tutorial",
        github_url="https://mchou69.github.io",
        nav_section=nav,
        topics=parser.sections,
        content=main_content
    )
    )

    f.close()

    # print('opening \'', generated_html, '\' on browser..')
    # webbrowser.open(generated_html, new=2)  # open in new tab


class CustomHeadings(Extension):
    def extendMarkdown(self, md, md_globals):
        H1_RE = r'(blockquote p Positive) (.*)(/p /blockquote)'

        xxx = SimpleTagPattern(H1_RE, 'span class="x"')
        md.inlinePatterns.add('xx', xxx, '>not_strong')


def md():
    markdown_source_file = 'md/source0.md'  # input('template file name (*.md) : ')

    source = open(markdown_source_file, encoding='utf-8', mode="r")
    html = markdown.markdown(source.read(),
                             extensions=[CustomHeadings()])

    print(html)

    # generate(html)


if __name__ == '__main__':
    print('--------------------------------------------------')
    md()
    print('--------------------------------------------------')
