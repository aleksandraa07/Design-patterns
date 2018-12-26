'''Model-View-Controller (MVC) is a software architecture, currently considered an architectural pattern used in software engineering. The pattern isolated "domain logic" (the application logic for the user) from input and presentation (GUI), permitting independent development, testing and maitenance of each.'''

'''In MVC Design Pattern , the application is divided into three interacting categories knows as the Model, the View and the Controller. The pattern aims at separating out the inputs to the application(the Controlles part) the business processing logic (the Model part) and the output format logic (the View part)
 In simple words: 
    - Controller associates the user input to a Model and a       View 
    - Model fetches the data to be presented fromm persistent      storage
    - View deals with how the fetched data is presented to        the user'''

'''Controller can be considered as a middle man between user and processing(Model)&formatting(View) logic. It is an entry point for all the user requests or inputs to the application. 
Model represents the business processing logic of the application. This component would be encapsulated vesrion of the application logic. model is also responsible for working with the databases and performing operations like Insertion, Update and Deletation. 
View also referred as presentation layer, is responsible for displaying the results obtained by the controller from the model component in a way that user wants them to see or a pre-determinated format. '''


#Model
import sqlite3
import types

class DefectModel:
    def get_defect_list(self,component):
        query = "SELECT ID FROM Defects WHERE COMPONENT = " + component
        defectlist = self._dbselect(query)
        list = []
        for row in defectlist:
            list.append(row[0])
            return list

    def get_summary(self, id):
        query = "SELECT Summary FROM Defects where ID = "+id
        summary = self._dbselect(query)
        for row in summary:
            return row[0]

    def _dbselect(self,query):
        connection = sqlite3.connect('TMS')
        cursor_obj = connection.cursor()
        results = cursor_obj.execute(query)
        connection.commit()
        cursor_obj.close()
        return results


class DetectView:
    def summary(self, summary, defectid):
        print("###### Defect Summary for defect {} \n {}".format(defectid,summary))

    def defect_list(self,list, category):
        print("###### Defect Summary for {} \n {}".format(category))
        for defect in list:
            print(defect)


class Controller:
    def __init__(self):
        pass

    def get_defect_summary(self,defectid):
        model = DefectModel()
        view = DetectView()
        summary_data = model.get_summary(defectid)
        return view.summary(summary_data, defectid)

    def get_defect_list(self,component):
        model = DefectModel()
        view = DetectView()
        defect_list_data = model.get_defect_list(component)
        return view.defect_list(defect_list_data,component)

#this should be in different module
controller = Controller()
print(controller.get_defect_summary(2))
print(controller.get_defect_list('ABC'))








