'use client'

import { useEffect, useState } from 'react'
import { useSearchParams, useRouter } from 'next/navigation'
import axios from 'axios'

export default function VerifyEmailPage() {
  const [status, setStatus] = useState('Verifying...')
  const searchParams = useSearchParams()
  const router = useRouter()

  useEffect(() => {
    const uid = searchParams.get('uid')
    const token = searchParams.get('token')

    if (uid && token) {
      axios
        .post('http://localhost:8000/users/api/RegisterUser/', {
          uidb64: uid,
          verifyed_token: token,
        })
        .then((res) => {
          setStatus('✅ Email verified! Redirecting to login...')
          setTimeout(() => router.push('/auth/login'), 3000)
        })
        .catch((err) => {
          console.error(err)
          setStatus('❌ Verification failed. Please try registering again.')
        })
    } else {
      setStatus('Invalid verification link.')
    }
  }, [searchParams, router])

  return (
    <div className="h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-6 rounded shadow-md max-w-md w-full text-center">
        <h2 className="text-xl font-semibold mb-4">Email Verification</h2>
        <p>{status}</p>
      </div>
    </div>
  )
}
