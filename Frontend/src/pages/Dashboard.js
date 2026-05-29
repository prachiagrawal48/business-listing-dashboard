import React, { useEffect, useState } from "react";
import axios from "axios";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

function Dashboard() {

  const [cityData, setCityData] = useState([]);
  const [categoryData, setCategoryData] = useState([]);
  const [sourceData, setSourceData] = useState([]);

  useEffect(() => {

    axios.get("http://127.0.0.1:8000/city-count")
      .then((response) => {
        setCityData(response.data);
      });

    axios.get("http://127.0.0.1:8000/category-count")
      .then((response) => {
        setCategoryData(response.data);
      });

    axios.get("http://127.0.0.1:8000/source-count")
      .then((response) => {
        setSourceData(response.data);
      });

  }, []);

  return (
    <div style={{ padding: "20px" }}>

      <h1>Business Dashboard</h1>

      {/* City Chart */}
      <h2>City-wise Business Count</h2>

      <BarChart width={500} height={300} data={cityData}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="city" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="count" fill="#8884d8" />
      </BarChart>

      {/* Category Chart */}
      <h2>Category-wise Business Count</h2>

      <BarChart width={500} height={300} data={categoryData}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="category" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="count" fill="#82ca9d" />
      </BarChart>

      {/* Source Chart */}
      <h2>Source-wise Business Count</h2>

      <BarChart width={500} height={300} data={sourceData}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="source" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="count" fill="#ffc658" />
      </BarChart>

    </div>
  );
}

export default Dashboard;