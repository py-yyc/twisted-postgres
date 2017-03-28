## <h1>twisted basics</h1>

from twisted.internet import defer, task

@task.react
def main(reactor):
    d = defer.Deferred()
    print("Running with {}".format(type(reactor).__name__))
    d.callback(None)
    return d

## show-output
