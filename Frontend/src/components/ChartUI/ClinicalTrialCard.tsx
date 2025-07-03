import clsx from "clsx"
import { ClinicalTrial } from "@/utils/data/hospitals/hospitalsTypes"

type ClinicalTrialCardProps = {
	trial: ClinicalTrial
	key: string
}

export const ClinicalTrialCard = ({ trial, key }: ClinicalTrialCardProps) => {
	const { name, status, endDate, startDate, totalPatients } = trial

	return (
		<div
			key={key}
			className="flex flex-col mb-4 bg-white shadow-md rounded-md p-4 space-y-2">
			<div className="font-semibold">{name}</div>
			<div>
				<span
					className={clsx(
						status === "En cours" ? "bg-tertiary text-white" : "bg-vi/10",
						"rounded-full px-2 py-[2px] text-sm"
					)}>
					{status}
				</span>
			</div>
			<p className="text-sm">
				<strong>Start Date:</strong> {startDate}
			</p>
			<p className="text-sm">
				<strong>End Date:</strong> {endDate}
			</p>
			<p className="text-sm">
				<strong>Patients:</strong> {totalPatients}
			</p>
		</div>
	)
}
