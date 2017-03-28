## <h1>twisted basics</h1>

from twisted.internet import defer, task
#!
def main(reactor):
    d = defer.Deferred()
#!
    print("Running with {}".format(type(reactor).__name__))
    d.callback(None)
    return d
#!
if __name__ == '__main__':
    task.react(main)

## show-output
