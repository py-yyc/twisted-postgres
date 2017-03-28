## <h1>txpostgres</h1>

from twisted.internet import defer, task  # noslide
from txpostgres import txpostgres  # noslide

_create_table = '..'
_create_table = '''DROP TABLE IF EXISTS todo;\n\nCREATE TABLE todo\n(\n    id                  SERIAL,\n    todo                VARCHAR(254)        NOT NULL,\n    created_at          TIMESTAMP           NOT NULL,\n    PRIMARY KEY (id)\n);'''  # noslide

@task.react
@defer.inlineCallbacks
def main(reactor):
    conn = txpostgres.Connection()
    db = yield conn.connect('dbname=postgres')
    yield db.runOperation(_create_table)
#!
    to_insert = ['teach PyYYC', 'find beers', '???', 'profit']
#!
    for item in to_insert:
        yield db.runOperation(
            'INSERT INTO todo (todo, created_at) '
            'VALUES (%s, NOW());', [item],
        )
