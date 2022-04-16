from setuptools import setup, find_packages

setup(
    name="slack_async_alert",
    version="1.0.2",
    packages=find_packages(),
    package_data={'slack_async_alert': ['slrt']},
    url="https://github.com/gudwns1215/slack_async_alert",
    install_requires=[
        "slack-sdk>=3.11.1",
        "typer>=0.4.0",
        'python_version >= "3.5"',
        "InquirerPy>=0.3.0",
    ],
    include_package_data=True,
    script=["slack_async_alert"],
    entry_points={
        "console_scripts": [
            "slrt-configure = slack_async_alert.configure:set_configure"
        ],
    },
)
