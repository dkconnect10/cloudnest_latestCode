type CustomPieLabelProps = {
	x?: number
	y?: number
	totalEmployees: number
}

export const CustomPieLabel = ({ totalEmployees }: CustomPieLabelProps) => {
	return (
		<>
			<text
				x="50%"
				y="50%"
				dy={0} // Ajuste pour centrer verticalement
				textAnchor="middle"
				fill="#082F49"
				style={{ fontSize: "20px", fontWeight: "bold" }}>
				{totalEmployees}
			</text>
			<text
				x="50%"
				y="50%"
				dy={18} // Ajuste pour centrer verticalement
				textAnchor="middle"
				fill="#082F49"
				style={{ fontSize: "15px", fontWeight: "semibold" }}>
				Employees
			</text>
		</>
	)
}
