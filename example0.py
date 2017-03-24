

from twisted.internet.task import react
from twisted.internet import defer

from txpostgres import txpostgres

_create_table = '''
DROP TABLE IF EXISTS todo;

CREATE TABLE todo
(
    id                  SERIAL,
    todo                VARCHAR(254)        NOT NULL,
    created_at          TIMESTAMP           NOT NULL,
    PRIMARY KEY (id)
);
'''


@defer.inlineCallbacks
def main(reactor):
    conn = txpostgres.Connection()
    db = yield conn.connect('dbname=postgres')
    print("Databse connected {}".format(db))
    yield db.runOperation(_create_table)
    for item in ['teach PyYYC', 'find beers', '???', 'profit']:
        yield db.runOperation(
            'INSERT INTO todo (todo, created_at) VALUES (%s, NOW());', [item],
        )

    print("done creating database")
    print("Querying all TODOs:")
    res = yield db.runQuery('SELECT * from todo;')
    for _id, todo, created_at in res:
        print("  {}: '{}' at '{}'".format(_id, todo, created_at))


if __name__ == '__main__':
    react(main)
