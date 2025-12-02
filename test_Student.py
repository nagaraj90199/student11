import pytest
from Student import Student_details

def test_Student_details():
    expected_output = (
        "Student Name: nagaraj\n"
        "Student ID: S102\n"
        "Course Enrolled: BCA\n"
        "Academic Year: 2025\n"
    )
    assert student_details("nagaraj", "S102", "BCA", "2025") == expected_output
