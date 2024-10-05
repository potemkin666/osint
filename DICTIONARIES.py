
#dictionary


suspect_1 = {
    "name": "John Doe",
    "age": 35,
    "home": "123 yyyyyyyyyy",
    "type": "BURGLAR"
    }

suspect_2 = {
    "name": "fsadigdsjio",
    "age": 35400,
    "home": "sfdfsdfsdsdf",
    "type": "BURTHIEF"
} 


suspect_3 = {
    "name": "fsadiFGGFGFGFFGGFDSjio",
    "age": 40,
    "home": "sfGFsdsdf",
    "type": "BURTROPNBBERYF"
} 


#suspect database

suspect_database = {
"S1" : suspect_1,
"S2" : suspect_2,
"S3" : suspect_3
}



#PRINT

print (suspect_database)

print(f"the adrress for subject 12 is: {suspect_database["S2"]["home"]}")


#APPEMND DATABASE

suspect_database["S1"]["home"].append("whatever")



#new sdhyuspecft

suspect_4 = {
"name": "david becks",
"age": "99",
"address": "sdf 7 greemn dribe",
"bank balance": 2.50,
}


#delete suspect from the database

del suspect_database["S3"]


#for means for loop 

for suspect_id, suspect_info in suspect_database .items():
    print(suspect_info["name"])