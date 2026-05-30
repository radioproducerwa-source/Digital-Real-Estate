'use client';

import { useState } from 'react';
import { createClient } from '@/lib/supabase/client';

interface Task {
  id: string;
  title: string;
  date: string;
  completed: boolean;
  rolled_over: boolean;
}

interface TasksCardProps {
  tasks: Task[];
  onTasksChange: (tasks: Task[]) => void;
}

const today = new Date().toISOString().split('T')[0];

export default function TasksCard({ tasks, onTasksChange }: TasksCardProps) {
  const supabase = createClient();
  const [newTitle, setNewTitle] = useState('');
  const [adding, setAdding] = useState(false);

  const completedCount = tasks.filter(t => t.completed).length;

  async function addTask() {
    if (!newTitle.trim()) return;
    setAdding(true);
    const { data } = await supabase
      .from('tasks')
      .insert({ title: newTitle.trim(), date: today, completed: false, rolled_over: false })
      .select()
      .single();
    if (data) onTasksChange([...tasks, data]);
    setNewTitle('');
    setAdding(false);
  }

  async function toggleTask(task: Task) {
    const { data } = await supabase
      .from('tasks')
      .update({ completed: !task.completed })
      .eq('id', task.id)
      .select()
      .single();
    if (data) onTasksChange(tasks.map(t => t.id === task.id ? data : t));
  }

  async function deleteTask(id: string) {
    await supabase.from('tasks').delete().eq('id', id);
    onTasksChange(tasks.filter(t => t.id !== id));
  }

  async function toggleRollover(task: Task) {
    const { data } = await supabase
      .from('tasks')
      .update({ rolled_over: !task.rolled_over })
      .eq('id', task.id)
      .select()
      .single();
    if (data) onTasksChange(tasks.map(t => t.id === task.id ? data : t));
  }

  return (
    <div className="card">
      <div className="card-header">
        <div className="flex items-center gap-3">
          <div className="w-3 h-3 rounded-full bg-emerald-500" />
          <h2 className="card-title">Tasks</h2>
        </div>
        <span className="text-sm font-semibold text-emerald-400">{completedCount} / {tasks.length}</span>
      </div>

      <ul className="space-y-2 mb-4">
        {tasks.map(task => (
          <li key={task.id} className="flex items-center gap-2 group">
            <button
              onClick={() => toggleTask(task)}
              className={`w-5 h-5 rounded border-2 flex items-center justify-center flex-shrink-0 transition-colors ${
                task.completed ? 'bg-emerald-600 border-emerald-600' : 'border-slate-500 hover:border-emerald-400'
              }`}
            >
              {task.completed && <span className="text-xs text-white">✓</span>}
            </button>
            <span className={`flex-1 text-sm ${
              task.completed ? 'line-through text-slate-500' : 'text-slate-200'
            }`}>{task.title}</span>
            <div className="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
              <button
                onClick={() => toggleRollover(task)}
                title={task.rolled_over ? 'Cancel roll over' : 'Roll to tomorrow'}
                className={`text-xs px-1.5 py-0.5 rounded transition-colors ${
                  task.rolled_over ? 'bg-amber-600 text-white' : 'text-slate-500 hover:text-amber-400'
                }`}
              >➡</button>
              <button
                onClick={() => deleteTask(task.id)}
                className="text-xs text-slate-500 hover:text-red-400 px-1"
              >×</button>
            </div>
          </li>
        ))}
      </ul>

      <div className="flex gap-2">
        <input
          type="text"
          value={newTitle}
          onChange={e => setNewTitle(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && addTask()}
          placeholder="Add a task..."
          className="input text-sm py-1.5"
        />
        <button
          onClick={addTask}
          disabled={adding || !newTitle.trim()}
          className="btn-primary bg-emerald-600 text-sm px-3 disabled:opacity-50"
        >+</button>
      </div>
    </div>
  );
}
