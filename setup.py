from setuptools import setup, find_packages

setup(
    name="finances",
    version="1.0.0",
    description="Pacote para gerenciamento de finanças pessoais",
    author="Rodolfo Rodrigues",
    author_email="rorcf2010@gmail.com",
    packages=find_packages(), 
    install_requires=[],  
    classifiers=[
        "Programming Language :: Python :: 3.1.1",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",  
)