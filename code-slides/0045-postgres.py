## <h1>txpostgres</h1>

from twisted.internet import defer, task  # noslide
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
