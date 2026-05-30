'use client';

import { useState } from 'react';
import { createClient } from '@/lib/supabase/client';

interface Habit {
  id: string;
  name: string;
  type: 'checkbox' | 'number' | 'rating' | 'text';
  target: number | null;
}

interface HabitLog {
  id?: string;
  habit_id: string;
  date: string;
  value: any;
  completed: boolean;
}

interface HabitsCardProps {
  habits: Habit[];
  logs: HabitLog[];
  onLogsChange: (logs: HabitLog[]) => void;
}

const today = new Date().toISOString().split('T')[0];

export default function HabitsCard({ habits, logs, onLogsChange }: HabitsCardProps) {
  const supabase = createClient();
  const [saving, setSaving] = useState<string | null>(null);

  const getLog = (habitId: string) => logs.find(l => l.habit_id === habitId);

  const completedCount = habits.filter(h => getLog(h.id)?.completed).length;

  async function upsertLog(habitId: string, value: any, completed: boolean) {
    setSaving(habitId);
    const existing = getLog(habitId);
    const payload = { habit_id: habitId, date: today, value, completed };

    let result;
    if (existing?.id) {
      result = await supabase.from('habit_logs').update(payload).eq('id', existing.id).select().single();
    } else {
      result = await supabase.from('habit_logs').insert(payload).select().single();
    }

    if (result.data) {
      onLogsChange(logs.map(l => l.habit_id === habitId ? result.data : l)
        .concat(existing ? [] : [result.data]));
    }
    setSaving(null);
  }

  return (
    <div className="card">
      <div className="card-header">
        <div className="flex items-center gap-3">
          <div className="w-3 h-3 rounded-full bg-indigo-500" />
          <h2 className="card-title">Today's Habits</h2>
        </div>
        <span className="text-sm font-semibold text-indigo-400">{completedCount} / {habits.length}</span>
      </div>

      {habits.length === 0 ? (
        <p className="text-slate-400 text-sm">No habits yet. <a href="/habits/settings" className="text-indigo-400 hover:underline">Add some</a></p>
      ) : (
        <ul className="space-y-3">
          {habits.map(habit => {
            const log = getLog(habit.id);
            const isSaving = saving === habit.id;

            return (
              <li key={habit.id} className="flex items-center gap-3">
                {habit.type === 'checkbox' && (
                  <button
                    onClick={() => upsertLog(habit.id, true, !log?.completed)}
                    disabled={isSaving}
                    className={`w-6 h-6 rounded-md border-2 flex items-center justify-center flex-shrink-0 transition-colors ${
                      log?.completed ? 'bg-indigo-600 border-indigo-600' : 'border-slate-500 hover:border-indigo-400'
                    }`}
                  >
                    {log?.completed && <span className="text-xs text-white">✓</span>}
                  </button>
                )}

                {habit.type === 'rating' && (
                  <div className="flex gap-1">
                    {[1,2,3,4,5].map(n => (
                      <button
                        key={n}
                        onClick={() => upsertLog(habit.id, n, true)}
                        className={`w-6 h-6 rounded text-xs font-bold transition-colors ${
                          (log?.value ?? 0) >= n ? 'bg-indigo-600 text-white' : 'bg-slate-700 text-slate-400 hover:bg-slate-600'
                        }`}
                      >{n}</button>
                    ))}
                  </div>
                )}

                {habit.type === 'number' && (
                  <input
                    type="number"
                    value={log?.value ?? ''}
                    placeholder={habit.target ? `Goal: ${habit.target}` : '0'}
                    onChange={e => upsertLog(habit.id, Number(e.target.value), Number(e.target.value) > 0)}
                    className="w-20 bg-slate-700 border border-slate-600 rounded px-2 py-1 text-white text-sm focus:outline-none focus:ring-1 focus:ring-indigo-500"
                  />
                )}

                {habit.type === 'text' && (
                  <input
                    type="text"
                    value={log?.value ?? ''}
                    placeholder="Note..."
                    onBlur={e => upsertLog(habit.id, e.target.value, !!e.target.value)}
                    onChange={e => {
                      const updated = logs.map(l => l.habit_id === habit.id ? { ...l, value: e.target.value } : l);
                      onLogsChange(updated);
                    }}
                    className="flex-1 bg-slate-700 border border-slate-600 rounded px-2 py-1 text-white text-sm focus:outline-none focus:ring-1 focus:ring-indigo-500"
                  />
                )}

                <span className={`text-sm flex-1 ${
                  log?.completed && habit.type === 'checkbox' ? 'line-through text-slate-500' : 'text-slate-200'
                }`}>{habit.name}</span>

                {isSaving && <span className="text-xs text-slate-500">...</span>}
              </li>
            );
          })}
        </ul>
      )}
    </div>
  );
}
