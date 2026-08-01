import axios from "axios";

function Buttons({
  language,
  code,
  setCode,
  setOutput,
  setStatus,
  setExecutionTime,
}) {

  const runCode = async () => {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/execute",
        {
          language,
          code,
        }
      );

      setOutput(response.data.output);
      setStatus(response.data.status);
      setExecutionTime(response.data.execution_time + " sec");

    } catch (error) {
      setStatus("Error");
      setExecutionTime("-");
      setOutput("Unable to connect to backend.");
    }
  };

  const clearCode = () => {
    setCode("");
    setOutput("");
    setStatus("");
    setExecutionTime("");
  };

  return (
    <div className="button-container">
      <button onClick={runCode}>▶ Run Code</button>
      <button onClick={clearCode}>Clear</button>
    </div>
  );
}

export default Buttons;