import re, io
from setuptools import setup, find_packages

# Load version from module (without loading the whole module)
with open('src/python_ms_excel/__init__.py', 'r') as fo:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fo.read(), re.MULTILINE).group(1)

# Read in the README.md for the long description.
with io.open('README.md', encoding='utf-8') as fo:
    long_description = fo.read()

setup(
    name='python_ms_excel',
    version=version,
    url='https://github.com/jameswpriceio/python_ms_excel',
    author='James Price',
    author_email='jwp@jameswprice.io',
    description=('This package installs apps as described in README.md'),
    long_description=long_description,
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    license='MIT',
    install_requires=[
        'send2trash==1.5.0',
        'requests==2.21.0',
        'beautifulsoup4==4.7.1',
        'selenium==3.141.0',
        'openpyxl==2.6.1',
        'PyPDF2==1.26.0',
        'python-docx==0.8.10',
        'imapclient==2.1.0',
        'pyzmail36==1.0.4',
        'twilio',
        'ezgmail',
        'ezsheets',
        'pyinputplus',
        'pillow==6.0.0',
        'pyautogui',
    ],
    keywords="python microsoft excel automation",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: ',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Ubuntu 20.04',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)