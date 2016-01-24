from setuptools import setup

setup(
    name='socials-preview',
    version='1.0.0',
    description='Simple socials share preview by Python',
    url='https://github.com/namnv609/python-socials-preview',
    author='NamNV609',
    author_email='namnv609@gmail.com',
    license='MIT',
    packages=['socials-preview'],
    install_requires=[
        'bottle',
        'requests',
        'beautifulsoup4',
        'html5lib',
    ]
)
