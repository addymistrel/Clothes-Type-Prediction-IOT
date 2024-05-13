import { useState, React, useEffect } from "react";
import axios from "axios";
import "./App.css";

function Home() {
  const DURL = "http://127.0.0.1:8000/";
  const [tempvalue, setTempvalue] = useState("Trying to Connect");
  const [humidvalue, setHumidvalue] = useState("Trying to Connect");

  async function getTemperature() {
    const response = await axios
      .post(DURL + "getTemperature/", { key: "temperature" })
      .then((res) => {
        console.log(res);
        setTempvalue(res.data);
      })
      .catch((err) => {
        console.log(err);
        setTempvalue("Connection Failed");
      });
  }

  async function getHumidity() {
    const response = await axios
      .post(DURL + "getHumidity/", { key: "humidity" })
      .then((res) => {
        console.log(res);
        setHumidvalue(res.data);
      })
      .catch((err) => {
        console.log(err);
        setHumidvalue("Connection Failed");
      });
  }

  return (
    <div className="App">
      <h1 style={{ fontSize: "xx-large", fontWeight: "700" }}>
        Backend Server Check for Django
      </h1>
      <br />
      <br />
      <h3>
        <span style={{ fontWeight: "bold", fontSize: "large" }}>
          Temperature :
        </span>{" "}
        {tempvalue}
      </h3>
      <button
        style={{ border: "2px solid black", padding: "2%" }}
        onClick={() => getTemperature()}
      >
        Get Temperature
      </button>
      <br />
      <h3>
        <span style={{ fontWeight: "bold", fontSize: "large" }}>
          Humidity :
        </span>{" "}
        {humidvalue}
      </h3>
      <button
        style={{ border: "2px solid black", padding: "2%" }}
        onClick={() => getHumidity()}
      >
        Get Humidity
      </button>
    </div>
  );
}

export default Home;
