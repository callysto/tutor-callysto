import io
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.rst"), "rt", encoding="utf8") as f:
    readme = f.read()

about = {}
with io.open(os.path.join(here, "tutor_callysto", "__about__.py"), "rt", encoding="utf-8") as f:
    exec(f.read(), about)


setup(
    name="tutor-callysto",
    version=about["__version__"],
    url="https://callysto.ca",
    project_urls={
        "Documentation": "https://github.com/callysto/tutor-callysto",
        "Code": "https://github.com/callysto/tutor-callysto",
        "Issue tracker": "https://github.com/callysto/tutor-callysto",
        "Community": "https://github.com/callysto/tutor-callysto",
    },
    license="Apache",
    author="Callysto",
    author_email="sysadmin@callysto.ca",
    description="Custom modifications for the Callysto project",
    long_description=readme,
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.5",
    entry_points={"tutor.plugin.v0": ["tutor_callysto = tutor_callysto.plugin"]},
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
