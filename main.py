from fastapi import FastAPI
from pydantic import BaseModel

# انشاء تطبيق fastapi
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# تعريف نموذج البيانات باستخدام pydantic
class Student(BaseModel):
    id: int
    name: str
    grade: int

# قائمة لتخزين البانات في الذاكرة
students = [
    Student(id=1, name="ahmed", grade=10),
    Student(id=2, name="Ali", grade=20),
]

# قراءة جميع العناصر
@app.get("/students/")
def read_students():
    return students

# لانشاء عنصر جديد
@app.post("/students/")
def create_student(New_Student: Student):
    students.append(New_Student)
    return New_Student
#تحديث عنصر معين بناءا على ID
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, Student in enumerate(students):
        if Student.id == student_id :
         students[index] = updated_student
        return updated_student
    return{"error":"student is not found"}
#حذف عنصر معين بناءا على ID
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, Student in enumerate(students):
        if Student.id == student_id:
            del students[index]
            return{"message":"student deleted"}
        return{"error":"student is not found"}
    
