import json
import xml.dom.minidom
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import LiteralString, Type

from dicttoxml import dicttoxml

HANDLER_REGISTRY = dict()


def register_handler(format_name: str):
    def decorator(handler_cls):
        HANDLER_REGISTRY[format_name] = handler_cls
        return handler_cls
    return decorator


class AbstractWriterMixin(ABC):

    @abstractmethod
    def write_file(self, data: dict | list):
        ...


class AbstractReaderMixin(ABC):

    @abstractmethod
    def read_file(self) -> dict | list:
        ...


@dataclass
class AbstractHandler(ABC):

    path: Path


@register_handler('json')
class JsonHandler(AbstractReaderMixin, AbstractWriterMixin, AbstractHandler):

    def read_file(self) -> dict | list:
        with open(self.path, 'r') as file:
            return json.load(file)

    def write_file(self, data: dict | list):
        with open(self.path, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


@register_handler('xml')
class XMLHandler(AbstractWriterMixin, AbstractHandler):

    root_tag: str

    def __init__(self, *args, root_tag, **kwargs):
        self.root_tag = root_tag
        super().__init__(*args, **kwargs)

    def write_file(self, data: dict | list):
        tag = self.root_tag
        xml = self.__class__.data_to_xml(data, tag)
        pretty_xml = self.__class__.prettyfy_xml(xml)
        with open(self.path, "w", encoding="utf-8") as f:
            f.write(pretty_xml)

    @staticmethod
    def data_to_xml(data: dict | list, tag: str) -> LiteralString | bytes:
        return dicttoxml(
            data,
            custom_root=tag,
            item_func=lambda x: x[:-1] if x[-1] == 's' else x,
            attr_type=False
        )

    @staticmethod
    def prettyfy_xml(xml_obj):
        dom = xml.dom.minidom.parseString(xml_obj)
        return dom.toprettyxml(indent="  ")


def get_handler_class(format: str) -> Type[AbstractHandler]:
    return HANDLER_REGISTRY[format]


def get_handler(path: Path, *args, **kwargs) -> AbstractHandler:
    format = path.name.split('.')[-1]
    return get_handler_class(format)(path, *args, **kwargs)
