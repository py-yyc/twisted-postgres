## <h1>twisted basics</h1>

from twisted.internet import defer, task

@task.react
@defer.inlineCallbacks
def main(reactor):
    print("Running with {}".format(type(reactor).__name__))
    yield defer.succeed(None)

## show-output
