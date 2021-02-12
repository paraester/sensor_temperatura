#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import datetime
import threading
import time
import telepot
from telepot.loop import MessageLoop
from pyA20.gpio import gpio
from pyA20.gpio import connector
from pyA20.gpio import port
import dht
import urllib.request
import socket
ip = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

proxy = urllib.request.ProxyHandler({'https': r'http://usuario:senha@proxy.dominio.com:8080'})
#opener = urllib.request.build_opener(proxy)
#urllib.request.install_opener(opener)
telepot.api.set_proxy('http://proxy.dominio.com:8080', ('usuario', 'senha'))
#PIN2 = port.PG7
PIN2 = port.PA12
gpio.init()
instance = dht.DHT(pin=PIN2, sensor=22)



def handle(msg):
    try:
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)
        username = msg['from']['username']
        user_id = msg['from']['id']
        #chat_id = msg['chat']['id']
        command = msg['text']
        print ('Received:')
        print(command)
        if command == '/hi':
            print ('hi')
            if username == '':
                username = str("@getout")
                bot.sendMessage (chat_id, str("Por favor Set seu username no Telegram para usar este bot"))
                return
            bot.sendMessage (chat_id, str("Olá ") + str(username) + str(" este é um teste para o sensor DHT11 - testes em Guarapuava"))
        elif command == '/ip':
            bot.sendMessage(chat_id, str("@umtemp_bot diz: meu ip é ")+str(ip) + str(" ") + str(username) )
        elif command == '/hora':
            bot.sendMessage(chat_id, str("Hora: ") + str(now.hour) + str(":") + str(now.minute) + str(":") + str(now.second))
        elif command == '/data':
            bot.sendMessage(chat_id, str("Data: ") + str(now.day) + str("/") + str(now.month) + str("/") + str(now.year))
        elif command == '/sensor':
            parada = 1
            sucesso = 0
            while parada < 10:
                result = instance.read()
                if result.is_valid():
                    bot.sendMessage(chat_id, str("@umtemp_bot diz: "))
                    bot.sendMessage(chat_id, str(username) + str(" estou lendo a temperatura, por favor aguarde "))
                    bot.sendMessage(chat_id, str("Em Guarapuava: temperatura em Celsius: ") + str(result.temperature))
                    bot.sendMessage(chat_id, str("Humidade: ")  + str(result.humidity))
                    parada = 10
                    time.sleep(3)
                    sucesso = 1
                else :
                    bot.sendMessage(chat_id, str("."))
                    parada = parada + 1
                    sucesso = 2
            if sucesso == 2:
                bot.sendMessage(chat_id, str("Error: ") + str(result.error_code) + str("Temperatura: ") + str(result.temperature) + str("Humidade: ") + str(result.humidity))
    except Exception:
        pass
bot = telepot.Bot('970660657:AAFCd72tfm7QpNEoQmvroQRxA__iMTkj2LI')
print (bot.getMe())
MessageLoop(bot, handle).run_as_thread()
print ('Eu bot estou esperando....')
while True:
    time.sleep(3)
