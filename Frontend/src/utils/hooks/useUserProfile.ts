'use client'

import { useEffect, useState } from 'react'
import axios from 'axios'

export interface UserType {
  id: number
  username: string
  email: string
  full_name: string
  phone: string
  avatar: string
  gender: string
  is_email_verified: boolean
  onboarding_complete: boolean
  signup_source: string
  // add others if needed
}

export const useUserProfile = () => {
  const [user, setUser] = useState<UserType | null>(null)  // ✅ typed state
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchProfile = async () => {
      const token = localStorage.getItem('token')
      if (!token) return

      try {
        const response = await axios.get<UserType>('http://localhost:8000/users/api/GetProfile/', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })

        setUser(response.data) // ✅ now correctly typed
      } catch (error) {
        console.error('Error fetching profile:', error)
      } finally {
        setLoading(false)
      }
    }

    fetchProfile()
  }, [])

  return { user, loading }
}
