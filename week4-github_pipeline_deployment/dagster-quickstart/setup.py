from setuptools import find_packages, setup

setup(
    name="dlt-github-openaq",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "dagster",
        "dagster-postgres",
        "dagster-docker",
        "dlt",
        "dlt[snowflake]",
    ],
)