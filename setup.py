from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ciet/__init__.py
from ciet import __version__ as version

setup(
	name="ciet",
	version=version,
	description="college project",
	author="Naveen",
	author_email="naveens10102002@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
