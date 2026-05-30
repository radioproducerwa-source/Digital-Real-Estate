'use client';

import { useState } from 'react';
import { createClient } from '@/lib/supabase/client';
import Link from 'next/link';

const CARDS = [
  { id: 'calendar', label: 'Outlook Calendar', color: 'bg-blue-500' },
  { id: 'bitcoin', label: 'Bitcoin Price', color: 'bg-orange-500' },
  { id: 'quote', label: 'Inspirational Quote', color: 'bg-violet-500' },
  { id: 'content', label: 'Content Ideas', color: 'bg-pink-500' },
];

export default function SettingsClient({ settings, msStatus }: { settings: any; msStatus: string | null }) {
  const supabase = createClient();
  const [visibleCards, setVisibleCards] = useState<string[]>(settings.visible_cards ?? []);
  const [currency, setCurrency] = useState<'AUD' | 'USD'>(settings.currency ?? 'AUD');
  const [saved, setSaved] = useState(false);

  function toggleCard(id: string) {
    setVisibleCards(prev =>
      prev.includes(id) ? prev.filter(c => c !== id) : [...prev, id]
    );
  }

  async function saveSettings() {
    await supabase.from('user_settings').upsert(
      { visible_cards: visibleCards, currency },
      { onConflict: 'user_id' }
    );
    setSaved(true);
    setTimeout(() => setSaved(false), 2000);
  }

  return (
    <div className="min-h-screen bg-slate-900">
      <header className="bg-slate-800 border-b border-slate-700 px-4 py-3">
        <div className="max-w-2xl mx-auto flex items-center gap-4">
          <Link href="/" className="text-slate-400 hover:text-white">←</Link>
          <h1 className="text-xl font-bold text-white">Settings</h1>
        </div>
      </header>

      <main className="max-w-2xl mx-auto px-4 py-8 space-y-6">
        {/* Microsoft Outlook */}
        <div className="card">
          <h2 className="text-base font-semibold text-white mb-4">Outlook Calendar</h2>
          {msStatus === 'connected' && (
            <div className="bg-emerald-900 text-emerald-300 text-sm px-3 py-2 rounded-lg mb-4">✓ Connected successfully</div>
          )}
          {msStatus === 'error' && (
            <div className="bg-red-900 text-red-300 text-sm px-3 py-2 rounded-lg mb-4">Connection failed. Please try again.</div>
          )}
          {settings.ms_refresh_token ? (
            <div className="flex items-center justify-between">
              <span className="text-sm text-slate-300">✅ Outlook connected</span>
              <a href="/api/auth/microsoft" className="btn-ghost text-xs">Reconnect</a>
            </div>
          ) : (
            <div className="flex items-center justify-between">
              <span className="text-sm text-slate-400">Not connected</span>
              <a href="/api/auth/microsoft" className="btn-primary bg-blue-700 hover:bg-blue-600 text-sm">
                Connect Outlook
              </a>
            </div>
          )}
        </div>

        {/* Toggle cards */}
        <div className="card">
          <h2 className="text-base font-semibold text-white mb-4">Visible Cards</h2>
          <div className="space-y-3">
            {CARDS.map(card => (
              <label key={card.id} className="flex items-center gap-3 cursor-pointer">
                <div className={`w-3 h-3 rounded-full ${card.color} flex-shrink-0`} />
                <span className="text-sm text-slate-300 flex-1">{card.label}</span>
                <input
                  type="checkbox"
                  checked={visibleCards.includes(card.id)}
                  onChange={() => toggleCard(card.id)}
                  className="w-4 h-4 accent-indigo-500"
                />
              </label>
            ))}
          </div>
        </div>

        {/* Currency */}
        <div className="card">
          <h2 className="text-base font-semibold text-white mb-4">Bitcoin Currency</h2>
          <div className="flex gap-3">
            {(['AUD', 'USD'] as const).map(c => (
              <button
                key={c}
                onClick={() => setCurrency(c)}
                className={`px-6 py-2 rounded-lg font-semibold text-sm transition-colors ${
                  currency === c ? 'bg-orange-600 text-white' : 'bg-slate-700 text-slate-400 hover:bg-slate-600'
                }`}
              >{c}</button>
            ))}
          </div>
        </div>

        <button onClick={saveSettings} className="btn-primary bg-indigo-600 w-full py-3">
          {saved ? '✓ Saved' : 'Save Settings'}
        </button>
      </main>
    </div>
  );
}
