import importlib
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(__file__).parent.parent / '.env/.django'

load_dotenv(dotenv_path=env_path)


def do_compare(settings):
    fn = '/Users/luiscberrocal/PycharmProjects/emr_sdk/output/base.py'
    spec = importlib.util.spec_from_file_location(settings, fn)
    my_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(my_module)

    module_attributes = dir(my_module)
    for i, att in enumerate(module_attributes):
        print(f'{i} {att} {type(getattr(my_module, att))}')

if __name__ == '__main__':
    do_compare('conf')
