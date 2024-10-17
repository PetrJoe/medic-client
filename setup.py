from setuptools import setup, find_packages

setup(
    name='medic-client',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Akanmu Akinkunmi Joseph',
    author_email='petrjoe01@gmail.com',
    description='A client library for interacting with the medic API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/petrjoe/medic-client',
)
