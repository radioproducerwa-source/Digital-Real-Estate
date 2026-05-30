import type { Config } from 'tailwindcss';

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        habits: {
          DEFAULT: '#6366f1',
          light: '#e0e7ff',
        },
        tasks: {
          DEFAULT: '#10b981',
          light: '#d1fae5',
        },
        calendar: {
          DEFAULT: '#3b82f6',
          light: '#dbeafe',
        },
        goals: {
          DEFAULT: '#f43f5e',
          light: '#ffe4e6',
        },
        summary: {
          DEFAULT: '#64748b',
          light: '#f1f5f9',
        },
        chat: {
          DEFAULT: '#06b6d4',
          light: '#cffafe',
        },
        bitcoin: {
          DEFAULT: '#f97316',
          light: '#ffedd5',
        },
        quote: {
          DEFAULT: '#8b5cf6',
          light: '#ede9fe',
        },
        content: {
          DEFAULT: '#ec4899',
          light: '#fce7f3',
        },
      },
    },
  },
  plugins: [],
};

export default config;
