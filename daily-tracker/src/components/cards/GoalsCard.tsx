'use client';

import { useState } from 'react';
import { createClient } from '@/lib/supabase/client';

interface Goal {
  id: string;
  title: string;
  description: string | null;
  target_date: string | null;
}

interface Milestone {
  id: string;
  goal_id: string;
  title: string;
  horizon: 'daily' | 'weekly' | 'monthly' | 'yearly';
  completed: boolean;
}

const HORIZON_COLOURS: Record<string, string> = {
  daily: 'text-rose-300',
  weekly: 'text-orange-300',
  monthly: 'text-amber-300',
  yearly: 'text-rose-400',
};

export default function GoalsCard({ goals, milestones }: { goals: Goal[]; milestones: Milestone[] }) {
  const supabase = createClient();
  const [expanded, setExpanded] = useState<string | null>(null);
  const [localMilestones, setLocalMilestones] = useState(milestones);

  const getGoalMilestones = (goalId: string) =>
    localMilestones.filter(m => m.goal_id === goalId);

  async function toggleMilestone(m: Milestone) {
    const { data } = await supabase
      .from('milestones')
      .update({ completed: !m.completed })
      .eq('id', m.id)
      .select()
      .single();
    if (data) setLocalMilestones(localMilestones.map(x => x.id === m.id ? data : x));
  }

  return (
    <div className="card">
      <div className="card-header">
        <div className="flex items-center gap-3">
          <div className="w-3 h-3 rounded-full bg-rose-500" />
          <h2 className="card-title">Goals & Milestones</h2>
        </div>
        <a href="/goals" className="text-xs text-rose-400 hover:underline">View all</a>
      </div>

      {goals.length === 0 ? (
        <p className="text-slate-400 text-sm">No active goals. <a href="/goals" className="text-rose-400 hover:underline">Add one</a></p>
      ) : (
        <ul className="space-y-2">
          {goals.slice(0, 5).map(goal => {
            const ms = getGoalMilestones(goal.id);
            const isOpen = expanded === goal.id;
            return (
              <li key={goal.id}>
                <button
                  onClick={() => setExpanded(isOpen ? null : goal.id)}
                  className="w-full flex items-center justify-between text-left py-2 px-3 rounded-lg hover:bg-slate-700 transition-colors"
                >
                  <span className="text-sm font-medium text-white">{goal.title}</span>
                  <span className="text-xs text-slate-500">{ms.length} milestones {isOpen ? '▲' : '▼'}</span>
                </button>
                {isOpen && ms.length > 0 && (
                  <ul className="pl-4 mt-1 space-y-1">
                    {ms.map(m => (
                      <li key={m.id} className="flex items-center gap-2">
                        <button
                          onClick={() => toggleMilestone(m)}
                          className={`w-4 h-4 rounded border flex items-center justify-center flex-shrink-0 ${
                            m.completed ? 'bg-rose-600 border-rose-600' : 'border-slate-500'
                          }`}
                        >
                          {m.completed && <span className="text-xs text-white">✓</span>}
                        </button>
                        <span className={`text-xs flex-1 ${
                          m.completed ? 'line-through text-slate-500' : 'text-slate-300'
                        }`}>{m.title}</span>
                        <span className={`text-xs ${HORIZON_COLOURS[m.horizon]}`}>{m.horizon[0].toUpperCase()}</span>
                      </li>
                    ))}
                  </ul>
                )}
              </li>
            );
          })}
        </ul>
      )}
    </div>
  );
}
