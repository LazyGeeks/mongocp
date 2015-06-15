# mongocp

A utility helps you copy data from remote MongoDB database to local one.


## Copy now

```
$ fab -H <dump-host> cp:<remote-mongodb-host>,<from-db>,<from-collection>,<query>,<local-mongodb-host>
```

Some descriptions about the arguments:

+ dump-host

        the hostname of the server where to run `mognodump`

+ remote-mongodb-host

        the hostname of the MongoDB from which to dump data

+ from-db

        the name of the database from which to dump data

+ from-collection

        the name of the collection from which to dump data

+ query

        the query condition to limit the output documents

+ local-mongodb-host

        the hostname of the MongoDB to which to restore data


## Todo

+ Wrap this fabfile as an user-friendly command
+ Support more `mongodump` and `mongorestore` arguments and options
