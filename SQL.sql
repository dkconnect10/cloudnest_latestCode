select * from public.users_user
select * from public.users_role
select * from public.hospital_hospital
select * from public.hospital_userhospital


INSERT INTO public.users_role (name, is_active, created_at, updated_at)
VALUES
('Super Admin', TRUE, NOW(), NOW()),
('Admin', TRUE, NOW(), NOW()),
('Doctor', TRUE, NOW(), NOW()),
('Nurse', TRUE, NOW(), NOW()),
('Receptionist', TRUE, NOW(), NOW()),
('Pharmacist', TRUE, NOW(), NOW()),
('Lab Technician', TRUE, NOW(), NOW()),
('Ward Boy', TRUE, NOW(), NOW());
