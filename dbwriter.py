from Objects.course_code import *
from Objects.course import *
from Objects.coordinator import *
from Objects.degree import *
from Objects.degree_core import *
from Objects.degree_plan import *
from Objects.degree_option import *

import sqlite3

class DBWriter:
    def __init__(self, db_path):
        self.db_path = db_path

    def writeCourseCode(self, array: dict[str, CourseCode]):
        """
            Writes course code information into database
        """
        
        try:
            con = sqlite3.connect(self.db_path)
            cur = con.cursor()
            for course_code_obj in array.values():
                cur.execute('''
                    INSERT INTO course_code (course_name, course_code, campus, career, school, learning_mode)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    course_code_obj.getName(),
                    course_code_obj.getCode(),
                    course_code_obj.getCampus(),
                    course_code_obj.getCareer(),
                    course_code_obj.getSchool(),
                    course_code_obj.getLearningMode()
                ))
            con.commit()
        except sqlite3.Error as e:
            print("Error while writing course codes:", e)
        finally:
            con.close()

    def writeDegree(self, array: dict[str, Degree]):
        """
            Writes degree information into database
        """
        try:
            con = sqlite3.connect(self.db_path)
            cur = con.cursor()

            for degree_obj in array.values():
                for student_type in ['domestic', 'international']:
                    if degree_obj.getAvailability().get(student_type) == True:
                        cur.execute('''
                            INSERT INTO degree (
                                degree_name, level_of_study, student_type, learning_mode,
                                entry_score, duration, fees, next_intake, location
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                        ''', (
                            degree_obj.getDegreeName(),
                            degree_obj.getLevelOfStudy(),
                            student_type,
                            degree_obj.getLearningMode().get(student_type),
                            degree_obj.getEntryScore().get(student_type),
                            degree_obj.getDuration().get(student_type),
                            degree_obj.getFees().get(student_type),
                            degree_obj.getNextIntake().get(student_type),
                            degree_obj.getLocation().get(student_type)
                        ))
                for plans in degree_obj.getDegreePlans().values():
                    cur.execute('''
                        INSERT INTO degree_plan (degree_name, plan_code, credit_description, major_minor_description)
                        VALUES (?, ?, ?, ?)
                    ''', (
                        degree_obj.getDegreeName(),
                        plans.getPlanCode(),
                        plans.getCreditDescription(),
                        plans.getMajorMinorDescription()
                    ))
                    
                    if plans.getCoreUnits():
                        for course_code, year in plans.getCoreUnits().items():
                            cur.execute('''
                                INSERT INTO degree_core (degree_name, program_year, course_code)
                                VALUES (?, ?, ?)
                            ''', (
                                plans.getPlanCode(),
                                year,
                                course_code
                            ))
                    
                    if plans.getMajorOptions():
                        unique = list(plans.getMajorOptions().values())
                        unique = list(set(unique))  # Remove duplicates
                        for type in unique:
                            cur.execute('''
                                INSERT INTO degree_options (option_name, degree_name)
                                VALUES (?, ?)
                            ''', (
                                type,
                                plans.getPlanCode()
                            ))
                        for courses in plans.getMajorOptions().keys():
                            cur.execute('''
                                INSERT or IGNORE INTO option_courses (option_name, course_code)
                                VALUES (?, ?)
                            ''', (
                                plans.getMajorOptions().get(courses),
                                courses
                            ))
                    
                    if plans.getMinorOptions():
                        unique = list(plans.getMinorOptions().values())
                        unique = list(set(unique))  # Remove duplicates
                        for type in unique:
                            cur.execute('''
                                INSERT INTO degree_options (option_name, degree_name)
                                VALUES (?, ?)
                            ''', (
                                type,
                                plans.getPlanCode()
                            ))
                        for courses in plans.getMinorOptions().keys():
                            cur.execute('''
                                INSERT or IGNORE INTO  option_courses (option_name, course_code)
                                VALUES (?, ?)
                            ''', (
                                plans.getMinorOptions().get(courses),
                                courses
                            ))
                    
                    if plans.getOtherOptions():
                        unique = list(plans.getOtherOptions().values())
                        unique = list(set(unique))  # Remove duplicates
                        for type in unique:
                            cur.execute('''
                                INSERT INTO degree_options (option_name, degree_name)
                                VALUES (?, ?)
                            ''', (
                                type,
                                plans.getPlanCode()
                            ))
                        for courses in plans.getOtherOptions().keys():
                            cur.execute('''
                                INSERT or IGNORE INTO option_courses (option_name, course_code)
                                VALUES (?, ?)
                            ''', (
                                plans.getOtherOptions().get(courses),
                                courses
                            ))

            con.commit()
        except sqlite3.Error as e:
            print("Error while writing degrees:", e)
        finally:
            con.close()

    def writeCoordinator(self, array: dict[str, Coordinator]):
        """
            Write co-ordinator information into database
        """
        try:
            con = sqlite3.connect(self.db_path)
            cur = con.cursor()
            for course_contact_obj in array.values():
                cur.execute('''
                    INSERT or IGNORE INTO course_coordinator (coordinator_name, coordinator_phone, coordinator_email, coordinator_location, coordinator_availability)
                    VALUES (?, ?, ?, ?, ?)
                ''', (
                    course_contact_obj.getCoordinatorName(),
                    course_contact_obj.getCoordinatorPhone(),
                    course_contact_obj.getCoordinatorEmail(),
                    course_contact_obj.getCoordinatorLocation(),
                    course_contact_obj.getCoordinatorAvailability()
                ))
            con.commit()
        except sqlite3.Error as e:
            print("Error while writing course codes:", e)
        finally:
            con.close()


    def writeCourses(self, array: dict[str, Course]):
        """
            Write course information inro database
        """
        try:
            con = sqlite3.connect(self.db_path)
            cur = con.cursor()
            for course_obj in array.values():
                cur.execute('''
                    INSERT INTO courses (course_name, credit_point, coordinator_name, description)
                    VALUES (?, ?, ?, ?)
                ''', (
                    course_obj.getCourseTitle(),
                    course_obj.getCreditPoints(),
                    course_obj.getCourseCoordinator(),
                    course_obj.getDescription()
                ))
            con.commit()
        except sqlite3.Error as e:
            print("Error while writing courses:", e)
        finally:
            con.close()



