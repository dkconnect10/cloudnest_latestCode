import type { Config } from "tailwindcss"

const config: Config = {
	content: [
		"./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
		"./src/components/**/*.{js,ts,jsx,tsx,mdx}",
		"./src/app/**/*.{js,ts,jsx,tsx,mdx}",
	],
	theme: {
		extend: {
			colors: {
				primary: "#3919a0",
				secondary: "#E8E3F6",
				tertiary: "#16043d",
				vi: "#5E17EB",
				jinx: "#C817EB",
				shimmer: "#A4EB17",
			},
		},
	},
	plugins: [],
}
export default config
