from setuptools import setup, find_packages

setup(name='trygrammar',
      version=open('VERSION').read(),
      description='Tryal.AI Grammar',
      author='Adam Green',
      author_email='neergmada@outlook.com',
      url='https://tryal.ai/',
      packages=find_packages(),
      install_requires=["monkeys-typewriter"],
      include_package_data=True
)
