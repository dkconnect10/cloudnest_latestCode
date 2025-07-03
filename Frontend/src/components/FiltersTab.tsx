import { useContext } from "react"
import { SelectInput } from "./UI/SelectInput"
import { years, HospitalContext, TimeLineContext } from "@/utils/Context"
import { hospitalsName } from "@/utils/data/hospitals/hospitals"

export const FiltersTab = () => {
	const hospitalCtxt = useContext(HospitalContext)
	const timeLineCtxt = useContext(TimeLineContext)
	const { handleHospital } = hospitalCtxt
	const { handleTimeLine } = timeLineCtxt

	const handleSelectHospital = (hospitalSelected: string) => {
		handleHospital(hospitalSelected)
	}

	const handleSelectTimeLine = (yearSelected: string) => {
		handleTimeLine(yearSelected)
	}

	return (
		<div className="flex max-h-fit h-full px-3 py-2 md:p-6 mt-2 md:mt-4 mb-4 md:gap-4 block bg-white/30 rounded-lg">
			<SelectInput
				labels={hospitalsName}
				title="Hospitals"
				onSelectChange={handleSelectHospital}
				placeholder="Select an hospital"
			/>

			<SelectInput
				labels={years}
				title="Date"
				onSelectChange={handleSelectTimeLine}
				placeholder="Select an year"
			/>
		</div>
	)
}
