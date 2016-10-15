# -*- coding: utf-8 -*-
import os
import yaml
import logging

def func(docs_dir):
    assert os.path.exists(docs_dir)

    if os.path.exists('./mkdocs.yml'):
        with open('mkdocs.yml', 'r') as yml_file:
            text = yml_file.read()
            config = yaml.load(text) 

    if config is None:
        config = dict()
    logging.debug('yaml context:{}'.format(config))
    

    config['pages'] = config.get('pages', []) 
    config['docs_dir'] = docs_dir
    for root, dirs, files in os.walk(docs_dir):
        for file in filter(lambda x: x.endswith('.md'), files):
            md_path = os.path.relpath(os.path.join(root, file), docs_dir)
            md_name = file.split('.')[0]
            md = [md_path, md_name]
            if md not in config['pages']:
                config['pages'].append(md) 

    with open('mkdocs.yml', 'w') as yml_file:
        yaml.dump(config, yml_file)


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)
    func('/vagrant/notebook/')
