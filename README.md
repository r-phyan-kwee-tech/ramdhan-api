
# ramdan-api  
A collection of the ramdan timetables of the different states from Myanmar.
  
  
## Installing Requirements  
Use Virtualenv and install the packages.  
```  
pip install -r requirements.txt  
```  
## Creating a new Database  
Create a database(Used SQLite) with the table structure mentioned in *struct.sql\* and update the database name in *database.py\* file.  
```  
database.py  
  
# Replace 'sqlite:///ramdan.db' with your path to database  
  
engine = create_engine('sqlite:///ramdan.db', convert_unicode=True)  
  
```
## Running Flask Server  
Go to the root dir and run the below line in the terminal.  
```  
python app.py  
```  
Browse to http://localhost:5000/api

## Development Orchestration
Make sure you have to install docker in your machine.
If you haven't install docker here is [how to](https://docs.docker.com/get-started/) 
After installation of Docker please follow steps below.
1. Go to your project folder from terminal 
 2. First remove the docker image if you already have one before.If you don't have any previous build skip directly to step 2

	```
	docker rm ramdan_api 
	```
	
3. Then build the docker image 
	```
	docker build ./ -t ramdan_api
	```
4. Then run the image
	```
	docker run --name ramdan_api -p 80:5000 ramdan_api
	```
5. Browse to http://localhost/api


## Usage
After Spinning up your docker and you will be able to see the Graphiql query editor. And paste the following query by replacing respective `object_id`

### Query Countries

 

     {
      countries(limit: 1, page: 1) {
        data {
          id
          objectId
          name
          createdDate
          updatedDate
        }
      }
    }

### Query SingleCountry

    {
      country(countryId: "147ed0930ae5469abdea3ac39b1edb5c") {
        id
        objectId
        name
        createdDate
        updatedDate
      }
    }
### Query States

    {
      states(limit: 1, page: 1, countryId: "147ed0930ae5469abdea3ac39b1edb5c") {
        data {
          id
          objectId
          nameMmUni
          nameMmZawgyi
          countryId
          createdDate
          updatedDate
        }
      }
    }
 ### Query Single State
 

    {
      state(stateId: "4e24be73d6e74aceaa609cd1118cce38") {
        id
        objectId
        nameMmUni
        nameMmZawgyi
        countryId
        createdDate
        updatedDate
      }
    }
### Query Days(TimeTable Days)

    {
      days(limit: 50, page: 1, stateId: "4e24be73d6e74aceaa609cd1118cce38") {
        data {
          id
          objectId
          day
          dayMm
          calendarDay
          hijariDay
          sehriTime
          iftariTime
          isKadir
          countryId
          stateId
          createdDate
          updatedDate
        }
      }
    }
### Query Single  Day (TimeTable Day)

    {
      day(dayId: "28494ac2030146ac80fc6a8b1b2fb9e1") {
        id
        objectId
        day
        dayMm
        calendarDay
        hijariDay
        sehriTime
        iftariTime
		sehriTimeDesc
        iftariTimeDesc
		sehriTimeDescMmUni
		sehriTimeDescMmZawgyi
		iftariTimeDescMmZawgyi
		iftariTimeDescMmUni
        isKadir
        countryId
        stateId
        createdDate
        updatedDate
      }
    }
