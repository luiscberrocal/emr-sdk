import importlib
import json
import pathlib
import sys
from pathlib import Path

import environ
from dotenv import load_dotenv


def load_environment_variables(environ_files):
    env_path = Path(__file__).parent / '.django'
    environ_files.append(env_path)
    for env_data_file in environ_files:
        load_dotenv(dotenv_path=env_data_file)


def read_settings(settings_file, module_name='my_module', **kwargs):
    verbose = kwargs.get('verbose', False)
    spec = importlib.util.spec_from_file_location(module_name, settings_file)
    my_module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(my_module)
    settings = dict()
    module_attributes = dir(my_module)
    for i, att in enumerate(module_attributes):
        data_type = type(getattr(my_module, att))
        accepted_types = [str, int, dict, list, set, bool, environ.environ.Path, pathlib.PosixPath]
        record = data_type in accepted_types and '__' not in att
        if verbose:
            rec = '[x]' if record else '[ ]'
            print(f'{i} {att:30} {data_type}  {rec}')
        if record:
            settings[att] = getattr(my_module, att)

    return settings


if __name__ == '__main__':
    config_file = Path(__file__).parent.parent / 'output/config.json'
    with open(config_file, 'r') as json_file:
        configuration = json.load(json_file)
    load_environment_variables(configuration['extras']['environs'])
    base_settings = read_settings(configuration['base_settings']['file'],
                                  module_name='base_settings')

    settings_2 = read_settings(configuration['other_settings']['file'], module_name='base_settings_2')
    differences = dict()

    for i, (key, item) in enumerate(base_settings.items()):
        val2 = settings_2.get(key)
        try:
            if val2 != item:
                differences[key] = (item, val2)
        except AttributeError:
            differences[key] = (item, val2)
        print(f'{i} {key:35} {item}')
        print('=' * 80)

    for i, (key, value) in enumerate(differences.items()):
        print(f'{i} {key}')
        print(f'{value[0]}')
        print(f'{value[1]}')
        print('-' * 100)
