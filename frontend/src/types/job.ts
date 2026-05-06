export interface Job {
  id: number
  title: string
  company: string
  location: string
  url: string
  source: string | null
  keyword: string | null
  description: string | null
  posted_at: string | null
}