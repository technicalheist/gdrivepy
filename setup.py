from setuptools import setup

setup(
  name = 'gdrivepy',
  packages = ['gdrivepy'],
  version = '1.9',
  description = 'Simplest way for using google drive api',
  long_description = open('README.rst').read(),
  license = 'MIT',
  author = 'Technical Heist',
  author_email = 'contact@technicalheist.com',
  url = 'https://github.com/technicalheist/gdrivepy.git',
  download_url = 'https://github.com/technicalheist/gdrivepy/archive/1.9.tar.gz',  #updated 1.9
  keywords = ['google drive python','python storage','cloud storage python'],
  install_requires=[
          'google-api-python-client',
          'google-auth-httplib2',
          'google-auth-oauthlib',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)
