#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.
    Attributes:
        state_id (str): state's id.
        name (str): The city's name.
    """

    state_id = ""
    name = ""