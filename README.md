# mongocp

A utility helps you copy data from remote MongoDB database to local one.


## Copy now

```
$ fab -H <dump-host> cp:<from-host>,<from-db>,<from-collection>,<query>,<to-host>
```

Some descriptions about the arguments:

+ dump-host

        The hostname of the server where to run `mongodump`.

+ from-host

        The hostname of the MongoDB from which to dump data.

+ from-db

        The name of the database from which to dump data.

+ from-collection

        The name of the collection from which to dump data.

+ query

        The query condition to limit the output documents.

+ to-host

        The hostname of the MongoDB to which to restore data.

+ to-db

        Default: <from-db>

        The name of the database to which to restore data.

+ to-collection

        Default: <from-collection>

        The name of the collection to which to restore data.


## Todo

+ Wrap this fabfile as an user-friendly command
+ Support more arguments and options of `mongodump` and `mongorestore`
