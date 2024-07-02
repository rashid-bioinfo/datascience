# Generator 

def remote_control_next():
    yield "CNN"
    yield "BBC"

itr = remote_control_next()
print(itr)
print(next(itr)) # prints CNN
print(next(itr)) # prints BBC
# OR you can also prints values as:

for i in remote_control_next():
    print(i) # prints CNN and BBC

