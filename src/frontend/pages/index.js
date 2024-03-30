// frontend/pages/index.js
import React, { useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [operand1, setOperand1] = useState('');
  const [operand2, setOperand2] = useState('');
  const [operator, setOperator] = useState('+');
  const [result, setResult] = useState('');

  const calculate = async () => {
    try {
      const response = await axios.post('http://localhost:8000/v1/calculate', {
        expression: `${operand1}${operator}${operand2}`
      });
      setResult(response.data.result);
    } catch (error) {
      console.error('Error during calculation:', error);
      setResult('Error');
    }
  };

  return (
    <div>
      <input
        type="number"
        value={operand1}
        onChange={(e) => setOperand1(e.target.value)}
      />
      <select value={operator} onChange={(e) => setOperator(e.target.value)}>
        <option value="+">+</option>
        <option value="-">-</option>
        <option value="*">*</option>
        <option value="/">/</option>
      </select>
      <input
        type="number"
        value={operand2}
        onChange={(e) => setOperand2(e.target.value)}
      />
      <button onClick={calculate}>Count</button>
      <div>Result: {result}</div>
    </div>
  );
}
