"use client"
import { useEffect, useState } from "react"
import {
	Legend,
	PolarAngleAxis,
	PolarGrid,
	PolarRadiusAxis,
	Radar,
	RadarChart,
	ResponsiveContainer,
	Tooltip,
} from "recharts"
import { ChartContainer } from "@components/ChartUI/ChartContainer"
import { ChartHeader } from "@components/ChartUI/ChartHeader"
import CustomTooltip from "@components/ChartUI/CustomToolType"
import { ComponentProps } from "@components/Layout/TopHospitalsLayout"
import { Hospital } from "@/utils/data/hospitals/hospitalsTypes"
import { handleChartHeight } from "@/utils/utils"
import stethoscopeIcon from "@assets/icons/stethoscope.svg"

type DatasDoctorSpecialties = {
	specialty: string
	numberOfDoctors: number
	satisfactionRate: number
}

export const DoctorSpecialtiesRadar = ({
	datas,
	hasHospitalSelected,
	isMobile,
}: ComponentProps) => {
	const [chartDatas, setChartDatas] = useState<DatasDoctorSpecialties[]>([])

	useEffect(() => {
		const specilatiesDatas = (
			datas: Hospital[]
		): DatasDoctorSpecialties[] | undefined => {
			if (hasHospitalSelected) {
				return datas[0].doctorSpecialties
			} else {
				const aggregatedData: Record<
					string,
					{ numberOfDoctors: number; totalSatisfaction: number; count: number }
				> = {}

				datas.forEach((hospital) => {
					hospital.doctorSpecialties.forEach(
						({ specialty, numberOfDoctors, satisfactionRate }) => {
							if (!aggregatedData[specialty]) {
								aggregatedData[specialty] = {
									numberOfDoctors: 0,
									totalSatisfaction: 0,
									count: 0,
								}
							}
							aggregatedData[specialty].numberOfDoctors += numberOfDoctors
							aggregatedData[specialty].totalSatisfaction += satisfactionRate
							aggregatedData[specialty].count += 1
						}
					)
				})

				return Object.keys(aggregatedData).map((specialty) => ({
					specialty,
					numberOfDoctors: aggregatedData[specialty].numberOfDoctors,
					satisfactionRate: Math.round(
						aggregatedData[specialty].totalSatisfaction /
							aggregatedData[specialty].count
					),
				}))
			}
		}

		const result = specilatiesDatas(datas)
		if (result) setChartDatas(result)
	}, [datas, hasHospitalSelected])

	return (
		<ChartContainer>
			<ChartHeader
				title="Specialties"
				icon={stethoscopeIcon}
				description="Ratio between satisfaction rate and number of doctors per specialty"
			/>

			<ResponsiveContainer
				width="100%"
				height={handleChartHeight({ isMobile })}>
				<RadarChart data={chartDatas}>
					<PolarGrid strokeWidth={0.7} />

					<PolarAngleAxis dataKey="specialty" />

					<PolarRadiusAxis scale="auto" angle={60} />

					{chartDatas.map((hospital) => (
						<Radar
							key={hospital.specialty}
							dataKey="numberOfDoctors"
							stroke="#5E17EB"
							strokeWidth={0.7}
							fill="transparent"
							fillOpacity={0.2}
							name="doctors"
						/>
					))}

					{chartDatas.map((hospital) => (
						<Radar
							key={hospital.satisfactionRate}
							dataKey="satisfactionRate"
							stroke="#C817EB"
							strokeWidth={0.3}
							fill="#da9ce5"
							fillOpacity={0.3}
							name="satisfaction rate"
						/>
					))}

					<Legend
						payload={[
							{ value: "doctors", type: "line", color: "#5E17EB" },
							{
								value: "satisfaction rate",
								type: "star",
								color: "#C817EB",
							},
						]}
					/>

					<Tooltip content={(props) => <CustomTooltip {...props} />} />
				</RadarChart>
			</ResponsiveContainer>
		</ChartContainer>
	)
}
