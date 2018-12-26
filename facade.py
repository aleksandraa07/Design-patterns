'''The facade pattern is a software engineering design pattern commonly udsed with Object-oriendted programming. A fasade is an object that provides a simplified interface to a larger body of code, such as a class library'''
'''Fasade pattern is nothing but an interface that hides the inside details and complexities of a system and provides a simplified "front end" to the client.'''

import time
class TC1:
    def run(self):
        print("###### In Test 1 ######")
        time.sleep(1)
        print("Setting up")
        time.sleep(1)
        print("Running test")
        time.sleep(1)
        print("Tearing down")
        time.sleep(1)
        print("Test Finished\n")

class TC2:
    def run(self):
        print("###### In Test 2 ######")
        time.sleep(1)
        print("Setting up")
        time.sleep(1)
        print("Running test")
        time.sleep(1)
        print("Tearing down")
        time.sleep(1)
        print("Test Finished\n")

class TC3:
    def run(self):
        print("###### In Test 3 ######")
        time.sleep(1)
        print("Setting up")
        time.sleep(1)
        print("Running test")
        time.sleep(1)
        print("Tearing down")
        time.sleep(1)
        print("Test Finished\n")

#Facade
class TestRunner:
    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()

    def runAll(self):
        self.tc1.run()
        self.tc2.run()
        self.tc3.run()


#Client
if __name__ == '__main__':
    test_runner = TestRunner()
    test_runner.runAll()