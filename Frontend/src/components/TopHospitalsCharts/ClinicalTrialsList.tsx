"use client"
import { useEffect, useState } from "react"
import Image from "next/image"
import clsx from "clsx"
import { ChartHeader } from "@components/ChartUI/ChartHeader"
import { ComponentProps } from "@components/Layout/TopHospitalsLayout"
import { ChartContainer } from "@components/ChartUI/ChartContainer"
import { ClinicalTrial, Hospital } from "@/utils/data/hospitals/hospitalsTypes"
import treatmentIcon from "@assets/icons/treatment.svg"
import sortIcon from "@assets/icons/sort.svg"
import { sortData } from "@/utils/utils"
import { ResumeCharts } from "../ChartUI/ResumeCharts"
import { ClinicalTrialCard } from "../ChartUI/ClinicalTrialCard"

export const ClinicalTrialsList = ({ datas, isMobile }: ComponentProps) => {
	const [chartData, setChartData] = useState<ClinicalTrial[] | null>(null)
	const [sortOrder, setSortOrder] = useState(true) //"true" = croissant, "false" = décroissant
	const [resumeDatas, setResumeDatas] = useState<ClinicalTrial | null>(null)

	useEffect(() => {
		const clinicalTrialsList = datas.flatMap(
			(hospital: Hospital) => hospital.clinicalTrials
		)

		setChartData(clinicalTrialsList)
	}, [datas])

	useEffect(() => {
		const highestPatients =
			chartData &&
			chartData.reduce(
				(max, hospital) =>
					hospital.totalPatients > max.totalPatients ? hospital : max,
				chartData[0]
			)

		setResumeDatas(highestPatients)
	}, [chartData])

	const handleSort = (key: string) => {
		if (chartData) {
			const sortedData = sortData(chartData, key, sortOrder)
			setChartData(sortedData)
			setSortOrder(!sortOrder) //inverse l’ordre de tri au prochain clic
		}
	}

	return (
		<ChartContainer>
			<ChartHeader title="Clinical Trials" icon={treatmentIcon} />

			<div className="w-full max-h-[350px] md:max-h-[550px] overflow-y-auto">
				{!isMobile ? (
					<table className="w-full">
						<thead className="text-left">
							<tr>
								<th className="pr-2" onClick={() => handleSort("name")}>
									<div className="inline-flex items-center hover:cursor-pointer ease-in-out duration-150 transform-all hover:opacity-80 font-semibold">
										<span>Name</span>
										<Image alt="" src={sortIcon} className="ml-2 h-3 w-3" />
									</div>
								</th>
								<th className="px-4" onClick={() => handleSort("status")}>
									<div className="inline-flex items-center hover:cursor-pointer ease-in-out duration-150 transform-all hover:opacity-80 font-semibold">
										<span>Status</span>
										<Image alt="" src={sortIcon} className="ml-2 h-3 w-3" />
									</div>
								</th>
								<th className="px-2" onClick={() => handleSort("startDate")}>
									<div className="inline-flex items-center hover:cursor-pointer ease-in-out duration-150 transform-all hover:opacity-80 font-semibold">
										<span>Start Date</span>
										<Image alt="" src={sortIcon} className="ml-2 h-3 w-3" />
									</div>
								</th>
								<th className="px-2" onClick={() => handleSort("endDate")}>
									<div className="inline-flex items-center hover:cursor-pointer ease-in-out duration-150 transform-all hover:opacity-80 font-semibold">
										<span>End Date</span>
										<Image alt="" src={sortIcon} className="ml-2 h-3 w-3" />
									</div>
								</th>
								<th
									className="px-2"
									onClick={() => handleSort("totalPatients")}>
									<div className="inline-flex items-center hover:cursor-pointer ease-in-out duration-150 transform-all hover:opacity-80 font-semibold">
										<span>Patients</span>
										<Image alt="" src={sortIcon} className="ml-2 h-3 w-3" />
									</div>
								</th>
							</tr>
						</thead>

						<tbody className="mx-[2px] divide-y divide-primary/20">
							{chartData?.map((trial: ClinicalTrial) => (
								<tr key={trial.name} className="px-2">
									<td className="truncate py-2 md:py-4">{trial.name}</td>
									<td className="px-2">
										<span
											className={clsx(
												trial.status === "En cours"
													? "bg-tertiary text-white"
													: "bg-vi/10",
												"rounded-2xl text-sm md:text-base px-2 py-[1px]"
											)}>
											{trial.status}
										</span>
									</td>
									<td className="px-2 w-fit">{trial.startDate}</td>
									<td className="px-2 w-fit">{trial.endDate}</td>
									<td className="text-center">{trial.totalPatients}</td>
								</tr>
							))}
						</tbody>
					</table>
				) : (
					<div>
						<div className="flex flex-col space-y-2 mb-4">
							<span className="font-medium text-sm">Sort by :</span>
							<div className="flex space-x-4">
								<div
									className="inline-flex items-center hover:cursor-pointer ease-in-out duration-150 transform-all hover:opacity-80 font-semibold"
									onClick={() => handleSort("name")}>
									<span>Name</span>
									<Image alt="" src={sortIcon} className="ml-2 h-3 w-3" />
								</div>

								<div
									className="inline-flex items-center hover:cursor-pointer ease-in-out duration-150 transform-all hover:opacity-80 font-semibold"
									onClick={() => handleSort("status")}>
									<span>Status</span>
									<Image alt="" src={sortIcon} className="ml-2 h-3 w-3" />
								</div>

								<div
									className="inline-flex items-center hover:cursor-pointer ease-in-out duration-150 transform-all hover:opacity-80 font-semibold"
									onClick={() => handleSort("totalPatients")}>
									<span>Patients</span>
									<Image alt="" src={sortIcon} className="ml-2 h-3 w-3" />
								</div>
							</div>
						</div>

						{chartData?.map((trial: ClinicalTrial) => (
							<ClinicalTrialCard trial={trial} key={trial.name} />
						))}
					</div>
				)}
			</div>

			{resumeDatas && (
				<ResumeCharts
					datas={[
						{
							description: `Clinical trial with the most patients - "${resumeDatas?.name}" :`,
							value: resumeDatas.totalPatients,
						},
					]}
				/>
			)}
		</ChartContainer>
	)
}
