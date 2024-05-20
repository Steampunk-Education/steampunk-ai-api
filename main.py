from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, RootModel

app = FastAPI()

class Course(BaseModel):
    course_id: str
    school: str
    class_name: str
    course_desc: str

class CourseList(BaseModel):
    courses: list[Course]

DESC_1 = """
Title: CSI 2101: Discrete Structures

URL Source: https://andrejb.net/csi2101/

Markdown Content:
University of Ottawa, Winter 2024

Recent Announcements
--------------------

*   18 Apr Akshat's office hour today will be in MRT 631 from 3-5pm.
*   16 Apr Yining's office hours tomorrow are cancelled.
*   04 Apr The [practice finals](https://andrejb.net/csi2101/hw/24PF.pdf) have been posted. The final exam will have a similar format. It covers lectures 1 to 10. No calculators are allowed or needed. You may bring in one double-sided sheet of handwritten notes.

Teaching Staff
--------------

| name | email | office | office hour |
| --- | --- | --- | --- |
| [Andrej Bogdanov](https://andrejb.net/)  
_instructor_ | abogdano@uottawa.ca | SITE 5068 | Fr 3–5 |
| Yanbo Chen  
_TA_ | ychen918@uottawa.ca | SITE 4035 | We 3-5 |
| Supriya Dara  
_Head TA_ | sdara100@uottawa.ca | SITE 4035 | We 3-5 |
| Akshat Khare  
_TA_ | akhar075@uottawa.ca | MRT 607 | Th 3-5 |
| Yuzhe Wang  
_corrector_ | ywan1035@uottawa.ca |  |  |
| Yining Zhang  
_TA_ | yzha1231@uottawa.ca | MRT 603 | We 12-2 |

Course Description
------------------

Discrete math is the study of objects that can be built from zeroes and ones. These are the objects that computers can manipulate effectively. They include numbers and graphs but also logical statements and computer programs. We will introduce methods for reasoning about discrete structures, including mathematical proofs, invariants, and recurrences and touch upon applications like public-key encryption and backpropagation.

  

Course information
------------------

*   **Schedule:** Lectures are held on We 10-11.20 and Fr 8.30-9.50 in MHN 257. Tutorials are on Th 5.30-6.50 in STE H0104. You are expected to attend in person. In case of emergency I will try to broadcast live at [this link](https://uottawa-ca.zoom.us/my/abogdano).
*   **Grading:** Your grade is determined by the quizzes (30%), the midterm exam (30%), and the final exam (40%). Your lowest two quiz grades will be dropped from the count. There are no makeup quizzes.
*   **Discussion board:** There is a [discussion board on piazza](https://piazza.com/class/lr16u6uvh6b3tz). Please register and sign in using your uOttawa email address.
*   **Textbook** The primary reference is [_Mathematics for Computer Science_](https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_and_Computation_Fundamentals/Mathematics_for_Computer_Science_\(Lehman_Leighton_and_Meyer\)) by Lehman, Leighton, and Meyer. Notes will be provided for material not covered in the textbook. The book [_Discrete Mathematics and Applications_](https://mhhe.com/rosen) (7th edition) by Kenneth Rosen can be used as a secondary reference and a source of additional exercises.
"""

COURSES = {
    "1": {
        "course_id": "1",
        "school": "University of Ottawa",
        "class_name": "CSI 2101",
        "course_desc": DESC_1
    },
    "2": {
        "course_id": "2",
        "school": "Earl of March Public High School",
        "class_name": "Grade 10 Math",
        "course_desc": ""
    }
}


@app.get("/courses")
def get_courses() -> CourseList:
    # TODO: Get courses from Firebase
    return { "courses": COURSES.values() }

@app.get("/courses/{course_id}")
def get_course(course_id: str) -> Course:
    if course_id not in COURSES:
        raise HTTPException(status_code=404, detail="Course not found")
    return COURSES[course_id]
