'use client';

import { useState } from 'react';
import { createClient } from '@/lib/supabase/client';
import Link from 'next/link';

const HORIZONS = ['daily', 'weekly', 'monthly', 'yearly'] as const;
const HORIZON_COLOURS: Record<string, string> = {
  daily: 'bg-slate-600 text-slate-300',
  weekly: 'bg-amber-900 text-amber-300',
  monthly: 'bg-orange-900 text-orange-300',
  yearly: 'bg-rose-900 text-rose-300',
};

export default function GoalsClient({ goals: initialGoals, milestones: initialMilestones }: { goals: any[]; milestones: any[] }) {
  const supabase = createClient();
  const [goals, setGoals] = useState(initialGoals);
  const [milestones, setMilestones] = useState(initialMilestones);
  const [expanded, setExpanded] = useState<string | null>(null);
  const [newGoalTitle, setNewGoalTitle] = useState('');
  const [newGoalDesc, setNewGoalDesc] = useState('');
  const [newMsTitle, setNewMsTitle] = useState<Record<string, string>>({});
  const [newMsHorizon, setNewMsHorizon] = useState<Record<string, string>>({});
  const [showArchived, setShowArchived] = useState(false);

  const activeGoals = goals.filter(g => !g.archived);
  const archivedGoals = goals.filter(g => g.archived);

  async function addGoal() {
    if (!newGoalTitle.trim()) return;
    const { data } = await supabase
      .from('goals')
      .insert({ title: newGoalTitle, description: newGoalDesc || null, archived: false })
      .select().single();
    if (data) setGoals([data, ...goals]);
    setNewGoalTitle('');
    setNewGoalDesc('');
  }

  async function addMilestone(goalId: string) {
    const title = newMsTitle[goalId]?.trim();
    if (!title) return;
    const { data } = await supabase
      .from('milestones')
      .insert({ goal_id: goalId, title, horizon: newMsHorizon[goalId] ?? 'weekly', completed: false })
      .select().single();
    if (data) setMilestones([...milestones, data]);
    setNewMsTitle(prev => ({ ...prev, [goalId]: '' }));
  }

  async function archiveGoal(id: string) {
    await supabase.from('goals').update({ archived: true }).eq('id', id);
    setGoals(goals.map(g => g.id === id ? { ...g, archived: true } : g));
  }

  async function toggleMilestone(m: any) {
    const { data } = await supabase.from('milestones').update({ completed: !m.completed }).eq('id', m.id).select().single();
    if (data) setMilestones(milestones.map(x => x.id === m.id ? data : x));
  }

  function renderGoalList(list: any[]) {
    return list.map(goal => {
      const ms = milestones.filter(m => m.goal_id === goal.id);
      const isOpen = expanded === goal.id;
      return (
        <div key={goal.id} className="card">
          <div className="flex items-start gap-3">
            <div className="flex-1">
              <button
                onClick={() => setExpanded(isOpen ? null : goal.id)}
                className="text-left"
              >
                <h3 className="font-semibold text-white">{goal.title}</h3>
                {goal.description && <p className="text-sm text-slate-400 mt-0.5">{goal.description}</p>}
              </button>
            </div>
            {!goal.archived && (
              <button onClick={() => archiveGoal(goal.id)} className="btn-ghost text-xs">Archive</button>
            )}
            <button
              onClick={() => setExpanded(isOpen ? null : goal.id)}
              className="text-slate-500 text-sm"
            >{isOpen ? '▲' : '▼'} {ms.length}</button>
          </div>

          {isOpen && (
            <div className="mt-4 space-y-2">
              {HORIZONS.map(h => {
                const hMs = ms.filter(m => m.horizon === h);
                return hMs.length ? (
                  <div key={h}>
                    <p className="text-xs text-slate-500 uppercase mb-1">{h}</p>
                    {hMs.map(m => (
                      <div key={m.id} className="flex items-center gap-2 py-1">
                        <button
                          onClick={() => toggleMilestone(m)}
                          className={`w-4 h-4 rounded border flex items-center justify-center ${
                            m.completed ? 'bg-rose-600 border-rose-600' : 'border-slate-500'
                          }`}
                        >{m.completed && <span className="text-xs text-white">✓</span>}</button>
                        <span className={`text-sm flex-1 ${m.completed ? 'line-through text-slate-500' : 'text-slate-200'}`}>{m.title}</span>
                        <span className={`text-xs px-1.5 py-0.5 rounded ${HORIZON_COLOURS[m.horizon]}`}>{m.horizon}</span>
                      </div>
                    ))}
                  </div>
                ) : null;
              })}

              {!goal.archived && (
                <div className="flex gap-2 mt-3">
                  <input
                    type="text"
                    value={newMsTitle[goal.id] ?? ''}
                    onChange={e => setNewMsTitle(prev => ({ ...prev, [goal.id]: e.target.value }))}
                    placeholder="New milestone..."
                    className="input text-sm py-1.5 flex-1"
                  />
                  <select
                    value={newMsHorizon[goal.id] ?? 'weekly'}
                    onChange={e => setNewMsHorizon(prev => ({ ...prev, [goal.id]: e.target.value }))}
                    className="input text-sm py-1.5 w-32"
                  >
                    {HORIZONS.map(h => <option key={h} value={h}>{h}</option>)}
                  </select>
                  <button onClick={() => addMilestone(goal.id)} className="btn-primary bg-rose-700 text-sm px-3">+</button>
                </div>
              )}
            </div>
          )}
        </div>
      );
    });
  }

  return (
    <div className="min-h-screen bg-slate-900">
      <header className="bg-slate-800 border-b border-slate-700 px-4 py-3">
        <div className="max-w-3xl mx-auto flex items-center gap-4">
          <Link href="/" className="text-slate-400 hover:text-white">←</Link>
          <h1 className="text-xl font-bold text-white">Goals & Milestones</h1>
        </div>
      </header>

      <main className="max-w-3xl mx-auto px-4 py-8 space-y-6">
        <div className="card">
          <h2 className="text-base font-semibold text-white mb-4">New Goal</h2>
          <div className="space-y-3">
            <input type="text" value={newGoalTitle} onChange={e => setNewGoalTitle(e.target.value)} placeholder="Goal title" className="input" />
            <input type="text" value={newGoalDesc} onChange={e => setNewGoalDesc(e.target.value)} placeholder="Description (optional)" className="input" />
            <button onClick={addGoal} disabled={!newGoalTitle.trim()} className="btn-primary bg-rose-700 disabled:opacity-50">Add Goal</button>
          </div>
        </div>

        {activeGoals.length > 0 && renderGoalList(activeGoals)}

        {archivedGoals.length > 0 && (
          <>
            <button onClick={() => setShowArchived(!showArchived)} className="btn-ghost text-sm">
              {showArchived ? 'Hide' : 'Show'} archived ({archivedGoals.length})
            </button>
            {showArchived && renderGoalList(archivedGoals)}
          </>
        )}
      </main>
    </div>
  );
}
