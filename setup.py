from setuptools import setup


setup(
    name='Flask-Tokenauth',
    version='0.0.1',
    url='https://github.com/drusskikh/flask-tokenauth',
    license='MIT',
    author='Dmitry Russkikh',
    author_email='d.pycckux@gmail.com',
    description='User session management for Flask',
    py_modules=['flask_tokenauth'],
    zip_safe=False,
    platforms='any',
    install_requires=['Flask']
)
