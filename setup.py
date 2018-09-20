import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tomark",
    version="0.1.4",
    author="Joel Dare",
    author_email="joel@joeldare.com",
    description="Convert a list of dictionaries to a markdown formatted table.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codazoda/tomark",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Markup',
        'Operating System :: OS Independent',
    ],
)