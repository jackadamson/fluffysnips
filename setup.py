import setuptools

setuptools.setup(
    name="fluffysnips",
    version="0.0.1",
    author="Jack Adamson",
    description="Various useful CLI tools",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "mvscreenshot=fluffysnips.mvscreenshot:main",
        ]
    },
)
