import Image from "next/image"
import ProfilPicture from "@assets/john-doe.jpg"

export const Profil = () => {
	return (
		<div className="w-fit flex items-center self-end">
			<div className="flex flex-col mr-2">
				<p className="w-full text-right text-lg md:text-xl font-semibold">
					John Doe
				</p>
				<p className="w-full text-right font-medium text-sm">
					Clinical System Analyst
				</p>
			</div>

			<div className="w-16 h-16 rounded-full place-self-end">
				<Image
					src={ProfilPicture}
					alt="john-doe-profil-picture"
					className="w-full h-full rounded-full object-cover"
				/>
			</div>
		</div>
	)
}
