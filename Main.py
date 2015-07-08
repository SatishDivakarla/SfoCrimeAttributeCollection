import pandas as pd
import GooglePlace as gp
import MongoClient as mongo_client


train = pd.read_csv("<Train CSV file location>")

coordinates = train.ix[1:len(train), ['X', 'Y']]




for index, coordinate in coordinates.iterrows():
    latitude = str(coordinate['Y'])
    longitude = str(coordinate['X'])
    radius = 3000;
    authKey = "<Google API Key>"

    # Refer below link for set of valid place types supported by google places API
    # https://developers.google.com/places/supported_types
    types = "police|post_office|bus_station|train_station|taxi_stand|airport|fire_station|bank|gas_station|school|university|night_club|casino|shopping_mall|convenience_store|lodging"
    #types="cafe"
    mongo_collection = mongo_client.mongodb_connections("sfocrimelocs","neighbourhood")
    if mongo_client.isRecordsExists(mongo_collection, latitude, longitude) == False:
        json_data = gp.GooglePlace(latitude, longitude, radius, types, authKey)
        # Get MongoDB connection and collection to insert
        json_data['latitude']=latitude
        json_data['longitude']=longitude
        mongo_collection.insert(json_data);
        print "inserted"
    else:
        print "records already exists"

