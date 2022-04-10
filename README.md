

### Overview
Regional Weather forecast APIs to get weather related data. API key is required. 

You can start using it immediately!

### Features
- Weather forecast for 30 days
- Location-wise weather forecast available
- Provide date-wise weather description
- Get list of all the available regions

### Endpoints
Different endpoints available in the <b>weather_api</b>
<ol>
    <li><b>http://localhost:5000/forecast/location_list</b>
        <br>
            List all the available locations to get weather forecast.
        <br>
    </li>
    <li>
    <b>http://localhost:5000/forecast/&lt;location-id&gt;</b>
        <br>
            Return weather forecast for specific region 
        <br>
    </li>
    <li>
    <b>http://localhost:5000/forecast/</b>
        <br>
        Return weather forecast for all the available regions
        <br>
    </li>
</ol>

### Installation
##### 1. Git clone the application

##### 2. Create a virtual environment inside the application 

```

    virtualenv -p /usr/bin/python3 venv    

    source venv/bin/activate

```

##### 3. Install Python modules

```

   pip3 install -r requirements.txt 
    
```


##### 4. Run the application using

```

    python app.py

```


##### 5. You will get below REST API

```

    http://localhost:5000/forecast/location_list
    http://localhost:5000/forecast/
    http://localhost:5000/forecast/<location-id>

```

##### 6. Using Docker commands

```
    
        // List all running container
        docker ps

        // list all containers
        docker ps -a


        // list all docker images
        docker images

        // build a docker image
        docker build -t <imageName:version> dockerFilePath

        
        // run a docker container in daemon mode with ports exposed
        docker run -it -d -p <outsidePort>:<dockerInsidePort> <imageName:version>




```


### Reference

https://www.metoffice.gov.uk/services/data/datapoint/api-reference#textual-data
 
