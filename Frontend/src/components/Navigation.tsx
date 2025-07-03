"use client"

import { useContext, useState } from "react"
import Image from "next/image"
import { DashboardsContext } from "@/utils/Context"
import { tabs } from "@/utils/data/tabs"
import { ListTabs } from "./UI/ListTabs"
import { useBreakpoint } from "@/utils/hooks/useBP"
import menuIcon from "@assets/icons/hamburger.svg"
import tabIcon from "@assets/icons/arrow.png"

export const Navigtation = () => {
  const breakpoint = useBreakpoint()
  const isMobile = breakpoint === "mobile"

  const dashboardCtxt = useContext(DashboardsContext)
  const { dashboard, handleDashboard } = dashboardCtxt

  const handleSelectTab = (tabSelected: string) => {
    handleDashboard(tabSelected)
    setOpen(false) // Auto-close menu on selection
  }

  const [isOpen, setOpen] = useState(false)

  return isMobile ? (
    <div className="fixed top-0 right-0 w-full p-5 z-50 flex justify-end">
      {/* Toggle button */}
      {isOpen ? (
        <button
          onClick={() => setOpen(false)}
          className="text-3xl font-bold text-gray-700"
        >
          ×
        </button>
      ) : (
        <button onClick={() => setOpen(true)}>
          <Image
            src={menuIcon}
            alt="menu-icon"
            width={30}
            height={30}
            className="self-end"
          />
        </button>
      )}

      {/* Slide-in sidebar */}
      <div
        className={`fixed top-0 left-0 h-full w-[80%] bg-[#D5DDE6] shadow-lg transform transition-transform duration-300 ease-in-out ${
          isOpen ? "translate-x-0" : "-translate-x-full"
        }`}
      >
        <div className="p-4 flex flex-col items-start mt-10">
          <p className="font-semibold text-sm mb-3">Select a dashboard</p>

          <ul className="w-full flex flex-col divide-y divide-gray-300">
            {tabs.map((tab: string) => (
              <li
                key={tab}
                onClick={() => handleSelectTab(tab)}
                className={`w-full py-3 px-2 flex items-center justify-between cursor-pointer transition-all duration-150 ${
                  dashboard === tab
                    ? "text-blue-600 font-semibold"
                    : "hover:text-blue-500"
                }`}
              >
                <p>{tab}</p>
                <Image
                  src={tabIcon}
                  alt="arrow-icon"
                  width={14}
                  height={14}
                  className="rotate-90"
                />
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  ) : (
    <ListTabs dashboard={dashboard} handleSelectTab={handleSelectTab} />
  )
}
