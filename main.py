import face_recognition
image = face_recognition.load_image_file("class_image.png")
image = face_recognition.face_encodings(image)[0]
# print(type(image))
# face_locations = list(map(numpy.asarray, face_recognition.face_locations(image)))
# face_locations = face_recognition.face_locations(image)
studentlist=[["0001","a",face_recognition.load_image_file("a.png")],["0002","b",face_recognition.load_image_file("b.png")],["0003","c",face_recognition.load_image_file("c.png")],["0004","d",face_recognition.load_image_file("d.png")],["0005","e",face_recognition.load_image_file("e.png")],["0006","f",face_recognition.load_image_file("f.png")],["0007","g",face_recognition.load_image_file("g.png")]]
faceenc=[]
for i in studentlist:
    faceenc.append(face_recognition.face_encodings(i[2])[0])
attendance=[]
for studet in faceenc:
    fnrj=face_recognition.compare_faces([studet],image, tolerance=1)
    if fnrj[0]:
        attendance.append(True)
    else:
        attendance.append(False)
temp=0
for boool in attendance:
    if boool:
        print(studentlist[temp][1],"is present")
    else:
        print(studentlist[temp][1],"is absent")
    temp+=1
# face_recognition.c
# print(type(face_locations[0]),type(studentlist[0][2]))
# print(face_locations[0])
# print(studentlist[0][2])
# print(image[studentlist[0][2]])
# print(image[facecoord[0]:facecoord[1], facecoord[2]:facecoord[3]])