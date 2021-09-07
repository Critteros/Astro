#!python
import pathlib
import os
import sys


def run():
    project_location: pathlib.Path = pathlib.Path(
        __file__).resolve().parents[1]
    # Out file paths
    requirements_file_path = project_location.joinpath('requirements.txt')
    requirements_dev_file_path = project_location.joinpath(
        'dev-requirements.txt')
    # In file paths
    requirements_dev_in_file_path = project_location.joinpath(
        'dev-requirementsz.in')

    if not requirements_dev_in_file_path.exists():
        print('dev-requirements.in' + ' was not found, exitting',
              file=sys.stderr, flush=True)
        sys.exit(1)
    print('ok')


if __name__ == '__main__':
    run()
