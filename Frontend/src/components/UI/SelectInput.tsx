import React, { useState } from "react"
import Image from "next/image"
import clsx from "clsx"
import refreshIcon from "@assets/icons/refresh.png"
import arrowIcon from "@assets/icons/arrow.png"

type SelectInputProps = {
	labels: string[]
	title?: string
	onSelectChange: (value: string) => void
	placeholder?: string
	resetLabel?: boolean
}

export const SelectInput = ({
	labels,
	title,
	onSelectChange,
	placeholder,
	resetLabel = false,
}: SelectInputProps) => {
	const [selectedValue, setSelectedValue] = useState<string>("")
	const [isOpen, setIsOpen] = useState<boolean>(false)

	const handleSelect = (value: string) => {
		setSelectedValue(value)
		onSelectChange(value)
		setIsOpen(false)
	}

	const handleRefresh = () => {
		if (resetLabel) {
			onSelectChange(labels[0])
		} else {
			onSelectChange(placeholder ? placeholder : "")
		}
		setSelectedValue("")
	}

	return (
		<div
			className={clsx(
				selectedValue && "flex items-center justify-center gap-2",
				"w-fit mt-1 mb-3 relative group"
			)}>
			<div>
				{title && (
					<p className="text-sm tracking-wide font-medium mb-2">{title}</p>
				)}

				<div className="flex items-center">
					{selectedValue && (
						<Image
							onClick={handleRefresh}
							className="w-4 h-4 hover:cursor-pointer hover:opacity-70 transition-all ease-in-out duration-150 mr-2"
							src={refreshIcon}
							alt="refresh filter"
						/>
					)}

					<button
						className="w-fit flex items-center px-2 py-1 bg-transparent hover:opacity-80 focus:outline-none transition-all ease-in-out duration-150 rounded-lg italic"
						onClick={() => setIsOpen(!isOpen)}>
						{selectedValue || placeholder || "Select an option"}

						<Image
							onClick={handleRefresh}
							className="group-hover:rotate-180
								w-4 h-4 hover:cursor-pointer transition-all ease-in-out duration-300 ml-4"
							src={arrowIcon}
							alt="refresh filter"
						/>
					</button>

					<ul className="max-h-0 group-hover:max-h-[300px] -translate-y-2 group-hover:translate-y-2 group-hover:opacity-100 opacity-0 absolute top-16 bg-white divide divide-primary/20 rounded-md shadow-lg transition-all ease-in-out duration-300 z-50 overflow-hidden">
						{labels.map((label: string) => (
							<li
								key={label}
								className="px-4 py-[6px] cursor-pointer border-b border-primary/20 transition-all ease-in-out duration-150 hover:font-medium"
								onClick={() => handleSelect(label)}>
								{label}
							</li>
						))}
					</ul>
				</div>
			</div>
		</div>
	)
}
