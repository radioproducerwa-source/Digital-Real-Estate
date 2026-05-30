'use client';

import { createClient } from '@/lib/supabase/client';
import { useRouter } from 'next/navigation';
import { useState } from 'react';
import type { User } from '@supabase/supabase-js';
import Link from 'next/link';

const TOGGLEABLE_CARDS = [
  { id: 'calendar', label: 'Calendar', color: 'bg-blue-500' },
  { id: 'bitcoin', label: 'Bitcoin', color: 'bg-orange-500' },
  { id: 'quote', label: 'Quote', color: 'bg-violet-500' },
  { id: 'content', label: 'Content Ideas', color: 'bg-pink-500' },
];

interface TopBarProps {
  user: User;
  visibleCards: string[];
  onToggleCard: (cards: string[]) => void;
}

export default function TopBar({ user, visibleCards, onToggleCard }: TopBarProps) {
  const router = useRouter();
  const supabase = createClient();
  const [menuOpen, setMenuOpen] = useState(false);

  async function handleSignOut() {
    await supabase.auth.signOut();
    router.push('/login');
  }

  function toggleCard(id: string) {
    const next = visibleCards.includes(id)
      ? visibleCards.filter(c => c !== id)
      : [...visibleCards, id];
    onToggleCard(next);
  }

  const today = new Date().toLocaleDateString('en-AU', { weekday: 'long', day: 'numeric', month: 'long' });

  return (
    <header className="bg-slate-800 border-b border-slate-700 px-4 py-3">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        <div>
          <h1 className="text-xl font-bold text-white">Daily Tracker</h1>
          <p className="text-sm text-slate-400">{today}</p>
        </div>
        <div className="flex items-center gap-3">
          <Link href="/habits/settings" className="btn-ghost text-sm">Habits</Link>
          <Link href="/goals" className="btn-ghost text-sm">Goals</Link>
          <Link href="/settings" className="btn-ghost text-sm">Settings</Link>
          <div className="relative">
            <button
              onClick={() => setMenuOpen(!menuOpen)}
              className="w-9 h-9 rounded-full bg-indigo-600 flex items-center justify-center text-sm font-bold hover:bg-indigo-500 transition-colors"
            >
              {user.email?.[0].toUpperCase()}
            </button>
            {menuOpen && (
              <div className="absolute right-0 top-12 bg-slate-800 border border-slate-700 rounded-xl shadow-xl p-4 w-56 z-50">
                <p className="text-xs text-slate-400 mb-3 truncate">{user.email}</p>
                <p className="text-xs font-semibold text-slate-300 mb-2">Toggle cards</p>
                {TOGGLEABLE_CARDS.map(card => (
                  <label key={card.id} className="flex items-center gap-2 py-1.5 cursor-pointer">
                    <div className={`w-3 h-3 rounded-full ${card.color}`} />
                    <span className="text-sm text-slate-300 flex-1">{card.label}</span>
                    <input
                      type="checkbox"
                      checked={visibleCards.includes(card.id)}
                      onChange={() => toggleCard(card.id)}
                      className="accent-indigo-500"
                    />
                  </label>
                ))}
                <hr className="border-slate-700 my-3" />
                <button onClick={handleSignOut} className="w-full text-left text-sm text-red-400 hover:text-red-300">
                  Sign out
                </button>
              </div>
            )}
          </div>
        </div>
      </div>
    </header>
  );
}
