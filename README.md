# mongocp

A utility helps you copy data from remote MongoDB database to local one.


## Usage

### 1. Set the operation host

```
$ vi fabfile.py
@hosts('user@operation-host')
```

### 2. Start to copy

```
$ fab cp:<remote-mongodb-host>,<from-db>,<from-collection>,<query>,<local-mongodb-host>
```


## Todo

+ Make the operation host customizable
+ Wrap this fabfile as an user-friendly command
+ Support more `mongodump` and `mongorestore` arguments and options
