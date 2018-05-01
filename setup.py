import setuptools

setuptools.setup(
    name="pygrowthmodels",
    version="0.0.3",
    url="https://github.com/drodriguezperez/pygrowthmodels.git",

    author=u"Daniel Rodríguez Pérez",
    author_email="daniel.rodriguez.perez@gmail.com",

    license='GPL-3',

    description="A compilation of nonlinear growth models",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
