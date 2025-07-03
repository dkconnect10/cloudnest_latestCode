"use client"
import { useState, useEffect } from "react"

type BreakpointName = "mobile" | "tablet" | "desktop" | "largeScreen"

type BreakpointProps = {
	name: BreakpointName
	min: number
	max: number
}

type UseBreakpointType = () => BreakpointName

const DefaultBreakpoints: BreakpointProps[] = [
	{ name: "mobile", min: 320, max: 599 },
	{ name: "tablet", min: 600, max: 1023 },
	{ name: "desktop", min: 1024, max: 1279 },
	{ name: "largeScreen", min: 1280, max: Infinity },
]

export const useBreakpoint: UseBreakpointType = () => {
	const [breakpoint, setBreakPoint] = useState<BreakpointName>("largeScreen")

	useEffect(() => {
		function handleResize() {
			const windowSize = window.innerWidth

			for (const bp of DefaultBreakpoints) {
				if (windowSize > bp.min && windowSize <= bp.max) {
					setBreakPoint(bp.name)
					break //stop la boucle une fois le bp trouvé
				}
			}
		}

		window.addEventListener("resize", handleResize)

		handleResize()

		return () => {
			window.removeEventListener("resize", handleResize)
		}
	}, [])

	return breakpoint
}
