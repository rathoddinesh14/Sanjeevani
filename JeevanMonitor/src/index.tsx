import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const htmlElement: HTMLElement = document.getElementById('root') as HTMLElement;
const root = ReactDOM.createRoot(htmlElement);
root.render(<App />);