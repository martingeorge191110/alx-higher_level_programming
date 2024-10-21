#!/usr/bin/python3
"""Base class module"""
import json


class Base:
    """Base class
    This class will be the “base” of all other classes in this project
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating same code"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ([])
        else:
            return (json.dump(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """saves list of instance to a file"""
        jsonList = []
        if list_objs:
            for obj in list_objs:
                jsonList.append(obj.to_dictionary())
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(jsonList))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(11)
        dummy.update(**dictionary)

        return (dummy)