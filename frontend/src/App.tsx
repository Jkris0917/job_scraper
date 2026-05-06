import useJob from "./hooks/useJob"

export default function App() {
  const { job, lastPage, loading, page, search, setPage, setSearch } = useJob()

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <h1 className="text-3xl text-center font-bold mb-4">Job Scraper</h1>

      <input
        type="text"
        placeholder="Search jobs..."
        value={search}
        onChange={(e) => setSearch(e.target.value)} className="w-full p-3 rounded-lg border mb-6 shadow-sm"
      />
      <table className="">
        <thead>
          <tr>
            <th className="text-left p-2 border-b">Title</th>
            <th className="text-left p-2 border-b">Company</th>
            <th className="text-left p-2 border-b">Location</th>
            <th className="text-left p-2 border-b">Date Posted</th>
          </tr>
        </thead>
        <tbody>
          {loading ? (
            <tr>
              <td colSpan={4} className="text-center p-4">Loading...</td>
            </tr>
          ) : job.length > 0 ? (
            job.map((job) => (
              <tr key={job.id}>
                <td className="p-2 border-b">{job.title}</td>
                <td className="p-2 border-b">{job.company}</td>
                <td className="p-2 border-b">{job.location}</td>
                <td className="p-2 border-b">{job.posted_at ? new Date(job.posted_at).toLocaleDateString() : "N/A"}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan={4} className="text-center p-4">No jobs found.</td>
            </tr>
          )}
        </tbody>
      </table>
      <div className="flex justify-between mt-4">
        <button
          onClick={() => setPage((prev) => Math.max(prev - 1, 1))}
          disabled={page === 1}
          className="px-4 py-2 bg-blue-500 text-white rounded disabled:bg-gray-300"
        >
          Previous
        </button>
        <span>Page {page} of {lastPage}</span>
        <button
          onClick={() => setPage((prev) => Math.min(prev + 1, lastPage))}
          disabled={page === lastPage}
          className="px-4 py-2 bg-blue-500 text-white rounded disabled:bg-gray-300"
        >
          Next
        </button>
      </div>
    </div>
  )
}