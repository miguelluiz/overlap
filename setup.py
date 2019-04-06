import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='xLineOver',  
     version='0.1',
     scripts=['xLineOver'] ,
     author="Miguel Almeida",
     author_email="mplabdev@gmail.com",
     description="Check whether two lines A (x1,x2) and B (x3,x4) on the x-axis whether they overlap or not",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/miguelluiz/overlap",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )