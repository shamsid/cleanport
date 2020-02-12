import setuptools
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here,"README.md"),encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
        name="cleanport",
        version="1.0.0",
        author="Shamsher Ahmed",
       author_email='hi@shamsherahmed.in',
        description="A package to free port",
        long_description=long_description,
        long_description_content_type="text/markdown",
        #packages="src",
        scripts=['src/cleanport'],
        url="https://github.com/shamsid/cleanport",
        package_dir={'': 'src'},
        packages=setuptools.find_packages(where='src'),
        keywords='port-clean process-kill development',
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: MIT License",
            "Operating System :: OS Independent",
        ],
        project_urls={  # Optional
                'Bug Reports': 'https://github.com/shamsid/cleanport/issues',
                'Source': 'https://github.com/shamsid/cleanport',
        },
)


