"use client"
import clsx from "clsx"
import React, { useEffect, useState } from "react"

export type TabProps = {
	title: string
	dashboardSelected: string
	onClick: (tabSelected: string) => void
}

export const Tab = ({ title, dashboardSelected, onClick }: TabProps) => {
	const [hoveredTab, setHoveredTab] = useState<string>(dashboardSelected)

	const isActive = title === dashboardSelected
	const isHovered = title === hoveredTab

	useEffect(() => {
		setHoveredTab(dashboardSelected)
	}, [dashboardSelected])

	const boxShadow =
		"shadow-[inset_2px_4px_5px_rgba(0,0,0,0.1),_inset_-2px_-4px_6px_rgba(255,255,255,0.5)] border-primary/30 bg-secondary/50"

	return (
		<li
			onMouseEnter={() => setHoveredTab(title)}
			onMouseLeave={() => setHoveredTab(dashboardSelected)}
			className={clsx(
				"group z-10 w-fit flex items-center justify-center transition-all duration-300 ease-in-out rounded-fullfont-medium tracking-widdest"
			)}>
			<button
				onClick={() => onClick(title)}
				className={clsx(
					isActive && boxShadow,
					isHovered && boxShadow,
					`px-3 py-2 transition-all duration-300 ease-in-out rounded-full hover:bg-secondary/80 border border-transparent`
				)}>
				{title}
			</button>
		</li>
	)
}
