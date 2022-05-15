#!/usr/bin/env python

import os
import setuptools


def readme():
    with open('README.MD') as f:
        return f.read()


def get_requirements_filename():
    return "REQUIREMENTS.txt"


install_requires = [
    line.rstrip() for line in open(os.path.join(os.path.dirname(__file__), get_requirements_filename()))
]

setuptools.setup(
    name='gatk_sv_genotyper',
    version='0.1.0',
    description='Tools for genotyping structural variants, built for use '
                'with the GATK-SV pipeline',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research'
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    keywords='genomics sv bioinformatics',
    url='http://github.com/broadinstitute/gatk-sv-genotyper',
    author='Mark Walker',
    license='BSD (3-Clause)',
    packages=['gatk_sv_genotyper'],
    install_requires=install_requires,
    entry_points={
        'console_scripts': ['gatk_sv_genotyper=gatk_sv_genotyper.base_cli:main'],
    },
    include_package_data=True,
    zip_safe=False
)