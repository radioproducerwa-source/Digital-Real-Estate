'use client';

import { useEffect, useRef, useState } from 'react';
import { createClient } from '@/lib/supabase/client';

interface Message {
  id?: string;
  role: 'user' | 'assistant';
  content: string;
  created_at?: string;
}

interface ChatCardProps {
  habits: any[];
  habitLogs: any[];
  tasks: any[];
  goals: any[];
  milestones: any[];
}

export default function ChatCard({ habits, habitLogs, tasks, goals, milestones }: ChatCardProps) {
  const supabase = createClient();
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [loadingHistory, setLoadingHistory] = useState(true);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    supabase
      .from('chat_messages')
      .select('*')
      .order('created_at', { ascending: true })
      .limit(50)
      .then(({ data }) => {
        if (data) setMessages(data);
        setLoadingHistory(false);
      });
  }, []);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  async function sendMessage() {
    if (!input.trim() || loading) return;

    const userMsg: Message = { role: 'user', content: input };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setLoading(true);

    const context = {
      date: new Date().toISOString().split('T')[0],
      habits: habits.map(h => ({
        name: h.name,
        type: h.type,
        completed: !!habitLogs.find(l => l.habit_id === h.id && l.completed),
      })),
      tasks: tasks.map(t => ({ title: t.title, completed: t.completed })),
      goals: goals.map(g => ({
        title: g.title,
        milestones: milestones.filter(m => m.goal_id === g.id).map(m => ({
          title: m.title,
          horizon: m.horizon,
          completed: m.completed,
        })),
      })),
    };

    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input, context, history: messages.slice(-10) }),
      });

      const data = await res.json();
      const assistantMsg: Message = { role: 'assistant', content: data.reply };
      setMessages(prev => [...prev, assistantMsg]);

      // Persist both messages
      await supabase.from('chat_messages').insert([
        { role: 'user', content: input, context_snapshot: context },
        { role: 'assistant', content: data.reply, context_snapshot: null },
      ]);
    } catch {
      setMessages(prev => [...prev, { role: 'assistant', content: 'Sorry, something went wrong. Please try again.' }]);
    }

    setLoading(false);
  }

  return (
    <div className="card flex flex-col" style={{ minHeight: '500px' }}>
      <div className="card-header">
        <div className="flex items-center gap-3">
          <div className="w-3 h-3 rounded-full bg-cyan-500" />
          <h2 className="card-title">Claude Chat</h2>
        </div>
        <a href="/chat/history" className="text-xs text-cyan-400 hover:underline">History</a>
      </div>

      <div className="flex-1 overflow-y-auto space-y-3 mb-4 pr-1" style={{ maxHeight: '380px' }}>
        {loadingHistory ? (
          <div className="flex items-center justify-center h-20">
            <span className="text-slate-400 text-sm">Loading history...</span>
          </div>
        ) : messages.length === 0 ? (
          <div className="text-center py-8">
            <p className="text-slate-400 text-sm">Ask Claude anything about your day.</p>
            <div className="flex flex-wrap gap-2 justify-center mt-3">
              {[
                'What should I prioritise this afternoon?',
                'Am I on track for my monthly goals?',
                'Write a LinkedIn post based on what I worked on',
              ].map(prompt => (
                <button
                  key={prompt}
                  onClick={() => { setInput(prompt); }}
                  className="text-xs bg-slate-700 hover:bg-slate-600 text-slate-300 px-3 py-1.5 rounded-full transition-colors"
                >{prompt}</button>
              ))}
            </div>
          </div>
        ) : (
          messages.map((msg, i) => (
            <div key={i} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
              <div className={`max-w-[80%] rounded-2xl px-4 py-2.5 text-sm leading-relaxed ${
                msg.role === 'user'
                  ? 'bg-cyan-700 text-white rounded-tr-sm'
                  : 'bg-slate-700 text-slate-100 rounded-tl-sm'
              }`}>
                {msg.content}
              </div>
            </div>
          ))
        )}
        {loading && (
          <div className="flex justify-start">
            <div className="bg-slate-700 rounded-2xl rounded-tl-sm px-4 py-2.5">
              <span className="flex gap-1">
                <span className="w-2 h-2 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
                <span className="w-2 h-2 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
                <span className="w-2 h-2 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
              </span>
            </div>
          </div>
        )}
        <div ref={bottomRef} />
      </div>

      <div className="flex gap-2">
        <input
          type="text"
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && !e.shiftKey && sendMessage()}
          placeholder="Message Claude..."
          disabled={loading}
          className="input text-sm py-2"
        />
        <button
          onClick={sendMessage}
          disabled={loading || !input.trim()}
          className="btn-primary bg-cyan-700 hover:bg-cyan-600 disabled:opacity-50 px-4"
        >↑</button>
      </div>
    </div>
  );
}
