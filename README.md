# mongocp

A utility helps you copy data from a (remote or local) MongoDB database to another (local) one.


## Copy now

Copy remotely:

```
$ fab -H <dump_host> cp:<from_host>,<from_db>,<from_collection>,<query>,<to_host>
```

Copy locally:

```
$ fab cp:<from_host>,<from_db>,<from_collection>,<query>,<to_host>
```


## Arguments

Some descriptions about the arguments:

+ dump_host

        The host string of the server where to run `mongodump`. In the form
        of `username@hostname:port`. If not specified, this utility will run
        `mongodump` locally.

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

        The authentication arguments for dumping. In the form of
        `user:password@authentication_database`.

+ restore_auth

        Default: ''

        The authentication arguments for restoring. In the form of
        `user:password@authentication_database`.


## Todo

+ Wrap this fabfile as an user-friendly command
+ Support more arguments and options of `mongodump` and `mongorestore`
