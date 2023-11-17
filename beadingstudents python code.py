import pymongo
myclient= pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["databases1"]
mycol=mydb["beading students"]

mylist= [
    {"_id":"1","name":"Oluwalade Gift", "Matric.no":"20CJ027478","room":"Dorcas E311", "Gender":"Female", "Beading Exp.":"Advanced"},
    {"_id":"2","name":"Towoju Joy", "Matric.no":"20CJ027492","room":"Dorcas D105", "Gender":"Female", "Beading Exp.":"Beginner"},
    {"_id":"3","name":"Aki Jessica", "Matric.no":"20CJ027478","room":"Dorcas D205", "Gender":"Female", "Beading Exp.":"Advanced"},
    {"_id":"4","name":"Akin-olaiya Tamilore", "Matric.no":"20BE026982","room":"Deborah F101", "Gender":"Female", "Beading Exp.":"Moderate"},
    {"_id":"5","name":"Odjenima Anjola", "Matric.no":"20BE027030","room":"Deborah F201", "Gender":"Female", "Beading Exp.":"Advanced"},
    {"_id":"6","name":"Chukwuemeka Covenant", "Matric.no":"20AH027113","room":"Dorcas E106", "Gender":"Female", "Beading Exp.":"Beginner"},
    {"_id":"7","name":"Bayagbon Victory", "Matric.no":"20AH027009","room":"Dorcas E407", "Gender":"Female", "Beading Exp.":"Moderate"},
    {"_id":"8","name":"Grant-elsie Charisa", "Matric.no":"20BE027013","room":"Deborah C109", "Gender":"Female", "Beading Exp.":"Beginner"},
    {"_id":"9","name":"Adeyemo Toluwalashe", "Matric.no":"20AA027472","room":"Dorcas B101", "Gender":"Female", "Beading Exp.":"Beginner"},
    {"_id":"10","name":"Adams Jordan", "Matric.no":"20CJ027406","room":"Daniel E311", "Gender":"male", "Beading Exp.":"Advanced"},
    {"_id":"11","name":"Oluwafemi Tireni", "Matric.no":"20CJ027477","room":"Peter A402", "Gender":"Male", "Beading Exp.":"Beginner"},
    {"_id":"12","name":"Oluwalade David", "Matric.no":"20CK027495","room":"Joseph G011", "Gender":"Male", "Beading Exp.":"Advanced"},
    {"_id":"13","name":" Oluwalade Reremi", "Matric.no":"20CK027456","room":"Mary E311", "Gender":"Female", "Beading Exp.":"Moderate"},
    {"_id":"14","name":" Ambrose Kenneth", "Matric.no":"20CG027567","room":"Paul A401", "Gender":"Male", "Beading Exp.":"Moderate"},
    {"_id":"15","name":" Ogundalu Oluwaseyi", "Matric.no":"20CI027288","room":"John 209", "Gender":"Male", "Beading Exp.":"Beginner"},
    {"_id":"16","name":" Soladoye Toluwanimi", "Matric.no":"20CK027580","room":"Dorcas C303", "Gender":"Female", "Beading Exp.":"Moderate"}]

#to insert a file(write)
x=mycol.insert_many(mylist)
print(x.inserted_ids) 


'''#to find file with a query
myquery ={"room":"Dorcas E407"}
mylist = mycol.find(myquery)
for x in mylist:
    print(x)'''

'''to sort file 
mylist = mycol.find().sort("name",-1)
for x in mylist:
    print(x)'''

'''#to update a file
myquery={"Matric.no":"20AH027009"}
newvalue = {"$set":{"Matric.no":"20AH027056"}}
mylist= mycol.update_one(myquery, newvalue)

for x in mycol.mylist():
    print(x)'''

'''to delete a file
mycol.delete_one(myquery)
print(x)'''