from setuptools import setup, find_packages

setup(
    name='minimath',  # Name of the package
        version='0.1.0',  # Version of the package
        description='A minimal Python library for mathematical functions',  # Short description
        long_description=open('README.md').read(),  # Detailed description from README.md
        long_description_content_type='text/markdown',  # Ensure it’s treated as Markdown
        author='Your Name',  # Your name
        author_email='your.email@example.com',  # Your email
        url='https://github.com/yourusername/minimath',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
