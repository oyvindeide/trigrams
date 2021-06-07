from setuptools import setup, find_packages

setup(
    name="trigrams",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    description="Trigrams",
    use_scm_version=True,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    license="GPL-3.0",
    install_requires=[],
    setup_requires=["setuptools_scm"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "trigram=trigrams.cli:main",
        ],
    },
)
