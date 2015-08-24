from setuptools import setup


setup(
    name='flake8-future',
    version='0.1',
    description='A flake8 plugin to warn when any file is missing certain '
                '__future__ imports.',
    url='https://github.com/kmaglione/flake8-future',

    author='Kris Maglione',
    author_email='maglione.k@gmail.com',

    license='MIT',

    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Software Development :: Testing',
                 'Programming Language :: Python :: 2.7'],

    py_modules=['flake8_future'],
    entry_points={'flake8.extension': ['F48 = flake8_future:CheckFutures']},
)
