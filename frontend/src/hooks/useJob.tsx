import { useEffect, useState } from "react";
import type { Job } from "../types/job";
import { toast } from "sonner";

export default function useJob() {
    const [job, setJob] = useState<Job[]>([])
    const [loading, setLoading] = useState(false)
    const [search, setSearch] = useState("")
    const [page, setPage] = useState(1)
    const [lastPage, setLastPage] = useState(1)


    const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

    const fetchJobs = async () => {
        setLoading(true)
        try {
            const response = await fetch(`${API_URL}/jobs?search=${search}&page=${page}`)
            const data = await response.json()
            setJob(data.jobs)
            setLastPage(data.last_page)
        } catch (err: any) {
            toast.error("Error fetching jobs:", err.message)
        } finally {
            setLoading(false)
        }
    }

    useEffect(() => {
        fetchJobs()
    }, [search, page])

    return { job, loading, search, setSearch, page, setPage, lastPage, setLastPage }

}