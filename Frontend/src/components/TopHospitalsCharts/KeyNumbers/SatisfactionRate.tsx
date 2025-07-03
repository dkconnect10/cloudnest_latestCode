"use client"
import React, { useEffect, useState } from "react"
import { Hospital } from "@/utils/data/hospitals/hospitalsTypes"
import { ChartContainer } from "@components/ChartUI/ChartContainer"
import { ChartHeader } from "@components/ChartUI/ChartHeader"
import { ComponentProps } from "@components/Layout/TopHospitalsLayout"
import notation from "@assets/icons/sparkles.svg"

export const SatisfactionRate = ({
	datas,
	hasHospitalSelected,
}: ComponentProps) => {
	const [chartDatas, setChartDatas] = useState<number>(0)

	useEffect(() => {
		if (!hasHospitalSelected) {
			const averageRate = (datas: Hospital[]) => {
				let totalRate = 0
				for (const hospital of datas) {
					totalRate += hospital.overview.satisfactionRate
				}
				return totalRate / datas.length
			}
			setChartDatas(averageRate(datas))
		} else {
			const hospitalFound = datas.filter((el) => el.name === datas[0].name)

			setChartDatas(hospitalFound[0].overview.satisfactionRate)
		}
	}, [datas, hasHospitalSelected])

	return (
		<ChartContainer dark>
			<ChartHeader
				title="Satisfaction"
				icon={notation}
				description={
					!hasHospitalSelected
						? "AVG satisfaction rate in 2024"
						: "Satisfaction rate in 2024"
				}
			/>

			<div className="flex flex-col">
				<p className="font-semibold text-4xl flex items-center justify-center">
					{chartDatas}%
				</p>
			</div>
		</ChartContainer>
	)
}
