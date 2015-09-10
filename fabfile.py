import os
import tempfile

from fabric.api import task, local, run, get, env


def make_auth_param(auth):
    """Make the authentication parameters based on the `auth` string.

    The input string format:
        'user:password@authentication_database'

    The output string format:
        '--authenticationDatabase <authentication_database> -u<user> -p<password>'
    """
    if not auth:
        return ''

    account, authentication_database = auth.split('@', 1)
    user, password = account.split(':', 1)
    return '--authenticationDatabase %s -u%s -p%s' % (
               authentication_database, user, password
           )


@task
def cp(from_host, from_db, from_collection, query,
       to_host, to_db=None, to_collection=None,
       dump_auth='', restore_auth=''):
    """Copy data from a (remote or local) MongoDB database to
    another (local) one.
    """
    to_db = to_db or from_db
    to_collection = to_collection or from_collection
    dump_auth = make_auth_param(dump_auth)
    restore_auth = make_auth_param(restore_auth)

    # The flag indicating whether to dump remotely
    remote = bool(env.hosts)

    # Make the temporary directory for dumping
    dump_tmp = tempfile.mkdtemp()

    cmd = 'mongodump %s -h %s -d %s -c %s -q %r -o %s' % (
        dump_auth, from_host, from_db, from_collection, query, dump_tmp
    )

    if remote:
        # Dump remotely
        run(cmd)
    else:
        # Dump locally
        local(cmd)

    # The temporary directory for restoring
    restore_tmp = dump_tmp

    if remote:
        # Download
        get(dump_tmp, os.path.dirname(restore_tmp))

        # Clean up remote temporary directory
        run('rm -rf %s' % dump_tmp)

    # Restore locally
    local(
        'mongorestore %s -h %s -d %s -c %s %s/%s/%s.bson' % (
             restore_auth, to_host, to_db, to_collection,
             restore_tmp, from_db, from_collection
        )
    )

    # Clean up local temporary directory
    local('rm -rf %s' % restore_tmp)
