import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="adl-recognition",
    version="0.0.1",
    author="Rivindu Madushan <rivindum.15@cse.mrt.ac.lk>, Danushka Madhuranga <danushka.15@cse.mrt.ac.lk>, Chathuranga Siriwwardana <chathuranga.15@cse.mrt.ac.lk>",
    author_email="rivindum.15@cse.mrt.ac.lk",
    description="Classification of Activities of Daily Living(ADL) using depth videos and audio",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RivinduM/AdlRecognition",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
    include_package_data=True
)
