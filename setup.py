from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='mudbrick',
    version='0.0.2',
    url='https://github.com/owen-eternal/flask-bucket',
    author_email='olwethuphakade89@gmail.com',
    description='Mudbrick Builds a flask application factory boilerplate.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='BSD',
    author='Owen O. Phakade',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'flask',
        'flask-Sqlalchemy'
    ],

    entry_points={
        'console_scripts': ['mudbrick=mudbrick.commands:main']
    },

    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
) 