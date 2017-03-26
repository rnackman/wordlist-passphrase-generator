from setuptools import setup

setup(name='eff_passphrase_generator',
  version='0.1',
  description='Simple passphrase generator using EFF long wordlist.',
  url='https://github.com/rnackman/eff-passphrase-generator',
  author='Rachel Nackman',
  author_email='rachel.nackman@gmail.com',
  license='MIT',
  packages=['eff_passphrase_generator'],
  install_requires=[
    'requests'
  ],
  scripts=['bin/eff-passphrase-generator'],
  zip_safe=False)
