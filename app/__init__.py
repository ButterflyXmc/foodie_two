from flask import Flask

#! Only a single app object is allowed
app = Flask(__name__)

from endpoints import client, client_login, resto, resto_login, menu, orders