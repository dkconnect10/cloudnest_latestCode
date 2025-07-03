import React from "react"

type InsightBtnProps = {
	onClick: () => void
}

export const InsightButton = ({ onClick }: InsightBtnProps) => {
	return (
		<div
			className="flex items-center justify-center place-self-end gap-1 mt-1 bg-vi/5 pt-3 pb-[10px] pl-3 pr-[10px] rounded-full border border-transparent hover:border-jinx/50 hover:cursor-pointer hover:text-jinx hover:fill-jinx hover:bg-jinx/5 transform-all duration-300 ease-in-out"
			onClick={() => onClick()}>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				id="Layer_1"
				data-name="Layer 1"
				className="w-5"
				viewBox="0 0 24 24">
				<path d="m23.271,23.979l-6.574-6.574c-1.775,1.607-4.12,2.596-6.697,2.596C4.486,20,0,15.514,0,10S4.486,0,10,0c2.486,0,4.759.918,6.51,2.425l-.656.753c-1.576-1.354-3.619-2.178-5.854-2.178C5.037,1,1,5.038,1,10c0,1.634.445,3.164,1.209,4.486l5.757-6.728,3.503,3.503L21.123.172l.754.656-10.357,11.898-3.497-3.497-5.24,6.124c1.642,2.207,4.261,3.646,7.217,3.646,4.963,0,9-4.038,9-9,0-.842-.125-1.654-.342-2.428l.767-.881c.366,1.038.575,2.148.575,3.31,0,2.577-.989,4.922-2.596,6.697l6.574,6.574-.707.707Z" />
			</svg>

			{/* <p className="">More insight</p> */}
		</div>
	)
}
