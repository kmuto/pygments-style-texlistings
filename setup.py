#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='pygments-style-texlistings',
    version='0.1',
    description='Pygments version of the TeX listings theme. VS Code marker theme',
    long_description=open('README.rst').read(),
    keywords='pygments style tex listings',
    license='BSD',

    author='Kenshi Muto',
    author_email='kmuto@kmuto.jp',

    url='httpss://github.com/kmuto/pygments-style-texlistings',

    packages=find_packages(),
    install_requires=['pygments >= 1.4'],

    entry_points='''[pygments.styles]
                    texlistings=pygments_style_texlistings:TeXListingsStyle
                    vsmarker=pygments_style_texlistings:VSMarkerStyle''',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
