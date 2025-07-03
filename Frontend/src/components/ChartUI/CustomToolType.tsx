import React from "react"
import { TooltipProps } from "recharts"
import {
	NameType,
	ValueType,
} from "recharts/types/component/DefaultTooltipContent"
import { shadowTool } from "@/utils/utils"

const CustomTooltip = ({
	active,
	payload,
	label,
}: TooltipProps<ValueType, NameType>) => {
	// vérifie si le tooltip est actif et si des données sont présentes
	if (active && payload && payload.length) {
		const uniquePayload = payload.reduce((acc: typeof payload, entry) => {
			if (!acc.some((item) => item.name === entry.name)) {
				acc.push(entry)
			}
			return acc
		}, [])

		return (
			<div
				className="custom__tooltip"
				style={{
					border: "none",
					padding: "20px",
					paddingBottom: "15px",
					borderRadius: "8px",
					boxShadow: `${shadowTool}`,
					fontSize: "15px",
					backgroundColor: "#fff",
				}}>
				<p
					className="label"
					style={{
						fontSize: "16px",
						fontWeight: 400,
						lineHeight: "1",
						marginBottom: 6,
					}}>
					{label}
				</p>

				<div className="item" style={{ marginBottom: "5px" }}>
					{uniquePayload.map((entry) => (
						<div className="item" key={entry.name}>
							<span
								style={{
									fontSize: "15px",
									fontWeight: "600",
									lineHeight: "1",
									color: entry.color,
								}}>
								{entry.name} : {entry.value}
							</span>
						</div>
					))}
				</div>
			</div>
		)
	}

	return null
}

export default CustomTooltip
