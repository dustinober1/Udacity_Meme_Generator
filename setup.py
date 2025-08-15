from setuptools import setup, find_packages

setup(
    name="meme-generator",
    version="1.0.0",
    description="A multimedia application to dynamically generate memes",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "Flask>=3.0.0",
        "Pillow>=10.0.1",
        "requests>=2.31.0",
        "pandas>=2.1.1",
        "python-docx>=0.8.11",
        "PyMuPDF>=1.23.4",
    ],
    entry_points={
        "console_scripts": [
            "meme-generator=meme:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)