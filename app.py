from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

#START

""" Utility objects to mimic in-memory database 
    TODO : Configure database later
"""

student_table = []

#END


#RESTful API routes and business logic configuration

#1. Generic Error Handler for 404
@app.errorhandler(404)
def not_found(error):
    return {"status":"Fail","code":"404","error": "Not found", "message":"API endpoint not found"}, 404


#2. Generic Error Handler for 405
@app.errorhandler(405)
def not_found(error):
    return {"status":"Fail","code":"405","errorMsg": "Method Not Allowed", "message":"API request verb inappropriate"}, 405

#App Page - HOME (/v1/home/)
@app.route("/v1/home/", methods=['GET'])
def home():
    return {"message" : "Welcome to Student RESTful API Home Page!"}

#App Page - About Us (/v1/aboutus/)
@app.route("/v1/aboutus/", methods=['GET'])
def aboutus():
    return {"message" : "Aditya Kawale"}

#App Page - Contact (/v1/contact/)
@app.route("/v1/contact/", methods=['GET'])
def contact():
    return {"message" : "Email : developer.adityakawale@gmail.com"}

#Student App (/v1/apps/student) - Student Search
@app.route("/v1/apps/student/", methods=['GET'])
def app_studentSearchAllStudents():
    responsePayloadJSON = {
        "status":"Success",
        "message":"List of all the students",
        "data": {
            "rows":len(student_table),
            "studentRecords": student_table
        }
    }
    return jsonify(responsePayloadJSON)

#Student App (/v1/apps/student) - Specific Student Search
@app.route("/v1/apps/student/<filterField>/<filterValue>", methods=['GET'])
def app_studentSearchSpecificStudents(filterField,filterValue):
    studentRecords = []
    for i in range(len(student_table)):
        if(student_table[i][filterField] == filterValue):
            studentRecords.append(student_table[i])
        
    responsePayloadJSON = {
        "status":"Success",
        "message":"List of all the students with {}:{}".format(filterField, filterValue),
        "data": {
            "rows":len(studentRecords),
            "studentRecords": studentRecords
        }
    }
    return jsonify(responsePayloadJSON)

#Student App (/v1/apps/student) - Student Create
@app.route("/v1/apps/student/", methods=['POST'])
def app_studentCreate():
    student_requestPayloadJSON = request.json
    stduent_id = student_requestPayloadJSON['id']
    stduent_name = student_requestPayloadJSON['name']
    studentDBRecord = {
        'id' : stduent_id,
        'name': stduent_name
    }
    student_table.append(studentDBRecord)
    responsePayloadJSON = {
    "status":"Success",
    "message":"Student with {}:{} created into student table".format("id",stduent_id)
    }

    return jsonify(responsePayloadJSON), 201

#Student App (/v1/apps/student) - Student Update
@app.route("/v1/apps/student/<filterField>/<filterValue>", methods=['PUT'])
def app_studentUpdate(filterField, filterValue):
    updateFlag=False
    updateCount=0
    student_requestPayloadJSON = request.json
    for i in range(len(student_table)):
        if(student_table[i][filterField] == filterValue):
            student_table[i].update(student_requestPayloadJSON)
            updateFlag=True
            updateCount+=1


    if updateFlag == True:
        responsePayloadJSON = {
            "status":"Success",
            "message":"Students with {}:{} updated into student table  (Affected rows : {})".format(filterField, filterValue, updateCount),
            "rowsAffected":updateCount
        }
        return jsonify(responsePayloadJSON), 200
    else:
        responsePayloadJSON = {
            "status":"Failed",
            "message":"Student with {}:{} not found in student table".format(filterField, filterValue)
        }
        return jsonify(responsePayloadJSON), 400

#Student App (/v1/apps/student) - Student Delete
@app.route("/v1/apps/student/<filterField>/<filterValue>", methods=['DELETE'])
def app_studentDelete(filterField, filterValue):
    deleteFlag=False
    deleteIndexList=[]
    for i in range(len(student_table)):
        if(student_table[i][filterField] == filterValue):
            deleteIndexList.append(i)

    for i in sorted(deleteIndexList, reverse=True):
        student_table.pop(i)
        deleteFlag=True

    if deleteFlag == True:
        responsePayloadJSON = {
            "status":"Success",
            "message":"Students with {}:{} deleted from student table (Affected rows : {})".format(filterField, filterValue, len(deleteIndexList)),
            "rowsAffected":len(deleteIndexList)
        }
        return jsonify(responsePayloadJSON), 200
    else:
        responsePayloadJSON = {
            "status":"Failed",
            "message":"Students with {}:{} not found in student table".format(filterField, filterValue)
        }
        return jsonify(responsePayloadJSON), 400

# if __name__ == "__main__":
#     app.run()