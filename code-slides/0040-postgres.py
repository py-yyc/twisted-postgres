## <h1>txpostgres basics</h1>

from twisted.internet import defer, task
from txpostgres import txpostgres


@task.react
@defer.inlineCallbacks
def main(reactor):
    conn = txpostgres.Connection()
    db = yield conn.connect('dbname=postgres')
    

## show-output
