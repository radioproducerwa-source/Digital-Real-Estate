'use client';

import { useEffect, useState } from 'react';

export default function BitcoinCard({ currency }: { currency: 'AUD' | 'USD' }) {
  const [price, setPrice] = useState<number | null>(null);
  const [change24h, setChange24h] = useState<number | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const sym = currency === 'AUD' ? 'aud' : 'usd';
    fetch(`https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=${sym}&include_24hr_change=true`)
      .then(r => r.json())
      .then(d => {
        setPrice(d.bitcoin?.[sym] ?? null);
        setChange24h(d.bitcoin?.[`${sym}_24h_change`] ?? null);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, [currency]);

  const fmt = (n: number) => n.toLocaleString('en-AU', { style: 'currency', currency, maximumFractionDigits: 0 });
  const isUp = (change24h ?? 0) >= 0;

  return (
    <div className="card">
      <div className="card-header">
        <div className="flex items-center gap-3">
          <div className="w-3 h-3 rounded-full bg-orange-500" />
          <h2 className="card-title">Bitcoin</h2>
        </div>
        <span className="text-xs text-slate-400">{currency}</span>
      </div>

      {loading ? (
        <div className="h-12 bg-slate-700 rounded-lg animate-pulse" />
      ) : price === null ? (
        <p className="text-slate-400 text-sm">Unable to fetch price.</p>
      ) : (
        <div className="flex items-end gap-3">
          <span className="text-3xl font-bold text-orange-400">{fmt(price)}</span>
          <span className={`text-sm font-semibold mb-0.5 ${isUp ? 'text-emerald-400' : 'text-red-400'}`}>
            {isUp ? '▲' : '▼'} {Math.abs(change24h!).toFixed(2)}%
          </span>
        </div>
      )}
      <p className="text-xs text-slate-500 mt-1">24h change · via CoinGecko</p>
    </div>
  );
}
