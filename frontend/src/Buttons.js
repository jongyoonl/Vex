import React, { Component } from 'react';
import './Buttons.css';
import Canvas from './Canvas.js';
import axios from 'axios';

axios.defaults.baseURL = "http://localhost:8080"
axios.defaults.withCredentials = true;
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

class Buttons extends Component {

    render() {
        return (
            <div>
                <button className="Button" id="clear" ref="clear" onClick={this.clearBoard}>
                    Clear
                </button>
                <button className="Button" id="submit" ref="submit" onClick={this.submitImage}>
                    Submit
                </button>
            </div>
        );
    }

    clearBoard() {
        Canvas.prototype.eraseBoard(document.getElementById("canvas"));
    }

    submitImage() {

        var image = document.getElementById("canvas").toDataURL();
    
        axios.post("/vexapp/vex/", image)
            .then( (response) => {

                Buttons.prototype.drawFlag(response, "0");
                Buttons.prototype.drawFlag(response, "1");
                Buttons.prototype.drawFlag(response, "2");
                Buttons.prototype.drawFlag(response, "3");

                console.log(response.config);
                console.log(response.data);
                console.log(response.headers);

            })
            .catch( (error) => {

                console.log(error.response.data);
                console.log(error.response.status);
                console.log(error.response.headers);

            });
    }


    drawFlag(response, index) {
        var anchor = document.getElementById("anc" + index)
        var canvas = document.getElementById("sugg" + index);
        var ctx = canvas.getContext("2d");

        var sugg = new Image();
        sugg.onload = function () {
            ctx.drawImage(sugg, 0, 0, sugg.width, sugg.height,
                                0, 0, canvas.width, canvas.height);
        }

        sugg.src = "data:image/png;base64," + response.data["sugg" + index].substr(2).slice(0, -1);

        var link = "http://en.wikipedia.org/wiki/Flag_of_" + response.data["tag" + index];
        anchor.setAttribute("href", link);
    }


}

export default Buttons;