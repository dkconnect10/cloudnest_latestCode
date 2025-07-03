import React from "react"

const truncateLabel = (label: string, maxLength: number) => {
	return label.length > maxLength ? `${label.slice(0, maxLength)}..` : label
}

const formatLabel = (label: string) => {
	const words = label.split(" ")

	if (words.length > 1) {
		return (
			<>
				<tspan x="0">{words[0]}</tspan>
				<tspan x="0" dy="1.2em">
					{words.slice(1).join(" ")}
				</tspan>
			</>
		)
	}
	return label
}

type CustomAxisTickProps = {
	x: number
	y: number
	payload: { value: string }
	isMobile?: boolean
	maxLabelLength?: number
}

export const CustomAxisTick: React.FC<CustomAxisTickProps> = ({
	x,
	y,
	payload,
	isMobile,
	maxLabelLength,
}) => {
	const longLabel = payload.value.length > 7
	const label =
		maxLabelLength && isMobile
			? truncateLabel(payload.value, maxLabelLength)
			: payload.value

	return (
		<g
			transform={`translate(${isMobile && longLabel ? x - 12 : x},${
				isMobile && longLabel ? y + 12 : y
			})`}>
			<text
				textAnchor="middle"
				fill="#16043d"
				fontSize={15}
				transform={
					isMobile && longLabel
						? "rotate(-38)"
						: isMobile
						? "rotate(-45)"
						: undefined
				}>
				{formatLabel(label)}
			</text>
		</g>
	)
}
