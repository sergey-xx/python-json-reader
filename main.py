import logging
import json
from pathlib import Path

from configs import configure_argument_parser

MEDIA_DIR = Path(__file__).resolve().parent / "media"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO)


def read_json(path: Path) -> dict | list:
    with open(path, 'r') as file:
        return json.load(file)


def write_json(path: Path, data: dict | list):
    with open(path, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def match_lists(list_1: list, attr_1, list_2: list, attr_2, obj_name):
    """
    Enriches an object of the second list with an object from the first list
    if attr_1 == attr_2
    """
    dict_1 = {obj[attr_1]: obj for obj in list_1}
    for obj_2 in list_2:
        if obj_2[attr_2] in dict_1.keys():
            obj_2[obj_name] = dict_1[obj_2[attr_2]]
    return list_2


def main():
    arg_parser = configure_argument_parser()
    args = arg_parser.parse_args()
    logger.info(f'Command line args: {(args)}')
    rooms = read_json(MEDIA_DIR / args.f1)
    students = read_json(MEDIA_DIR / args.f2)
    if all((isinstance(students, list), isinstance(rooms, list))):
        result = match_lists(rooms, args.a1, students, args.a2, 'student')
        write_json(MEDIA_DIR / f'{args.result}.{args.output}', result)


if __name__ == "__main__":
    main()
