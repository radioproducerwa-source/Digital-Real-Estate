'use client';

import { useState } from 'react';

interface Task { title: string; completed: boolean; }

const CONTENT_TYPES = [
  { id: 'social', label: 'Social Media', emoji: '📱' },
  { id: 'blog', label: 'Blog Articles', emoji: '✏️' },
  { id: 'video', label: 'Video / Podcast', emoji: '🎬' },
];

export default function ContentIdeasCard({ tasks }: { tasks: Task[] }) {
  const [ideas, setIdeas] = useState<Record<string, string[]>>({});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  async function generateIdeas() {
    setLoading(true);
    setError('');
    try {
      const res = await fetch('/api/content-ideas', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ tasks }),
      });
      const data = await res.json();
      if (data.error) throw new Error(data.error);
      setIdeas(data.ideas);
    } catch (e: any) {
      setError(e.message ?? 'Failed to generate ideas');
    }
    setLoading(false);
  }

  const hasIdeas = Object.keys(ideas).length > 0;

  return (
    <div className="card">
      <div className="card-header">
        <div className="flex items-center gap-3">
          <div className="w-3 h-3 rounded-full bg-pink-500" />
          <h2 className="card-title">Content Ideas</h2>
        </div>
        <button
          onClick={generateIdeas}
          disabled={loading}
          className="btn-primary bg-pink-700 hover:bg-pink-600 text-xs disabled:opacity-50"
        >{loading ? 'Generating...' : hasIdeas ? 'Regenerate' : 'Generate'}</button>
      </div>

      {error && <p className="text-red-400 text-sm mb-3">{error}</p>}

      {!hasIdeas && !loading && (
        <p className="text-slate-400 text-sm">Click Generate to get AI-powered content ideas based on your day.</p>
      )}

      {loading && (
        <div className="space-y-3">
          {[1,2,3].map(i => <div key={i} className="h-16 bg-slate-700 rounded-lg animate-pulse" />)}
        </div>
      )}

      {hasIdeas && !loading && (
        <div className="space-y-4">
          {CONTENT_TYPES.map(type => (
            ideas[type.id]?.length ? (
              <div key={type.id}>
                <p className="text-xs font-semibold text-slate-400 mb-2">{type.emoji} {type.label}</p>
                <ul className="space-y-1.5">
                  {ideas[type.id].map((idea, i) => (
                    <li key={i} className="flex items-start gap-2 text-sm text-slate-200">
                      <span className="text-pink-400 flex-shrink-0 mt-0.5">•</span>
                      {idea}
                    </li>
                  ))}
                </ul>
              </div>
            ) : null
          ))}
        </div>
      )}
    </div>
  );
}
