from setuptools import setup

setup(
   name='remote-commands-servers',
   version='1.0',
   description='Run remote ssh commands on multiple servers',
   author='DennyZhang',
   author_email='contact@dennyzhang.com',
   packages=['remote-commands-servers'],  #same as name
   install_requires=['paramiko'], #external packages as dependencies
)
