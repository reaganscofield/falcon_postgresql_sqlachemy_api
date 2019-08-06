
import re
import falcon
import json

from sqlalchemy.orm.exc import NoResultFound
from cerberus import Validator
from cerberus.errors import ValidationError

from app import log
from app.api.common import BaseResource

from app.model import Company

from app.errors import (
    AppError,
    InvalidParameterError,
    UserNotExistsError,
    PasswordNotMatch,
)


class CompanyCollection(BaseResource):
    def on_get(self, req, res):
        session = req.context["session"]
        companies = session.query(Company).all()
        if companies:
            obj = [company.to_dict() for company in companies]
            self.on_success(res, obj)
        else:
            raise AppError()


class CompanyCollect(BaseResource):
    def on_get(self, req, res, id):
        session = req.context["session"]
        company = Company.find_by_id(session, id)
        if company:
            self.on_success(res, company.to_dict())
        else:
            raise AppError()



class CompanyCreate(BaseResource):
    def on_post(self, req, res):
        session = req.context["session"]
        data = req.context["data"]

        if data:
            company = Company()

            company.contact_number = data["contact_number"]
            company.email = data["email"]
            company.vat_no = data["vat_no"]
            company.name = data["name"]
            company.website = data["website"]

            session.add(company)

            companyData = {
                "name": company.name
            }

            self.on_success(res, companyData)
        else:
            raise InvalidParameterError(req.context["data"])


class CompanyUpdate(BaseResource):
    def on_put(self, req, res, id):
        session = req.context["session"]
        data = req.context["data"]

        if data:
            args = {
                "contact_number": data["contact_number"],
                "email": data["email"],
                "vat_no": data["vat_no"],
                "name": data["name"],
                "website": data["website"]
            }
            Company.find_update(session, id, args)

            self.on_success(res, args)
        else:
            raise InvalidParameterError(req.context["data"])



class CompanyDelete(BaseResource):
    def on_delete(self, req, res, id):
        session = req.context["session"]
        company = Company.find_delete(session, id)
        if company:
            self.on_success(res, {"sucess deleted": f"{id}"})
        else:
            raise AppError()


class CompanyFilter(BaseResource):

    def on_get(self, req, res):
        session = req.context["session"]
        data = req.context["data"]
        args = {
            "contact_number": data["contact_number"],
            "email": data["email"],
            "vat_no": data["vat_no"],
            "name": data["name"],
        }
        companies = Company.filters(session, args)
        if companies:
            obj = [company.to_dict() for company in companies]
            self.on_success(res, obj)
        else:
            raise AppError()