import pandas as pd
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod #This is for RentedCarclass.

class Car:
    def __init__(self,id,brand,revenue,availability):
        self._id = id
        self._brand = brand
        self._properties = []
        self._maintenanceNeeds = {'Engine':'None','Tires':'None','BodyShell':'None','Frame':'None','Interior':'None'}
        self._potentialRevenue = revenue
        self._availability = availability

    def addProperty(self,property):
        if property not in self._properties:
            self._properties.append(property)
        else :
            print("Thar car has already have that property")

    def changeMaintenanceNeed(self,reqToChange,level):
        if reqToChange in self._maintenanceNeeds.keys():
            self._maintenanceNeeds[reqToChange]= level

    def getRevenue(self):
        return self._potentialRevenue

    def checkIfMaintained(self):
        score = 0
        for i in self._maintenanceNeeds:
            if self._maintenanceNeeds[i] == "None":
                temp = 0
            elif self._maintenanceNeeds[i] == "Low":
                temp = 1
            elif self._maintenanceNeeds[i] == "Medium":
                temp = 2
            else :
                temp = 3
            score = temp + score
        if score>=11:
            return False
        return True

    def hasProperty(self,property):
        if type(property) == list:
            for i in property:
                if i not in self._properties:
                    return False
        """
        else:
            if property not in self._properties:
                return False
        """
        return True

    def __str__(self):
        status = "Available" if self._availability else "Sold/Rented"
        return f"Car ID: {self._id} | Brand: {self._brand} | Revenue: {self._potentialRevenue} | Status: {status}\n Properties: {", ".join(self._properties)}\n Maintance {self._maintenanceNeeds}"

class RentedCar(Car):
    def __init__(self,id,brand,revenue,days):
        super().__init__(id,brand,revenue,False)
        self._days = days

    def getRevenue(self):
        return ((self._potentialRevenue/40) * 30)

    def __str__(self):
        if self._availability == False:
            status = "Rented"
        return f"RentedCar ID: {self._id} | Brand: {self._brand} | Base Revenue: {self._potentialRevenue} | {status} for: {self._days}\n Properties: {", ".join(self._properties)}\n Maintance {self._maintenanceNeeds}"

class Dealership:
    def __init__(self,id,region):
        self._id = id
        self._region = region
        self._cars = []

    def addCar(self,car):
        self._cars.append(car)

    def getCarsByProperty(self,property):
        allcars = []
        for car in self._cars:
            if car.hasProperty(property): # If we want exact search we could have used car._properities == property
                allcars.append(car)
        return allcars

    def getTotalRevenue(self):
        Total_Revenue = 0
        for car in self._cars:
            if not(car._availability):
                Total_Revenue = car.getRevenue()
        return Total_Revenue

    def getAllMaintained(self):
        maintained_cars = []
        for car in self._cars:
            if car.checkIfMaintained():
                maintained_cars.append(car)
        return maintained_cars

    def getHighestRevenueForEachBrand(self):
        pass

    def __str__(self):
        return f"Dealership ID: {self._id}, Region: {self._region}, Cars: {len(self._cars)}"


class Manager:
    def __init__(self,code):
        self._code = code
        self._dealerships = []

    def addDealership(self,dealership):
        self._dealerships.append(dealership)

    def getCarsByProperty(self,property):
        matching_cars = {}
        pass




    def getTotalRevenue(self):
        pass

    def MaintainedPercentage(self):
        pass

    def getHighestRevenueForEachBrand(self):
        pass

"""
try:
    file= open("clients.txt","r")
except IOError:
    print("File could not be opened")
    exit(1)

records = file.read().split("\n")[0:-1] #Böyle yaparsak en sonda boş bir küme de geliyor ından dolayı şunu ekledik [0:-1]

for record in records:
    fields = record.split(" ")
    print(f"Account: {fields[0]}, Name: {fields[1]}, Balance: {fields[2]} ")

file.close()


"""
if __name__ == "__main__":
    print("This is the Dealership Analyser program.")
    test = {'Engine':'None','Tires':'Low','BodyShell':'Medium','Frame':'High','Interior':'None'}
    id = 2
    brand = "toyota"
    properties = "RecentModel"
    maintenanceNeeds = {'Engine': 'Low', 'Tires': 'None', 'BodyShell': 'High','Frame': 'Low', 'Interior': 'None'}
    potentialRevenue = 12610
    availability = False
    status = "Available" if availability else "Sold/Rented"
    print(f"Car ID: {id} | Brand: {brand} | Revenue: {potentialRevenue} | Status: {status}\n Properties: {", ".join(properties)}\n Maintance {maintenanceNeeds}")
    
    

