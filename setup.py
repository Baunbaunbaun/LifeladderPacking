from setuptools import find_packages, setup

setup(
    name='lifeladderpacking',
    version='1.0.3',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
	    'binpacking',
    ],
)
