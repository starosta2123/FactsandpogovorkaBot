import telebot
import random
from telebot import types

f = open('data/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()

f = open('data/thinks.txt', 'r', encoding='UTF-8')
thinks  = f.read().split('\n')
f.close()

bot = telebot.TeleBot('2115904546:AAEqr_FUahUjhPkyVJaklybJtCVx6xGCZdk')
