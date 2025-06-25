# cloudnest_latestCode

hospital_management/
├── apps/
│   ├── users/
│   ├── doctors/
│   ├── patients/
│   ├── appointments/
│   ├── prescriptions/
│   ├── medical_records/
│   ├── billing/
│   ├── rooms/
│   └── inventory/
├── src/
│   ├── settings/
│   └── urls.py
├── manage.py


✅ Roles का Structure समझें (RBAC – Role Based Access Control):
Role	अधिकार/Actions
SuperUser	System का मालिक – सब कुछ manage कर सकता है
Admin	Staff और operations manage कर सकता है (limited to hospital)
Doctor	Appointments, prescriptions, patient history access
Receptionist	Appointments create/edit, patient register
Nurse	Basic patient info update, vitals add
Lab Admin	Test report upload/view