'use client'

import { useRouter } from 'next/navigation'

export default function HomePage() {
  const router = useRouter()

  return (
    <div className="h-screen flex flex-col items-center justify-center gap-4 bg-gray-100">
      <h1 className="text-3xl font-bold">Welcome to Meditec</h1>

      <div className="flex gap-6">
        <button
          onClick={() => router.push('/auth/register')}
          className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 transition"
        >
          Register
        </button>

        <button
          onClick={() => router.push('/auth/login')}
          className="bg-green-600 text-white px-6 py-2 rounded hover:bg-green-700 transition"
        >
          Login
        </button>
      </div>
    </div>
  )
}
