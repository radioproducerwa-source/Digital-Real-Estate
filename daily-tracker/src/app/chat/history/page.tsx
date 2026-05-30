import { createClient } from '@/lib/supabase/server';
import { redirect } from 'next/navigation';
import Link from 'next/link';

export default async function ChatHistoryPage() {
  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) redirect('/login');

  const { data: messages } = await supabase
    .from('chat_messages')
    .select('*')
    .order('created_at', { ascending: false })
    .limit(200);

  // Group by date
  const grouped: Record<string, any[]> = {};
  for (const msg of messages ?? []) {
    const date = msg.created_at.split('T')[0];
    if (!grouped[date]) grouped[date] = [];
    grouped[date].push(msg);
  }

  return (
    <div className="min-h-screen bg-slate-900">
      <header className="bg-slate-800 border-b border-slate-700 px-4 py-3">
        <div className="max-w-3xl mx-auto flex items-center gap-4">
          <Link href="/" className="text-slate-400 hover:text-white">←</Link>
          <h1 className="text-xl font-bold text-white">Chat History</h1>
        </div>
      </header>

      <main className="max-w-3xl mx-auto px-4 py-8 space-y-8">
        {Object.entries(grouped).map(([date, msgs]) => (
          <div key={date}>
            <h2 className="text-sm font-semibold text-slate-400 mb-3">
              {new Date(date).toLocaleDateString('en-AU', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' })}
            </h2>
            <div className="space-y-2">
              {msgs.reverse().map(msg => (
                <div key={msg.id} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                  <div className={`max-w-[80%] rounded-2xl px-4 py-2.5 text-sm ${
                    msg.role === 'user'
                      ? 'bg-cyan-800 text-white rounded-tr-sm'
                      : 'bg-slate-700 text-slate-100 rounded-tl-sm'
                  }`}>
                    {msg.content}
                  </div>
                </div>
              ))}
            </div>
          </div>
        ))}

        {Object.keys(grouped).length === 0 && (
          <p className="text-slate-400 text-center py-12">No chat history yet. Start a conversation on the dashboard.</p>
        )}
      </main>
    </div>
  );
}
