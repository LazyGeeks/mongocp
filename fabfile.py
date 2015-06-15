import os
import tempfile

from fabric.api import task, local, run, get


@task
def cp(from_host, from_db, from_collection, query,
       to_host, to_db=None, to_collection=None):
    """Copy data from remote MongoDB database to local one."""
    to_db = to_db or from_db
    to_collection = to_collection or from_collection

    # Dump remotely
    dump_tmp = tempfile.mkdtemp()
    run(
        'mongodump --authenticationDatabase admin -uroot -proot '
        '-h %s -d %s -c %s -q %r -o %s' % (
            from_host, from_db, from_collection, query, dump_tmp
        )
    )

    # Download
    restore_tmp = dump_tmp
    get(dump_tmp, os.path.dirname(restore_tmp))

    # Clean up remote temporary directory
    run('rm -rf %s' % dump_tmp)

    # Restore locally
    local(
        'mongorestore --authenticationDatabase admin -uroot -proot '
        '-h %s -d %s -c %s %s/%s/%s.bson' % (
             to_host, to_db, to_collection,
             restore_tmp, from_db, from_collection
        )
    )

    # Clean up local temporary directory
    local('rm -rf %s' % restore_tmp)
