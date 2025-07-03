type datasResumeChart = {
	description: string
	value?: number | string
}

type ResumeChartsProps = {
	datas: datasResumeChart[]
}

export const ResumeCharts = ({ datas }: ResumeChartsProps) => {
	return (
		<div className="w-full flex flex-col mt-4 text-tertiary/60">
			{datas.map((el, index) => (
				<p key={index}>
					<span className="text-sm">{el.description}</span>

					{el.value && (
						<span className="font-semibold text-base ml-1">{el.value}</span>
					)}
				</p>
			))}
		</div>
	)
}
