import json
from datetime import datetime

from django.http import JsonResponse
from django.db.models import Count, Q, Sum
from .models import Student, Instructor, Thesis, ExamRecord, \
    TeachingAssignment, InstructorLoad, Subject, Department, StudentGroup, \
    Faculty, InstructorCategory, Curriculum


# 1. Получить перечень и общее число студентов указанных групп либо
# указанного курса (курсов) факультета полностью, по половому признаку,
# году рождения, возрасту, признаку наличия детей, по признаку получения
# и размеру стипендии.
def get_students(request):
    groups = request.GET.getlist('groups')
    course = request.GET.get('course')
    gender = request.GET.get('gender')
    birth_year = request.GET.get('birth_year')
    age = request.GET.get('age')
    has_children = request.GET.get('has_children')
    scholarship = request.GET.get('scholarship')

    students = Student.objects.all()

    if groups:
        students = students.filter(student_group__name__in=groups)
    if course:
        students = students.filter(student_group__year_of_admission=course)
    if gender:
        students = students.filter(gender=gender)
    if birth_year:
        students = students.filter(birth_year=birth_year)
    if age:
        students = students.filter(birth_year=datetime.now().year - (
                    int(age)))
    if has_children is not None:
        students = students.filter(has_children=has_children)
    if scholarship:
        students = students.filter(scholarship__gte=scholarship)

    total_students = students.count()

    data = {
        'total_students': total_students,
        'students': list(students.values())
    }

    return JsonResponse(data)


# 2. Перечень и число преподавателей
def get_instructors(request):
    departments = request.GET.getlist('departments')
    faculty = request.GET.get('faculty')
    categories = request.GET.getlist('categories')
    gender = request.GET.get('gender')
    birth_year = request.GET.get('birth_year')
    has_children = request.GET.get('has_children')
    is_phd = request.GET.get('is_phd')
    is_doctor = request.GET.get('is_doctor')
    postgraduate = request.GET.get('postgraduate')
    salary = request.GET.get('salary')

    instructors = Instructor.objects.all()

    if departments:
        instructors = instructors.filter(department__name__in=departments)
    if faculty:
        instructors = instructors.filter(department__faculty__name=faculty)
    if categories:
        instructors = instructors.filter(category__name__in=categories)
    if gender:
        instructors = instructors.filter(gender=gender)
    if birth_year:
        instructors = instructors.filter(birth_year=birth_year)
    if has_children is not None:
        instructors = instructors.filter(has_children=has_children)
    if salary:
        instructors = instructors.filter(salary__gte=salary)
    if postgraduate is not None:
        instructors = instructors.filter(is_postgraduate_student=postgraduate)
    if is_phd:
        instructors = instructors.filter(is_phd=is_phd)
    if is_doctor:
        instructors = instructors.filter(is_doctor=is_doctor)

    total_instructors = instructors.count()

    data = {
        'total_instructors': total_instructors,
        'instructors': list(instructors.values())
    }

    return JsonResponse(data)


# 3. Перечень тем кандидатских и докторских диссертаций
def get_dissertations(request):
    faculty = request.GET.get('faculty')
    department = request.GET.get('department')

    dissertations = Thesis.objects.all()
    if faculty:
        dissertations = dissertations.filter(
            instructor__department__faculty__name=faculty)
    if department:
        dissertations = dissertations.filter(
            instructor__department__name=department)

    total_dissertations = dissertations.count()

    data = {
        'total_dissertations': total_dissertations,
        'dissertations': list(dissertations.values())
    }

    return JsonResponse(data)


# 4. Перечень кафедр, проводящих занятия в указанной группе или на курсе
def get_departments(request):
    group = request.GET.get('group')
    faculty = request.GET.get('faculty')
    semester = request.GET.get('semester')
    period = request.GET.get('period')

    departments = Department.objects.all()

    if group:
        faculty = Faculty.objects.filter(studentgroup__name=group).first()
        departments = departments.filter(faculty=faculty)
    elif faculty and semester:
        departments = departments.filter(
            faculty__name=faculty,
            faculty__studentgroup__year_of_admission=int(
                (datetime.now().year - (
                        int(semester) - 1) * 0.5) // 1))
    elif period:
        start, end = period.split(',')
        departments = departments.filter(
            faculty__studentgroup__year_of_admission__range=(start, end))

    departments = departments.distinct()

    total_departments = departments.count()

    data = {
        'total_departments': total_departments,
        'departments': list(departments.values())
    }

    return JsonResponse(data)


# 5. Получить список и общее число преподавателей, проводивших (проводящих)
# занятия по указанной дисциплине в указанной группе либо на указанном курсе
# указанного факультета
def get_instructors_by_subject(request):
    subject = request.GET.get('subject')
    group = request.GET.get('group')
    course = request.GET.get('course')
    faculty = request.GET.get('faculty')

    instructors = Instructor.objects.all()

    if subject and group:
        instructors = instructors.filter(
            department__faculty__curriculum__subject__name=subject
        )
        instructors = instructors.filter(
            department__faculty__studentgroup__name=group)
    if course and faculty:
        instructors = instructors.filter(
            department__faculty__studentgroup__year_of_admission=datetime.now().year - (
                    int(course) - 1))
        instructors = instructors.filter(department__faculty__name=faculty)

    instructors = instructors.distinct()

    total_instructors = instructors.count()

    data = {
        'total_instructors': total_instructors,
        'instructors': list(instructors.values())
    }

    return JsonResponse(data)


# 6. Список и число преподавателей проводивших лекции и др. виды занятий
def get_instructors_by_activity(request):
    group = request.GET.get('group')
    course = request.GET.get('course')
    faculty = request.GET.get('faculty')
    semester = request.GET.get('semester')
    period = request.GET.get('period')

    instructors = Instructor.objects.all()

    if group:
        instructors = instructors.filter(
            department__faculty__studentgroup__name=group
        )

    if course and faculty and semester:
        instructors = instructors.filter(
            department__faculty__studentgroup__year_of_admission=datetime.now().year - (
                    int(course) - 1))
        instructors = instructors.filter(
            department__faculty__name=faculty,
            department__faculty__studentgroup__year_of_admission=int(
                (datetime.now().year - (
                        int(semester) - 1) * 0.5) // 1)
        )
    if period:
        start, end = period.split(',')
        instructors = instructors.filter(
            department__faculty__studentgroup__year_of_admission__range=(
                int(start), int(end)))

    instructors = instructors.distinct()

    total_instructors = instructors.count()

    data = {
        'total_instructors': total_instructors,
        'instructors': list(instructors.values())
    }

    return JsonResponse(data)


# 7. Получить список и общее число студентов указанных групп, сдавших зачет
# либо экзамен по указанной дисциплине с указанной оценкой.
def get_exam_results(request):
    group = request.GET.get('group')
    subject = request.GET.get('subject')
    grade = request.GET.get('grade')

    exam_records = ExamRecord.objects.filter(
        student__student_group__name=group, subject__name=subject, grade=grade)

    total_students = exam_records.count()

    data = {
        'total_students': total_students,
        'exam_records': list(exam_records.values())
    }

    return JsonResponse(data)


# 8. Получить список и общее число студентов указанных групп или указанного
# курса указанного факультета, сдавших указанную сессию на отлично, без троек,
# без двоек.
def get_session_results(request):
    group = request.GET.get('group')
    course = request.GET.get('course')
    faculty = request.GET.get('faculty')
    grade = request.GET.get('grade')

    students = Student.objects.all()
    if group:
        students = students.filter(student_group__name=group)
    elif course:
        students = students.filter(
            student_group__year_of_admission=datetime.now().year - (
                    int(course) - 1
            ))
    if faculty:
        students = students.filter(student_group__faculty__name=faculty)

    if grade == 'excellent':
        students = students.filter(examrecord__grade='A')

    elif grade == 'no_threes':
        students = students.filter(examrecord__grade__in=['A', 'B'])
    elif grade == 'no_twos':
        students = students.filter(examrecord__grade__in=['A', 'B', 'C'])

    total_students = students.count()

    data = {
        'total_students': total_students,
        'students': list(students.values())
    }

    return JsonResponse(data)


# 9. Получить перечень преподавателей, принимающих экзамены в указанных группах, по указанным дисциплинам, в указанном семестре.
def get_examiners(request):
    group = request.GET.get('group')
    subject = request.GET.get('subject')
    semester = request.GET.get('semester')

    examiners = Instructor.objects.filter(
        examrecord__student__student_group__name=group,
        examrecord__subject__name=subject,
        examrecord__semester=semester).distinct()

    total_examiners = examiners.count()

    data = {
        'total_examiners': total_examiners,
        'examiners': list(examiners.values())
    }

    return JsonResponse(data)


# 10. Список студентов, которым преподаватель поставил оценку за экзамен по определенным дисциплинам, в указанных семестрах, за некоторый период
def get_grades_by_instructor(request):
    instructor = request.GET.get('instructor')
    subject = request.GET.get('subject')
    semester = request.GET.get('semester')

    exam_records = ExamRecord.objects.filter(instructor__name=instructor,
                                             subject__name=subject,
                                             semester=semester)

    total_records = exam_records.count()

    data = {
        'total_records': total_records,
        'exam_records': list(exam_records.values())
    }

    return JsonResponse(data)


# 11. Список студентов и тем дипломных работ, выполняемых ими на указанной кафедре либо у указанного преподавателя
def get_thesis_topics(request):
    department = request.GET.get('department')
    instructor = request.GET.get('instructor')

    theses = Thesis.objects.filter(instructor__department__name=department)

    if instructor:
        theses = theses.filter(instructor__name=instructor)

    total_theses = theses.count()

    data = {
        'total_theses': total_theses,
        'theses': list(theses.values())
    }

    return JsonResponse(data)


# 12. Список руководителей дипломных работ с указанной кафедры либо факультета полностью и раздельно по категориям преподавателей
def get_thesis_supervisors(request):
    department = request.GET.get('department')
    faculty = request.GET.get('faculty')
    category = request.GET.get('category')

    instructors = Instructor.objects.filter(
        thesis__instructor__department__name=department)

    if faculty:
        instructors = instructors.filter(department__faculty__name=faculty)
    if category:
        instructors = instructors.filter(category=category)

    instructors = instructors.distinct()

    total_supervisors = instructors.count()

    data = {
        'total_supervisors': total_supervisors,
        'supervisors': list(instructors.values())
    }

    return JsonResponse(data)


# 13. Нагрузка преподавателей в указанном семестре для конкретного преподавателя либо для преподавателей указанной кафедры
def get_instructor_load(request):
    instructor = request.GET.get('instructor')
    department = request.GET.get('department')
    semester = request.GET.get('semester')

    load = InstructorLoad.objects.filter(
        teaching_assignment__semester=semester)

    if instructor:
        load = load.filter(instructor__name=instructor)
    if department:
        load = load.filter(instructor__department__name=department)

    total_hours = load.aggregate(total_hours=Sum('hours'))

    data = {
        'total_hours': total_hours['total_hours'],
        'load': list(load.values())
    }

    return JsonResponse(data)
