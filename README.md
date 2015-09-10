# mongocp

A utility helps you copy data from remote MongoDB database to local one.


## Copy now

```
$ fab -H <dump_host> cp:<from_host>,<from_db>,<from_collection>,<query>,<to_host>
```

Some descriptions about the arguments:

+ dump_host

        The hostname of the server where to run `mongodump`.

+ from_host

        The hostname of the MongoDB from which to dump data.

+ from_db

        The name of the database from which to dump data.

+ from_collection

        The name of the collection from which to dump data.

+ query

        The query condition to limit the output documents.

+ to_host

        The hostname of the MongoDB to which to restore data.

+ to_db

        Default: <from-db>

        The name of the database to which to restore data.

+ to_collection

        Default: <from-collection>

        The name of the collection to which to restore data.

+ dump_auth

        Default: ''

        The the authentication parameters in the form `user:password@authentication_database` for dumping.

+ restore_auth

        Default: ''

        The the authentication parameters in the form `user:password@authentication_database` for restoring.


## Todo

+ Wrap this fabfile as an user-friendly command
+ Support more arguments and options of `mongodump` and `mongorestore`
