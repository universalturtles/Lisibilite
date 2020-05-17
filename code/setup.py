from setuptools import setup

setup(
    # Ref: https://packaging.python.org/guides/distributing-packages-using-setuptools/#setup-args
    # Ref: https://docs.python.org/3/distutils/setupscript.html
    name='lisibilite',
    version='1.0.0',
    packages=['utils', 'utils.io', 'utils.lexis', 'utils.helpers', 'utils.encoding', 'config', 'models', 'lisibilite',
              'customexceptions'],
    url='',
    license='MIT',
    author='UniversalTurtles',
    author_email='',
    description='A Util for calculating the readability Metrics',
    classifiers=[
        # Ref: https://pypi.org/classifiers/
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS"
    ],
    install_requires=[
        "joblib==0.14.1",
        "nltk==3.5",
        "PyYAML==5.3.1",
        "regex==2020.5.7",
        "tqdm==4.46.0",
        "syllables==0.1.0"
    ],
    python_requires='>=3'
)
