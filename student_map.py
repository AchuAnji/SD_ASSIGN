from typing import Dict
def get_student_name(student_map: Dict[int, str], student_id: int) -> str:
    return student_map.get(student_id, "Unknown")


def add_student(student_map: Dict[int, str], student_id: int, name: str) -> None:
    student_map[student_id] = name


def remove_student(student_map: Dict[int, str], student_id: int) -> None:
    if student_id in student_map:
        del student_map[student_id]


def print_all_students(student_map: Dict[int, str]) -> None:
    for sid, name in student_map.items():
        print(f"ID: {sid}, Name: {name}")


if __name__ == "__main__":
    students = {
        101: "Alice",
        102: "Bob",
        103: "Charlie"
    }

    print("Original student list:")
    print_all_students(students)
    print()

    print("Look up ID 102:", get_student_name(students, 102))
    print("Look up ID 999:", get_student_name(students, 999))
    print()

    print("Adding new student 104: Diana")
    add_student(students, 104, "Diana")
    print_all_students(students)
    print()

    print("Removing student 101")
    remove_student(students, 101)
    print_all_students(students)