"use client"
import React, { useEffect, useState } from "react"
import { Area, AreaChart, ResponsiveContainer, Tooltip, XAxis } from "recharts"
import { ResumeCharts } from "@/components/ChartUI/ResumeCharts"
import { ChartContainer } from "../ChartUI/ChartContainer"
import { ChartHeader } from "@components/ChartUI/ChartHeader"
import CustomTooltip from "@components/ChartUI/CustomToolType"
import { CustomAxisTick } from "@components/ChartUI/CustomAxisTick"
import { handleChartHeight } from "@/utils/utils"
import { Hospital } from "@/utils/data/hospitals/hospitalsTypes"
import patientsIcon from "@assets/icons/patients.svg"
import { ComponentProps } from "../Layout/TopHospitalsLayout"

type ChartData = {
	month: string
	year: number
	hospitalizations: number
}

export const MonthlyHospitalizations = ({
	datas,
	hasHospitalSelected,
	isMobile,
	timeLine,
}: ComponentProps) => {
	const [chartData, setChartData] = useState<ChartData[] | []>([])
	const [resumeDatas, setResumeDatas] = useState<ChartData | null>(null)
	// console.log("graphic datas", timeLine)

	useEffect(() => {
		const aggregateMonthlyHospitalizations = (
			datas: Hospital[]
		): ChartData[] => {
			const aggregatedData: { [key: string]: number } = {}

			datas.forEach((hospital: Hospital) => {
				hospital.monthlyHospitalizations.forEach(
					({ month, year, hospitalizations }) => {
						const key = `${month}-${year}`
						if (!aggregatedData[key]) {
							aggregatedData[key] = hospitalizations
						} else {
							aggregatedData[key] += hospitalizations
						}
					}
				)
			})

			return Object.keys(aggregatedData).map((key) => {
				const [month, year] = key.split("-")
				return {
					month,
					year: parseInt(year),
					hospitalizations: aggregatedData[key],
				}
			})
		}

		const aggregatedData = aggregateMonthlyHospitalizations(datas)

		const sumByYear = aggregatedData.filter((el: ChartData) => {
			return el.year.toString() === timeLine
		})

		setChartData(sumByYear)
	}, [datas, hasHospitalSelected, timeLine])

	useEffect(() => {
		const highestHospitalizations =
			chartData &&
			chartData.reduce(
				(max, hospital) =>
					hospital.hospitalizations > max.hospitalizations ? hospital : max,
				chartData[0]
			)

		setResumeDatas(highestHospitalizations)
	}, [chartData])

	return (
		<ChartContainer>
			<ChartHeader
				title="Monthly hospitalizations"
				icon={patientsIcon}
				description="Number of hospitalizations per month"
			/>

			<ResponsiveContainer
				width="100%"
				height={handleChartHeight({ isMobile })}>
				<AreaChart
					data={chartData}
					barGap={3}
					margin={{
						top: isMobile ? 14 : 12,
						right: isMobile ? 8 : 30,
						left: isMobile ? 8 : 30,
						bottom: 0,
					}}>
					<XAxis
						dataKey="month"
						stroke="#16043d"
						height={50}
						tick={(props) => <CustomAxisTick {...props} isMobile={isMobile} />}
						tickMargin={20}
						interval={0}
					/>

					<defs>
						<linearGradient id="colorGradient" x1="0" y1="0" x2="0" y2="1">
							<stop offset="0%" stopColor="#b298ea" stopOpacity={0.9} />
							<stop offset="100%" stopColor="#ffffff" stopOpacity={0.4} />
						</linearGradient>
					</defs>

					<Area
						dataKey="hospitalizations"
						stroke="#5E17EB"
						fill="url(#colorGradient)"
						type={"monotone"}
						dot={false}
					/>

					<Tooltip content={(props) => <CustomTooltip {...props} />} />
				</AreaChart>
			</ResponsiveContainer>

			{resumeDatas && (
				<ResumeCharts
					datas={[
						{
							description: `Month with the most hospitalizations - "${resumeDatas.month}" :`,
							value: resumeDatas.hospitalizations,
						},
					]}
				/>
			)}
		</ChartContainer>
	)
}
