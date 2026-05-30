export type Json = string | number | boolean | null | { [key: string]: Json | undefined } | Json[];

export type HabitType = 'checkbox' | 'number' | 'rating' | 'text';
export type MilestoneHorizon = 'daily' | 'weekly' | 'monthly' | 'yearly';
export type ChatRole = 'user' | 'assistant';

export interface Database {
  public: {
    Tables: {
      habits: {
        Row: {
          id: string;
          user_id: string;
          name: string;
          type: HabitType;
          target: number | null;
          order: number;
          active: boolean;
          created_at: string;
        };
        Insert: Omit<Database['public']['Tables']['habits']['Row'], 'id' | 'created_at'>;
        Update: Partial<Database['public']['Tables']['habits']['Insert']>;
      };
      habit_logs: {
        Row: {
          id: string;
          habit_id: string;
          date: string;
          value: Json | null;
          completed: boolean;
        };
        Insert: Omit<Database['public']['Tables']['habit_logs']['Row'], 'id'>;
        Update: Partial<Database['public']['Tables']['habit_logs']['Insert']>;
      };
      tasks: {
        Row: {
          id: string;
          user_id: string;
          title: string;
          date: string;
          completed: boolean;
          rolled_over: boolean;
          created_at: string;
        };
        Insert: Omit<Database['public']['Tables']['tasks']['Row'], 'id' | 'created_at'>;
        Update: Partial<Database['public']['Tables']['tasks']['Insert']>;
      };
      goals: {
        Row: {
          id: string;
          user_id: string;
          title: string;
          description: string | null;
          target_date: string | null;
          archived: boolean;
          created_at: string;
        };
        Insert: Omit<Database['public']['Tables']['goals']['Row'], 'id' | 'created_at'>;
        Update: Partial<Database['public']['Tables']['goals']['Insert']>;
      };
      milestones: {
        Row: {
          id: string;
          goal_id: string;
          title: string;
          horizon: MilestoneHorizon;
          completed: boolean;
          created_at: string;
        };
        Insert: Omit<Database['public']['Tables']['milestones']['Row'], 'id' | 'created_at'>;
        Update: Partial<Database['public']['Tables']['milestones']['Insert']>;
      };
      chat_messages: {
        Row: {
          id: string;
          user_id: string;
          role: ChatRole;
          content: string;
          context_snapshot: Json | null;
          created_at: string;
        };
        Insert: Omit<Database['public']['Tables']['chat_messages']['Row'], 'id' | 'created_at'>;
        Update: Partial<Database['public']['Tables']['chat_messages']['Insert']>;
      };
      user_settings: {
        Row: {
          id: string;
          user_id: string;
          visible_cards: string[];
          currency: 'AUD' | 'USD';
          ms_refresh_token: string | null;
          updated_at: string;
        };
        Insert: Omit<Database['public']['Tables']['user_settings']['Row'], 'id' | 'updated_at'>;
        Update: Partial<Database['public']['Tables']['user_settings']['Insert']>;
      };
    };
  };
}
