import telebot
import random
from telebot import types

f = open('data/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()