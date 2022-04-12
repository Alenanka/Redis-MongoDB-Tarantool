
# Для счетчика посещений используем множеста, в page:index:users:'+day добавляем уникальных пользователей
# user -  идентифицирует пользователя
#  на страничке http://127.0.0.1:5000/stat/ видим количество уникальных посещений за текущий день

import random
import redis
from flask import Flask, make_response, request
from time import strftime

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/')
def theanswer():
    user = random.randint(1,20)
    day = strftime("%Y-%m-%d")
    r.sadd('page:index:users:'+day,user)
    return str(r.smembers('page:index:users:'+day))

@app.route('/stat/')
def stat():
    day = strftime("%Y-%m-%d")
    return 'Сегодня страницу посещали ' + str(r.scard('page:index:users:'+day)) + ' раз'