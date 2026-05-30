import { createClient } from '@/lib/supabase/server';
import { NextResponse } from 'next/server';

export async function GET(request: Request) {
  const { searchParams, origin } = new URL(request.url);
  const code = searchParams.get('code');
  if (!code) return NextResponse.redirect(`${origin}/settings?error=ms_auth_failed`);

  const tokenRes = await fetch('https://login.microsoftonline.com/common/oauth2/v2.0/token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      client_id: process.env.MICROSOFT_CLIENT_ID!,
      client_secret: process.env.MICROSOFT_CLIENT_SECRET!,
      code,
      redirect_uri: `${process.env.NEXT_PUBLIC_APP_URL}/api/auth/microsoft/callback`,
      grant_type: 'authorization_code',
      scope: 'Calendars.Read offline_access',
    }),
  });

  const tokens = await tokenRes.json();
  if (!tokens.refresh_token) return NextResponse.redirect(`${origin}/settings?error=ms_no_refresh_token`);

  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) return NextResponse.redirect(`${origin}/login`);

  await supabase.from('user_settings').upsert({
    user_id: user.id,
    ms_refresh_token: tokens.refresh_token,
  }, { onConflict: 'user_id' });

  return NextResponse.redirect(`${origin}/settings?ms=connected`);
}
