from setuptools import find_packages, setup

setup(
    name="inter_pixpy_samueljansem",
    version="0.0.1",
    description="A Python package to interact with the Banco Inter's Pix API",
    author="Samuel Jansem",
    author_email="samuel.jansem@gmail.com",
    url="https://github.com/samueljansem/inter-pixpy",
    license="MIT",
    keywords=["pix", "inter", "bank", "api", "python", "sdk"],
    packages=find_packages(),
    include_package_data=True,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "requests",
    ],
    python_requires=">=3",
    project_urls={
        "Source Code": "https://github.com/samueljansem/inter-pixpy",
        "Issues": "https://github.com/samueljansem/inter-pixpy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)