def Student_details(name, student_id, course_enrolled, academic_year):
    """
    Accepts student details and returns a well-formatted string.
    """
    result = (
        f"Student Name: {name}\n"
        f"Student ID: {student_id}\n"
        f"Course Enrolled: {course_enrolled}\n"
        f"Academic Year: {academic_year}\n"
    )
    return result


if __name__ == "__main__":
    name = "nagaraj"
    student_id = "S102"
    course_enrolled = "BCA"
    academic_year = "2025"
    print(Student_details(name, student_id, course_enrolled, academic_year))
