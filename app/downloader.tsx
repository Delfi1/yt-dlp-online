'use client'

import { useState } from "react"

export default function Dowloader() {
  const [link, setLink] = useState('');

  return (
    <div className="downloader">
      <input value={link} onChange={(e) => setLink(e.target.value)} placeholder="Video download link"></input>
      <div className="download">
        <a href={`/api/yt_dlp/download?link=${link}`}>Download</a>
      </div>
    </div>
  )
}