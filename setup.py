from setuptools import setup, find_packages

setup(
    name='minimath',
    version='0.1.0',
    description='A minimal Python library for mathematical functions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='CYCNO',
    url='https://github.com/CYCNO/minimath',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
