import os
from setuptools import find_packages, setup

from badia.common import __version__


with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='badia-common',
    version=__version__,
    packages=find_packages(),
    namespace_packages=['badia'],
    include_package_data=True,
    license='AGPL-3.0',
    description='Shared code for Badia and related services',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/fm-futura/badia-common',
    author='Adrián Pardini',
    author_email='github@tangopardo.com.ar',
    classifiers=[
        'Environment :: Web Environment',
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Communications',
    ],
    keywords='radio schedule grid programming audio',
)
