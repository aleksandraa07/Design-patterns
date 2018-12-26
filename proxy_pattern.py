'''A proxy in its most general form is a class functionind as an interface to something else. The proxy could interface to anything: a network connection, a large object in memory, a file, or some other resource tht is expensive or imposible to duplicate. A well-known example of the prxy pattern is a reference couting pointer object'''
'''Proxt Pattern is an example of Structural Design Patterns. It is also referred to as "Surrogate" pattern as the intention of this pattern is to creare a surrogate for the real object
Proxy pattern has three essential elements: 
- Real Subject ( that performs the business objectives, represented by Proxy)
-Proxy Class(that acts as an interface touser requests and shields the real Subject
-Client(that makes the requests for getting thhe job done)

Typical used:
1. Creation of object for a Real Subject Class is costly in terms od resources and a simple object creation by Proxy Class can be a cheaper option
2. A need arises that an object must be protected from direct use by its clients
3. There is a need that an object creation for the Real Subject Class can be delaed to a point when it is actually required.
Real world examples: 
- Website where the Cache Proxy can cache certain set of frequently requested web pages to cater to clients requests. This helps in avoiding many requests getting hit on the sercer and improves preformance
- The message box which gives the status od a file copy operation giving the progress in terms od percentage completion
- Opening a large file in a word processor leads to a message saying "Please wait while the software opens the document..." '''

import time
class Manager(object):
    def work(self):
        pass

    def talk(self):
        pass


class SalesManager(Manager):
    def work(self):
        print("Sales Manager working..")

    def talk(self):
        print("Sales Manager ready to talk..")


class Proxy(Manager):
    def __init__(self):
        self.busy = 'Yes'
        self.sales = None

    def work(self):
        print('Proxy checking for Sales Manager availability')
        if self.busy =="Yes":
            self.sales = SalesManager()
            time.sleep(2)
            self.sales.talk()
        else:
            time.sleep(2)
            print("Sales Manager is busy")

if __name__ == '__main__':
    p = Proxy()
    p.work()


