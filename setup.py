from setuptools import setup
import re


with open('README.md') as f:
    long_description = f.read()

with open('PyLMQ/version.py', 'r', encoding='utf-8') as f:
    version = re.search(r"^__version__\s*=\s*'(.*)'.*$", f.read(), flags=re.MULTILINE).group(1)

setup(
    name='PyLMQ',
    version=version,
    packages=['PyLMQ'],
    description='Python Library for LMQ',
    long_description=long_description,
    author='Misam saki',
    author_email='misamplus@gmail.com',
    url='https://github.com/misamplus/PyLMQ',
    install_requires=['requests'],
    license='Proprietary',
    classifiers=[
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Development',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers'
    ]
)
