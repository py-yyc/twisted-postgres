import sys

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
    dl = []
#    for item in ['teach PyYYC', 'find beers', '???', 'profit']:
    for item in range(1000):
        d = db.runOperation(
            'INSERT INTO todo (todo, created_at) VALUES (%s, NOW());', [item],
        )
        dl.append(d)
    print("All inserts queued")
    s = reactor.seconds()
    yield defer.DeferredList(dl)
    diff = reactor.seconds() - s

    print("done creating database")
    print("Querying all TODOs:")
    res = yield db.runQuery('SELECT * from todo;')
    expected = 1
    last = None
    for _id, todo, created_at in res:
        print("  {}: '{}' at '{}'".format(_id, todo, created_at))
        if last and created_at < last:
                print("out of order")
                sys.exit(3)
        last = created_at

        if _id != expected:
            print("DING")
            sys.exit(4)
        expected += 1
    print("done {}".format(diff))


if __name__ == '__main__':
    react(main)
