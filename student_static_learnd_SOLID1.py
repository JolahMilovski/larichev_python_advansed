from dataclasses import dataclass

@dataclass
class Student:
    """
    describe student 
    """
    name:str
    score:int

@dataclass
class StudentRepository:
    """
    store list of student
    add new student to list
    return list of student
    
    """
    list_of_student =[] 

            
    def add_student(self, student: Student):
        
        self.list_of_student.append(student)

    def return_list_of_student(self):
        return self.list_of_student

@dataclass        
class StudentJournal:

    journal: StudentRepository

    def  get_average_score(self) -> float:

        student = self.journal.return_list_of_student()
        if not student:
            return 0;

        average = sum (s.score for s in student ) / len(student)

        return  average
    
    def get_best_student(self) -> Student:

        student = self.journal.return_list_of_student()
        return max(student, key = lambda s: s.score)

@dataclass
class RepositoryPrint():

    repository: StudentRepository
    stat_service: StudentJournal

    def print_report(self):
        print("Student report")

        for s in self.repository.return_list_of_student():
            print(f"    {s.name}    {s.score}")

        best = self.stat_service.get_best_student()
        print(f" The best is {best}")


repo = StudentRepository()

stat_service = StudentJournal(repo)

printer = RepositoryPrint(repo, stat_service )

repo.add_student(Student("QWE", 42))
repo.add_student(Student("ASD", 53))
repo.add_student(Student("ERF", 78))

printer.print_report()
