from rest_framework.exceptions import APIException


class ProfileNotFound(APIException):
    status_code = 404
    default_detail = "The requested profile was not found"


class NotYourProfile(APIException):
    status_code = 403
    default_detail = "You do not have permissions to edit this profile"
