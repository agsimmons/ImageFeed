from setuptools import setup, find_packages

setup(
    # Package Metadata
    name='ImageFeed',
    version='1.0.0',
    description='Expose a VideoCapture image sequence through a web server',
    url='https://github.com/agsimmons/ImageFeed',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],

    packages=find_packages(),
    data_files=[
        ('', ['config.json']),
    ],

    entry_points={
        'console_scripts': [
            'imagefeed = imagefeed.__main__:main'
        ]
    },

    author='Andrew Simmons',
    author_email='agsimmons0@gmail.com'
)
