import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

from wiki_core import VERSION

setup(
    name='django-wiki-core',
    version=VERSION,
    description="Django based simple wiki",
    long_description=README,
    author='Vittorio Zamboni',
    author_email='vittorio.zamboni@gmail.com',
    license='MIT',
    url='https://github.com/vittoriozamboni/django-wiki-core',
    packages=[
        'wiki_core',
    ],
    include_package_data=True,
    install_requires=[
        'awesome-slugify',
        'django>=1.7',
        'django-braces',
        'django-guardian',
        'django-mptt',
        'jsonfield',
    ],
    dependency_links=[
        'https://bitbucket.org/zamboni/django-utils/get/tip.zip',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
