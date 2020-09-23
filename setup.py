import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weather_app_cjhsu", # Replace with your own username
    version="0.0.1",
    author="Chia-Jung Hsu",
    author_email="chiajung@chalmers.se",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cjhsu/weather_app",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3 License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts":[
            "smhpy=weather_app.app:smhpy"
        ]
    },
    python_requires='>=3.7',
)
