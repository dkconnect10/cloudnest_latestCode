"use client"
import { useContext } from "react"
import { DashboardsContext } from "@/utils/Context"
import { TopHospitalsLayout } from "@components/Layout/TopHospitalsLayout"
import { DashboardIntro } from "./DashboardIntro"
import { MoleculesLayout } from "../Layout/MoleculesLayout"

export const DashboardContainer = () => {
	const dashboardCtxt = useContext(DashboardsContext)
	const { dashboard } = dashboardCtxt
	const isHospitalDashboard = dashboard === "Hospitals Performances"

	return (
		<div className="w-full h-full">
			<DashboardIntro isHospitalDashboard={isHospitalDashboard} />
			{isHospitalDashboard ? <TopHospitalsLayout /> : <MoleculesLayout/>}
		</div>
	)
}
