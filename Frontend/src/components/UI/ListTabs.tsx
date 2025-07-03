"use client"
import { Tab } from "@components/UI/Tab"
import { tabs } from "@/utils/data/tabs"

export type ListTabProps = {
	dashboard: string
	handleSelectTab: (tabSelected: string) => void
}

export const ListTabs = ({ dashboard, handleSelectTab }: ListTabProps) => {
	return (
		<ul className="flex w-fit justify-self-end bg-white rounded-full">
			{tabs.map((title: string) => {
				return (
					<Tab
						key={title}
						title={title}
						dashboardSelected={dashboard}
						onClick={handleSelectTab}
					/>
				)
			})}
		</ul>
	)
}
