import React, { Component } from 'react';
import './Suggestions.css';

class Suggestions extends Component {

    render() {
        return (
            <div>
                <p className="Guesses">
                    Guesses
                </p>
                <a href="about:blank" target="_blank" rel="noopener noreferrer" id="anc0">
                <canvas className="Suggestion" id="sugg0" ref="sugg0" width="360%" height="200%"/>
                </a>
                <a href="about:blank" target="_blank" rel="noopener noreferrer" id="anc1">
                <canvas className="Suggestion" id="sugg1" ref="sugg1" width="360%" height="200%"/> 
                </a>
                <a href="about:blank" target="_blank" rel="noopener noreferrer" id="anc2">
                <canvas className="Suggestion" id="sugg2" ref="sugg2" width="360%" height="200%"/>
                </a>
                <a href="about:blank" target="_blank" rel="noopener noreferrer" id="anc3">
                <canvas className="Suggestion" id="sugg3" ref="sugg3" width="360%" height="200%"/>
                </a>
            </div>
        );
    }

    componentDidMount() {

        for (var sugg in this.refs) {
            const canvas = this.refs[sugg];
            const ctx = canvas.getContext("2d");
            ctx.fillStyle = "white";
            ctx.fillRect(0,0, canvas.width, canvas.height);
        }
    }

    onClick(link) {
        const canvas = this.refs[link];
        const href = canvas["href"];
        const win = window.open(href, href);
        win.focus()
    }
}

export default Suggestions;