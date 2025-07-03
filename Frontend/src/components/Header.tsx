import React from "react"
import Image from "next/image"
import { Navigtation } from "./Navigation"
import logo from "@assets/logo-meditec-gray.png"

export const Header = () => {
	return (
		<header className="w-full flex items-center justify-between md:py-6 border border-b-tertiary/50 md:border-none md:px-[6%]">
			<Image
				src={logo}
				alt={"logo-meditec"}
				className="w-14 h-16 md:w-28 md:h-28"
			/>
			<Navigtation />
		</header>
	)
}
