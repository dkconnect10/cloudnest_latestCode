"use client"
import React, { useContext } from "react"
import { useHospitalSelected } from "@/utils/hooks/useHospitalSelected"
import { useBreakpoint } from "@/utils/hooks/useBP"
import { ClinicalTrialsList } from "../TopHospitalsCharts/ClinicalTrialsList"
import { DepartmentsBar } from "../TopHospitalsCharts/DepartmentsBar"
import { DoctorSpecialtiesRadar } from "../TopHospitalsCharts/DoctorSpeciltiesRadar"
import { Patients } from "../TopHospitalsCharts/KeyNumbers/Patients"
import { SatisfactionRate } from "../TopHospitalsCharts/KeyNumbers/SatisfactionRate"
import { Treatments } from "../TopHospitalsCharts/KeyNumbers/Treatments"
import { MonthlyHospitalizations } from "../TopHospitalsCharts/MonthlyHospitalizations"
import { Hospital } from "@/utils/data/hospitals/hospitalsTypes"
import { TimeLineContext } from "@/utils/Context"
import { EmployeesDuoTons } from "../TopHospitalsCharts/EmployeesDuoTons"

export type ComponentProps = {
	datas: Hospital[]
	hasHospitalSelected: boolean
	isMobile: boolean
	timeLine?: string
}

export const TopHospitalsLayout = () => {
	const { hasHospitalSelected, hospital } = useHospitalSelected()
	const timeLineCtxt = useContext(TimeLineContext)
	const { timeLine } = timeLineCtxt
	const breakpoint = useBreakpoint()
	const isMobile = breakpoint === "mobile"

	return (
		<section className="w-full flex flex-col md:bg-white/20 md:flex-row flex-wrap md:gap-4 md:p-8 rounded-lg">
			<div className="key__number__container w-full md:w-[88%] md:flex md:gap-4">
				<SatisfactionRate
					datas={hospital}
					isMobile={isMobile}
					hasHospitalSelected={hasHospitalSelected}
				/>
				<Patients
					datas={hospital}
					isMobile={isMobile}
					hasHospitalSelected={hasHospitalSelected}
				/>
				<Treatments
					datas={hospital}
					isMobile={isMobile}
					hasHospitalSelected={hasHospitalSelected}
				/>
			</div>

			<div className="w-full md:flex md:gap-4">
				<div className="w-full flex flex-col md:gap-4">
					<MonthlyHospitalizations
						datas={hospital}
						isMobile={isMobile}
						hasHospitalSelected={!hasHospitalSelected}
						timeLine={timeLine}
					/>
					<DoctorSpecialtiesRadar
						datas={hospital}
						isMobile={isMobile}
						hasHospitalSelected={hasHospitalSelected}
					/>
				</div>

				<div className="w-full flex flex-col md:gap-4">
					<EmployeesDuoTons
						datas={hospital}
						isMobile={isMobile}
						hasHospitalSelected={hasHospitalSelected}
					/>
					<DepartmentsBar
						datas={hospital}
						isMobile={isMobile}
						hasHospitalSelected={hasHospitalSelected}
					/>
				</div>
			</div>

			<ClinicalTrialsList
				datas={hospital}
				isMobile={isMobile}
				hasHospitalSelected={hasHospitalSelected}
			/>
		</section>
	)
}
