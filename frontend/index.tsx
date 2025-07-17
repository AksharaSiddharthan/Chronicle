import React, { useState, useEffect } from "react";
import { PieChart, Pie, Cell, Legend, ResponsiveContainer } from "recharts";
import Calendar from "react-calendar";
import "react-calendar/dist/Calendar.css";

// Tailwind for react-calendar override
import "./calendar.css"; // assume we define minimal styling here

const CATEGORY_COLORS: Record<string, string> = {
  Nutrition: "#34D399",
  Exercise: "#60A5FA",
  Education: "#FBBF24",
  Chores: "#9CA3AF",
  Soul: "#A78BFA",
  Projects: "#F472B6",
  Social: "#F87171",
};

type Entry = {
  text: string;
  categories: string[];
  timestamp: string;
};

export default function Home() {
  const [entryText, setEntryText] = useState("");
  const [entries, setEntries] = useState<Entry[]>([]);
  const [loading, setLoading] = useState(false);
  const [darkMode, setDarkMode] = useState(false);
  const [selectedDate, setSelectedDate] = useState<Date | null>(null);

  const fetchEntries = async () => {
    try {
      const res = await fetch("http://localhost:8000/entries");
      const data = await res.json();
      setEntries(data.reverse());
    } catch (err) {
      console.error("Error fetching entries:", err);
    }
  };

  useEffect(() => {
    fetchEntries();
  }, []);

  const handleSubmit = async () => {
    if (!entryText.trim()) return;
    setLoading(true);
    try {
      const res = await fetch("http://localhost:8000/entry", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: entryText }),
      });
      if (res.ok) {
        setEntryText("");
        await fetchEntries();
      }
    } catch (err) {
      console.error("Submission error:", err);
    } finally {
      setLoading(false);
    }
  };

  const formatDate = (iso: string) => new Date(iso).toLocaleString();

  const categoryTotals: Record<string, number> = {};
  entries.forEach((entry) => {
    entry.categories.forEach((cat) => {
      categoryTotals[cat] = (categoryTotals[cat] || 0) + 1;
    });
  });

  const pieData = Object.entries(categoryTotals).map(([name, value]) => ({
    name,
    value,
  }));

  const filteredEntries = selectedDate
    ? entries.filter((e) =>
        new Date(e.timestamp).toDateString() === selectedDate.toDateString()
      )
    : entries;

  return (
    <div className={`${darkMode ? "bg-gray-900 text-white" : "bg-slate-50 text-black"} min-h-screen transition-colors duration-300 p-4`}>
      <div className="max-w-4xl mx-auto space-y-6">
        <div className="flex justify-between items-center">
          <h1 className="text-3xl font-bold mt-6">🧠 Life Tracker</h1>
          <button
            className="px-3 py-1 border rounded-lg text-sm"
            onClick={() => setDarkMode(!darkMode)}
          >
            {darkMode ? "☀️ Light" : "🌙 Dark"}
          </button>
        </div>

        <div className="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow">
          <textarea
            className="w-full p-4 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-black dark:text-white rounded-xl resize-none focus:outline-none focus:ring-2 focus:ring-blue-500"
            rows={4}
            placeholder="Write about your day..."
            value={entryText}
            onChange={(e) => setEntryText(e.target.value)}
          />
          <button
            onClick={handleSubmit}
            className={`mt-4 px-6 py-2 rounded-xl font-semibold transition ${
              loading ? "bg-gray-400" : "bg-blue-500 hover:bg-blue-600 text-white"
            }`}
            disabled={loading}
          >
            {loading ? "Submitting..." : "Submit"}
          </button>
        </div>

        {/* Calendar */}
        <div className="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow">
          <h2 className="font-semibold text-lg mb-2">📅 Calendar</h2>
          <Calendar
  onChange={(date) => {
    if (Array.isArray(date)) {
      setSelectedDate(date[0]); // Pick the first date in the range
    } else {
      setSelectedDate(date);
    }
  }}
  value={selectedDate}
/>
          {selectedDate && (
            <p className="text-sm mt-2">
              Showing entries for: <strong>{selectedDate.toDateString()}</strong>
            </p>
          )}
        </div>




















        {/* Pie Chart */}
        <div className="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow">
          <h2 className="font-semibold text-lg mb-4">📊 Category Overview</h2>
          <ResponsiveContainer width="100%" height={250}>
            <PieChart>
              <Pie
                dataKey="value"
                data={pieData}
                cx="50%"
                cy="50%"
                outerRadius={80}
                label={({ name }) => name}
              >
                {pieData.map((entry, index) => (
                  <Cell
                    key={`cell-${index}`}
                    fill={CATEGORY_COLORS[entry.name] || "#ccc"}
                  />
                ))}
              </Pie>
              <Legend />
            </PieChart>
          </ResponsiveContainer>
        </div>

        {/* Entries */}
        <div className="space-y-4">
          {filteredEntries.map((entry, index) => (
            <div
              key={index}
              className="bg-white dark:bg-gray-800 p-4 rounded-2xl shadow border border-gray-200 dark:border-gray-700"
            >
              <div className="text-sm text-gray-500 dark:text-gray-400 mb-2">
                {formatDate(entry.timestamp)}
              </div>
              <p className="mb-3 text-gray-800 dark:text-gray-100">{entry.text}</p>
              <div className="flex flex-wrap gap-2">
                {entry.categories.map((cat) => (
                  <span
                    key={cat}
                    className="px-3 py-1 text-sm rounded-full font-medium"
                    style={{
                      backgroundColor: CATEGORY_COLORS[cat] || "#e5e7eb",
                      color: "#111827",
                    }}
                  >
                    {cat}
                  </span>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
