
from setuptools import setup, find_packages

setup(
    name='perception_evaluation',
    version='0.1.0',
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        'numpy',
        'pyyaml',
        'matplotlib',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'perception-eval=perception_evaluation.core.pipeline:main',
        ],
    },
)
