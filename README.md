ec2 instance
------------------------------------------------
**collect static files and media
     cammand =>  python manage.py collectstatic
 ** restart gunicon 
  command => sudo systemctl restart gunicorn
*** Restart Nginx
	commnd =>sudo systemctl restart nginx
	
	----------------------------------------
	python manage.py collectstatic --noinput
	sudo systemctl restart gunicorn
	sudo systemctl restart nginx
------------------------------------------------
** check sarvices start or not 
sudo systemctl status gunicorn
sudo systemctl status nginx
  
  
  
  --------------------------------
  token=>
   Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUxODIzMzU0LCJpYXQiOjE3NTE3ODAxNTQsImp0aSI6ImRmYmM5MWYzMDMzNTRkOTViY2E1MDBlYTBjMzY5Yzk1IiwidXNlcl9pZCI6MX0.KOqlkxTvj7P6XPN54XE3sIB9sGhRovGY-yuR9bCdYW8



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