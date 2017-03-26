from setuptools import setup

setup(name='wordlist_passphrase_generator',
  version='0.1',
  description='Simple wordlist-based passphrase generator using EFF\'s long wordlist.',
  url='https://github.com/rnackman/wordlist-passphrase-generator',
  author='Rachel Nackman',
  author_email='rachel.nackman@gmail.com',
  license='MIT',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python :: 2',
    'Topic :: Security',
  ],
  packages=['wordlist_passphrase_generator'],
  install_requires=[
    'requests'
  ],
  scripts=['bin/wordlist-passphrase-generator'],
  zip_safe=False)
