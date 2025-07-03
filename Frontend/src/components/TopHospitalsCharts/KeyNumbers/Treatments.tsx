"use client"
import React, { useEffect, useState } from "react"
import { ChartContainer } from "../../ChartUI/ChartContainer"
import { ChartHeader } from "@components/ChartUI/ChartHeader"
import { ComponentProps } from "@components/Layout/TopHospitalsLayout"
import { Hospital } from "@/utils/data/hospitals/hospitalsTypes"
import treatmentIcon from "@assets/icons/treatment.svg"

export const Treatments = ({ datas, hasHospitalSelected }: ComponentProps) => {
	const [chartDatas, setChartDatas] = useState<number>(0)

	useEffect(() => {
		if (!hasHospitalSelected) {
			const sumOfTreatments = (datas: Hospital[]) => {
				let total = 0
				for (const hospital of datas) {
					total += hospital.overview.totalTreatments
				}
				return total
			}
			setChartDatas(sumOfTreatments(datas))
		} else {
			const hospitalFound = datas.filter((el) => el.name === datas[0].name)

			setChartDatas(hospitalFound[0].overview.totalTreatments)
		}
	}, [datas, hasHospitalSelected])

	return (
		<ChartContainer>
			<ChartHeader
				title="Treatments"
				icon={treatmentIcon}
				description="Number of treatments"
			/>

			<div className="flex flex-col">
				<p className="font-semibold text-4xl flex items-center justify-center">
					{chartDatas}
				</p>
			</div>
		</ChartContainer>
	)
}
