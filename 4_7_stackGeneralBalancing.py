# come back to the general case of balancing 
def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


#print(matches('(',')'))

opens = "([{"
print(opens.index('('))