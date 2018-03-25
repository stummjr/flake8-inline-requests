# coding: utf-8
import setuptools


setuptools.setup(
    name='flake8-inline-requests',
    license='MIT',
    version='0.0.1',
    description='Plugin to catch inline_requests without handle_httpstatus_all',
    author='Valdir Stumm Junior',
    author_email='stummjr@gmail.com',
    url='http://github.com/stummjr/flake8-inline-requests',
    py_modules=['flake8_inline_requests'],
    entry_points={
        'flake8.extension': [
            'SIR00 = flake8_inline_requests:InlineRequestsChecker',
        ],
    },
    install_requires=['flake8'],
    tests_require=['pytest'],
    classifiers=[
        'Framework :: Flake8',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
