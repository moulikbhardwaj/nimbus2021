from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404
from utils.helper_response import SuccessfullyUpdatedResponse, FieldsNotPresentErrorResponse, \
    DepartMentNotFoundErrorResponse, InternalServerErrorResponse, InvalidPasswordResponse
from .models import Department


def checkValidPassWord(password, department) -> bool:
    return check_password(password, department.password)


def DepartmentAuthentication(request, update, *args, **kwargs):
    try:
        department = get_object_or_404(Department, pk=kwargs["pk"])
        if department:
            try:
                if checkValidPassWord(request.data["password"], department):
                    update()
                    return SuccessfullyUpdatedResponse
                else:
                    return InvalidPasswordResponse
            except:
                return FieldsNotPresentErrorResponse
        else:
            return DepartMentNotFoundErrorResponse
    except:
        return InternalServerErrorResponse
