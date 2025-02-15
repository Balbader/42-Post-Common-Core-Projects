from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    author="baalbade",
    author_email="baalbade@student.42.fr",
    description="A sample test package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Balbader/42-Post-Common-Core-Projects\
        /tree/main/python_for_data_science/0_Starting/ex09/ft_package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
