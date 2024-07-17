import "./App.css";

function App() {
  return (
    <>
      <h1>To Do List</h1>
      <div className="card">
        <p>This is a very quick and dirty basic to-do list setup.</p>
        <ul className="no-bullets">
          <li>
            <input type="checkbox" id="item1" name="item1" value="item1" />
            <label htmlFor="item1"> Test...</label>
          </li>
          <li>
            <input type="checkbox" id="item2" name="item2" value="item2" />
            <label htmlFor="item1"> Write a Readme</label>
          </li>
          <li>
            <input type="checkbox" id="item3" name="item3" value="item3" />
            <label htmlFor="item1"> Kiss my homies goodnight</label>
          </li>
          {/* This will need to loop and display however many items there are in the backend, eventually */}
        </ul>
      </div>
      <p className="read-the-docs">Testing...</p>
    </>
  );
}

export default App;
