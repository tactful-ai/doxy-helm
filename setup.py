from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='helm2readme',
    version='1.1.4',
    description='helm2readme is a command-line utility designed to streamline the process of creating comprehensive documentation for Helm charts. Helm charts provide a convenient way to package and deploy Kubernetes applications, but documenting their configurations can be time-consuming. Doxy-Helm automates this task by extracting information from Helm charts values files and templates and generating Markdown documentation.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Yousef Alwaer',
    author_email='elwaeryousef@gmail.com',
    url='https://github.com/tactful-ai/helm2readme',
    packages=find_packages(),
    install_requires=[
        'argparse',
        'typing',
        'markdown',
        'pyyaml'
    ],
    entry_points={
        'console_scripts': [
            'helm2readme = pkg.runner:full_run'
        ]
    },
)
