from setuptools import find_packages

DISTNAME = "grplot"
VERSION = "1.0.6"
MAINTAINER = "Ghiffary Rifqialdi"
MAINTAINER_EMAIL = "grifqialdi@gmail.com"
DESCRIPTION = "grplot: lazy statistical data visualization"
LICENSE = "BSD (3-clause)"
URL = "https://github.com/ghiffaryr/grplot"
PROJECT_URLS = {
                "Bug Tracker": "https://github.com/ghiffaryr/grplot/issues"
               }
CLASSIFIERS = [
               "Intended Audience :: Science/Research",
               "Programming Language :: Python :: 3.10",
               "Programming Language :: Python :: 3.11",
               "Programming Language :: Python :: 3.12",
               "Programming Language :: Python :: 3.13",
               "License :: OSI Approved :: BSD License",
               "Topic :: Scientific/Engineering :: Visualization",
               "Topic :: Multimedia :: Graphics",
               "Operating System :: OS Independent",
               "Framework :: Matplotlib",
              ]
DOWNLOAD_URL = "https://github.com/ghiffaryr/grplot"
PYTHON_REQUIRES = ">=3.10"
INSTALL_REQUIRES = [
    "numpy>=1.20, !=1.24.0",
    "pandas>=1.2",
    "matplotlib>=3.4, !=3.6.1",
    "ipython",
]
PACKAGES = find_packages(include=["grplot*", "grplot_seaborn*"],
                         exclude=["tests*", "docs*"])

if __name__ == "__main__":

    from setuptools import setup

    import sys
    if sys.version_info[:2] < (3, 10):
        raise RuntimeError("grplot requires python >= 3.10.")

    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setup(
        name=DISTNAME,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=long_description,
        long_description_content_type="text/markdown",
        license=LICENSE,
        url=URL,
        project_urls=PROJECT_URLS,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        python_requires=PYTHON_REQUIRES,
        install_requires=INSTALL_REQUIRES,
        packages=PACKAGES,
        classifiers=CLASSIFIERS
    )