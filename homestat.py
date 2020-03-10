#!/usr/bin/env python3
from collections import Counter
from urllib.request import urlopen
import re
import operator


def make_stat(filename):
    """
    Функция вычисляет статистику по именам за каждый год с учётом пола
    """
    with urlopen('ftp://shannon.usu.edu.ru/python/hw2/home.html') as fh:
        html = str(fh.read(), encoding="Windows-1251")
    names = Counter()
    stat = dict()
    while(html.find('<h3') != -1):
        html = html[html.find('<h3'):]
        html = html[html.find('>') + 1:]
        year = html[:html.find('<h3')]
        number_year = year[:year.find('<')]
        while(year.find('<a') != -1):
            year = year[year.find('<a'):]
            year = year[year.find('>') + 1:]
            full_name = year[:year.find('<')]
            last, first = full_name.split()
            names[first] += 1
        stat_year = list()
        for k, v in names.items():
            if((k[-1] == 'а') or (k[-1] == 'я') or (k == 'Любовь')) and\
               (k != 'Илья') and (k != 'Никита') and (k != 'Лёва'):
                stat_year.append('{0} {1} {2}'.format(k, v, 'ж'))
            else:
                stat_year.append('{0} {1} {2}'.format(k, v, 'м'))
        stat[number_year] = stat_year
        names.clear()
    return stat


def extract_years(stat):
    """
    Функция принимает на вход вычисленную статистику и выдаёт список годов,
    упорядоченный по возрастанию.
    """
    list_years = list()
    for year in stat.keys():
        list_years.append(year)
    list_years.sort()
    return list_years


def extract_general(stat):
    """
    Функция принимает на вход вычисленную статистику и выдаёт список tuple'ов
    (имя, количество) общей статистики для всех имён.
    Список должен быть отсортирован по убыванию количества.
    """
    count = Counter()
    result = list()
    for k, v in stat.items():
        for element in v:
            key, value, sex = element.split()
            count[key] += int(value)
    result = sorted(count.items(), key=operator.itemgetter(1))
    result.reverse()
    return result


def extract_general_male(stat):
    """
    Функция принимает на вход вычисленную статистику и выдаёт список tuple'ов
    (имя, количество) общей статистики для имён мальчиков.
    Список должен быть отсортирован по убыванию количества.
    """
    count = Counter()
    result = list()
    for k, v in stat.items():
        for element in v:
            key, value, sex = element.split()
            if (sex == 'м'):
                count[key] += int(value)
    result = sorted(count.items(), key=operator.itemgetter(1))
    result.reverse()
    return result


def extract_general_female(stat):
    """
    Функция принимает на вход вычисленную статистику и выдаёт список tuple'ов
    (имя, количество) общей статистики для имён девочек.
    Список должен быть отсортирован по убыванию количества.
    """
    count = Counter()
    result = list()
    for k, v in stat.items():
        for element in v:
            key, value, sex = element.split()
            if (sex == 'ж'):
                count[key] += int(value)
    result = sorted(count.items(), key=operator.itemgetter(1))
    result.reverse()
    return result


def extract_year(stat, year):
    """
    Функция принимает на вход вычисленную статистику и год.
    pезультат — список tuple'ов (имя, количество) общей статистики для всех
    имён в указанном году.
    Список должен быть отсортирован по убыванию количества.
    """
    count = Counter()
    result = list()
    for element in stat[year]:
        key, value, sex = element.split()
        count[key] += int(value)
    result = sorted(count.items(), key=operator.itemgetter(1))
    result.reverse()
    return result


def extract_year_male(stat, year):
    """
    Функция принимает на вход вычисленную статистику и год.
    результат — список tuple'ов (имя, количество) общей статистики для всех
    имён мальчиков в указанном году.
    Список должен быть отсортирован по убыванию количества.
    """
    count = Counter()
    result = list()
    for element in stat[year]:
        key, value, sex = element.split()
        if (sex == 'м'):
            count[key] += int(value)
    result = sorted(count.items(), key=operator.itemgetter(1))
    result.reverse()
    return result


def extract_year_female(stat, year):
    """
    Функция принимает на вход вычисленную статистику и год.
    результат — список tuple'ов (имя, количество) общей статистики для всех
    имён девочек в указанном году.
    Список должен быть отсортирован по убыванию количества
    """
    count = Counter()
    result = list()
    for element in stat[year]:
        key, value, sex = element.split()
        if (sex == 'ж'):
            count[key] += int(value)
    result = sorted(count.items(), key=operator.itemgetter(1))
    result.reverse()
    return result
