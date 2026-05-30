'use client';

import { useState } from 'react';
import { createClient } from '@/lib/supabase/client';

interface SummaryCardProps {
  habitTotal: number;
  habitDone: number;
  taskTotal: number;
  taskDone: number;
}

export default function SummaryCard({ habitTotal, habitDone, taskTotal, taskDone }: SummaryCardProps) {
  const supabase = createClient();
  const [note, setNote] = useState('');
  const [saved, setSaved] = useState(false);

  const habitPct = habitTotal > 0 ? Math.round((habitDone / habitTotal) * 100) : 0;
  const taskPct = taskTotal > 0 ? Math.round((taskDone / taskTotal) * 100) : 0;

  async function saveNote() {
    const today = new Date().toISOString().split('T')[0];
    await supabase.from('chat_messages').insert({
      role: 'user',
      content: `[Daily Note] ${note}`,
      context_snapshot: { type: 'daily_note', date: today },
    });
    setSaved(true);
    setTimeout(() => setSaved(false), 2000);
  }

  return (
    <div className="card">
      <div className="card-header">
        <div className="flex items-center gap-3">
          <div className="w-3 h-3 rounded-full bg-slate-400" />
          <h2 className="card-title">Daily Summary</h2>
        </div>
        <span className="text-xs text-slate-400">{new Date().toLocaleDateString('en-AU', { weekday: 'long', day: 'numeric', month: 'long' })}</span>
      </div>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
        <div className="bg-slate-700 rounded-xl p-4 text-center">
          <div className="text-3xl font-bold text-indigo-400">{habitPct}%</div>
          <div className="text-xs text-slate-400 mt-1">Habits done</div>
          <div className="text-xs text-slate-500">{habitDone}/{habitTotal}</div>
        </div>
        <div className="bg-slate-700 rounded-xl p-4 text-center">
          <div className="text-3xl font-bold text-emerald-400">{taskPct}%</div>
          <div className="text-xs text-slate-400 mt-1">Tasks done</div>
          <div className="text-xs text-slate-500">{taskDone}/{taskTotal}</div>
        </div>
        <div className="bg-slate-700 rounded-xl p-4 text-center">
          <div className="text-3xl font-bold text-blue-400">-</div>
          <div className="text-xs text-slate-400 mt-1">Meetings today</div>
          <div className="text-xs text-slate-500">Calendar needed</div>
        </div>
        <div className="bg-slate-700 rounded-xl p-4 text-center">
          <div className="text-3xl font-bold text-amber-400">-</div>
          <div className="text-xs text-slate-400 mt-1">Focus time</div>
          <div className="text-xs text-slate-500">Phase 2</div>
        </div>
      </div>

      <div className="flex gap-3">
        <textarea
          value={note}
          onChange={e => setNote(e.target.value)}
          placeholder="Add a note for today..."
          rows={2}
          className="input resize-none text-sm flex-1"
        />
        <button
          onClick={saveNote}
          disabled={!note.trim()}
          className="btn-primary bg-slate-600 self-end disabled:opacity-50"
        >{saved ? '✓ Saved' : 'Save'}</button>
      </div>
    </div>
  );
}
