# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.location_result_concordance import LocationResultConcordance  # noqa: F401,E501
from swagger_server import util


class LocationResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, concordance: List[LocationResultConcordance]=None, input: str=None):  # noqa: E501
        """LocationResult - a model defined in Swagger

        :param concordance: The concordance of this LocationResult.  # noqa: E501
        :type concordance: List[LocationResultConcordance]
        :param input: The input of this LocationResult.  # noqa: E501
        :type input: str
        """
        self.swagger_types = {
            'concordance': List[LocationResultConcordance],
            'input': str
        }

        self.attribute_map = {
            'concordance': 'concordance',
            'input': 'input'
        }
        self._concordance = concordance
        self._input = input

    @classmethod
    def from_dict(cls, dikt) -> 'LocationResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The location_result of this LocationResult.  # noqa: E501
        :rtype: LocationResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def concordance(self) -> List[LocationResultConcordance]:
        """Gets the concordance of this LocationResult.


        :return: The concordance of this LocationResult.
        :rtype: List[LocationResultConcordance]
        """
        return self._concordance

    @concordance.setter
    def concordance(self, concordance: List[LocationResultConcordance]):
        """Sets the concordance of this LocationResult.


        :param concordance: The concordance of this LocationResult.
        :type concordance: List[LocationResultConcordance]
        """
        if concordance is None:
            raise ValueError("Invalid value for `concordance`, must not be `None`")  # noqa: E501

        self._concordance = concordance

    @property
    def input(self) -> str:
        """Gets the input of this LocationResult.


        :return: The input of this LocationResult.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input: str):
        """Sets the input of this LocationResult.


        :param input: The input of this LocationResult.
        :type input: str
        """
        if input is None:
            raise ValueError("Invalid value for `input`, must not be `None`")  # noqa: E501

        self._input = input
