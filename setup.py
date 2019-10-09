import setuptools
from distutils.core import setup


setup(
    name='pySerasa',
    version='0.1',
    license='MIT license',
    packages=['pyserasa'],
    url='https://github.com/kmee/pySerasa',
    author='KMEE',
    author_email='contato@kmee.com.br',
    description='Modulo para consulta de string de dados SERASA',
    setup_requires=['wheel'],
    install_requires=[
	'requests', 'locales',
    ],

)
