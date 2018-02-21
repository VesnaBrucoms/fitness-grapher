from setuptools import setup, find_packages

from fitness_grapher import service_details

setup(
    name=service_details['name'],
    version=service_details['version'],

    packages=find_packages(),

    install_requires=[
        'google-api-python-client==1.6.5',
        'click==6.7'
    ],

    entry_points={
        'console_scripts': [
            'fitness-grapher = fitness_grapher.__main__:main'
        ]
    }
)
