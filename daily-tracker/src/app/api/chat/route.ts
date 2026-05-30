import Anthropic from '@anthropic-ai/sdk';
import { createClient } from '@/lib/supabase/server';
import { NextResponse } from 'next/server';

const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

export async function POST(req: Request) {
  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });

  const { message, context, history } = await req.json();

  const systemPrompt = `You are a personal productivity assistant for a marketing and media professional. 
Today is ${context.date}.

The user's current state:
- Habits today: ${context.habits.map((h: any) => `${h.name} (${h.completed ? 'done' : 'not done'})`).join(', ') || 'none set'}
- Tasks: ${context.tasks.map((t: any) => `${t.title} (${t.completed ? 'done' : 'pending'})`).join(', ') || 'none'}
- Active goals: ${context.goals.map((g: any) => g.title).join(', ') || 'none'}

Be concise, practical, and encouraging. Reference their specific habits, tasks, and goals when relevant.`;

  const messages: Anthropic.MessageParam[] = [
    ...(history ?? []).map((m: any) => ({ role: m.role as 'user' | 'assistant', content: m.content })),
    { role: 'user', content: message },
  ];

  const response = await anthropic.messages.create({
    model: 'claude-sonnet-4-6',
    max_tokens: 1024,
    system: systemPrompt,
    messages,
  });

  const reply = response.content[0].type === 'text' ? response.content[0].text : '';

  return NextResponse.json({ reply });
}
