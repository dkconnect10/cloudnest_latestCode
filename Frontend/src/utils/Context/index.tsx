"use client"
import { createContext, useState, ReactNode } from "react"
import { tabs } from "@/utils/data/tabs"
import { topHospitals } from "@utils/data/hospitals/hospitals"
import { Hospital } from "@utils/data/hospitals/hospitalsTypes"

export const aggregateYears = (datas: Hospital[]): string[] => {
	return datas.reduce((acc, hospital) => {
		hospital.monthlyHospitalizations.forEach((el) => {
			const year = el.year.toString()
			if (!acc.includes(year)) {
				acc.push(year)
			}
		})
		return acc
	}, [] as string[])
}

export const getClosestYear = (years: string[]): string => {
	const currentYear = new Date().getFullYear().toString()

	return years.includes(currentYear) ? currentYear : years[years.length - 1]
}

export const years = aggregateYears(topHospitals)
export const closestYear = getClosestYear(years)

// Dashboards Ctxt
export type DashboardsContextProps = {
	dashboard: string
	handleDashboard: (dashboardSelected: string) => void
}

export const DashboardsContext = createContext<DashboardsContextProps>({
	dashboard: tabs[0],
	handleDashboard: () => {},
})

// Hospital Ctxt
export type HospitalContextProps = {
	hospital: Hospital[]
	handleHospital: (hospitalSelected: string) => void
}

export const HospitalContext = createContext<HospitalContextProps>({
	hospital: topHospitals,
	handleHospital: () => {},
})

// TimeLine Ctxt
export type TimeLineContextProps = {
	timeLine: string
	handleTimeLine: (timeLineSelected: string) => void
}

export const TimeLineContext = createContext<TimeLineContextProps>({
	timeLine: closestYear,
	handleTimeLine: () => {},
})

//Providers pour encapsuler la logique de gestion des états
export const AppProviders = ({ children }: { children: ReactNode }) => {
	const [dashboard, setDashboard] = useState<string>(tabs[0])
	const [hospital, setHospital] = useState<Hospital[]>(topHospitals)
	const [timeLine, setTimeLine] = useState<string>(closestYear)

	const handleDashboard = (dashboardSelected: string) => {
		setDashboard(dashboardSelected)
	}

	const handleHospital = (hospitalSelected: string) => {
		const selectedHospital = topHospitals.filter(
			(el) => el.name === hospitalSelected
		)
		setHospital(selectedHospital.length ? selectedHospital : topHospitals)
	}

	const handleTimeLine = (timeLineSelected: string) => {
		setTimeLine(timeLineSelected)
	}

	return (
		<DashboardsContext.Provider value={{ dashboard, handleDashboard }}>
			<HospitalContext.Provider value={{ hospital, handleHospital }}>
				<TimeLineContext.Provider value={{ timeLine, handleTimeLine }}>
					{children}
				</TimeLineContext.Provider>
			</HospitalContext.Provider>
		</DashboardsContext.Provider>
	)
}
