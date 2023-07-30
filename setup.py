from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='py_dark_web_scraper',
    version='0.1',
    description='A dark web link and image scraper',
    author= 'Pritam Sarbajna',
    url = 'https://github.com/PritamSarbajna/py-dark-web-scraper',
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['darkweb', 'web scraper', 'scraper'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.10',
    py_modules=['py_dark_web_scraper'],
    package_dir={'':'src'},
    install_requires = [
        'requests',
        'faskeuser_agent',
        'beautifulsoup4'
    ]
)
