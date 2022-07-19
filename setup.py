import setuptools

setuptools.setup(
    name='related-ontologies',
    version='0.0.1',
    description='A package to generate related clinical ontologies (LOINC, SNOMED-CT)',
    url='https://github.com/justin13601/related-ontologies',
    author='Justin Xu',
    author_email='justin13601@hotmail.com',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy>=1.19.2', 'pandas>=1.1.3',
        'pytest>=4.2.0', 'scikit-learn>=0.23.2'
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': ['related-ontologies = related-ontologies.__main__:main'],
        'related-ontologies.__main__':
            [
                'apply = related-ontologies.__main__:apply',
                'download = related-ontologies.__main__:download'
            ]
    },
)