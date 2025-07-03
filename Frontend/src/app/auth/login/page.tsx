'use client'

import { useState } from 'react'
import axios from 'axios'
import { useRouter } from 'next/navigation'

// ✅ Define the expected structure of the API response
type LoginResponse = {
  access_token: string
  refresh_Token: string
  user: string
  message: string
  status: number
}

export default function LoginUser() {
  const router = useRouter()

  const [formData, setFormData] = useState({
    email: '',
    password: '',
  })

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    })
  }

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    try {
      // ✅ Pass the LoginResponse type to axios.post
      const response = await axios.post<LoginResponse>('http://localhost:8000/users/api/loginUser/', formData)

      const { access_token } = response.data

      localStorage.setItem('token', access_token)
      router.push('/dashboard')  // make sure dashboard exists
    } catch (error: any) {
      console.error('Login failed:', error?.response?.data || error.message)
      alert(error?.response?.data?.error || 'Something went wrong')
    }
  }

  return (
    <div className="p-8">
      <h2 className="text-2xl mb-4">Login</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          className="border px-3 py-2 w-full"
          required
        />

        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          className="border px-3 py-2 w-full"
          required
        />

        <button
          type="submit"
          className="bg-green-600 hover:bg-green-700 text-white px-6 py-2 rounded"
        >
          Login
        </button>
      </form>
    </div>
  )
}
