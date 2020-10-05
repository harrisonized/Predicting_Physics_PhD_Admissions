CREATE DATABASE gradcafe_physics;

\c gradcafe_physics;

CREATE TABLE physics_df(
  institution TEXT
  subject TEXT
  degree_type_and_admission_semester TEXT
  accept_or_reject TEXT
  method_of_communication TEXT
  date_ DATE
  gpa FLOAT
  gre_verbal INT
  gre_quantitative INT
  gre_writing INT
  gre_subject INT
  student_classification TEXT
  date_posted DATE
  comments TEXT
  american TEXT
  papers TEXT
  research TEXT
  decision TEXT
);

\copy physics_df FROM '/home/harrisonized/github/metis/gradcafe-physics/data/physics-df.csv' DELIMITER ',' CSV HEADER;
