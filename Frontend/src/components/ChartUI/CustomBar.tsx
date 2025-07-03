import React from "react"
import { BarProps } from "recharts/types/cartesian/Bar"

export type CustomBarProps = BarProps & { fill: string; x: number; y: number }

export const CustomBar = ({ fill, x, y, width, height }: CustomBarProps) => {
	return (
		<rect
			x={x}
			y={y - 4}
			width={width}
			height={height}
			fill={fill}
			rx={5}
			ry={5}
		/>
	)
}
