import React, { useState, useEffect, useCallback } from 'react';
import axios from 'axios';
import './App.css';

const API_BASE_URL = 'https://mahnameisayush.pythonanywhere.com'; // Directly specify the base URL

function RBTreeGenerator() {
  const [response, setResponse] = useState('');
  const [insertValue, setInsertValue] = useState('');
  const [values, setValues] = useState([]);
  const [svgContent, setSvgContent] = useState('');

  const handleGenerateRBTree = useCallback(async () => {
    try {
      const res = await axios.post(`${API_BASE_URL}/generate`);
      console.log(res.data);
      setResponse(res.data);
      setValues([]); // Clear the list of nodes
      await handleFetchSVG(); // Fetch SVG after generating
    } catch (error) {
      console.error('Error generating RB Tree:', error);
    }
  }, []);

  useEffect(() => {
    handleGenerateRBTree();
  }, [handleGenerateRBTree]);

  const handleInsertValue = async () => {
    try {
      const value = parseInt(insertValue);
      const res = await axios.post(`${API_BASE_URL}/insert`, { value });
      console.log(res.data);
      setResponse(res.data);
      setInsertValue(''); // Clear input field
      setValues([...values, value]); // Add value to the list
      await handleFetchSVG(); // Fetch SVG after insert
    } catch (error) {
      console.error('Error inserting value:', error);
    }
  };

  const handleDeleteValue = async (value) => {
    try {
      const res = await axios.post(`${API_BASE_URL}/delete`, { value });
      console.log(res.data);
      setResponse(res.data);
      setValues(values.filter(v => v !== value)); // Remove value from the list
      await handleFetchSVG(); // Fetch SVG after delete
    } catch (error) {
      console.error('Error deleting value:', error);
    }
  };

  const handleFetchSVG = async () => {
    try {
      const res = await axios.get(`${API_BASE_URL}/svg`, { responseType: 'text' });
      setSvgContent(res.data);
    } catch (error) {
      console.error('Error fetching SVG:', error);
    }
  };

  return (
    <div>
      <div className="controlsContainer">
        <button className="actionButton" onClick={handleGenerateRBTree}>Generate RB Tree</button>
        <div>
          <input
            className="insertInput"
            type="number"
            value={insertValue}
            onChange={(e) => setInsertValue(e.target.value)}
            placeholder="Insert value"
          />
          <button className="actionButton" onClick={handleInsertValue}>Insert</button>
        </div>
        <div className="valueContainer">
          {values.map((value, index) => (
            <div key={index} className="valueBox">
              {value}
              <button className="deleteButton" onClick={() => handleDeleteValue(value)}>X</button>
            </div>
          ))}
        </div>
        {response && <p>{response}</p>}
      </div>
      <div className="svgContainer">
        {svgContent && <div dangerouslySetInnerHTML={{ __html: svgContent }} />}
      </div>
    </div>
  );
}

export default RBTreeGenerator;
