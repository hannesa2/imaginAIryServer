# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class WeatherForecast(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, summary: str=None, description: str=None, icon: str=None):  # noqa: E501
        """WeatherForecast - a model defined in Swagger

        :param summary: The summary of this WeatherForecast.  # noqa: E501
        :type summary: str
        :param description: The description of this WeatherForecast.  # noqa: E501
        :type description: str
        :param icon: The icon of this WeatherForecast.  # noqa: E501
        :type icon: str
        """
        self.swagger_types = {
            'summary': str,
            'description': str,
            'icon': str
        }

        self.attribute_map = {
            'summary': 'summary',
            'description': 'description',
            'icon': 'icon'
        }
        self._summary = summary
        self._description = description
        self._icon = icon

    @classmethod
    def from_dict(cls, dikt) -> 'WeatherForecast':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The WeatherForecast of this WeatherForecast.  # noqa: E501
        :rtype: WeatherForecast
        """
        return util.deserialize_model(dikt, cls)

    @property
    def summary(self) -> str:
        """Gets the summary of this WeatherForecast.


        :return: The summary of this WeatherForecast.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary: str):
        """Sets the summary of this WeatherForecast.


        :param summary: The summary of this WeatherForecast.
        :type summary: str
        """

        self._summary = summary

    @property
    def description(self) -> str:
        """Gets the description of this WeatherForecast.


        :return: The description of this WeatherForecast.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this WeatherForecast.


        :param description: The description of this WeatherForecast.
        :type description: str
        """

        self._description = description

    @property
    def icon(self) -> str:
        """Gets the icon of this WeatherForecast.


        :return: The icon of this WeatherForecast.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon: str):
        """Sets the icon of this WeatherForecast.


        :param icon: The icon of this WeatherForecast.
        :type icon: str
        """

        self._icon = icon
