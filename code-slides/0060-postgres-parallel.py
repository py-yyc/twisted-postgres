## <h1>txpostgres</h1>

from twisted.internet import defer, task
from txpostgres import txpostgres

_create_table = '..'
_create_table = '''DROP TABLE IF EXISTS todo;\n\nCREATE TABLE todo\n(\n    id                  SERIAL,\n    todo                VARCHAR(254)        NOT NULL,\n    created_at          TIMESTAMP           NOT NULL,\n    PRIMARY KEY (id)\n);'''  # noslide

@task.react
@defer.inlineCallbacks
def main(reactor):
    connections = []
    for x in range(25):
        conn = txpostgres.Connection()
        db = yield conn.connect('dbname=postgres')
        connections.append(db)
#!
    yield connections[0].runOperation(_create_table)
#!
    # a 'real' generator, round-robin all connections
    def connection_generator():
        while True:
            for c in connections:
                yield c
#!
    connect = connection_generator()
    inserts = []
#!
    for item in range(1000):
        db = next(connect)
        d = db.runOperation(
            'INSERT INTO todo (todo, created_at) '
            'VALUES (%s, NOW());', [item],
        )
        inserts.append(d)

    start = reactor.seconds()
    yield defer.DeferredList(inserts)
    diff = reactor.seconds() - start
    print("Took {}s".format(diff))

## show-output
