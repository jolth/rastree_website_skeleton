# -*- coding: utf-8 -*-
import web

# Database
db = web.database(dbn='postgres', db='appname', user='username', pw='')

# Cache
cache = False

# mensaje de error para depuración y reloader 
web.config.debug = True # False # Producción

# enviar mensajes de error a
email_errors = ''
