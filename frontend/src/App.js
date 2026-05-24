import React, { useState } from "react";
import axios from "axios";
import "./App.css";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend
} from "chart.js";

ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

function App() {
  const [activeMode, setActiveMode] = useState(null);
  const [datasetFile, setDatasetFile] = useState(null);
  const [modelFile, setModelFile] = useState(null);
  const [result, setResult] = useState(null);
  const [popup, setPopup] = useState("");
  const [loading, setLoading] = useState(false);

  const showPopup = (msg) => {
    setPopup(msg);
    setTimeout(() => setPopup(""), 3500);
  };

  const validFile = (file) => {
    return file && (file.name.endsWith(".csv") || file.name.endsWith(".xlsx"));
  };

  const selectMode = (mode) => {
    setActiveMode(mode);
    setResult(null);
    setDatasetFile(null);
    setModelFile(null);
  };

  const runDatasetAudit = async () => {
    if (!validFile(datasetFile)) {
      showPopup("Please upload a valid Dataset file in CSV or XLSX format.");
      return;
    }

    const formData = new FormData();
    formData.append("file", datasetFile);
    setLoading(true);

    const response = await axios.post("https://realitycheck-ai-backend.onrender.com/upload-dataset", formData);
    setResult(response.data);
    setLoading(false);
  };

  const runModelAudit = async () => {
    if (!validFile(modelFile)) {
      showPopup("Please upload model output file with actual, predicted, confidence columns.");
      return;
    }

    const formData = new FormData();
    formData.append("file", modelFile);
    setLoading(true);
    const response = await axios.post("https://realitycheck-ai-backend.onrender.com/upload-model-output", formData);
    setResult(response.data);
    setLoading(false);
  };

  const runCombinedAudit = async () => {
    if (!validFile(datasetFile) || !validFile(modelFile)) {
      showPopup("Please upload both Dataset and Model Output files correctly.");
      return;
    }

    const formData = new FormData();
    formData.append("dataset_file", datasetFile);
    formData.append("model_output_file", modelFile);
    setLoading(true);

    const response = await axios.post("https://realitycheck-ai-backend.onrender.com/upload-combined", formData);
    setResult(response.data);
    setLoading(false);
  };

  const chartData = (data) =>
    data?.missing_values
      ? {
          labels: Object.keys(data.missing_values),
          datasets: [
            {
              label: "Missing Values",
              data: Object.values(data.missing_values)
            }
          ]
        }
      : null;

  const List = ({ title, items }) =>
    items && (
      <div className="panel">
        <h3>{title}</h3>
        <ul>{items.map((x, i) => <li key={i}>{x}</li>)}</ul>
      </div>
    );

  const DatasetReport = ({ data }) => {
    const cData = chartData(data);

    return (
      <div className="report">
        <h2>Dataset Audit Report</h2>

        <div className="metrics">
          <Card title="Rows" value={data.rows} />
          <Card title="Trust Score" value={data.trust_score} />
          <Card title="Risk Level" value={data.risk_level} />
          <Card title="Grade" value={data.grade} />
          <Card title="Anomalies" value={data.anomalies_detected} />
          <Card title="Duplicates" value={data.duplicates} />
          <Card title="Confidence" value={data.confidence} />
          <Card title="Health" value={data.health_status} />
        </div>

        <div className="panel">
          <h3>Missing Values</h3>
          <pre>{JSON.stringify(data.missing_values, null, 2)}</pre>
        </div>

        <List title="AI Insights" items={data.insights} />
        <List title="Consistency Issues" items={data.consistency_issues} />
        <List title="AI Recommendations" items={data.recommendations} />
        <List title="Data Drift Detection" items={data.drift_detection} />
        <List title="Bias Detection" items={data.bias_detection} />

        {data.relationships && (
          <div className="panel">
            <h3>Auto Relationship Discovery</h3>
            <ul>
              {data.relationships.map((item, index) => (
                <li key={index}>
                  {item.message} | Correlation: {item.correlation}
                </li>
              ))}
            </ul>
          </div>
        )}

        {cData && (
          <div className="chart">
            <h3>Missing Values Chart</h3>
            <Bar data={cData} />
          </div>
        )}
      </div>
    );
  };

  const ModelReport = ({ audit }) => (
    <div className="report">
      <h2>Model Output Verification</h2>

      <div className="metrics">
        <Card title="Status" value={audit.status} />
        <Card title="Accuracy" value={audit.accuracy !== null ? audit.accuracy + "%" : "N/A"} />
        <Card title="Wrong Predictions" value={audit.wrong_predictions ?? "N/A"} />
        <Card title="Overconfident Errors" value={audit.overconfident_errors ?? "N/A"} />
        <Card title="Model Trust" value={audit.model_trust} />
      </div>

      <div className="panel">
        <h3>Audit Message</h3>
        <p>{audit.message}</p>
      </div>
    </div>
  );

  const CombinedReport = ({ data }) => (
    <div className="report">
      <h2>Combined AI Trust Verification</h2>

      {data.final_verdict && (
        <div className="verdict-card">
          <h3>Final AI Trust Verdict</h3>
          <h1>{data.final_verdict.verdict}</h1>
          <p>{data.final_verdict.message}</p>
        </div>
      )}

      {data.dataset_audit && <DatasetReport data={data.dataset_audit} />}
      {data.model_output_audit && <ModelReport audit={data.model_output_audit} />}

      {data.ai_output_audit && (
        <div className="report">
          <h2>AI Output Reasoning Audit</h2>

          <List title="Hallucination Detection" items={data.ai_output_audit.hallucinations} />
          <List title="Generated AI Observations" items={data.ai_output_audit.generated_observations} />
          <List title="Contradiction Detection" items={data.ai_output_audit.contradictions} />

          {data.ai_output_audit.claim_validation && (
            <div className="panel">
              <h3>Claim Validation</h3>
              {data.ai_output_audit.claim_validation.map((item, index) => (
                <div className="claim" key={index}>
                  <p><b>Claim:</b> {item.claim}</p>
                  <p><b>AI Confidence:</b> {item.ai_confidence}%</p>
                  <p><b>Confidence Audit:</b> {item.confidence_verdict}</p>
                  <p><b>Exaggeration:</b> {item.exaggeration}</p>
                  <p><b>Evidence:</b> {item.evidence?.evidence_level}</p>
                  <p>{item.evidence?.verdict}</p>
                  <ul>
                    {item.validation?.map((v, i) => (
                      <li key={i}>{v.message}</li>
                    ))}
                  </ul>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );

  const Card = ({ title, value }) => (
    <div className="metric-card">
      <span>{title}</span>
      <h3>{value}</h3>
    </div>
  );

  return (
    <div className="app">
      {popup && <div className="popup">{popup}</div>}

      <header className="hero">
        <h1>RealityCheck AI</h1>
        <p>AI Model Reliability, Dataset Trust and Output Verification Platform</p>
        <div className="creator-tag">
          Built by Mahasiva Saravagna Sai Lakshmi
        </div>
      </header>

      <section className="tutorial">
        <h2>How to Use RealityCheck AI</h2>
        <p>RealityCheck AI helps users evaluate whether datasets and AI model outputs are trustworthy.</p>
        <p>Choose Dataset Audit if you only want to check the quality of a dataset.</p>
        <p>Choose Model Output Verification if you already have model predictions.</p>
        <p>Choose Combined Verification if you want to compare dataset quality with model prediction reliability.</p>
        <p>Dataset files can be CSV or XLSX format.</p>
        <p>Model output files must contain actual, predicted and confidence columns.</p>
        <p>The system performs black-box model auditing, so model code is not required.</p>
        <p>It checks accuracy, wrong predictions, overconfident errors and model trust.</p>
        <p>It also detects hallucinations, contradictions, weak evidence and risky AI claims.</p>
        <p>Final reports help users decide whether AI outputs can be trusted or need human verification.</p>
      </section>

      <section className="mode-grid">
        <div className={`mode-card ${activeMode === "dataset" ? "active" : ""}`}>
          <h2>Dataset Audit</h2>
          <p>Check missing values, anomalies, bias, drift, relationships and trust score.</p>
          <button onClick={() => selectMode("dataset")}>Open Dataset Audit</button>
        </div>

        <div className={`mode-card ${activeMode === "model" ? "active" : ""}`}>
          <h2>Model Output Verification</h2>
          <p>Upload prediction results to check accuracy, confidence and model trust.</p>
          <button onClick={() => selectMode("model")}>Open Model Audit</button>
        </div>

        <div className={`mode-card ${activeMode === "combined" ? "active" : ""}`}>
          <h2>Combined Verification</h2>
          <p>Upload dataset and model outputs together for final AI trust verification.</p>
          <button onClick={() => selectMode("combined")}>Open Combined Audit</button>
        </div>
      </section>
      {loading && (
  <div className="loader">
    Analyzing... Please wait
  </div>
)}

      {activeMode === "dataset" && (
        <section className="upload-box">
          <h2>Dataset Audit</h2>
          <input type="file" onChange={(e) => setDatasetFile(e.target.files[0])} />
          <button onClick={runDatasetAudit}>Run Dataset Audit</button>
        </section>
      )}

      {activeMode === "model" && (
        <section className="upload-box">
          <h2>Model Output Verification</h2>
          <input type="file" onChange={(e) => setModelFile(e.target.files[0])} />
          <button onClick={runModelAudit}>Run Model Verification</button>
        </section>
      )}

      {activeMode === "combined" && (
        <section className="upload-box">
          <h2>Combined Verification</h2>
          <label>Upload Dataset File</label>
          <input type="file" onChange={(e) => setDatasetFile(e.target.files[0])} />

          <label>Upload Model Output File</label>
          <input type="file" onChange={(e) => setModelFile(e.target.files[0])} />

          <button onClick={runCombinedAudit}>Run Combined Verification</button>
        </section>
      )}

      {result && activeMode === "dataset" && <DatasetReport data={result} />}
      {result && activeMode === "model" && <ModelReport audit={result.model_output_audit} />}
      {result && activeMode === "combined" && <CombinedReport data={result} />}
      <footer className="footer">
  © 2026 RealityCheck AI • Built by Mahasiva Saravagna Sai Lakshmi
</footer>
    </div>
  );
  
}

export default App;