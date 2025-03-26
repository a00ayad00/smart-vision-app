from setuptools import setup, find_packages


__version__ = '0.1'
ProjectName = "deformity_detection"
AuthorUserName = "a00ayad00"
AuthorEmail = "3bdullah3yad@gmail.com"
RepoName = "Visual-Deformity"


setup(
    name=ProjectName,
    version=__version__,
    license="MIT",
    author=AuthorUserName,
    author_email=AuthorEmail,
    description="Python package to detect road deformaties",
    long_description_content="text/markdown",
    url=f"https://github.com/{AuthorUserName}/{RepoName}",
    packages=find_packages()
)