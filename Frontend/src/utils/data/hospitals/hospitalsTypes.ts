type HospitalDepartment = {
	department: string
	patientsPerDay: number
	averageWaitTime: number
}

type ClinicalTrial = {
	name: string
	status: string
	startDate: string
	endDate: string
	totalPatients: number
}

type DoctorSpecialty = {
	specialty: string
	numberOfDoctors: number
	satisfactionRate: number
}

type MonthlyHospitalization = {
	month: string
	year: number
	hospitalizations: number
}

type Overview = {
	totalPatients: number
	satisfactionRate: number
	totalTreatments: number
	numberOfDoctors: number
	numberOfNurses: number
}

type Hospital = {
	name: string
	location: string
	overview: Overview
	monthlyHospitalizations: MonthlyHospitalization[]
	doctorSpecialties: DoctorSpecialty[]
	clinicalTrials: ClinicalTrial[]
	hospitalDepartments: HospitalDepartment[]
}

export type {
	Hospital,
	Overview,
	DoctorSpecialty,
	MonthlyHospitalization,
	HospitalDepartment,
	ClinicalTrial,
}
