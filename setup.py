from setuptools import find_packages, setup

setup(
    name="my-stocks",
    version="0.0.1",
    author="Avinash Raj",
    author_email="avistylein3105@gmail.com",
    description="This is a simple PySide6 application that allows users to keep track of the stocks they own and their performance.",
    packages=find_packages(),
    include_package_data=True,
    keywords=["python", "pyside", "pyqt", "stocks", "finance"],
    install_requires=["poetry-core", "PySide6==6.5.0", "yfinance==0.2.18", "currencyconverter==0.17.7"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
)
