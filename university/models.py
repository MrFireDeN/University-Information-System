from django.db import models


# Факультет
class Faculty(models.Model):
    name = models.CharField(max_length=255)
    deanery = models.CharField(max_length=255)  # Деканат

    def __str__(self):
        return self.name


# Кафедра
class Department(models.Model):
    name = models.CharField(max_length=255)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Категории преподавателей
class InstructorCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Преподаватель
class Instructor(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.ForeignKey(InstructorCategory, on_delete=models.CASCADE)
    birth_year = models.IntegerField()
    has_children = models.BooleanField(default=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2,
                                 null=True,
                                 blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,
                              default=GENDER_CHOICES[0][0])

    is_phd = models.BooleanField(default=False)  # Кандидат наук
    is_doctor = models.BooleanField(default=False)  # Доктор наук
    is_postgraduate_student = models.BooleanField(default=False)  # Аспирант

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


# Группа студентов
class StudentGroup(models.Model):
    name = models.CharField(max_length=255)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    year_of_admission = models.IntegerField()

    def __str__(self):
        return self.name


# Студент
class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)
    course = models.IntegerField()  # Курс
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_year = models.IntegerField()
    has_children = models.BooleanField(default=False)
    scholarship = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=True,
                                      blank=True)  # Размер стипендии, если есть

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


# Учебная дисциплина
class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Учебный план
class Curriculum(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    year_of_admission = models.IntegerField()  # Год набора студентов
    semester = models.IntegerField()  # Номер семестра
    lecture_hours = models.IntegerField()
    seminar_hours = models.IntegerField()
    lab_hours = models.IntegerField()
    consultation_hours = models.IntegerField()
    coursework_hours = models.IntegerField()
    independent_work_hours = models.IntegerField()
    control_form = models.CharField(max_length=50)  # Зачет, экзамен и т.д.

    def __str__(self):
        return f"{self.subject.name} - {self.year_of_admission} year - {self.semester} semester"


# Учебное поручение
class TeachingAssignment(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)
    semester = models.IntegerField()

    def __str__(self):
        return f"{self.department.name} - {self.subject.name} - {self.student_group.name}"


# Распределение нагрузки преподавателей
class InstructorLoad(models.Model):
    teaching_assignment = models.ForeignKey(TeachingAssignment,
                                            on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    lecture_hours = models.IntegerField(null=True, blank=True)
    seminar_hours = models.IntegerField(null=True, blank=True)
    lab_hours = models.IntegerField(null=True, blank=True)
    consultation_hours = models.IntegerField(null=True, blank=True)
    coursework_hours = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.instructor} - {self.teaching_assignment}"


# Экзамены и зачеты
class ExamRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)  # Оценка или "зачет"/"незачет"
    date = models.DateField()

    def __str__(self):
        return f"{self.student} - {self.subject.name} - {self.grade}"


# Работа
class Thesis(models.Model):
    title = models.CharField(max_length=255)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    defense_date = models.DateField()

    def __str__(self):
        return f"{self.title} - {self.student} - {self.instructor}"
