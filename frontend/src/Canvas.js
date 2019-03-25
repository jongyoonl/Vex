import React, { Component } from 'react';
import './Canvas.css';
import './Colors';

class Canvas extends Component {

    render() {
        return (
            <canvas className="Canvas" ref="canvas" id="canvas" width="450%" height="250%"
                onMouseDown = {this.onStart.bind(this)}
                onMouseUp = {this.onEnd.bind(this)}
                onMouseMove = {this.onMove.bind(this)}
                onTouchStart = {this.onStart.bind(this)}
                onTouchEnd = {this.onEnd.bind(this)}
                onTouchMove = {this.onMove.bind(this)}
            />
        );
    }

    componentDidMount() {
        this.eraseBoard(this.refs.canvas);
        this.setState({
            canvas: this.refs.canvas,
            ctx: this.refs.canvas.getContext("2d"),
            drawing: false,
            lastX: undefined,
            lastY: undefined,
        });
    }

    shouldComponentUpdate() {
        return (this.state != null) && this.state.drawing;
    }

    onStart(e) {
        var rect = this.state.canvas.getBoundingClientRect();

        this.setState({
            drawing: true,
            lastX: e.clientX - rect.x,
            lastY: e.clientY - rect.y,
        });
    }

    onEnd() {
        this.setState({
            drawing: false,
            lastX: undefined,
            lastY: undefined,
        });
    }

    onMove(e) {

        var rect = this.state.canvas.getBoundingClientRect();
        
        if (this.state.drawing) {

            const ctx = this.state.ctx;
            ctx.beginPath();
            ctx.strokeStyle = document.getElementById("current").style["backgroundColor"];
            ctx.moveTo(this.state.lastX, this.state.lastY);
            ctx.lineTo(e.clientX - rect.x, e.clientY - rect.y);
            ctx.stroke();
        }

        this.setState({
            lastX: e.clientX - rect.x,
            lastY: e.clientY - rect.y,
        });
        
    }

    eraseBoard(canvas) {

        const ctx = canvas.getContext("2d");

        ctx.fillStyle = "white";
        ctx.fillRect(0,0, canvas.width, canvas.height);

    }
}

export default Canvas;
