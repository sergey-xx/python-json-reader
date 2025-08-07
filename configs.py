import argparse


def configure_argument_parser():
    parser = argparse.ArgumentParser(description='Matcher of json-files')
    parser.add_argument(
        '-f1',
        help='First filename',
        required=True,
    )
    parser.add_argument(
        '-f2',
        help='Second filename',
        required=True,
    )
    parser.add_argument(
        '-a1',
        help='First attribute',
        required=True,
    )
    parser.add_argument(
        '-a2',
        help='Second attribute',
        required=True,
    )

    parser.add_argument(
        '-r',
        '--result',
        default='result',
        help='Output filename'
    )
    parser.add_argument(
        '-o',
        '--output',
        default='json',
        choices=('json', 'xml'),
        help='Outpuf format.'
    )
    return parser
