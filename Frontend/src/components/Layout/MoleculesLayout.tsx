import { useState } from "react"
import { MoleculeCard } from "../MoleculesCharts/MoleculeCard"
import { molecules } from "@/utils/data/molecules/molecules"
import { Molecule } from "@/utils/data/molecules/moleculesTypes"
import { useBreakpoint } from "@/utils/hooks/useBP"

export const MoleculesLayout = () => {
	const breakpoint = useBreakpoint()
	const isMobile = breakpoint === "mobile"

	const [expandedMolecule, setExpandedMolecule] = useState<string | null>(null)

	const handleExpand = (moleculeName: string) => {
		setExpandedMolecule((prevSate) =>
			prevSate === moleculeName ? null : moleculeName
		)
	}

	return (
		<section className="w-full grid grid-cols-1 md:grid-cols-3 md:bg-white/20 flex-wrap md:gap-4 md:p-8 rounded-lg mt-4">
			{molecules.map((molecule: Molecule) => (
				<MoleculeCard
					molecule={molecule}
					key={molecule.name}
					isMobile={isMobile}
					handleExpand={handleExpand}
					isExpand={expandedMolecule === molecule.name}
				/>
			))}
		</section>
	)
}
