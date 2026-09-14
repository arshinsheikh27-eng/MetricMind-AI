This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
# MetricMind Frontend

MetricMind Frontend is a Next.js-based Business Intelligence dashboard for the MetricMind Agentic Semantic BI platform.

The frontend connects to the MetricMind FastAPI backend and displays real business analytics, KPI metrics, interactive charts, and an AI Analyst interface.

---

## 1. Frontend Responsibilities

The MetricMind frontend is responsible for:

- Displaying business KPI metrics
- Displaying revenue analytics
- Displaying profit analytics
- Connecting to the FastAPI backend
- Providing interactive dashboard navigation
- Providing the Ask AI interface
- Sending natural-language questions to the backend
- Displaying AI-generated answers
- Handling loading states
- Handling API errors
- Providing a responsive user interface

---

## 2. Technology Stack

| Component | Technology |
|---|---|
| Framework | Next.js |
| UI Library | React |
| Language | TypeScript |
| Styling | Tailwind CSS |
| Charts | Recharts |
| Backend API | FastAPI |
| Database | PostgreSQL |
| AI Service | OpenAI API through backend |

---

## 3. Project Structure

```text
frontend/
│
├── app/
│   ├── page.tsx
│   ├── layout.tsx
│   └── globals.css
│
├── public/
│
├── package.json
├── package-lock.json
├── next.config.ts
├── tsconfig.json
├── postcss.config.mjs
│
├── .env.local.example
└── README.md