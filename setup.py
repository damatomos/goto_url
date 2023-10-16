from setuptools import setup
setup(
    name = 'to',
    version = '0.1.0',
    packages = ['extension'],
    entry_points = {
        'console_scripts': [
            'to = extension.__main__:main'
        ]
    })
