DROP TABLE IF EXISTS course_coordinator;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS degree;
DROP TABLE IF EXISTS degree_options;
DROP TABLE IF EXISTS degree_plan;
DROP TABLE IF EXISTS course_code;
DROP TABLE IF EXISTS degree_core;
DROP TABLE IF EXISTS options_details;
DROP TABLE IF EXISTS option_courses;

CREATE TABLE course_coordinator (
  coordinator_name VARCHAR(100) NOT NULL PRIMARY KEY,
  coordinator_phone VARCHAR(20),
  coordinator_email VARCHAR(100),
  coordinator_location VARCHAR(100),
  coordinator_avaliability VARCHAR(50),
)

CREATE TABLE courses (
  course_name VARCHAR(100) NOT NULL PRIMARY KEY,
  credit_point int,
  coordinator_name VARCHAR(100),
  decscription VARCHAR(255),
  FOREIGN KEY (coordinator_name) REFERENCES course_coordinator(coordinator_name)
);

CREATE TABLE degree (
    degree_name VARCHAR(100) NOT NULL,
    level_of_study VARCHAR(50),
    student_type VARCHAR(50) NOT NULL,
    learning_mode VARCHAR(50),
    entry_score VARCHAR(50),
    duration INT,
    fees VARCHAR(50),
    next_intake VARCHAR(50),
    location VARCHAR(50),
    PRIMARY KEY (degree_name, student_type)
);

CREATE TABLE degree_options (
  option_name VARCHAR(100) NOT NULL,
  degree_name VARCHAR(100) NOT NULL,
  PRIMARY KEY (option_name, degree_name)
  FOREIGN KEY (degree_name) REFERENCES degree_plan(degree_name)
)

CREATE TABLE degree_plan (
  degree_name VARCHAR(100) NOT NULL,
  plan_code VARCHAR(50) NOT NULL,
  credit_description VARCHAR(255),
  major_minor_description VARCHAR(255),
  PRIMARY KEY (degree_name, plan_code)
  FOREIGN KEY (degree_name) REFERENCES degree(degree_name)
)

CREATE TABLE course_code (
  course_name VARCHAR(100) NOT NULL,
  course_code VARCHAR(10) NOT NULL,
  campus VARCHAR(50),
  career VARCHAR(50),
  school VARCHAR(50),
  learning_mode VARCHAR(50),
  PRIMARY KEY (course_code, course_name),
  FOREIGN KEY (course_name) REFERENCES courses(course_name),
)

CREATE TABLE degree_core (
  degree_name VARCHAR(100) NOT NULL,
  program_year VARCHAR(50) NOT NULL,
  course_code int  NOT NULL,
  PRIMARY KEY (degree_name, program_year, course_code),
  FOREIGN KEY (degree_name) REFERENCES degree(degree_name),
  FOREIGN KEY (course_code) REFERENCES course_code(course_code)
)

CREATE TABLE options_details (
  option_name VARCHAR(100) NOT NULL PRIMARY KEY,
  option_type VARCHAR(50),
)

CREATE TABLE option_courses (
  option_name VARCHAR(100) NOT NULL,
  course_code VARCHAR(10) NOT NULL,
  PRIMARY KEY (option_name, course_code),
  FOREIGN KEY (option_name) REFERENCES options_details(option_name),
  FOREIGN KEY (course_code) REFERENCES courses(course_code)
)
