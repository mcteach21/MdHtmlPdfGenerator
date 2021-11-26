import os
import sys
import webbrowser
import markdown
import re
import unidecode
from bs4 import BeautifulSoup

# from pygments import highlight
# from pygments.formatters.html import HtmlFormatter
# from pygments.lexers.python import PythonLexer

from termcolor import colored
from mako.template import Template

import mysoup
from mysoup import MySoupParser

menu_color = 'green'

generated_path = 'html\\'
generated_html = ''
template_html_name = 'html/template.html'


def directory_files(directory):
    import glob
    return [f for f in glob.glob(directory + "/*.*")]


def list_files(ext):
    import glob
    return [f for f in glob.glob(ext + "/*." + ext)]


def browse(ext):
    files = list_files(ext)
    print(files)


def slugify(text):
    text = unidecode.unidecode(text).lower()
    return re.sub(r'[\W_]+', '-', text)


def md_html(markdown_source_file):
    source = open(markdown_source_file, encoding='utf-8', mode="r")
    html = markdown.markdown(source.read(), extensions=['markdown.extensions.tables', 'markdown.extensions.codehilite'])
    return html


def next_elem(elem):
    while elem is not None:
        elem = elem.next_sibling
        return elem

        # if hasattr(elem, 'name'):
        #     return elem


def generate_html_from_md():
    files = list_files('md')
    num_file = display_list_choice(files, mess='(0 for absolut path)')
    if num_file == 0:
        markdown_source_file = input('template file name (*.md) : ')  # 'md/android_lesson_data.md'
    else:
        markdown_source_file = files[num_file - 1]

    source_html = md_html(markdown_source_file)

    parser = MySoupParser()
    parser.feed(source_html)
    output = Template(filename=template_html_name, input_encoding='utf-8')

    nav = '<ul>'
    i = 1

    num_section = 0
    for section in parser.sections:

        subsections = parser.sommaire[num_section]

        nav += '<li class="toctree-l0" data-subsections="' + str(
            len(subsections)) + '"><a class="reference internal dropdown-btn toctree-l1" href="#' \
               + slugify(section) + '"  id="nav_' + str(num_section + 1) + '">' + section + '</a>'

        if len(subsections) > 0:
            nav += '<div class ="dropdown-container" id="nav_' + str(num_section + 1) + '_sub" >'
            nav += '<ul>'
            n = 1
            subsections = parser.sommaire[num_section]
            for subsection in subsections:
                nav += '<li id="nav_' + str(num_section + 1) + str(n) + '" class ="toctree-l1"><a href="#' + slugify(
                    subsection) + '">' + subsection + '</a></li>'
                n = n + 1

            nav += '</ul></div>'

        nav += '</li>'
        num_section = num_section + 1

    nav += '</ul>'

    main_content = ''
    class_name = 'active'
    i = 0

    for page in parser.pages:
        # print('******************************************')
        # print(page)
        # print('******************************************')

        # page_new = page  # parser.clean_code_header(page)
        main_content += '<section id="' + slugify(parser.sections[i]) + '" class="article ' + class_name + '">' + str(page) + '</section>'
        class_name = 'hidden'
        i += 1

    global generated_html

    generated_html = generated_path + slugify(parser.title) + ".html"

    f = open(generated_html, encoding='utf-8', mode="w+")

    f.write(
        output.render(
            title=parser.header,
            doc_title=parser.title,
            page_name="Tutorial",
            github_url=parser.github_url,
            nav_section=nav,
            topics=parser.sections,
            content=main_content
        )
    )

    f.close()

    print('opening \'', generated_html, '\' on browser..')
    webbrowser.open(generated_html, new=2)  # open in new tab


def display_list_choice(files, mess=''):
    if len(files) == 0:
        print(colored("no file to display!", 'white'))
        return 0

    print(colored("************** File to Open **************", menu_color))
    if mess != '':
        print(mess)
    i = 1
    for file in files:
        print(colored(str(i) + '-' + file, 'white'))
        i = i + 1
    print(colored("******************************************", menu_color))
    num_file = int(input("your choice (1-" + str(len(files)) + ") : "))
    return num_file


def display_and_open(ext):
    files = list_files(ext)
    num_file = display_list_choice(files)
    if len(files) >= num_file > 0:
        file_to_open = files[num_file - 1]
        print('opening \'', file_to_open, '\' on browser..')
        webbrowser.open(os.path.dirname(os.path.abspath(__file__)) + '\\' + file_to_open, new=2)  # open in new tab


def open_pdf():
    display_and_open('pdf')


def open_html():
    global generated_html
    if generated_html != '':
        print('opening \'', generated_html, '\' on browser..')
        webbrowser.open(os.path.dirname(os.path.abspath(__file__)) + '\\' + generated_html, new=2)  # open in new tab
    else:
        display_and_open('html')


def display(message):
    print(colored("***************************************", menu_color))
    print(colored(message, 'white'))
    print(colored("***************************************", menu_color))


def delete_file(filename):
    import os
    print(colored('delete file..' + filename, 'red'))
    os.remove(filename)


def bye():
    print(colored('Thank you for using Generator :). Bye!', 'blue'))


def error(mess):
    print(colored(mess, 'red'))


def html_pdf_prepare(input_filename):
    import bs4
    with open(input_filename) as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt, "html.parser")

    new_link = soup.new_tag("link", rel="stylesheet", href="assets/css/html_pdf_correct.css")
    soup.head.append(new_link)

    output_filename = r'html\updated.html'
    with open(output_filename, "w") as outf:
        outf.write(str(soup))
    return output_filename


def html_to_pdf(html_filename, pdf_filename):
    import pdfkit

    print(colored('generating pdf', 'white'))
    input_filename = html_pdf_prepare(html_filename)
    output_filename = pdf_filename

    pdfkit.from_url(os.path.dirname(os.path.abspath(__file__)) + '\\' + input_filename, output_filename)

    delete_file(input_filename)
    return output_filename


def generate_pdf():
    print(colored('generating pdf..', 'white'))
    files = directory_files('html')
    if len(files) == 0:
        print(colored("no file to convert!", 'white'))
        return 0

    print(colored("************* File to Convert *************", menu_color))
    i = 1
    for file in files:
        print(colored(str(i) + '-' + file, 'white'))
        i = i + 1
    print(colored("******************************************", menu_color))
    nb_file = int(input("file to convert to pdf (1-" + str(len(files)) + ") : "))

    if len(files) >= nb_file > 0:
        input_filename = files[nb_file - 1]
        output_filename = input_filename.replace('html\\', 'pdf\\').replace('.html', '.pdf')
        output_filename = html_to_pdf(input_filename, output_filename)
        print('opening \'', output_filename, '\' on browser..')
        webbrowser.open(os.path.dirname(os.path.abspath(__file__)) + '\\' + output_filename, new=2)  # open in new tab


def switch_function(arg):
    switcher = {
        0: bye,
        1: generate_html_from_md,
        2: open_html,
        3: lambda: browse('md'),
        4: lambda: browse('html'),
        5: generate_pdf,
        6: open_pdf
    }
    _func = switcher.get(arg, 'not implemented yet!!')
    # print('========================================')
    # print(_func)
    # print('========================================')
    return _func


nb = 1


def menu():
    print(colored("************** Menu *******************", menu_color))
    print(colored("***************************************", menu_color))
    print(colored("1- Generate", menu_color))
    print(colored("2- Open HTML", menu_color))
    print(colored("3- Sources (*.md)", menu_color))
    print(colored("4- Generated (*.html)", menu_color))
    print(colored("5- PDF from HTML", menu_color))
    print(colored("6- Open PDF", menu_color))
    print(colored("0- Quit!", menu_color))
    print(colored("***************************************", menu_color))

    global nb
    try:
        nb = int(input("your choice (1-6) : "))
        func = switch_function(nb)
        if not callable(func):
            error('unknown function!')
            menu()
        else:
            # print('function (exec.) : ', func.__name__)
            func()
    except Exception as e:
        tb = sys.exc_info()
        error(e.with_traceback(tb[2]))
    finally:
        if nb != 0:
            menu()


def main():
    title = """ 
    _    ___       __                    
|V|| \ |_|||V||   /__ _ __  _ ____|_ _ __
| ||_/o| ||| ||__ \_|(/_| |(/_|(_||_(_)| 
    """
    os.system('color')
    # display('MC. - Python MARKDOWN => HTML Generator!')
    display(title)
    # import sys
    # for arg in sys.argv:
    #     print(arg)

    while nb > 0:
        menu()


if __name__ == '__main__':
    # try:
    main()
    # except BaseException:
    #     import sys
    #     print(sys.exc_info()[0])
    #
    #     import traceback
    #     print(traceback.format_exc())
    # finally:
    #     print("Press Enter to continue ...")
    #     input()
