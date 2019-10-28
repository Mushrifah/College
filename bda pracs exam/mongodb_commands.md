# Mongo DB commands

1. Create a database or use an existing one<br>
`use demo`
2. Show existing databases<br>
`show databases`
3. Show existing collections<br>
`show collections`
4. Create a collection named "project"<br>
`db.createCollection("project")`
5. Insert into Collection<br>
` db.project.insert({id:1,prjname:"chatbot",pdomain:"nlp"})`<br>
outputs as:- `{"_id":"5db69bc52fd13dd46932d5c5","id":1,"prjname":"chatbot","pdomain":"nlp"}` <br>
`db.project.insert({_id:2,prjname:"gans",pdomain:"dl"})`<br>
outputs as:- `{"_id":2,"prjname":"gans","pdomain":"dl"}` <br>
6. Display all contents of collection<br>
`db.project.find()`<br>
outputs as:- `{ "_id" : ObjectId("5db69bc52fd13dd46932d5c5"), "id" : 1, "prjname" : "chatbot", "pdomain" : "nlp" }
{ "_id" : 2, "prjname" : "gans", "pdomain" : "dl" }
{ "_id" : ObjectId("5db69da62fd13dd46932d5c6"), "prjname" : "gans", "pdomain" : "dl" }
{ "_id" : 1, "prjname" : "cmf", "pdomain" : "web" }`
7. Types of insert: <br>
  7.1 Having id (i.e. `_id`) in collection and inserting in it, so this will result in duplicate error <br>
  ` db.project.insert({_id:2,prjname:"gans",pdomain:"dl"})` <br>
  7.2 Not having id will automatically generate its own<br>
  `db.project.insert({prjname:"gans",pdomain:"dl"})` <br> outputs as:-
  `{"_id":"5db69da62fd13dd46932d5c6","prjname":"gans","pdomain":"dl"}`<br>
  7.3 id doesn't exists in collection so it gets added<br>
  `db.project.insert({_id:1,prjname:"cmf",pdomain:"web"})`<br>
  outputs as:- `{"_id":1,"prjname":"cmf","pdomain":"web"}`<br>
8. 
  
