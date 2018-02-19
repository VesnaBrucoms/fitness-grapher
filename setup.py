from setuptools import setup, find_packages

from fitness-grapher import service_details

setup(
    name=service_details['name'],
    version=service_details['version'],

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'fitness-grapher = fitness-grapher:main'
        ]
    }
)
