# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 22:42:52 2022

@author: Asus
"""

from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Basics computational methods',
  version='0.0.1',
  description='maths algorithms',
  url='',  
  author='Thomas Gomez',
  author_email='t.gomezs2@uniandes.edu.co',
  license='MIT', 
  classifiers=classifiers,
  keywords='computational methods', 
  packages=find_packages(),
  install_requires=['numpy','scipy','statistics'] 
)
