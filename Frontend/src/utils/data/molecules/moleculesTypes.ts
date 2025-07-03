type PriceHistory = {
	date: string
	priceEUR: number
	priceUSD: number
}

type Medication = {
	name: string
	dosage: number
	priceHistory: PriceHistory[]
}

type Molecule = {
	name: string
	description: string
	codeATC: string
	formula: string
	image: string
	medications: Medication[]
}

export type { Molecule, Medication, PriceHistory }
