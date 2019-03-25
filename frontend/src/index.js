import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Canvas from './Canvas'
import Colors from './Colors'
import Suggestions from './Suggestions'
import Buttons from './Buttons'
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<App />, document.getElementById('root'));
ReactDOM.render(<Colors />, document.getElementById('colors-div'))
ReactDOM.render(<Suggestions />, document.getElementById('suggestions-div'));
ReactDOM.render(<Canvas />, document.getElementById('canvas-div'));
ReactDOM.render(<Buttons />, document.getElementById('buttons-div'))
registerServiceWorker();
