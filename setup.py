from setuptools import setup, find_packages

setup(
    name='network_intelligence',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'psutil',
        'requests',
        'PyYAML'
    ],
    entry_points={
        'console_scripts': [
            'network-intelligence = network_intelligence.main:main',
        ],
    },
    author='Dobry Nikolov',
    author_email='dobry989@gmail.com',
    description='Network Intelligence Application to gather network connection information and check it against threat intelligence platforms.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bovf/network-intelligence',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
