#!/usr/bin/env python3
from urllib.request import urlopen
from urllib.parse import quote
from urllib.parse import unquote
from urllib.error import URLError, HTTPError
import re


def get_content(name):
    """
    Функция возвращает содержимое вики-страницы name из русской Википедии.
    В случае ошибки загрузки или отсутствия страницы возвращается None.
    """
    try:
        with urlopen('http://ru.wikipedia.org/wiki/' + quote(name)) as fh:
            page = quote(fh.read().decode('utf-8', errors='ignore'))
    except (URLError, HTTPError):
        return None
    return unquote(page)


def extract_content(page):
    """
    Функция принимает на вход содержимое страницы и возвращает 2-элементный
    tuple, первый элемент которого — номер позиции, с которой начинается
    содержимое статьи, второй элемент — номер позиции, на котором заканчивается
    содержимое статьи.
    Если содержимое отсутствует, возвращается (0, 0).
    """
    if (page is not None) and (page.find('<body') != -1) and (page.find('</body') != -1):
        return (page.find('<body'), page.find('</body'))
    else:
        return (0, 0)


def extract_links(page, begin, end):
    """
    Функция принимает на вход содержимое страницы и начало и конец интервала,
    задающего позицию содержимого статьи на странице и возвращает все имеющиеся
    ссылки на другие вики-страницы без повторений и с учётом регистра.
    """
    links = re.findall(r'["\']/wiki/([\w%]+?)["\']', page[begin:end])
    new_links = set(links)
    result = []
    for l in new_links:
        result.append(unquote(l))
    return result


def find_chain(start, finish):
    count = 0
    steps = []
    used = []
    recursion(start, finish, steps, used, count)
    if finish in steps:
        return steps
    else:
        return None


def recursion(start, finish, steps, used, count):
    if (count == 6):
        return None
    else:
        count += 1
        steps.append(start)
        page = get_content(start)
        if page is None:
            return None
        begin, end = extract_content(page)
        links = extract_links(page, begin, end)
        if finish in links:
            steps.append(finish)
            return steps
        else:
            for l in links:
                if l not in used:
                    used.append(l)
                    recursion(l, finish, steps, used, count)
                    if finish in steps:
                        return steps
                    else:
                        continue
                else:
                    continue
        steps.pop()


def main():
    """
    Функция находит путь от Музыки до Философии и печатает его
    """
    result = find_chain("Самолёт", "Философия")
    print(result)


if __name__ == '__main__':
    main()
