"use client"
import { useEffect, useState } from "react"
import { Cell, Pie, PieChart, ResponsiveContainer, Tooltip } from "recharts"
import { CustomPieLabel } from "@components/ChartUI/CustomPieLabel"
import { ChartHeader } from "@components/ChartUI/ChartHeader"
import { InsightButton } from "@components/UI/InsightButton"
import { ChartContainer } from "@components/ChartUI/ChartContainer"
import { ComponentProps } from "@components/Layout/TopHospitalsLayout"
import { handleChartHeight } from "@/utils/utils"
import { Hospital } from "@/utils/data/hospitals/hospitalsTypes"
import nurseIcon from "@assets/icons/nurse.svg"
import CustomTooltip from "../ChartUI/CustomToolType"

type EmployeesPie = {
	name: string
	value: number
}
export const EmployeesPie = ({
	datas,
	hasHospitalSelected,
	isMobile,
}: ComponentProps) => {
	const [chartDatas, setChartDatas] = useState<EmployeesPie[]>([
		{ name: "nurses", value: 0 },
		{ name: "doctors", value: 0 },
	])
	const totalEmployees = chartDatas.reduce((acc, data) => acc + data.value, 0)
	// eslint-disable-next-line @typescript-eslint/no-unused-vars
	const [hasBeenClicked, setHasBeenClicked] = useState<boolean>(false)

	useEffect(() => {
		const employeesDatas = (datas: Hospital[]) => {
			if (!datas) {
				return [
					{ name: "nurses", value: 0 },
					{ name: "doctors", value: 0 },
				]
			} else {
				if (hasHospitalSelected) {
					const hospitalSelected = datas[0]
					return [
						{
							name: "nurses",
							value: hospitalSelected.overview.numberOfNurses,
						},
						{
							name: "doctors",
							value: hospitalSelected.overview.numberOfDoctors,
						},
					]
				} else {
					const total = datas.reduce(
						(acc, hospital) => {
							return [
								{
									name: "nurses",
									value: (acc[0].value += hospital.overview.numberOfNurses),
								},
								{
									name: "doctors",
									value: (acc[1].value += hospital.overview.numberOfDoctors),
								},
							]
						},
						[
							{ name: "nurses", value: 0 },
							{ name: "doctors", value: 0 },
						] //valeur initiale contenant les totaux
					)

					return total
				}
			}
		}

		setChartDatas(employeesDatas(datas))
	}, [datas, hasHospitalSelected])

	return (
		<ChartContainer>
			<ChartHeader
				title="Employees"
				icon={nurseIcon}
				description="Distribution nurses vs doctors"
			/>

			<ResponsiveContainer
				width="100%"
				height={handleChartHeight({ isMobile, isPie: true })}
				className="recharts-surface">
				<PieChart>
					<Pie
						dataKey="value"
						startAngle={360}
						endAngle={0}
						data={chartDatas}
						cx="50%"
						cy="50%"
						outerRadius={80}
						innerRadius={55}
						stroke="none"
						label={(props) => (
							<CustomPieLabel totalEmployees={totalEmployees} {...props} />
						)}
						labelLine={false}>
						<Cell key="nurses" fill="#5E17EB" />
						<Cell key="doctors" fill="#beea64" />
					</Pie>

					<Tooltip content={(props) => <CustomTooltip {...props} />} />
				</PieChart>
			</ResponsiveContainer>

			<InsightButton
				onClick={() => setHasBeenClicked((prevState) => !prevState)}
			/>
		</ChartContainer>
	)
}
