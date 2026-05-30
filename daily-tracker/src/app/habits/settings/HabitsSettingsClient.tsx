'use client';

import { useState } from 'react';
import { createClient } from '@/lib/supabase/client';
import Link from 'next/link';

const TYPES = [
  { id: 'checkbox', label: 'Checkbox' },
  { id: 'number', label: 'Number' },
  { id: 'rating', label: 'Rating (1–5)' },
  { id: 'text', label: 'Text note' },
];

export default function HabitsSettingsClient({ habits: initialHabits }: { habits: any[] }) {
  const supabase = createClient();
  const [habits, setHabits] = useState(initialHabits);
  const [newName, setNewName] = useState('');
  const [newType, setNewType] = useState('checkbox');
  const [newTarget, setNewTarget] = useState('');
  const [adding, setAdding] = useState(false);

  async function addHabit() {
    if (!newName.trim()) return;
    setAdding(true);
    const { data } = await supabase
      .from('habits')
      .insert({
        name: newName.trim(),
        type: newType,
        target: newTarget ? Number(newTarget) : null,
        order: habits.length,
        active: true,
      })
      .select()
      .single();
    if (data) setHabits([...habits, data]);
    setNewName('');
    setNewTarget('');
    setAdding(false);
  }

  async function toggleActive(habit: any) {
    const { data } = await supabase
      .from('habits')
      .update({ active: !habit.active })
      .eq('id', habit.id)
      .select()
      .single();
    if (data) setHabits(habits.map(h => h.id === habit.id ? data : h));
  }

  async function deleteHabit(id: string) {
    await supabase.from('habits').delete().eq('id', id);
    setHabits(habits.filter(h => h.id !== id));
  }

  return (
    <div className="min-h-screen bg-slate-900">
      <header className="bg-slate-800 border-b border-slate-700 px-4 py-3">
        <div className="max-w-2xl mx-auto flex items-center gap-4">
          <Link href="/" className="text-slate-400 hover:text-white">←</Link>
          <h1 className="text-xl font-bold text-white">Manage Habits</h1>
        </div>
      </header>

      <main className="max-w-2xl mx-auto px-4 py-8 space-y-6">
        <div className="card">
          <h2 className="text-base font-semibold text-white mb-4">Add New Habit</h2>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-3">
            <input
              type="text"
              value={newName}
              onChange={e => setNewName(e.target.value)}
              placeholder="Habit name"
              className="input sm:col-span-1"
            />
            <select
              value={newType}
              onChange={e => setNewType(e.target.value)}
              className="input"
            >
              {TYPES.map(t => <option key={t.id} value={t.id}>{t.label}</option>)}
            </select>
            {(newType === 'number') && (
              <input
                type="number"
                value={newTarget}
                onChange={e => setNewTarget(e.target.value)}
                placeholder="Target (optional)"
                className="input"
              />
            )}
          </div>
          <button
            onClick={addHabit}
            disabled={adding || !newName.trim()}
            className="btn-primary bg-indigo-600 disabled:opacity-50"
          >Add Habit</button>
        </div>

        <div className="card">
          <h2 className="text-base font-semibold text-white mb-4">Your Habits</h2>
          {habits.length === 0 ? (
            <p className="text-slate-400 text-sm">No habits yet.</p>
          ) : (
            <ul className="space-y-2">
              {habits.map(habit => (
                <li key={habit.id} className="flex items-center gap-3 py-2 px-3 rounded-lg bg-slate-700">
                  <span className="flex-1 text-sm text-white">{habit.name}</span>
                  <span className="text-xs text-slate-400 bg-slate-600 px-2 py-0.5 rounded">{habit.type}</span>
                  <button
                    onClick={() => toggleActive(habit)}
                    className={`text-xs px-2 py-0.5 rounded transition-colors ${
                      habit.active ? 'bg-emerald-700 text-emerald-200' : 'bg-slate-600 text-slate-400'
                    }`}
                  >{habit.active ? 'Active' : 'Inactive'}</button>
                  <button
                    onClick={() => deleteHabit(habit.id)}
                    className="text-slate-500 hover:text-red-400 text-sm"
                  >×</button>
                </li>
              ))}
            </ul>
          )}
        </div>
      </main>
    </div>
  );
}
