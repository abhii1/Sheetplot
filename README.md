# gsheetplots_

>gheetplot is small wrapper around  [Google Sheet API](https://developers.google.com/sheets/) ,[Pandas](https://pandas.pydata.org/) and [Matplotlib](https://matplotlib.org/) provide **access** to [Google Sheet](https://docs.google.com/spreadsheets/u/0/) and help to plot graph with desired axis by user .


To access [Google Sheet](https://developers.google.com/sheets/) one need to [Turn_on_the_API ](#Quickstart)  , download service credinatial JSON file and use ``read_spreadsheet()`` to read spreadsheet and underneath it takes the help of [gspread](https://gspread.readthedocs.io/en/latest/) ,[ServiceAccountCredentials](https://oauth2client.readthedocs.io/en/latest/source/oauth2client.service_account.html) to create connection with [Google Sheet API](https://developers.google.com/sheets/api)  and function convert it into a dataframe which can be used data analysis .


## Table of contents


* [Link](#Link)
* [Installation](#screenshots)
* [Quickstart](#Quickstart)
* [Languages_and_API](#Languages_and_API)
* [See_Also](#See_Also)
* [Contact](#contact)
* [License](#License)


## Link



- [X] GitHub : https://github.com/abhii1/Sheetplot
- [x] PyPi :  https://pypi.org/project/gsheet-plots/0.0.0/
- [x] Documention : https://github.com/abhii1/Sheetplot
- [x] Download : https://github.com/abhii1/Sheetplot


## Installation


This package runs under ``Python 3.5+ `` ,use [pip](https://pip.pypa.io/en/stable/)  to install


     pip install gsheet-plots==0.0.0

 This will install gsheetplot module you need to install [gspread](https://gspread.readthedocs.io/en/latest/)

 Requirements: ``Python 2.7+ or Python 3+``
 ```sh
pip install gspread

```
you  need install oauth2client to use  [ServiceAccountCredentials](https://oauth2client.readthedocs.io/en/latest/source/oauth2client.service_account.html)

 ```sh
pip install oauth2client

```

## Quickstart


Log into the [Google Developers console](https://console.developers.google.com/) with the google account whose spreadsheets you want to access . Create(or select) a project and enable the **Drive APP** and **Sheet API** under (**Google Apps APIs**).

Steps for turn on API

1__ [Go to google API console](https://console.developers.google.com/)

2__  create new project

3__ Click Enable API. Search for and enable the Google Drive API.

4__ Create credentials for a Web Server to access Application Data.

5__ Name the service account and grant it a Project Role of Editor.

6__ Download the JSON file
 7__ Copy the JSON file to your code directory and rename it to client_secret.json

                              this some how its looklike


                              {

                              "type": "service_account",

                              "project_id": "spreadsheet-291117",

                              "private_key_id":_________________,

                              "private_key":  _______ here will be some key,

                              "client_email": "________________,

                              "client_id": __________________________,

                              [auth_uri]("https://accounts.google.com/o/oauth2/auth"),

                              [token_uri]("https://oauth2.googleapis.com/token"),

                              [auth_provider_x509_cert_url]("https://www.googleapis.com/oauth2/v1/certs"),

                              [client_x509_cert_url](https://www.googleapis.com/robot/v1/metadata/x509/spreadsheet%40spreadsheet-291117.iam.gserviceaccount.com"),

                              }

 8__ if you spread sheet is private then you have give drop client_email of JSON file to share with client file


 Create a object to acces member function and convert into dataframe

 ```Python

 #import libary
from plotgraph import GET

 #url of the spreadsheet
connection_url='https://docs.google.com/spreadsheets/d/1077QfadB_V_Nl8-jomsb62RYyrs0_Is-IGlVRl8QF2I/edit?usp=sharing'

#servicecrendiatl JSON file
driveouth_json='spreadsheetouth.json'

#creating a object to access member function
>>> dataframeObj=GET.read_sheet_to_dataframe(connection_url,driveouth_json)

#converting to dataframe
dataframe=dataframeobj.read_spreadsheet()


```

Option for user input

```python

#tuple for X axis and y axis
X,Y=dataframe.select_axis()

```

plot graph with user input

```python
#input from user
>>> X,Y=dataframe.select_axis()

#calling plot function

plot=r.plot_chart(g,X,Y,'line',imagename='test')


```

you can provide range of data example from (200,500)

```python

plot=r.plot_chart(g,X,Y,'line',range=(200,500),imagename='test')

```
imagename is name of image that will saved in system you can make empty also

```python

plot=r.plot_chart(g,X,Y,'line')

```

diffrent kind of plot

```python

#plot kde
plot=r.plot_chart(g,X,Y,'kde')

```


## Languages_and_API


[<img src="https://pluralsight.imgix.net/paths/python-7be70baaac.png?w=70" width="150" height="140">](https://www.python.org/)

[<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSsIK2jA5rNj9I7ttMIgAReruBAkUKOPVRr6g&usqp=CAU" width="150" height="140">](https://developers.google.com/drive)

[<img src="https://api.framer.com/store/assets/aroagb/google-sheet-component/artwork.png?ZDg0MzF" width="150" height="140">](https://developers.google.com/sheets/api)



## See_also


* [Google Sheets API]( https://developers.google.com/sheets/) : Read, write, and format data in Sheets. The latest version of the Sheets API lets developers programmatically

* [Pandas](https://pandas.pydata.org/) : pandas is a software library written for the Python programming language for data manipulation and analysis

* [gspread](https://gspread.readthedocs.io/en/latest/) : Python wrapper, currently using the XML-based ``legacy v3 API`` example ``Jupyter notebook`` using gspread_ to fetch a sheet into a pandas DataFrame

* [matplotlib](https://matplotlib.org/) : Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy




## Contact


Created by Abhishek pratap singh

[<img src="https://cdns.iconmonstr.com/wp-content/assets/preview/2012/240/iconmonstr-linkedin-3.png" width="42" height="42">](https://www.linkedin.com/in/abhishek-pratap-singh-44a96816b/)

[<img src="https://9to5google.com/wp-content/uploads/sites/4/2016/08/gmail-logo.png?w=1280" width="42" height="42">](abhisheklumiamicro@gmail.com)


## License

This package is distributed under the `MIT license`_.
