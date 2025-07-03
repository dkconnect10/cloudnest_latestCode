import React from "react"
import clsx from "clsx"

type ChartContainerProps = {
	children: React.ReactNode
	dark?: boolean
	transparent?: boolean
}

export const ChartContainer = ({
	children,
	dark,
	transparent,
}: ChartContainerProps) => {
	return (
		<div
			className={clsx(
				dark
					? "bg-tertiary text-white"
					: transparent
					? "bg-transparent border border-primary"
					: "bg-white/80",
				"w-full min-w-[200px] h-fit overflow-hidden flex flex-col items-center mt-2 md:mt-0 rounded-lg p-4 opacity-95 hover:opacity-100 ease-in-out duration-150 transition-all shadow-lg ring-1 ring-black/5 isolate backdrop-blur"
			)}>
			{children}
		</div>
	)
}
