import  setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
      name='gsheet_plots',
      version='0.0.0',
      url='https://github.com/abhii1/gsheetplot',
      author='abhishek pratap singh',
      author_email='abhisheklumiamicro@gmail.com',
      description='gsheet will help to create your connection between google sheet and python through API and help to plot graph by you choice',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=setuptools.find_packages(),
      install_requires=['gspread','oauth2client'],
      classifiers=["Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.6",
                   "Operating System :: OS Independent"],
      python_requires='>=3.6'
      )
