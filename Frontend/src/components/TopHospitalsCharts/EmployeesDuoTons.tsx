"use client"
import { useEffect, useState } from "react"
import clsx from "clsx"
import { ChartHeader } from "../ChartUI/ChartHeader"
import { ChartContainer } from "../ChartUI/ChartContainer"
import { ComponentProps } from "../Layout/TopHospitalsLayout"
import { Hospital } from "@/utils/data/hospitals/hospitalsTypes"
import nurseIcon from "@assets/icons/nurse.svg"

type Employees = {
	name: string
	value: number
	color: string
}

export const EmployeesDuoTons = ({
	datas,
	hasHospitalSelected,
}: ComponentProps) => {
	const defaultValues = [
		{ name: "nurses", value: 0, color: "bg-[#E9F6CF]" },
		{ name: "doctors", value: 0, color: "bg-[#DCCEF7]" },
		{ name: "total employees", value: 0, color: "bg-[#5A4D76]" },
	]
	const [chartDatas, setChartDatas] = useState<Employees[]>(defaultValues)

	useEffect(() => {
		const employeesDatas = (datas: Hospital[]) => {
			if (!datas) {
				return defaultValues
			} else {
				if (hasHospitalSelected) {
					const hospitalSelected = datas[0]
					return [
						{
							name: "nurses",
							value: hospitalSelected.overview.numberOfNurses,
							color: "bg-[#E9F6CF]",
						},
						{
							name: "doctors",
							value: hospitalSelected.overview.numberOfDoctors,
							color: "bg-[#DCCEF7]",
						},
						{
							name: "total employees",
							value:
								hospitalSelected.overview.numberOfDoctors +
								hospitalSelected.overview.numberOfNurses,
							color: "bg-[#5A4D76]",
						},
					]
				} else {
					const total = datas.reduce(
						(acc, hospital) => {
							return [
								{
									name: "nurses",
									value: (acc[0].value += hospital.overview.numberOfNurses),
									color: "bg-[#E9F6CF]",
								},
								{
									name: "doctors",
									value: (acc[1].value += hospital.overview.numberOfDoctors),
									color: "bg-[#DCCEF7]",
								},
								{
									name: "total employees",
									value:
										(acc[2].value += hospital.overview.numberOfDoctors +=
											hospital.overview.numberOfNurses),
									color: "bg-[#5A4D76]",
								},
							]
						},
						defaultValues //valeur initiale contenant les totaux
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

			<div className="w-full flex flex-col realtive">
				{chartDatas.map((el: Employees, index: number) => {
					return (
						<div
							key={el.name}
							className={clsx(
								"w-full rounded-lg px-4 py-3 flex flex-col justify-around",
								el.color,
								el.name === "total employees" && "text-white h-[120px]"
							)}
							style={{
								zIndex: index,
								transform: `translateY(${index * -15}px)`,
								boxShadow:
									"rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.06) 0px 1px 2px 0px",
							}}>
							<p className="text-right text-3xl font-semibold">{el.value}</p>
							<p
								className={clsx(
									el.name === "total employees" ? "mb-0" : "mb-3",
									"font-medium capitalize"
								)}>
								{el.name}
							</p>
						</div>
					)
				})}
			</div>
		</ChartContainer>
	)
}
