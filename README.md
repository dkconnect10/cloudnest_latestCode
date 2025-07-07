# cloudnest_latestCode


Hospital Management Portal Access Tree

This tree illustrates the hierarchy of user roles and their access levels, starting with the first user who registers.

+--------------------------+
|  Super Admin (First User)|
+--------------------------+
      |
      |  (Creates and Manages)
      v
+--------------------------+
|          Admins          |
+--------------------------+
      |
      |  (Creates and Manages)
      v
+--------------------------+
|        Departments       |
+--------------------------+
  /      |       |      \
 /       |       |       \
v        v       v        v
+--------+ +--------+ +--------+
| Doctor | | Nurse  | |  Lab   |
|        | |        | |  Tech  |
+--------+ +--------+ +--------+
                               |
                               v
                        +-------------+
                        |   Patient   |
                        |   (Access   |
                        |   View)     |
                        +-------------+

Sr	Role Name	Use / Responsibility
1	Hospital Director	Top-level decision maker
2	Medical Superintendent	Day-to-day overall operations
3	Chief Medical Officer	Supervises doctors and medical policies
4	Head of Department	Leads a specific medical department (e.g. Ortho, Neuro)
5	Doctor	General doctor (can be classified further)
6	Nurse	Patient care
7	Lab Technician	Medical test handling
8	Pharmacist	Manages and distributes medicines
9	Receptionist	Handles patient entry, appointment, billing