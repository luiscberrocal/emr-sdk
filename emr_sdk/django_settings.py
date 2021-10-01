import importlib
from pathlib import Path

import environ
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent / '.env/.django'

load_dotenv(dotenv_path=env_path)


def read_settings(settings_file, module_name='my_module'):
    spec = importlib.util.spec_from_file_location(module_name, settings_file)
    my_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(my_module)
    settings = dict()
    module_attributes = dir(my_module)
    for i, att in enumerate(module_attributes):
        data_type = type(getattr(my_module, att))
        record = data_type in [str, int, dict, list, set, bool, environ.environ.Path] and '__' not in att
        rec = '[x]' if record else '[ ]'
        print(f'{i} {att:30} {data_type}  {rec}')
        if record:
            settings[att] = getattr(my_module, att)
    return settings


if __name__ == '__main__':
    fn = '/Users/luiscberrocal/PycharmProjects/emr_sdk/output/base.py'
    res = read_settings(fn, 'base_settings')
    print(res)
