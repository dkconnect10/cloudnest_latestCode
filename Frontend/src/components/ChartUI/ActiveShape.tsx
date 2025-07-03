// import React from "react"
// import { Sector } from "recharts"
// import { HospitalDepartment } from "@/utils/data/hospitals/hospitalsTypes"

// type ActiveShapeProps = {
// 	cx: number
// 	cy: number
// 	midAngle: number
// 	innerRadius: number
// 	outerRadius: number
// 	startAngle: number
// 	endAngle: number
// 	fill: string
// 	payload: HospitalDepartment
// 	percent?: number
// 	value?: string
// }

// export const ActiveShape = ({
// 	cx,
// 	cy,
// 	midAngle,
// 	innerRadius,
// 	outerRadius,
// 	startAngle,
// 	endAngle,
// 	payload,
// }: ActiveShapeProps) => {
// 	const RADIAN = Math.PI / 180
// 	const sin = Math.sin(-RADIAN * midAngle)
// 	const cos = Math.cos(-RADIAN * midAngle)
// 	const sx = cx + (outerRadius + 10) * cos
// 	const sy = cy + (outerRadius + 10) * sin
// 	const mx = cx + (outerRadius + 30) * cos
// 	const my = cy + (outerRadius + 30) * sin
// 	const ex = mx + (cos >= 0 ? 1 : -1) * 15
// 	const ey = my
// 	const textAnchor = cos >= 0 ? "start" : "end"

// 	return (
// 		<g>
// 			<text x={cx} y={cy} dy={8} textAnchor="middle" fill="#2100AD">
// 				{payload.department}
// 			</text>
// 			<Sector
// 				cx={cx}
// 				cy={cy}
// 				innerRadius={innerRadius}
// 				outerRadius={outerRadius}
// 				startAngle={startAngle}
// 				endAngle={endAngle}
// 				fill="#8ed0ff"
// 			/>
// 			<Sector
// 				cx={cx}
// 				cy={cy}
// 				startAngle={startAngle}
// 				endAngle={endAngle}
// 				innerRadius={outerRadius + 6}
// 				outerRadius={outerRadius + 8}
// 				fill="#5E17EB"
// 			/>
// 			<path
// 				d={`M${sx},${sy}L${mx},${my}L${ex},${ey}`}
// 				stroke="#5E17EB"
// 				fill="none"
// 			/>
// 			<circle cx={ex} cy={ey} r={2} fill="#5E17EB" stroke="none" />
// 			<text
// 				x={ex + (cos >= 0 ? 1 : -1) * 12}
// 				y={ey}
// 				textAnchor={textAnchor}
// 				fontSize={15}
// 				fill="#333">{`${payload.patientsPerDay} Patients per day`}</text>
// 			<text
// 				x={ex + (cos >= 0 ? 1 : -1) * 4}
// 				y={ey}
// 				dy={18}
// 				textAnchor={textAnchor}
// 				fontSize={13}
// 				fill="#5E17EB">
// 				{`(Average wait time ${payload.averageWaitTime})`}
// 			</text>
// 		</g>
// 	)
// }
