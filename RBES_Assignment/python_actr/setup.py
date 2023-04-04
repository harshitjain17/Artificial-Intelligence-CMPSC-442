from setuptools import setup, find_packages

import python_actr

setup(
    name='python_actr',
    #packages=['python_actr', 'python_actr.display', 'python_actr.actr', 'python_actr.ui', 'python_actr.lib'],
    packages=find_packages(),
    version=python_actr.version.version,
    author='Carleton Cognitive Modelling Lab (Original), Penn State THiCC Lab (Mods)',
    description='Python implementation of the ACT-R cognitive architecture',
    url='https://github.com/CarletonCognitiveModelingLab/python_actr',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        ]
    )
