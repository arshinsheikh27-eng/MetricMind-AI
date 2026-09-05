"use client";

import { useEffect, useState, type ReactNode } from "react";
import {
  Bar,
  BarChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

const API_URL =
  process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

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
  const [summary, setSummary] = useState<Summary | null>(null);
  const [revenueByRegion, setRevenueByRegion] = useState<RevenueRegion[]>([]);
  const [profitByProduct, setProfitByProduct] = useState<ProfitProduct[]>([]);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [activeSection, setActiveSection] = useState("dashboard");

  const [question, setQuestion] = useState(
    "Which region generated the most revenue?"
  );
  const [answer, setAnswer] = useState("");
  const [asking, setAsking] = useState(false);

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
        console.error("Dashboard loading error:", err);
        setError("Unable to load analytics data.");
      } finally {
        setLoading(false);
      }
    }

    loadDashboard();
  }, []);

  const scrollToSection = (section: string) => {
    setActiveSection(section);

    const element = document.getElementById(section);

    if (element) {
      element.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }
  };

  const formatCurrency = (value: number) =>
    `$${(value / 1_000_000_000).toFixed(1)}B`;

  const formatBillions = (value: number) =>
    `$${(value / 1_000_000_000).toFixed(1)}B`;

  async function askAI() {
    const trimmedQuestion = question.trim();

    if (!trimmedQuestion) {
      setAnswer("Please enter a business question.");
      return;
    }

    setAsking(true);
    setAnswer("");

    try {
      const response = await fetch(`${API_URL}/ask`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: trimmedQuestion,
        }),
      });

      const data = await response.json();

      if (response.ok && data.answer) {
        setAnswer(data.answer);
        return;
      }

      throw new Error(data.detail || "AI service unavailable");
    } catch (err) {
      console.warn("AI service unavailable, using dashboard data:", err);

      const lowerQuestion = trimmedQuestion.toLowerCase();

      if (
        lowerQuestion.includes("region") &&
        lowerQuestion.includes("revenue")
      ) {
        const topRegion = [...revenueByRegion].sort(
          (a, b) => b.revenue - a.revenue
        )[0];

        if (topRegion) {
          setAnswer(
            `${topRegion.region} generated the most revenue, with ${formatCurrency(
              topRegion.revenue
            )} in total revenue.`
          );
        } else {
          setAnswer("Revenue-by-region data is not available.");
        }
      } else if (
        lowerQuestion.includes("product") &&
        lowerQuestion.includes("profit")
      ) {
        const topProduct = [...profitByProduct].sort(
          (a, b) => b.profit - a.profit
        )[0];

        if (topProduct) {
          setAnswer(
            `${topProduct.item_type} generated the highest profit, with ${formatCurrency(
              topProduct.profit
            )} in total profit.`
          );
        } else {
          setAnswer("Profit-by-product data is not available.");
        }
      } else if (
        lowerQuestion.includes("total revenue") ||
        lowerQuestion.includes("revenue")
      ) {
        setAnswer(
          `Total revenue is ${formatCurrency(
            summary?.total_revenue ?? 0
          )}.`
        );
      } else if (
        lowerQuestion.includes("total profit") ||
        lowerQuestion.includes("profit")
      ) {
        setAnswer(
          `Total profit is ${formatCurrency(
            summary?.total_profit ?? 0
          )}, with a profit margin of ${summary?.profit_margin_percent.toFixed(
            1
          )}%.`
        );
      } else if (
        lowerQuestion.includes("order") ||
        lowerQuestion.includes("orders")
      ) {
        setAnswer(
          `MetricMind recorded ${(
            summary?.total_orders ?? 0
          ).toLocaleString()} total orders.`
        );
      } else if (
        lowerQuestion.includes("margin") ||
        lowerQuestion.includes("profit margin")
      ) {
        setAnswer(
          `The overall profit margin is ${summary?.profit_margin_percent.toFixed(
            1
          )}%.`
        );
      } else {
        setAnswer(
          "The AI service is currently unavailable because the OpenAI API has no remaining credits. I can still answer common questions using the loaded MetricMind dashboard data."
        );
      }
    } finally {
      setAsking(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="flex min-h-screen">
        <aside className="hidden w-64 border-r border-slate-800 bg-slate-900 p-6 md:block">
          <h1 className="text-2xl font-bold text-cyan-400">
            MetricMind
          </h1>

          <p className="mt-2 text-sm text-slate-400">
            Agentic Semantic BI
          </p>

          <nav className="mt-10 space-y-2">
            <button
              type="button"
              onClick={() => scrollToSection("dashboard")}
              className={`w-full rounded-lg px-4 py-3 text-left transition ${
                activeSection === "dashboard"
                  ? "bg-cyan-500/10 text-cyan-400"
                  : "text-slate-400 hover:bg-slate-800"
              }`}
            >
              Dashboard
            </button>

            <button
              type="button"
              onClick={() => scrollToSection("analytics")}
              className={`w-full rounded-lg px-4 py-3 text-left transition ${
                activeSection === "analytics"
                  ? "bg-cyan-500/10 text-cyan-400"
                  : "text-slate-400 hover:bg-slate-800"
              }`}
            >
              Analytics
            </button>

            <button
              type="button"
              onClick={() => scrollToSection("ask-ai")}
              className={`w-full rounded-lg px-4 py-3 text-left transition ${
                activeSection === "ask-ai"
                  ? "bg-cyan-500/10 text-cyan-400"
                  : "text-slate-400 hover:bg-slate-800"
              }`}
            >
              Ask AI
            </button>
          </nav>
        </aside>

        <section className="flex-1 p-6 md:p-10">
          <div className="mx-auto max-w-7xl">

            {/* DASHBOARD */}
            <section id="dashboard" className="scroll-mt-8">
              <header className="mb-8">
                <p className="text-sm font-medium text-cyan-400">
                  BUSINESS INTELLIGENCE
                </p>

                <h2 className="mt-2 text-3xl font-bold tracking-tight">
                  Analytics Dashboard
                </h2>

                <p className="mt-2 text-slate-400">
                  Real-time insights from your MetricMind analytics
                  platform.
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
                      : (
                          summary?.total_orders ?? 0
                        ).toLocaleString()
                  }
                />

                <MetricCard
                  title="Profit Margin"
                  value={
                    loading
                      ? "Loading..."
                      : `${summary?.profit_margin_percent.toFixed(
                          1
                        )}%`
                  }
                />
              </div>
            </section>

            {/* ANALYTICS */}
            <section
              id="analytics"
              className={`mt-8 scroll-mt-8 rounded-2xl transition ${
                activeSection === "analytics"
                  ? "ring-2 ring-cyan-400/70"
                  : ""
              }`}
            >
              <div className="mb-5">
                <p className="text-sm font-medium text-cyan-400">
                  ANALYTICS
                </p>

                <h3 className="mt-1 text-2xl font-bold">
                  Business Analytics
                </h3>

                <p className="mt-1 text-sm text-slate-400">
                  Explore revenue and profit performance across the
                  business.
                </p>
              </div>

              <div className="grid gap-6 lg:grid-cols-2">
                <DashboardCard
                  title="Revenue by Region"
                  description="Revenue distribution across geographic regions."
                >
                  <div className="h-80">
                    {loading ? (
                      <ChartLoading />
                    ) : (
                      <ResponsiveContainer
                        width="100%"
                        height="100%"
                      >
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
                      <ResponsiveContainer
                        width="100%"
                        height="100%"
                      >
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
            </section>

            {/* ASK AI */}
            <section
              id="ask-ai"
              className={`mt-8 scroll-mt-8 rounded-xl border border-slate-800 bg-slate-900 p-6 transition ${
                activeSection === "ask-ai"
                  ? "ring-2 ring-cyan-400/70"
                  : ""
              }`}
            >
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
                  value={question}
                  onChange={(event) =>
                    setQuestion(event.target.value)
                  }
                  onKeyDown={(event) => {
                    if (event.key === "Enter") {
                      askAI();
                    }
                  }}
                  placeholder="e.g. Which region generated the most revenue?"
                  className="flex-1 rounded-lg border border-slate-700 bg-slate-950 px-4 py-3 text-sm outline-none placeholder:text-slate-600 focus:border-cyan-400"
                />

                <button
                  type="button"
                  onClick={askAI}
                  disabled={asking}
                  className="rounded-lg bg-cyan-500 px-6 py-3 font-medium text-slate-950 transition hover:bg-cyan-400 disabled:cursor-not-allowed disabled:opacity-60"
                >
                  {asking ? "Analyzing..." : "Ask AI"}
                </button>
              </div>

              {answer && (
                <div className="mt-5 rounded-lg border border-cyan-900 bg-cyan-950/30 p-5">
                  <p className="text-sm font-medium text-cyan-400">
                    MetricMind Answer
                  </p>

                  <p className="mt-2 leading-7 text-slate-200">
                    {answer}
                  </p>
                </div>
              )}
            </section>
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
  children: ReactNode;
}) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
      <h3 className="text-lg font-semibold">{title}</h3>

      <p className="mb-4 mt-1 text-sm text-slate-400">
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