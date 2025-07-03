export const handleChartWidth = (isMobile: boolean) => {
	if (isMobile) {
		return 300
	} else {
		return 580
	}
}

type HandleChartHeightProps = {
	isMobile: boolean
	isPie?: boolean
}

export const handleChartHeight = ({
	isMobile,
	isPie,
}: HandleChartHeightProps) => {
	const baseHeight = isPie ? 160 : isMobile ? 260 : 320
	return Math.max(baseHeight, 160) //assure une hauteur minimale
}

export const shadowTool: string =
	"3.4px 3.4px 2.7px rgba(0, 0, 0, 0.022), 8.7px 8.7px 6.9px rgba(0, 0, 0, 0.031),17.7px 17.7px 14.2px rgba(0, 0, 0, 0.039),36.5px 36.5px 29.2px rgba(0, 0, 0, 0.048),100px 100px 80px rgba(0, 0, 0, 0.07)"

//fonction de tri
// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const sortData = (data: any, key: string | number, ascending = true) => {
	return [...data].sort((a, b) => {
		const aValue = a[key]
		const bValue = b[key]

		if (typeof aValue === "string" && typeof bValue === "string") {
			return ascending
				? aValue.localeCompare(bValue)
				: bValue.localeCompare(aValue)
		}

		if (typeof aValue === "number" && typeof bValue === "number") {
			return ascending ? aValue - bValue : bValue - aValue
		}

		return 0
	})
}
