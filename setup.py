from setuptools import setup

setup(
    name="web_to_csv",
    packages=["web_to_csv"],
    include_package_data=True,
    install_requires=["flask", "python-dotenv"],
)
