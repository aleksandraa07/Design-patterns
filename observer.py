'''The observer pattern is a software pattern in which an object, called the subject, maintains a list of its dependants, called observers and notifies them automatically of any state changwes usually by calling one of their methods. It is mainly used to implement distributed event handling systems.'''
'''Observer pattern has: 
1. Publisher class that would contain methods for:
    - registring other objects which would like to receive        notifications 
    - notyfing any changes that occur in the main object to       the registered objects
    - unregistering objects that do not want to receive any      further notifications
2. Subscriber class that would contain:
    - a method that is used by the Publisher Class to notify the objects registered with it, of any change that occurs
3. An event that triggers a state change that leads the Publisher to call its notification method'''

class Publisher:
    def __init__(self):
        #make it uninheritable
        pass

    def register(self):
        #overide
        pass

    def unregister(self):
        # overide
        pass

    def notify_all(self):
        # overide
        pass

class TechForum(Publisher):
    def __init__(self):
        self._list_of_Users = []
        self.postname = None

    def register(self, user_obj):
        if user_obj not in self._list_of_Users:
            self._list_of_Users.append(user_obj)

    def unregister(self,user_obj):
        self._list_of_Users.remove(user_obj)

    def notify_all(self):
        for objects in self._list_of_Users:
            objects.notify(self.postname)

    def write_new_post(self,postname):
        #User write a post
        self.postname = postname
        #when submit the post is published and noti is send
        self.notify_all()

class Subscriber:
    def __init__(self):
        pass

    def notify(self):
        pass

class User1(Subscriber):
    def notify(self,postname):
        print('User1 notified of a new post '+postname)


class User2(Subscriber):
    def notify(self, postname):
        print('User2 notified o+f a new post ' + postname)

class SisterSites(Subscriber):
    def __init__(self):
        self._sisterWebsites = ["Site1","Site2","Site3"]
    def notify(self, postname):
        for site in self._sisterWebsites:
            #send updates by any means
            print("Send notification to site: " + site)

if __name__ == "__main__":
    tech_forum = TechForum()

    user1 = User1()
    user2 = User2()

    sites = SisterSites()
    tech_forum.register(user1)
    tech_forum.register(user2)
    tech_forum.register(sites)

    tech_forum.write_new_post("Observer pattern in Python")
    tech_forum.unregister(user2)
    tech_forum.write_new_post("MVC pattern in Python")




