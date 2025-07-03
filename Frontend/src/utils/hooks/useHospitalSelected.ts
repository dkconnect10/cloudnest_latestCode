"use client"
import { useContext } from "react"
import { HospitalContext, HospitalContextProps } from "@utils/Context/index"
import { topHospitals } from "@utils/data/hospitals/hospitals"

export const useHospitalSelected = () => {
	const hospitalCtxt: HospitalContextProps = useContext(HospitalContext)
	let hasHospitalSelected: boolean = false

	if (!hospitalCtxt) {
		console.error("Hospital context is not available.")
		return { hospital: topHospitals, hasHospitalSelected: false }
	}

	const { hospital } = hospitalCtxt

	hasHospitalSelected = hospital.length === 1 && true

	return { hospital, hasHospitalSelected }
}
