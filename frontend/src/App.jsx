import { useState } from "react";
import "./App.css";

import CodeEditor from "./components/CodeEditor";
import Buttons from "./components/Buttons";
import OutputBox from "./components/OutputBox";

function App() {
  const [language, setLanguage] = useState("python");
  const [code, setCode] = useState("");
  const [output, setOutput] = useState("");
  const [status, setStatus] = useState("");
  const [executionTime, setExecutionTime] = useState("");

  return (
    <div className="container">
      <h1>🐳 CodeBox Docker</h1>
      <p className="subtitle">Secure Online Code Execution Platform</p>

      <div className="section">
        <label>Language</label>

        <select
          value={language}
          onChange={(e) => setLanguage(e.target.value)}
        >
          <option value="python">Python</option>
          <option value="java">Java</option>
        </select>
      </div>

      <div className="section">
        <label>Code</label>

        <CodeEditor code={code} setCode={setCode} />
      </div>

      <Buttons
        language={language}
        code={code}
        setCode={setCode}
        setOutput={setOutput}
        setStatus={setStatus}
        setExecutionTime={setExecutionTime}
      />

      <div className="status">
        <p>
          <strong>Status :</strong> {status}
        </p>

        <p>
          <strong>Execution Time :</strong> {executionTime}
        </p>
      </div>

      <OutputBox output={output} />
    </div>
  );
}

export default App;