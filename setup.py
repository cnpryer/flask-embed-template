"""A setuptools based setup module."""

from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='flask-embed-temp',
    version='0.0.1',
    description='Flask web application for engineering models.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/christopherpryer/flask-embed-template',
    author='Christopher Pryer',
    author_email='christophpryer@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='Plotly Dash Flask OR Tools fyords',
    packages=find_packages(),
    install_requires=['flask',
                      'flask_redis',
                      'flask_sqlalchemy',
                      'pandas',
                      'psycopg2-binary',
                      'dash',
                      'dash_core_components',
                      'dash_html_components',
                      'pathlib'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
        'env': ['python-dotenv']
    },
    entry_points={
        'console_scripts': [
            '__main__',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/christopherpryer/flask-embed-template/issues',
        'Source': 'https://github.com/christopherpryer/flask-embed-template',
    },
)