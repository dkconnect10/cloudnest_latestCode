"use client"
import { Medication } from "@/utils/data/molecules/moleculesTypes"
import {
	ResponsiveContainer,
	BarChart,
	XAxis,
	YAxis,
	Tooltip,
	Bar,
	CartesianGrid,
} from "recharts"
import { CustomBar } from "../ChartUI/CustomBar"
import CustomTooltip from "../ChartUI/CustomToolType"
import { CustomAxisTick } from "../ChartUI/CustomAxisTick"
import { handleChartHeight } from "@/utils/utils"

type DosageChartProps = {
	datas: Medication[]
	isMobile: boolean
}

export const DosageCharts = ({ datas, isMobile }: DosageChartProps) => {
	return (
		<ResponsiveContainer
			width={360}
			height={handleChartHeight({ isMobile })}
			className="m-8">
			<BarChart data={datas}>
				<CartesianGrid vertical={false} stroke="#ebf5fb" />

				<XAxis
					dataKey="name"
					stroke="#16043d"
					height={isMobile ? 80 : 50}
					interval={0}
					tickMargin={18}
					tick={(props) => (
						<CustomAxisTick {...props} isMobile={isMobile} maxLabelLength={6} />
					)}
				/>

				<YAxis
					dataKey="dosage"
					orientation="left"
					stroke="#16043d"
					label={{
						value: "dosage (mg)",
						angle: -90,
						dx: -28,
						fontSize: "14px",
						fill: "#16043d",
					}}
					style={{ fill: "#16043d" }}
				/>

				<Bar
					dataKey="dosage"
					name="dosage (mg)"
					type="monotone"
					fill="#3919a0"
					// eslint-disable-next-line @typescript-eslint/no-explicit-any
					shape={(props: any) => <CustomBar {...props} />}
				/>

				<Tooltip content={(props) => <CustomTooltip {...props} />} />
			</BarChart>
		</ResponsiveContainer>
	)
}
