import connexion
import six

from swagger_server.models.device_registration_info import DeviceRegistrationInfo  # noqa: E501
from swagger_server import util


def get_devices(skip=None, limit=None):  # noqa: E501
    """get_devices

    returns all registered devices # noqa: E501

    :param skip: number of records to skip
    :type skip: int
    :param limit: max number of records to return
    :type limit: int

    :rtype: List[str]
    """
    return 'do some magic!'


def register(body=None):  # noqa: E501
    """register

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = DeviceRegistrationInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
