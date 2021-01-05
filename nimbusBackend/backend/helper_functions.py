from .models import Department
from django.contrib.auth.hashers import check_password


def departmentExistsOrNot(departmentName) -> bool:
    if departmentName in Department.objects.values_list('name').distinct():
        return True
    else:
        return False


def checkValidPassWord(password, department) -> bool:
    return check_password(password, department.password)
