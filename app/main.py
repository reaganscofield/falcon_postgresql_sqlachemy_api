# -*- coding: utf-8 -*-

import falcon

from app import log
from app.middleware import AuthHandler, JSONTranslator, DatabaseSessionManager
from app.database import db_session, init_session

from app.api.common import base
from app.api.v1 import users
from app.api.v1 import company
from app.errors import AppError

LOG = log.get_logger()


class App(falcon.API):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        LOG.info("API Server is starting")

        self.add_route("/", base.BaseResource())
        self.add_route("/v1/users", users.Collection())
        self.add_route("/v1/users/{user_id}", users.Item())
        self.add_route("/v1/users/self/login", users.Self())
        self.add_route("/users", users.GetUsers())
        self.add_route("/api/companies", company.CompanyCollection())
        self.add_route("/api/company_create", company.CompanyCreate())  # 
        self.add_route("/api/company/{id}", company.CompanyCollect())
        self.add_route("/api/company_update/{id}", company.CompanyUpdate())
        self.add_route("/api/company_destroy/{id}", company.CompanyDelete())

        self.add_error_handler(AppError, AppError.handle)


init_session()
middleware = [AuthHandler(), JSONTranslator(), DatabaseSessionManager(db_session)]
application = App(middleware=middleware)


if __name__ == "__main__":
    from wsgiref import simple_server

    httpd = simple_server.make_server("127.0.0.1", 5000, application)
    httpd.serve_forever()
