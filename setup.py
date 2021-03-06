from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="xlsxgrep",
    version="0.0.23",
    description="CLI tool to search text in XLSX and XLS files. It works similarly to Unix\GNU Linux grep",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/zazuum/xlsxgrep",
    author="Ivan Cvitic",
    author_email="cviticivan@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
	    "Intended Audience :: Education",
	    "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["xlsxgrep"],
    include_package_data=True,
    install_requires=["pyexcel-xls", "pyexcel-xlsx", "pyexcel-ods3", "pyexcel-ods"],
    entry_points={
        "console_scripts": [
            "xlsxgrep=xlsxgrep.xlsxgrep:main",
        ]
    },
)
