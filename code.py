# -*- coding: utf-8 -*-
import web
import config
import view
from view import render
from urls import urls


class Home:
    def GET(self):
        return render.base(view.index())

        
def setup_error_emaling(app):
    app.internalerror = web.emailerrors(config.email_errors, app.internalerror) # was web.webapi._InternalError

if __name__ == "__main__":
    app = web.application(urls, globals())
    if config.email_errors: setup_error_emaling(app)
    app.notfound = view.notfound
    app.internalerror = web.debugerror
    app.run()
