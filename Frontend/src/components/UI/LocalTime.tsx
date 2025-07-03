export const LocalTime = () => {
	const today = new Date()
	const date = today.getDate()
	const weekday = today.toLocaleString("en-GB", {
		weekday: "long",
	})
	const month = today.toLocaleString("en-GB", {
		month: "long",
	})
	// const year = today.getFullYear()

	return (
		<div className="flex items-center font-medium mt-8">
			<div className="rounded-lg w-12 h-12 md:w-16 md:h-16 text-2xl border border-tertiary flex items-center justify-center p-2 mr-2">
				{date}
			</div>
			<div className="flex md:flex-col">
				<p>{weekday}, &nbsp;</p>
				<p>{month}</p>
			</div>
		</div>
	)
}
