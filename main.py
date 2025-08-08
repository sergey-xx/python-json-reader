import logging
from pathlib import Path
from filehandler import get_handler
from configs import configure_argument_parser
from models import Room, Student

DIR = Path(__file__).resolve().parent / 'files'

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
logging.basicConfig(level=logging.WARNING)


def main():
    arg_parser = configure_argument_parser()
    args = arg_parser.parse_args()
    logger.info(f'Command line args: {(args)}')
    s_handler = get_handler(path=(DIR / args.students_filename))
    r_handler = get_handler(path=(DIR / args.rooms_filename))
    students = Student.from_list(s_handler.read_file())
    rooms = Room.from_list(r_handler.read_file())
    for room in rooms:
        room.match_students(students)
    kwargs = {'root_tag': 'rooms'} if args.output_format == 'xml' else {}
    result_handler = get_handler(
        DIR / f'{args.output_filename}.{args.output_format}',
        **kwargs
    )
    data = [room.to_dict() for room in rooms]
    result_handler.write_file(data)


if __name__ == "__main__":
    main()
