from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in purshase_order/__init__.py
from purshase_order import __version__ as version

setup(
	name="purshase_order",
	version=version,
	description="send a purchase order via email, or whatsapp app on phone",
	author="monir",
	author_email="mnyrskyk@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
