import clsx from "clsx"
import Image from "next/image"
import { Molecule } from "@/utils/data/molecules/moleculesTypes"
import { InsightButton } from "../UI/InsightButton"
import { DosageCharts } from "./DosageChart"

type MoleculeCardProps = {
	key: string
	isMobile: boolean
	molecule: Molecule
	handleExpand: (moleculeName: string) => void
	isExpand: boolean
}

export const MoleculeCard = ({
	molecule,
	handleExpand,
	isExpand,
	isMobile,
}: MoleculeCardProps) => {
	const { name, image, formula, codeATC, description, medications } = molecule

	return (
		<div
			className={clsx(
				isExpand && "md:col-span-2 md:row-span-2",
				"w-full min-w-[200px] overflow-hidden flex flex-col items-center mt-2 md:mt-0 rounded-lg p-4 opacity-95 hover:opacity-100 ease-in-out duration-150 transition-all shadow-lg ring-1 ring-black/5 isolate backdrop-blur bg-[#F4F4F5]"
			)}>
			<div className="w-full flex items-start justify-between mb-4">
				<div className="flex flex-col items-start">
					<Image
						src={image}
						alt={`${name}-formula-chemical-img`}
						width={200}
						height={200}
					/>
					<p className="text-sm text-vi">{formula}</p>
					{isExpand && (
						<p className="border-t border-t-vi/40 text-sm pt-4 mt-4">
							{description}
						</p>
					)}
				</div>

				<div className="w-full flex flex-col items-end">
					<p className="text-lg font-semibold">{name}</p>
					<p className="font-semibold text-jinx">{codeATC}</p>

					{isExpand && <DosageCharts datas={medications} isMobile={isMobile} />}
				</div>
			</div>

			{!isExpand && (
				<p className="border-t border-t-vi/40 text-sm pt-4">{description}</p>
			)}

			<InsightButton onClick={() => handleExpand(name)} />
		</div>
	)
}
