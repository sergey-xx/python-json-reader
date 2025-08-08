import argparse


def configure_argument_parser():
    parser = argparse.ArgumentParser(description='Matcher of json-files')
    parser.add_argument(
        '-s',
        '--students_filename',
        help='Students filename.',
        required=True,
    )
    parser.add_argument(
        '-r',
        '--rooms_filename',
        help='Rooms filename',
        required=True,
    )

    parser.add_argument(
        '-o',
        '--output_filename',
        default='result',
        help='Output filename'
    )
    parser.add_argument(
        '-f',
        '--output_format',
        default='json',
        choices=('json', 'xml'),
        help='Output format'
    )
    return parser
