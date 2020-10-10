'''

            class read_sheet_to_dataframe:# convert to DataFrame
                                          function:
                                                  read_spreadsheet(spreadsheet_url,driveouth_json)

                                                  ** spreadsheet_url : url spreadsheet in google drive

                                                                          before url you need give permission for api access for both drive and sheet

                                                                                steps :
                                                                                     1__ Go to google API console

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
                                                                                         "private_key_id":_________________
                                                                                         "private_key":  _______ here will be some key
                                                                                         "client_email": "________________
                                                                                         "client_id": __________________________,
                                                                                         "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                                                                                         "token_uri": "https://oauth2.googleapis.com/token",
                                                                                         "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                                                                                         "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/spreadsheet%40spreadsheet-291117.iam.gserviceaccount.com"
                                                                                       }

                                                                                       8__ if you spread sheet is private then you have give drop client_email of JSON file to share with client file

                                                                                             refrence :
                                                                                                       Thanks to https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html




                                       driveouth_json =jason file you have downloaded




                                    select_axis(self):
                                           used to select axis for ploting



                                           function:
                                                plot_chart(dataframe,X,Y,type='line',range=(0,100),legend='True',logx=False,logy=False,loglog=False,color='black',linestyle='-',linewidth=2,marker='o',markersize=10):


                                                         * dataframe is dataframe used for ploting or return of readdata for more information check readdata module

                                                         ** X = name of  X_axis

                                                         *** Y= name of Y_axis

                                                         *** range

                                                                default start =0 and end= 100

                                                                  but can be change to full lenght or some range as per convince

                                                       *** imagename #name of image

                                                        **** legend :
                                                                   default:True
                                                                      value can true or False

                                                        ****    logx:
                                                                    default False
                                                                        value can true or False

                                                                        converge value of x axis by log

                                                        *****   logy:
                                                                    default False
                                                                        value can true or False

                                                                        converge value of y axis by log


                                                        ******  loglog:
                                                                        default False
                                                                            value can true or False

                                                                            converge value of x and y  axis by log


                                                        ******* color:
                                                                         default=black
                                                                               can use any color in RGB ,RGBA more information
                                                                               ++++goto matplotlib
                                                                                      https://matplotlib.org/3.1.1/tutorials/colors/colors.html

                                                        ****** linestyle:
                                                                        default='-'
                                                                        can use any linestyle present in matplot
                                                                        https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html

                                                        ******* linewidth=4:

                                                                                     default 4
                                                                                        any numeric value

                                                        ******* marker='o'

                                                                       default = '.'

                                                                       but can use any marker in matplotlib
                                                                       https://matplotlib.org/api/markers_api.html


                                                        ***** markersize=10

                                                                        default=10
                                                                        any numeric value

'''


import gspread #for more information https://gspread.readthedocs.io/

import pandas #importing pandas for more information https://pandas.pydata.org/

from oauth2client.service_account import ServiceAccountCredentials #importing service account credentials for oauth2



class read_sheet_to_dataframe:


    def __init__(self,spreadsheet_url,driveouth_json):
        self.spreadsheet_url=spreadsheet_url
        self.driveouth_json=driveouth_json

    def read_spreadsheet(self):

        scope = ['https://www.googleapis.com/auth/drive'] # type of access read write

        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.driveouth_json, scope) #building connection


        client = gspread.authorize(credentials) #authirization

        spreadsheet_object = client.open_by_url(self.spreadsheet_url).sheet1 #open sheet

        return pandas.DataFrame(spreadsheet_object.get_all_records()) #converting data into dataframe

    def select_axis(self): #start of function

        print('\t Select x axis :')
        print('\n')
        X_axis=input() #input for x axis
        print('\n')
        print('Select y axis')
        print('\n')
        Y_axis=input() #input for y axis

        return X_axis,Y_axis #return
    def plot_chart(self,dataframe,X,Y,type='',range=(0,100),imagename='',legend='True',logx=False,logy=False,loglog=False,color='black',linestyle='-',linewidth=4,marker='.',markersize=10): #start of function body
        start,end=range #(unpacking of tuple)

        dataframe=dataframe[start:end+1]

        import matplotlib.pyplot as plt #importing matplot lib for move information go for https://matplotlib.org/


        plt.style.use('seaborn-dark') # style sheet type for more information go for https://matplotlib.org/3.1.0/gallery/style_sheets/style_sheets_reference.html

        fig, ax = plt.subplots(figsize=(100,40)) #figsize of plot

        

        plot=dataframe.plot(kind=type,x=X,y=Y,ax=ax,legend=legend,logx=logx,logy=logy,loglog=loglog,color=color,linestyle=linestyle,linewidth=linewidth,marker=marker,markersize=markersize) #plot of dataframe

        plt.xlabel(X,fontsize=80,fontname='fantasy')
        plt.ylabel(Y,fontsize=80,fontname='fantasy')
        plt.legend(prop={"size":90})

        ax.yaxis.tick_right()

        plt.xticks(fontsize=80)
        plt.yticks(fontsize=80)
        plt.tight_layout()
        if(len(imagename)>0):
            plt.savefig(imagename)
        plt.show()
        return plot #returning plot axis
