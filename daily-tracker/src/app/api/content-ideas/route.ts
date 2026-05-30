import Anthropic from '@anthropic-ai/sdk';
import { createClient } from '@/lib/supabase/server';
import { NextResponse } from 'next/server';

const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

export async function POST(req: Request) {
  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });

  const { tasks } = await req.json();
  const today = new Date().toLocaleDateString('en-AU', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' });
  const taskSummary = tasks.map((t: any) => t.title).join(', ') || 'general productivity and marketing';

  const response = await anthropic.messages.create({
    model: 'claude-sonnet-4-6',
    max_tokens: 1024,
    messages: [{
      role: 'user',
      content: `You are a content strategist for a marketing and media professional. Today is ${today}.

Based on these tasks/focus areas: ${taskSummary}

Generate 3-5 content ideas for each type. Return ONLY valid JSON in this exact format:
{
  "social": ["idea 1", "idea 2", "idea 3"],
  "blog": ["idea 1", "idea 2", "idea 3"],
  "video": ["idea 1", "idea 2", "idea 3"]
}

Make ideas specific, actionable, and relevant to marketing/media. No extra text.`,
    }],
  });

  const text = response.content[0].type === 'text' ? response.content[0].text : '{}';

  try {
    const ideas = JSON.parse(text);
    return NextResponse.json({ ideas });
  } catch {
    return NextResponse.json({ error: 'Failed to parse ideas' }, { status: 500 });
  }
}
