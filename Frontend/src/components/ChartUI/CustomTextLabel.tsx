"use client"
import React from "react"
import { useBreakpoint } from "@/utils/hooks/useBP"

type CustomLabelProps = {
	x: number
	y: number
	width: number
	value: string
}

export const CustomTextLabel = ({ x, y, width, value }: CustomLabelProps) => {
	const breakpoint = useBreakpoint()
	const isMobile = breakpoint === "mobile"

	return (
		<text
			x={x + width / 2} //centre le label
			y={y}
			dy={-10} //distance entre la barre et le label
			fill="#16043d"
			fontSize={isMobile ? 16 : 18}
			textAnchor="middle">
			{value}
		</text>
	)
}
