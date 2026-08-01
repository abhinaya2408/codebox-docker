function OutputBox({ output }) {
  return (
    <div className="output-container">
      <h3>Output</h3>

      <pre className="output-box">
        {output || "Your output will appear here..."}
      </pre>
    </div>
  );
}

export default OutputBox;