# -*- coding: utf-8 -*-
import web
import config

t_globals = dict(
    datestr=web.datestr,
)
render = web.template.render("templates/", cache=config.cache,
    globals=t_globals)
render._keywords['globals']['render'] = render


# Custom NotFound message
def notfound():
    return web.notfound(render.notfound())

# Home page
def index():
    return render.index()

