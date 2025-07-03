'use client'
import React from "react"
import { Profil } from "../Profil"
import { LocalTime } from "../UI/LocalTime"
import { FiltersTab } from "../FiltersTab"
import { useHospitalSelected } from "@/utils/hooks/useHospitalSelected"
import { useUserProfile } from "@/utils/hooks/useUserProfile"

// ✅ Define props type
type DashboardIntroProps = {
  isHospitalDashboard: boolean
}

export const DashboardIntro = ({ isHospitalDashboard }: DashboardIntroProps) => {
  const { hasHospitalSelected, hospital } = useHospitalSelected()
  const { user, loading } = useUserProfile()

  return (
    <div>
      <div className="w-full flex flex-col md:flex-row flex-reverse md:items-end justify-between px-1 md:px-0">
        <div className="flex flex-col md:items-start">
          <p className="md:text-xl mt-8">Welcome on your dashboard,</p>

          <h2 className="my-1 text-lg md:text-4xl font-semibold">
            {loading ? "Loading..." : user?.full_name || user?.username || "User"}
          </h2>
        </div>

        <Profil />
      </div>

      <LocalTime />

      {isHospitalDashboard && <FiltersTab />}
    </div>
  )
}
