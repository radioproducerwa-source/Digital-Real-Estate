'use client';

import { useEffect, useState } from 'react';

interface Quote { q: string; a: string; }

export default function QuoteCard() {
  const [quote, setQuote] = useState<Quote | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const cacheKey = `quote_${new Date().toISOString().split('T')[0]}`;
    const cached = localStorage.getItem(cacheKey);
    if (cached) { setQuote(JSON.parse(cached)); setLoading(false); return; }

    fetch('https://zenquotes.io/api/today')
      .then(r => r.json())
      .then(d => {
        const q = d[0];
        setQuote(q);
        localStorage.setItem(cacheKey, JSON.stringify(q));
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  return (
    <div className="card">
      <div className="card-header">
        <div className="flex items-center gap-3">
          <div className="w-3 h-3 rounded-full bg-violet-500" />
          <h2 className="card-title">Daily Quote</h2>
        </div>
      </div>

      {loading ? (
        <div className="space-y-2">
          <div className="h-4 bg-slate-700 rounded animate-pulse" />
          <div className="h-4 bg-slate-700 rounded animate-pulse w-3/4" />
        </div>
      ) : quote ? (
        <>
          <p className="text-slate-200 text-sm leading-relaxed italic">“{quote.q}”</p>
          <p className="text-violet-400 text-xs mt-3">— {quote.a}</p>
        </>
      ) : (
        <p className="text-slate-400 text-sm">No quote available today.</p>
      )}
    </div>
  );
}
