from setuptools import setup, find_packages


def readme():
      with open("README.md", encoding="utf-8") as f:
            return f.read()


setup(name="mapnlp",
      version="0.1.0",
      description="managing pipelines of algorithms in NLP",
      long_description=readme(),
      install_requires=[],
      url="",
      packages=find_packages()
)
