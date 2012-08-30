from setuptools import setup


setup(
    name='Flask-TokenAuth',
    version='0.0.1',
    url='https://github.com/maxcountryman/flask-login',
    license='MIT',
    author='Matthew Frazier',
    author_email='leafstormrush@gmail.com',
    description='User session management for Flask',
    long_description=__doc__,
    py_modules=['flask_login'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    tests_require=['Attest'],
    test_loader='attest:auto_reporter.test_loader',
    test_suite='tests.login.login'
)
