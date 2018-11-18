import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system's.
sys.path.pop(0)
from setuptools import setup
sys.path.append("..")
import sdist_upip

setup(name='micropython-ssd1306',
      version='0.2',
      description='ssd1306 module for MicroPython',
      long_description="",
      url='https://github.com/stlehmann/micropython-ssd1306',
      author='Stefan Lehmann',
      author_email='stlm@posteo.de',
      maintainer='Stefan Lehmann',
      maintainer_email='stlm@posteo.de',
      license='MIT',
      cmdclass={'sdist': sdist_upip.sdist},
      py_modules=['ssd1306'])
