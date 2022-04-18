from setuptools import setup

VERSION = "0.1"

setup(
    name="datasette-meteor-map",
    description="A Datasette plugin for visualizing meteor trajectories on leaflet "
                "maps",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License"
    ],
    version=VERSION,
    packages=["datasette_meteor_map"],
    entry_points={"datasette": ["meteor_map = datasette_meteor_map"]},
    install_requires=["datasette>=0.54", "datasette-leaflet>=0.2.2"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    package_data={
        "datasette_meteor_map": ["static/*", "templates/*"]
    },
    python_requires=">=3.7",
)
