'''Mediator pattern provides a unified interface to a set of interfaces in a subsystem, This pattern is considered to be a behavioral pattern due to the way it can alter the program's running behaviour'''
'''Mediator patter is used in cases where many classes start communicating amongst each other to produce result. When the software starts getting developed, more user requests get added and in turn more functionality need to be coded. This results in increased interaction with in the existing classes and in addition of new classes to address new fnctionality, With the increasing complexity of the system, interaction between classes becomes tedious to handle and maintaining the code becomes difficult. 
 
 Mediator class is aware od their functionality and interact with the Mediator class. Whenever there is a need of inteaction between the classes a class send information to the mediato and it's the responsibility of the Mediator to pass this information to the required class. 
 A typical example od Mediator Pattern can be manifested in a test automationn framework which consist of four classes namely, TC(TestCategory), TestManager, Reporter and DB(Database)
 1. Class TC is responsible for running the tests with the help of setup(), execute(), and tear_down() methods. 
 2. Class Reporter calls its prepare() method while the test category starts getting executed and calls its report() method when the test category finishes its execution. 
 3. Class DB stores the execution status od the test category by first calling the insert() method while the test category is in setup(), and then calls the update() method once the test categor has finished execution. In this way, at any given point of time, the test execution status is available for framework user to query from the database
 4. TestManager class is the one that co-ordinates for test ctegory execution(Class TC) and fetching the reports (Class Reporter) and getting the test execution statis in database ( Class DB) with the help of prepare_reporting() and publish_report() methods
 5. Methods setTM(), setTC(), set_reporter() and set_db() are used so that the classes could register with each other and can communicate easily. '''
import time

class TC:
    def __init__(self):
        self._tm = tm
        self._bproblem = 0

    def setup(self):
        print('Setting up the Test')
        time.sleep(1)
        self._tm.prepare_reporting()

    def execute(self):
        if not self._bproblem:
            print('Excecuting the test')
            time.sleep(1)
        else:
            print("Problem in setup. Test not executed")

    def tear_down(self):
        if not self._bproblem:
            print('Tearing down')
            time.sleep(1)
            self._tm.publish_report()
        else:
            print("Test not executed. No tear down required.")

    def setTM(self,tm):
        self._tm = tm

    def set_problem(self,value):
        self._bproblem = value


class Reporter:
    def __init__(self):
        self._tm = None

    def prepare(self):
        print('Report Class is preparing to report the results')
        time.sleep(1)

    def report(self):
        print('Report Class is preparing to report the results')
        time.sleep(1)

    def setTM(self, tm):
        self._tm = tm

class DB:
    def __init__(self):
        self._tm = None

    def insert(self):
        print('Inserting the execution begin status in the Database')
        time.sleep(1)
        import random
        if random.randrange(1,4) == 3:
            return -1

    def update(self):
        print('Updating the test results in Database')
        time.sleep(1)

    def setTM(self,tm):
        self._tm = tm


class TestManager:
    def __init__(self):
        self._reporter = None
        self._db = None
        self._tc = None

    def prepare_reporting(self):
        rvalue = self._db.insert()
        if rvalue == -1:
            self._tc.set_problem(1)
            self._reporter.prepare()

    def set_reporter(self,reporter):
        self._reporter = reporter

    def set_DB(self,db):
        self._db = db

    def publish_report(self):
        self._db.update()
        rvalue = self._reporter.report()

    def setTC(self,tc):
        self._tc = tc


if __name__ == '__main__':
    reporter = Reporter()
    db = DB()
    tm = TestManager()
    tm.set_reporter(reporter)
    tm.set_DB(db)

    reporter.setTM(tm)
    db.setTM(tm)

    while (1):
        tc = TC()
        tc.setTM(tm)
        tm.setTC(tc)
        tc.setup()
        tc.execute()
        tc.tear_down()
