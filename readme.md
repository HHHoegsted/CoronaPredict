# CORONAPREDICT

An attempt of making a predictor of tomorrows new corona cases in Denmark, based on numbers from Statens Seruminstitut.

## Datasource

Todays data is available to the public from [ssi.dk](https://www.ssi.dk/sygdomme-beredskab-og-forskning/sygdomsovervaagning/c/covid19-overvaagning/arkiv-med-overvaagningsdata-for-covid19) every day at 14:00 danish time. 

## Flow

So far, I have programmed individual python files, that will 

- Download individual .zip-files
- Unzip the files into folders 
- Get relevant data from the files and print out a list of dates and total cases (not counting cases that are subsequently free from infection)

## Future

The plan is to modify the data further, so the numbers also include new cases today (as opposed to total number of positive tests so far), and implement a predictor algoritm.

## Creator

[Hans-Henrik Høgsted](hh.hoegsted@gmail.com)