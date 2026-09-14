"use client";

import { useEffect, useState } from "react";
import {
  Bar,
  BarChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

type Summary = {
  total_revenue: number;
  total_cost: number;
  total_profit: number;
  total_units_sold: number;
  total_orders: number;
  profit_margin_percent: number;
  average_order_revenue: number;
  average_selling_price: number;
};

type RevenueRegion = {
  region: string;
  revenue: number;
};

type ProfitProduct = {
  item_type: string;
  profit: number;
};

export default function Home() {
  const API_URL =
    process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

  const [summary, setSummary] = useState<Summary | null>(null);
  const [revenueByRegion, setRevenueByRegion] = useState<RevenueRegion[]>([]);
  const [profitByProduct, setProfitByProduct] = useState<ProfitProduct[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadDashboard() {
      try {
        const [summaryResponse, regionResponse, productResponse] =
          await Promise.all([
            fetch(`${API_URL}/analytics/summary`),
            fetch(`${API_URL}/analytics/revenue-by-region`),
            fetch(`${API_URL}/analytics/profit-by-product`),
          ]);

        if (
          !summaryResponse.ok ||
          !regionResponse.ok ||
          !productResponse.ok
        ) {
          throw new Error("Failed to load analytics data");
        }

        const summaryData = await summaryResponse.json();
        const regionData = await regionResponse.json();
        const productData = await productResponse.json();

        setSummary(summaryData.data);
        setRevenueByRegion(regionData.data);
        setProfitByProduct(productData.data);
      } catch (err) {
        console.error("Failed to load dashboard:", err);
        setError("Unable to load analytics data.");
      } finally {
        setLoading(false);
      }
    }

    loadDashboard();
  }, [API_URL]);

  const formatCurrency = (value: number) =>
    `$${(value / 1_000_000_000).toFixed(1)}B`;

  const formatBillions = (value: number) =>
    `$${(value / 1_000_000_000).toFixed(1)}B`;

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="flex min-h-screen">
        <aside className="hidden w-64 border-r border-slate-800 bg-slate-900 p-6 md:block">
          <h1 className="text-2xl font-bold text-cyan-400">MetricMind</h1>

          <p className="mt-2 text-sm text-slate-400">
            Agentic Semantic BI
          </p>

          <nav className="mt-10 space-y-2">
            <div className="rounded-lg bg-cyan-500/10 px-4 py-3 text-cyan-400">
              Dashboard
            </div>

            <div className="rounded-lg px-4 py-3 text-slate-400 hover:bg-slate-800">
              Analytics
            </div>

            <div className="rounded-lg px-4 py-3 text-slate-400 hover:bg-slate-800">
              Ask AI
            </div>
          </nav>
        </aside>

        <section className="flex-1 p-6 md:p-10">
          <div className="mx-auto max-w-7xl">
            <header className="mb-8">
              <p className="text-sm font-medium text-cyan-400">
                BUSINESS INTELLIGENCE
              </p>

              <h2 className="mt-2 text-3xl font-bold tracking-tight">
                Analytics Dashboard
              </h2>

              <p className="mt-2 text-slate-400">
                Real-time insights from your MetricMind analytics platform.
              </p>
            </header>

            {error && (
              <div className="mb-6 rounded-lg border border-red-900 bg-red-950/40 p-4 text-sm text-red-300">
                {error}
              </div>
            )}

            <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
              <MetricCard
                title="Total Revenue"
                value={
                  loading
                    ? "Loading..."
                    : formatCurrency(summary?.total_revenue ?? 0)
                }
              />

              <MetricCard
                title="Total Profit"
                value={
                  loading
                    ? "Loading..."
                    : formatCurrency(summary?.total_profit ?? 0)
                }
              />

              <MetricCard
                title="Total Orders"
                value={
                  loading
                    ? "Loading..."
                    : summary?.total_orders.toLocaleString() ?? "0"
                }
              />

              <MetricCard
                title="Profit Margin"
                value={
                  loading
                    ? "Loading..."
                    : `${summary?.profit_margin_percent.toFixed(1) ?? "0"}%`
                }
              />
            </div>

            <div className="mt-8 grid gap-6 lg:grid-cols-2">
              <DashboardCard
                title="Revenue by Region"
                description="Revenue distribution across geographic regions."
              >
                <div className="h-80">
                  {loading ? (
                    <ChartLoading />
                  ) : (
                    <ResponsiveContainer width="100%" height="100%">
                      <BarChart
                        data={revenueByRegion}
                        layout="vertical"
                        margin={{
                          top: 10,
                          right: 20,
                          left: 20,
                          bottom: 10,
                        }}
                      >
                        <CartesianGrid
                          strokeDasharray="3 3"
                          stroke="#1e293b"
                        />

                        <XAxis
                          type="number"
                          tickFormatter={formatBillions}
                          stroke="#94a3b8"
                          fontSize={11}
                        />

                        <YAxis
                          type="category"
                          dataKey="region"
                          width={150}
                          stroke="#94a3b8"
                          fontSize={11}
                        />

                        <Tooltip
                          formatter={(value) =>
                            formatCurrency(Number(value))
                          }
                          contentStyle={{
                            backgroundColor: "#0f172a",
                            border: "1px solid #334155",
                            borderRadius: "8px",
                            color: "#fff",
                          }}
                        />

                        <Bar
                          dataKey="revenue"
                          fill="#06b6d4"
                          radius={[0, 5, 5, 0]}
                        />
                      </BarChart>
                    </ResponsiveContainer>
                  )}
                </div>
              </DashboardCard>

              <DashboardCard
                title="Profit by Product"
                description="Profit contribution across product categories."
              >
                <div className="h-80">
                  {loading ? (
                    <ChartLoading />
                  ) : (
                    <ResponsiveContainer width="100%" height="100%">
                      <BarChart
                        data={profitByProduct}
                        margin={{
                          top: 10,
                          right: 20,
                          left: 10,
                          bottom: 50,
                        }}
                      >
                        <CartesianGrid
                          strokeDasharray="3 3"
                          stroke="#1e293b"
                        />

                        <XAxis
                          dataKey="item_type"
                          angle={-35}
                          textAnchor="end"
                          interval={0}
                          stroke="#94a3b8"
                          fontSize={10}
                        />

                        <YAxis
                          tickFormatter={formatBillions}
                          stroke="#94a3b8"
                          fontSize={11}
                        />

                        <Tooltip
                          formatter={(value) =>
                            formatCurrency(Number(value))
                          }
                          contentStyle={{
                            backgroundColor: "#0f172a",
                            border: "1px solid #334155",
                            borderRadius: "8px",
                            color: "#fff",
                          }}
                        />

                        <Bar
                          dataKey="profit"
                          fill="#22c55e"
                          radius={[5, 5, 0, 0]}
                        />
                      </BarChart>
                    </ResponsiveContainer>
                  )}
                </div>
              </DashboardCard>
            </div>

            <div className="mt-6 rounded-xl border border-slate-800 bg-slate-900 p-6">
              <p className="text-sm font-medium text-cyan-400">
                AI ANALYST
              </p>

              <h3 className="mt-2 text-xl font-semibold">
                Ask MetricMind
              </h3>

              <p className="mt-2 text-sm text-slate-400">
                Ask a natural-language business question and get an
                AI-powered answer.
              </p>

              <div className="mt-5 flex flex-col gap-3 sm:flex-row">
                <input
                  type="text"
                  placeholder="e.g. Which region generated the most revenue?"
                  className="flex-1 rounded-lg border border-slate-700 bg-slate-950 px-4 py-3 text-sm outline-none placeholder:text-slate-600 focus:border-cyan-400"
                />

                <button className="rounded-lg bg-cyan-500 px-6 py-3 font-medium text-slate-950 transition hover:bg-cyan-400">
                  Ask AI
                </button>
              </div>
            </div>
          </div>
        </section>
      </div>
    </main>
  );
}

function MetricCard({
  title,
  value,
}: {
  title: string;
  value: string;
}) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-5">
      <p className="text-sm text-slate-400">{title}</p>

      <p className="mt-3 text-2xl font-bold">{value}</p>
    </div>
  );
}

function DashboardCard({
  title,
  description,
  children,
}: {
  title: string;
  description: string;
  children: React.ReactNode;
}) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
      <h3 className="text-lg font-semibold">{title}</h3>

      <p className="mt-1 mb-4 text-sm text-slate-400">
        {description}
      </p>

      {children}
    </div>
  );
}

function ChartLoading() {
  return (
    <div className="flex h-full items-center justify-center text-sm text-slate-500">
      Loading chart...
    </div>
  );
}